from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def homepage(request):
    return render(request, 'home/index.html')