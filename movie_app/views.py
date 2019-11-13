from rest_framework import viewsets
from django.http import HttpResponse
from .models import Movie, Director
from django.contrib.auth.models import User
from .serializers import MovieSerializer, DirectorSerializer, UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    A Viewset to retrieve, update and destroy movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    """
    A Viewset to retrieve, update and destroy directors.
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A Viewset to retrieve, update and destroy users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

def update_profile(request, user_id):
    """
    A view to update a profile associated with a user.
    """
    user = User.objects.get(id=user_id)
    user.profile.bio = "Lorem ipsum dolor sit amet, consectetur adipisicing elit..."
    user.save()
    return HttpResponse("Profile updated!")

def update_vote(request, movie_id):
    """
    A view to update a vote associated with a movie.
    """
    movie = Movie.objects.get(id=movie_id)
    movie.vote.total_rating += 5
    movie.vote.times_rated += 1
    movie.save()
    return HttpResponse("Movie updated!")