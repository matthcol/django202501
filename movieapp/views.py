from datetime import date
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from movieapp.models import Movie


def index(request):
    # return HttpResponse("Movie web site very soon here !")

    # last movies
    data = Movie.objects.filter(year=date.today().year - 10)
    movie_count = Movie.objects.count()
    return render(request, 'movie/index.html', context={
        'movie_list': data,
        'movie_count': movie_count
    })

def movie_detail(request, movie_id):
    return HttpResponse(f"Movie detail with id: #{movie_id}#")

def movie_add(request):
    return HttpResponse("Movie add page")

def movie_actor(request, movie_id, actor_id, role):
    return HttpResponse(f"Movie actor: {movie_id}, {actor_id}, {role}")