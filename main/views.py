from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Самый лучший интернет магазин рыболовных снастей - Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True
    }

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')
