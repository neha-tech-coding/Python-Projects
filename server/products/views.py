from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
# baseUrl='https://jsonplaceholder.typicode.com/posts'
products=[{
    "id":1,"title":"abc"
},{
    "id":2,"title":"xyz"
}]

def getProducts(request,*args,**kwargs):
    return render(request,'products/products.html',{"productsList":products,"name":"Arshad"})


#
# def getProducts(request,*args,**kwargs):
#     posts=requests.get(baseUrl).json()
#     return JsonResponse({"data":posts,"message":"I am from get products","status":200})





