from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("", views.users_page, name="users_page"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("reset-password/", views.reset_password, name="reset_password")
]
