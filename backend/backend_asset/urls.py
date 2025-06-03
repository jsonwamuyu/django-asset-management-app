from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # API routes from the assets app
    path("api/",include("assets.urls"), name="assets"),
]
