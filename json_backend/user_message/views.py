from django.shortcuts import render

# Create your views here.
# myapp/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Message
from .serializers import UserSerializer, MessageSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print("line 25", request.data)
        email = request.data['email']
        password = request.data['password']
        username = User.objects.get(email=email).username
        user = authenticate(request, username=username, password=password)
        print(user.is_active, "line number 29")
        print(user, "line number 29")
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

class UserLogoutView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        request.auth.delete()
        return Response(status=204)

class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.get_email_field_name)

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
