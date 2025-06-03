from django.http import HttpResponse
from django.utils import render


def homepage(request):
    context = "homepage.html"
    return render(request, {'context':context})
    # return HttpResponse("This is homepage.")


def about(request):
    return HttpResponse("This is the about page.")