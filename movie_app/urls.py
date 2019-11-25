from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'directors', views.DirectorViewSet)
router.register(r'actors', views.ActorViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
