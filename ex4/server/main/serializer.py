from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Products
        fields = '__all__'


class PurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Purchased
        fields = '__all__'