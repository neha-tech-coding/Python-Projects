from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


users_list=[{
    "id":1,"title":"Neha"
},{
    "id":2,"title":"Arshad"
},{
    "id":3, "title":"Chhanda"
}]

def getUsers(request, *args, **kwargs):
    return render(request,'users/users_list.html',{"usersList":users_list,"name":"Neha"})

def getUsersById(request, id):
    user_id=int(id)
    for users in users_list:
        if users["id"]==user_id:
            content=users
            return render(request,'users/users.html',{"usersDetail":content})
