from django.urls import path, include
from . import html_views


urlpatterns = [
    path('browse/movies/', html_views.MovieList.as_view(), name="html-movie-list"),
    path('browse/movies/<int:pk>', html_views.MovieDetail.as_view(), name="html-movie-detail"),
]
