from django.shortcuts import render

# Create your views here.

from .models import movie

def index(request):
    mov = movie.objects.all()
    # mov = movie.objects.get(id=pk)

    context = {
        # 'movie': 'How to train your dragon',
        # 'director': 'John Powell'
        'movies': mov,
    }

    return render(request, 'index.html', context)


