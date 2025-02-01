from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'Fishing-tackle',
        'values': ['Hello', True, '123'],
        'obj': {
            'car': 'BMW',
            'age': 25,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'Мы создаем удивительные веб-сайты.'
    }
    return render(request, 'main/about.html', context)
