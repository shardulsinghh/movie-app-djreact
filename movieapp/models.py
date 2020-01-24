from django.db import models

class Genre(models.Model):

    title = models.CharField(max_length=20, primary_key=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Movie(models.Model):
    name= models.CharField(max_length=100, default='N/A')
    popularity= models.IntegerField(default=0)
    director= models.CharField(max_length=50, default='N/A')
    imdb_score= models.FloatField(null = True, blank = True, default = None)
    
    genre= models.ManyToManyField(Genre, related_name='genre')


    def __str__(self):
        return self.name
    