from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def index(request):
    return HttpResponse("<h2>Hello, this is the home page</h2>")


def about(request):
    return HttpResponse("This is the About page")