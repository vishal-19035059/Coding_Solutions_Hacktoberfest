from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http.response import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'index.html')