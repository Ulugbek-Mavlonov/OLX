from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .serializers import CitySerializer, DistrictSerializer
from .models import City, District, Product, Ban, Banflud, CustomUser
from .serializers import ProductSerializer, BanSerializer, BanfludSerializer


class CityViewSet(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DistrictViewSet(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    
class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializers_class = ProductSerializer


class BanCreate(generics.CreateAPIView):
    queryset = Ban.objects.all()
    serializer_class = BanSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(CustomUser, id=self.request.data.dict().get('user_id'))
        product = get_object_or_404(Product, id=self.request.data.dict().get('product_id'))
        return serializer.save(user=user, product=product)



    