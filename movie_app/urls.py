from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('movies/', views.MovieList.as_view(), name="html-movie-list"),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name="html-movie-detail"),
    path('movies/create', views.MovieCreate.as_view(), name="html-movie-create"),
    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="html-movie-update"),
    path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name="html-movie-delete"),
    path('directors/', views.DirectorList.as_view(), name="html-director-list"),
    path('directors/<int:pk>', views.DirectorDetail.as_view(), name="html-director-detail"),
    path('directors/create', views.DirectorCreate.as_view(), name="html-director-create"),
    path('directors/<int:pk>/update', views.DirectorUpdate.as_view(), name="html-director-update"),
    path('directors/<int:pk>/delete', views.DirectorDelete.as_view(), name="html-director-delete"),
    path('moviecomment/create/<int:pk>', views.MovieCommentCreate.as_view(), name="html-moviecomment-create"),
    path('moviecomment/<int:pk>/update', views.MovieCommentUpdate.as_view(), name="html-moviecomment-update"),
    path('moviecomment/<int:pk>/delete', views.MovieCommentDelete.as_view(), name="html-moviecomment-delete"),
    path('movies/<int:pk>/vote', views.MovieVote, name="movie-vote"),
    path('movies/createnew', views.MovieCreateNew, name="html-movie-create-new"),
]
