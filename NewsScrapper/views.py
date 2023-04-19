from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .utils import *

# URLs of news websites to be scrapped.
ENGLISH_NEWS = 'https://news-decoder.com/category/world/'
ARABIC_NEWS = 'https://arabic-media.com/articles/id/news-dynamic.php'
FARSI_NEWS = 'https://ir.voanews.com/z/1696'
TURKISH_NEWS = 


# Create your views here.
def homepage(request):
    return render(request, 'home/index.html')

