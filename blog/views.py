from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(response):
        return HttpResponse("This is the blog you are looking for!")