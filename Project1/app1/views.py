from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from . import views
import requests


def index(request):
    return render(request, 'index.html')


def news(request, data):
    records = {}
    url = f'https://inshortsapi.vercel.app/news?category={data}'
    response = requests.get(url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'news.html', records)


def news1(request):
    records = {}
    url = f'https://inshortsapi.vercel.app/news?category='
    response = requests.get(url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'news.html', records)
