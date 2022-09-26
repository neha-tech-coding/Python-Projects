from django.urls import path
from . import views

urlpatterns=[
    path('products/',views.getProducts),
    path('products/<int:id>',views.getProductById),
    path('create-products/',views.createProduct),
    path('update-products/<int:id>',views.updateProduct),
    path('delete-products/<int:id>',views.deleteProduct)
]

