from django.shortcuts import render, HttpResponse
from .models import User, TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def users(request):
    users = User.objects.all()
    print(users)
    return render(request, 'users.html', {"users": users})