import datetime
from django.test import Client, TestCase
from django.urls import reverse
from .models import Movie, Director, Language, Genre, Actor, Quote
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class MovieTestCase(TestCase):
    """
    This class defines the test suite for the Movie Model
    """


class BaseTestCase(TestCase):
    """
    This class defines the test suite for the API views
    """
    def setUp(self):
        """
        Define test client and other variables.
        """

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
        self.create_user()
        self.create_other_user()

        # Logged In Client
        self.client = Client()
        self.client.login(username='sarah', password='secret')

        # Logged In REST Client
        self.rest_client = APIClient()
        self.rest_client.login(username='sarah', password='secret')


    def create_user(self):
        user = User(username='sarah', email='sarah@rebels.com')
        user.set_password('secret')
        user.save()


    def create_other_user(self):
        user = User(username='john', email='john@rebels.com')
        user.set_password('secret')
        user.save()


    def test_api_user_must_be_logged_in_to_create_movie(self):
        """
        Test api calls to create a movie should fail when not logged in.
        """
        # Create a rest client request without logging in
        rest_client_no_credentials = APIClient()
        response = rest_client_no_credentials.post('/api/movies/', {'title': 'The Irishman'}, format='json')

        self.assertEquals(response.status_code, 403)


    def test_logged_in_user_can_get_a_movie(self):
        """
        Test api can get a movie in json format.
        """
        movie = Movie.objects.get(title="Once Upon a Time in Hollywood")
        response = self.client.get(reverse("movie-detail", kwargs={"pk": movie.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, movie)


    def test_user_must_be_owner_to_update_movie(self):
        """
        Test api can get a movie in json format.
        """
        movie = self.client.post('/api/movies/', {'title': 'The Irishman'})
        movie = Movie.objects.get(title="The Irishman")
        self.client.login(username='john', password='secret')
        response = self.client.put(reverse("movie-detail", kwargs={"pk": movie.id}), {"title": "The Englishman"})

        self.assertEquals(response.status_code, 403)


    def test_api_displays_all_fields_of_movie_instance(self):
        """
        Test api displays all fields of a movie instance.
        """
        movie = Movie.objects.get(title="Once Upon a Time in Hollywood")
        director = movie.directed_by
        response = self.client.get(reverse("movie-detail", kwargs={"pk": movie.id}), format="json")

        self.assertContains(response, text="Once Upon a Time in Hollywood")
        self.assertEqual(movie.directed_by, director)
        self.assertEqual(movie.runtime, 159)
        self.assertEqual(movie.date_released, datetime.date(2019, 7, 26))

