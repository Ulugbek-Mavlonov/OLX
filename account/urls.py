from rest_framework import routers
from .views import CustomUserViewSet, ProfileViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'custom-users', CustomUserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
]
