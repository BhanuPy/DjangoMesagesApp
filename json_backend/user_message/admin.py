from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Message
User = get_user_model()
# Register your models here.
admin.site.register(Message)

