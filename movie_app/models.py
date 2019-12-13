from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import format_html
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    "Model representing genre of a movie"
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Language(models.Model):
    "Model representing language of a movie"
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Quote(models.Model):
    "Model representing genre of a movie"
    text = models.CharField(max_length=100)
    by = models.ForeignKey('Actor', related_name="quotes", on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey('Movie', related_name="quotes", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.text


class Director(models.Model):
    "Model representing a director"
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, default='')
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    "Model representing an actor"
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, default='')
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    "Model representing a review"
    owner = models.ForeignKey('auth.user', related_name="reviews", on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey('Movie', related_name="reviews", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)


class Profile(models.Model):
    "Model representing extra information that relates to a User instance."
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Movie(models.Model):
    "Model representing a movie"
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="created_movies", null=True)
    directed_by = models.ForeignKey(Director, related_name="movies", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    language = models.ForeignKey(Language, related_name="movies", on_delete=models.SET_NULL, null=True, blank=True)
    rated_by = models.ManyToManyField(Profile, related_name="has_rated", blank=True)
    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)
    cast = models.ManyToManyField(Actor, related_name="movies", blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_released = models.DateField(null=True, blank=True)

    def display_genre(self):
        """Create a string for the Genres. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genres.all()[:3])
    display_genre.short_description = "Genre"

    def display_cast(self):
        """Create a string for the Actors. This is required to display cast in Admin."""
        return ', '.join(f'{actor.first_name} {actor.last_name}' for actor in self.cast.all())

    def number_of_reviews(self):
        """Create an integer for the Reviews. This is required to represent number of reviews in Admin."""
        return self.reviews.count()
    number_of_reviews.short_description = "Reviews"

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('html-movie-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Vote(models.Model):
    "Model representing rating information that relates to a Movie instance."
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    times_rated = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    final_rating = models.IntegerField(default=0)

    def calc_rating(self):
        if self.times_rated > 0:
            r = self.total_rating / self.times_rated
            self.final_rating = r
            return r
        else:
            pass

    @receiver(post_save, sender=Movie)
    def create_movie_vote(sender, instance, created, **kwargs):
        if created:
            Vote.objects.create(movie=instance)

    @receiver(post_save, sender=Movie)
    def save_movie_vote(sender, instance, **kwargs):
        instance.vote.calc_rating()
        instance.vote.save()