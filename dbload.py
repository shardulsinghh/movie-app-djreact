import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eco_energy_assignment.settings')
django.setup()

import json


from movieapp.models import Movie, Genre
from django.core.management.base import BaseCommand
from datetime import datetime

from django.core import serializers

from movieapp.api.serializers import MovieSerializer
 

def foo():
    print("FOO")
    with open('moviedata.json') as data_file:
        data = json.load(data_file)
    

    with open('genre.json') as data_file:
        genredata = json.load(data_file)
    print(genredata)
    genrelist = []
    genrekey = {}
    for genre in genredata:

        fields = genre["fields"]
        genrekey[fields["title"]] = genre["pk"]

    # print(genrekey)

    # print("Data PRinted")
    # print(type(data))
    id = 1
    for movie in data:
        # print("*****************                   ********************",movie)
        m = Movie( id = id, name = movie["name"], popularity= movie["99popularity"], director= movie["director"],imdb_score= movie["imdb_score"])
        # m.genre.set( [Genre.objects.get(title=genrekey[x.strip()]) for x in movie["genre"]])
        for gen in movie["genre"]:
            # print(gen.strip())
            genreObject = Genre.objects.get(title = gen.strip())
            m.save()
            genreObject.save()
            m.genre.add(genreObject)

        m.save()
        id+=1

        print('OUT FINE')
    # print(Genre.objects.get(title='Adventure'))

foo() 
