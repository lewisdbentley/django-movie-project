from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name="movie-list"),
    path('movies/<int:pk>', views.MovieDetailView, name="movie-detail"),
    path('directors/', views.DirectorListView.as_view(), name="director-list"),
    path('director/<int:pk>', views.DirectorDetailView.as_view(), name="director-detail"),
    path('actors/', views.ActorListView.as_view(), name="actor-list"),
    path('actors/<int:pk>', views.ActorDetailView.as_view(), name="actor-detail"),
    path('update_profile/<int:user_id>/', views.update_profile, name="update_profile"),
    path('update_vote/<int:movie_id>/', views.update_vote, name="update_vote"),
]