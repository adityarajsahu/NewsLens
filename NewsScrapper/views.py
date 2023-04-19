from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .utils import *

# Create your views here.

def homepage(request):
    return render(request, 'home.html')

