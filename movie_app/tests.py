from django.test import TestCase
from django.urls import reverse
from .models import Movie, Director, Language, Genre, Actor, Quote
from django.contrib.auth.models import User
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
        Define test client and other variables.
        """
        self.client = APIClient()
        # Create a test Movie
        self.directed_by = Director(first_name="Quentin", last_name="Tarentino")
        self.directed_by.save()
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
            directed_by = self.directed_by,
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
        # Create a test User
        self.user = User(
            username="user",
            password="password",
        )
        self.user.save()

        
    def test_api_can_get_a_movie(self):
        """
        Test api can get a movie in json format.
        """
        movie = Movie.objects.get(title="Once Upon a Time in Hollywood")
        response = self.client.get(reverse("movie-detail", kwargs={"pk": movie.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, movie)


    def test_api_displays_all_fields_of_movie_instances(self):
        """
        Test api displays all fields of a movie instance.
        """
        movie = Movie.objects.get(title="Once Upon a Time in Hollywood")
        director = movie.directed_by
        response = self.client.get(reverse("movie-detail", kwargs={"pk": movie.id}), format="json")
        self.assertContains(response, text="Once Upon a Time in Hollywood")
        self.assertEqual(movie.directed_by, director)
        self.assertEqual(movie.runtime, 159)

    def test_api_can_create_a_movie(self):
        """
        Test api can create a movie.
        """
