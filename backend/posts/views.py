from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.

def posts(request):
    # return HttpResponse('posts page')
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts.html', {'page_obj':page_obj})
