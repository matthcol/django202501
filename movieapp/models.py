from django.db import models

# Create your models here.
# Ref: https://docs.djangoproject.com/en/5.1/ref/models/fields/
# Example: https://docs.djangoproject.com/en/5.1/topics/db/models/

class Movie(models.Model):
    class Meta:
        #db_table = 'data.movie'
        db_table = 'movie'

    # default: PK id = BigAutoField

    # explicit auto PK
    id = models.AutoField(primary_key=True)

    # explicit PK (non auto)
    # id = models.IntegerField(primary_key=True)

    title = models.CharField(max_length=300)
    year = models.IntegerField()
    duration = models.IntegerField(null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    poster_uri = models.CharField(max_length=300, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    poster_uri = models.CharField(max_length=15, null=True, blank=True)

    # ManyToOne association: models.ForeignKey
    # default FK name: director_id
    director = models.ForeignKey(
        # db_column=<custom fk name>
        to='Person',
        related_name='movies_directed', 
        null=True, blank=True,
        on_delete=models.DO_NOTHING # DELETE, SET_NULL
    )

    actors = models.ManyToManyField(
        to='Person',
        related_name='movies_played', 
        through='Play', # or db_table without explicit class
        through_fields=('movie_id', 'actor_id')
    )

    def __str__(self):
        return f"{self.title} ({self.year})#{self.pk}"
    

class Person(models.Model):
    class Meta:
        #db_table = 'data.person'
        db_table = 'person'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    birthdate = models.DateField(null=True, blank=True)

    
# Association explicit Class, advantages:
# - access to assocation extra columns
# - choose FK column names
class Play(models.Model):
    class Meta:
        #db_table = 'data.play'
        db_table = 'play'

    # implicit or explicit PK column (id)
    movie = models.ForeignKey(to=Movie, on_delete=models.DO_NOTHING) # custom: db_column=
    actor = models.ForeignKey(to=Person, on_delete=models.DO_NOTHING) # custom: db_column=
    role = models.CharField(max_length=100, null=True, blank=True)
    

