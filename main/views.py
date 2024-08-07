from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def news(request):
    return render(request, 'main/news.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def current_time(request):
    now = datetime.now()
    return HttpResponse(f'Текущее время: {now.strftime("%H:%M:%S")}')

# Create your views here.
