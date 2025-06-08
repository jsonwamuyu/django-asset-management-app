from django.shortcuts import render



def users_page(request):
    return render(request,"users/users_page.html")


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request,"users/register.html")


def reset_password(request):
    return render(request, 'users/reset_password.html')