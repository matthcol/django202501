from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>/", views.movie_detail, name="movie-detail"),
    path("add/", views.movie_add, name="movie-add"),
    path("<int:movie_id>/actor/<int:actor_id>/<str:role>", views.movie_actor, name="movie-actor"),
]