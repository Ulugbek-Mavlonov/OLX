from rest_framework import serializers
from .models import City, District, Product, Banflud, Ban


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BanfludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banflud
        fields = "__all__"


class BanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ban
        fields = ['comment', 'banflud', 'user', 'product']

    def validate_product(self, value):
        product_id = value
        ban_count = Ban.objects.filter(product__id=product_id).count()
        if ban_count >= 10:
            value.delete()
            raise serializers.ValidationError("Product has been banned more than 10 times.")
        return value
