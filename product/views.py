from rest_framework import generics

from .models import City, District


class CityViewSet(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = 'CitySerializer'

class DistrictViewSet(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = 'DistrictSerializer'