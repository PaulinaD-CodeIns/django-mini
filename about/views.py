from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about_me(response):
    return HttpResponse("About the wordlings!")