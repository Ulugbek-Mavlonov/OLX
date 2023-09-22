from django.urls import path
from .views import *

urlpatterns = [
    path('product/',ProductViewSet.as_view(), name='product' ),
    
]