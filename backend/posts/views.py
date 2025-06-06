from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.

Posts = [
    {
        'id':1,
        'title':'Make it happen', 
        'body':"Think of this as a way to make everything work out as expected"
    },
    {
        'id':2,
        'title':'Make it happen', 
        'body':"Think of this as a way to make everything work out as expected"
    },
    {
        'id':3,
        'title':'Make it happen', 
        'body':"Think of this as a way to make everything work out as expected"
    },
    {
        'id':4,
        'title':'Make it happen', 
        'body':"Think of this as a way to make everything work out as expected"
    },
    {
        'id':5,
        'title':'Make it happen', 
        'body':"Think of this as a way to make everything work out as expected"
    },
    {
        'id':6,
        'title':'Make it happen', 
        'body':"Think of this as a way to make everything work out as expected"
    }
]

def posts(request):
    # return HttpResponse('posts page')
    # posts = Post.objects.all().order_by('-id')
    paginator = Paginator(Posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/posts.html', {'page_obj':page_obj})
