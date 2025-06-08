from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns =[
    path("admin/", admin.site.urls),
    path("", views.homepage,name='homepage'),
    path("about/", views.about,name="about"),

    path("posts/", include('posts.urls', namespace='posts')),
    path("users/", include('users.urls', namespace="users")),

    # API routes from the assets app
    path("api/",include("assets.urls",namespace='assets')),
]

# Tells django where to find images to use inside app
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)