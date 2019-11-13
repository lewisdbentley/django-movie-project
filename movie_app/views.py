from rest_framework import viewsets
from rest_framework import generics
from django.http import HttpResponse
from .models import Movie, Director, Actor
from django.contrib.auth.models import User
from .serializers import MovieSerializer, DirectorSerializer, UserSerializer, ActorSerializer


class MovieListView(generics.ListCreateAPIView):
    """
    A view to list and create movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update and destroy movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorListView(generics.ListCreateAPIView):
    """
    A view to list and create directors.
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update and destroy movies.
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorListView(generics.ListCreateAPIView):
    """
    A view to list and create actors.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update and destroy actors.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    """
    A Viewset to retrieve, update and destroy directors.
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


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

