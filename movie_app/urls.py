from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('movies/', views.MovieList.as_view(), name="html-movie-list"),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name="html-movie-detail"),
    path('directors/', views.DirectorList.as_view(), name="html-director-list"),
    path('directors/<int:pk>', views.DirectorDetail.as_view(), name="html-director-detail"),
]
