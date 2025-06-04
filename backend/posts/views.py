from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.

def posts(request):
    # return HttpResponse('posts page')
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})
