from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout



def users_page(request):
    return render(request,"users/users_page.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # LOGIN HERE
            login(request, form.get_user())
            return redirect('posts:posts')
    else: # Means its a GET request
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})


def register(request):
    # Check if form has been submitted
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  #Validate form inputs
            login(request, form.save())
            return redirect("users:login")
    else:
        form = UserCreationForm()

    return render(request,"users/register.html", {"form":form})


def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:logout')

def reset_password(request):
    return render(request, 'users/reset_password.html')