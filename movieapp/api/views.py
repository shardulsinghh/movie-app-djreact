from ..models import Movie
from .serializers import MovieSerializer

from rest_framework import viewsets

"""
Handle basic CRUD functionality using Rest-Framework
"""

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()