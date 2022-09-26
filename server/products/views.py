from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product

# queryset=modelName.objects.all()

@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductById(request,id):
    product=Product.objects.get(id=id)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    serializer=ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()         #database save
    else:
        return Response(exception=True,status=405)
    return Response(serializer.data)

@api_view(['PUT'])     #TODO--- Find the Difference
def updateProduct(request,id):
    product=Product.objects.get(id=id)
    serializer=ProductSerializer(instance= product,data=request.data,partial=True)
    # print(request.data)
    # print(serializer)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(exception=True, status=405)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request,id):
    try:
        product=Product.objects.get(id=id)
        product.delete()
        return Response(status=204)
    except:
        return Response(exception=True,status=404)

























