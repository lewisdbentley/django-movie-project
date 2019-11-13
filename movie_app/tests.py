from django.test import TestCase
from django.urls import reverse
from .models import Movie, Director, Language, Genre, Actor, Quote
from rest_framework.test import APIClient
from rest_framework import status


class MovieTestCase(TestCase):
    """
    This class defines the test suite for the Movie Model
    """


class ViewTestCase(TestCase):
    """
    This class defines the test suite for the API views
    """
    def setUp(self):
        """
        Define the test client and other variables
        """
        self.client = APIClient()
        self.director = Director(first_name="Quentin", last_name="Tarentino")
        self.director.save()
        self.title = "Once Upon a Time in Hollywood"
        self.language = Language(name="English")
        self.language.save()
        self.genres = Genre(name="Drama")
        self.genres.save()
        self.cast = Actor(first_name="Leonardo", last_name="DiCaprio")
        self.cast.save()
        self.runtime = 159
        self.description = "Quentin Tarantino's ninth feature film..."
        self.date_released = "2019-07-26"
        self.movie = Movie(
            directed_by = self.director,
            title = self.title,
            language = self.language,
            runtime = self.runtime,
            description = self.description,
            date_released = self.date_released,
            )
        self.movie.save()
        self.movie.genres.add(self.genres)
        self.movie.cast.add(self.cast)
        self.movie.save()
        
    def test_api_can_get_a_movie(self):
        """
        Test if api can get a movie in json format
        """
        movie = Movie.objects.get(title="Once Upon a Time in Hollywood")
        response = self.client.get(reverse("movie-detail", kwargs={"pk": movie.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, movie)

    def test_api_displays_all_fields_of_movie_instances(self):
        """
        Test if api displays all fields of a movie instance
        """
        movie = Movie.objects.get(title="Once Upon a Time in Hollywood")
        director = movie.directed_by
        response = self.client.get(reverse("movie-detail", kwargs={"pk": movie.id}), format="json")
        self.assertContains(response, text="Once Upon a Time in Hollywood")
        self.assertEqual(movie.directed_by, director)
        self.assertEqual(movie.runtime, 159)