from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def users_page(request):
    return render(request,"users/users_page.html")


def login(request):
    return render(request, 'users/login.html')


def register(request):
    form = UserCreationForm()
    return render(request,"users/register.html", {"form":form})


def reset_password(request):
    return render(request, 'users/reset_password.html')