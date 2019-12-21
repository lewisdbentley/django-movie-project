from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Movie, Director, MovieComment
from .forms import MovieVoteForm, MovieCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


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


class MovieCreate(LoginRequiredMixin, generic.edit.CreateView):
    """
    A view to create a new movie.
    """
    model = Movie
    fields = {'directed_by', 'title', 'language', 'genres', 'cast', 'runtime', 'description', 'date_released'}
    initial = {'runtime': '259'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.profile
        return super(MovieCreate, self).form_valid(form)


def MovieCreateNew(request):
    if request.method == "POST":
        form = MovieCreateForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = MovieCreateForm()
    return render(request, "movie_app/MovieCreateNew.html", {'form': form})


class MovieUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    """
    A view to update a movie.
    """
    model = Movie
    fields = {'title', 'directed_by', 'runtime'}

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user.profile


class MovieDelete(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    """
    A view to delete a movie.
    """
    model = Movie
    success_url = reverse_lazy('html-movie-list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user.profile


def MovieVote(request, pk):
    """
    A view to allow users to vote on a movie.
    """
    movie = get_object_or_404(Movie, id=pk)

    # If this is a POST request then process the Form data.
    if request.method == 'POST':
        
        # Create a form instance and populate it with data from the request.
        form = MovieVoteForm(request.POST)

        # Check if the form is valid.
        if form.is_valid():
            # Process the data in form.cleaned_data as required. (Here we write the data to the vote associated with the movie)
            to_add = form.cleaned_data.get('vote')
            movie.vote.calc_rating(to_add=to_add)
            movie.save()

            # Redirect to a new URL.
            return HttpResponseRedirect(reverse('html-movie-detail', kwargs={'pk':movie.id}))
        
        else:
            context = {
                'form': form,
                'movie': movie,
            }

            return render(request, 'movie_app/movie_vote.html', context)

    # If this is a GET (or any other method) create the default form.
    else:
        form = MovieVoteForm

        context = {
            'form': form,
            'movie': movie,
        }

        return render(request, 'movie_app/movie_vote.html', context)


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


class DirectorCreate(LoginRequiredMixin, generic.edit.CreateView):
    """
    A view to create a new director.
    """
    model = Director
    fields = {'first_name', 'last_name', 'date_of_birth', 'date_of_death',}
    initial = {'date_of_birth': '01/01/2000'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.profile
        return super(DirectorCreate, self).form_valid(form)
    
class DirectorUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    """
    A view to update a director.
    """
    model = Director
    fields = {'date_of_birth', 'date_of_death', 'last_name'}

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user.profile

class DirectorDelete(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    """
    A view to delete a director.
    """
    model = Director
    success_url = reverse_lazy('html-director-list')

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user.profile


class MovieCommentCreate(LoginRequiredMixin, generic.edit.CreateView):
    """
    A view to create a comment.
    """
    model = MovieComment
    fields = {'text'}
    initial = {'text': 'Jeremy Hunt'}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user.profile
        obj.movie = Movie.objects.get(pk=self.kwargs['pk'])
        return super(MovieCommentCreate, self).form_valid(form)


class MovieCommentUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    """
    A view to update a comment.
    """
    model = MovieComment
    fields = {'text'}

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user.profile


class MovieCommentDelete(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    """
    A view to delete a comment.
    """
    model = MovieComment

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user.profile

    def get_success_url(self):
        movie = self.object.movie
        return reverse_lazy('html-movie-detail', kwargs={'pk':movie.id})