from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage,name='homepage'),
    path("about/", views.about,name="about"),

    path("posts/", include('posts.urls', namespace='posts'), name="posts"),

    # API routes from the assets app
    path("api/",include("assets.urls",namespace='assets'), name="assets"),
]
