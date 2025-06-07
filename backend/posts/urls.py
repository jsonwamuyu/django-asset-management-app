from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.posts, name='posts' ),
    path('<int:post_id>/', views.get_post, name="post")
]
