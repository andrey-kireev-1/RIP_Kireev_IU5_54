from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    content = Ice_cream.objects.all()

    context = {
        'content': content,
        'title': 'Master-страница',
    }

    return render(request, 'master.html', context=context)

def detail(request, id):
    content = Ice_cream.objects.filter(id=id)

    context = {
        'content': content,
        'title': 'Detail-страница',
    }

    return render(request, 'detail.html', context=context)