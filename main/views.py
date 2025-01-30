from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Мой первый сайт',
        'content': 'Добро пожаловать на мой сайт.'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'Мы создаем удивительные веб-сайты.'
    }
    return render(request, 'main/about.html', context)
