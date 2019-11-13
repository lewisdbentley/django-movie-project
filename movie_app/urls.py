from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('directors', views.DirectorViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update_profile/<int:user_id>/', views.update_profile, name="update_profile"),
    path('update_vote/<int:movie_id>/', views.update_vote, name="update_vote"),
]