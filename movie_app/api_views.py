from rest_framework import viewsets, generics, permissions
from .models import Movie, Director, Actor, Profile
from .serializers import MovieSerializer, DirectorSerializer, ProfileSerializer, ActorSerializer
from .permissions import isOwnerOrReadOnly


class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = []

    def get_permissions(self):
        """
        Set the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = []
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [isOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, Serializer):
        """
        Save current user as owner field of created movie.
        """
        Serializer.save(owner=self.request.user.profile)


class DirectorViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions.
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class ActorViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset that provides the standard actions.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer