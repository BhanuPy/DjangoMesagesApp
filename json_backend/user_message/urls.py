
# user_message/urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegisterView, UserLoginView, UserLogoutView, MessageListView, MessageDetailView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]
