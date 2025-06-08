from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



def users_page(request):
    return render(request,"users/users_page.html")


def login(request):
    return render(request, 'users/login.html')


def register(request):
    # Check if form has been submited
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  #Validate form inputs
            form.save()
            return redirect("users:login")
    else:
        form = UserCreationForm()
    return render(request,"users/register.html", {"form":form})


def reset_password(request):
    return render(request, 'users/reset_password.html')