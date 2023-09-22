from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer