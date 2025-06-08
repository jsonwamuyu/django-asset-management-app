from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.core.paginator import Paginator


def posts(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts.html', {'page_obj':page_obj})


def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/get_post.html', {'post':post})


def new_post(request):
    return render(request, 'posts/new_post.html')