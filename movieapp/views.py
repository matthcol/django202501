from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Movie web site very soon here !")

def movie_detail(request, movie_id):
    return HttpResponse("Movie detail with id:", movie_id)

def movie_add(request):
    return HttpResponse("Movie add page")