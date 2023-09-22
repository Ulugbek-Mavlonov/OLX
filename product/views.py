from rest_framework import generics

from django.contrib.auth import City, District


class CityViewSet(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = 'CitySerializer'

class DistrictViewSet(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = 'DistrictSerializer'