from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from api.serializers import CategoryS, SubcategoryS, ProductS
from api.models import Category, SubCategory, Product, Order

@permission_classes(IsAuthenticated)
@api_view(['GET'])
def categories(request):
    return JsonResponse(CategoryS(Category.objects.all(), many=True).data, safe=False)
    
@permission_classes(IsAuthenticated)
@api_view(['GET'])
def subcategories(request):
    return JsonResponse(SubcategoryS(SubCategory.objects.all(), many=True).data, safe=False)

@api_view(['GET'])
def by_category(request, id):
    category = Category.objects.get(id=id)
    return JsonResponse(ProductS(category.product_set.all(), many=True).data, safe=False)

@api_view(['POST'])
def by_subcat(request):
    subcategory=SubCategory.objects.get(name=request.data.get('id'))
    return JsonResponse(ProductS(subcategory.product_set.all(), many=True).data, safe=False)


class OrderV(APIView):
    def post(self, request):
        Order.objects.create(
            user = request.data.get('name'),
            phoneNumber = request.data.get('phone'),
            address = request.data.get('address')
        )
        return JsonResponse({"Success": "order created"}, safe=False)

class ProductV(APIView):
    def get(self, request):
        products=Product.objects.all()
        return JsonResponse(ProductS(products, many=True).data, safe=False)

    def post(self, request):
        category = Category.objects.get(name=request.data['category'])
        subcategory = SubCategory.objects.get(name=request.data['subcategory'])

        Product.objects.create(
            name = request.data['name'],
            category = category,
            subcategory = subcategory,
            image = request.data['image'],
            price = request.data['price']
        )
        return JsonResponse({"hello":'hello'}, safe=False)

class ProductDV(APIView):
    def put(self, request, id):
        product = Product.objects.get(id=request.data['id'])
        product.name = request.data['name']
        product.image = request.data['image']
        product.price = request.data['price']
        product.save()
        return JsonResponse({"hello":"hello"}, safe=False)        

    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse({"hello":"hello"}, safe=False)        
