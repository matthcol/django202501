# execute this script with django shell
from movieapp.models import Movie

# select all
movies = Movie.objects.all()
print(movies)

# add one
m = Movie(title="Free Guy", year=2024)
m.save()
print(m) # calls str
print(repr(m))
