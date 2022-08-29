from django.urls import path
from . import views

urlpatterns= [
    path('users/', views.getUsers),
    path('users/<int:id>',views.getUsersById)
]