from rest_framework.response import Response
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Movie, Director


def index(request):
    """
    A home page to display dynamic data. 
    """

    # Generate counts of some of the main objects    
    num_movies = Movie.objects.count()
    num_directors = Director.objects.count()

    # Number of visits to this view, as counted in the session variable
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_movies': num_movies,
        'num_directors': num_directors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class MovieList(generic.ListView):
    """
    A view to return a HTML response of all movies.
    """
    model = Movie
    paginate_by = 10


class MovieDetail(generic.DetailView):
    """
    A view to return a HTML response of a movie.
    """
    model = Movie


class DirectorList(generic.ListView):
    """
    A view to return a HTML response of all directors.
    """
    model = Director


class DirectorDetail(generic.DetailView):
    """
    A view to return a HTML response of a director.
    """
    model = Director