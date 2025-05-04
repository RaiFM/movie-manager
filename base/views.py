from django.shortcuts import render

# Create your views here.

from .models import movie

def index(request):
    mov = movie.objects.all()

    context = {
        'movies': mov,
    }

    return render(request, 'index.html', context)

def mov(request, pk):
    filme = movie.objects.get(id=pk)

    context = {
        'movie': filme,
    }
    return render(request, 'movie.html', context)
