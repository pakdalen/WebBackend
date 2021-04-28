from rest_framework import serializers
from api import models

class CategoryS(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = 'id', 'name'

class OrderS(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = 'id', 'user', 'phoneNumber', 'address'

class SubcategoryS(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    category = CategoryS()

class ProductS(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    category = CategoryS()
    subcategory = SubcategoryS()
    image = serializers.CharField()
    price = serializers.CharField()
    quantity = serializers.IntegerField()










