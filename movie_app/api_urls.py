from django.urls import path, include
from . import api_views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'directors', api_views.DirectorViewSet)
router.register(r'actors', api_views.ActorViewSet)
router.register(r'profiles', api_views.ProfileViewSet)
router.register(r'movies', api_views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
