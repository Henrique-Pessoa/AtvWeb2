from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductsView(APIView):
    def get(self,id=""):
        serializer = ProductsSerializer(Products.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "That's Okay"})

    def delete(self, id=""):        
        products = Products.objects.get(id=id)       
        products.delete()
        return Response({"msg": "Deleted"})
    
class PurchasedView(APIView):
    def get(self, id=""):
        serializer = PurchasedSerializer(Purchased.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchasedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "That's Okay"})