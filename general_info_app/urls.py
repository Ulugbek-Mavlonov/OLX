from django.urls import path
from .views import  AddressDetail, SocialnetworkDetail, FaqsList

urlpatterns = [
    path('address/<int:pk>/', AddressDetail.as_view(), name='AddressDetail'),
    path('social/<int:pk>/', SocialnetworkDetail.as_view(), name='SocialnetworkDetail'),
    path('faqs/list/', FaqsList.as_view(), name='FaqsList'),
]
