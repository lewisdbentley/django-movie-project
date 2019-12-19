from rest_framework import serializers
from .models import Movie, Director, Genre, Language, Actor, Quote, Profile, Vote
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Profile instances into representations such as json.
    """
    created_movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        """
        Specify the model and fields.
        """
        model = Profile
        fields = ['user', 'bio', 'created_movies',]


class UserSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize User instances into representations such as json.
    """
    profile = ProfileSerializer()
    
    class Meta:
        """
        Specify the model and fields.
        """
        model = User
        fields = ['username', 'is_superuser', 'profile',]


class LanguageSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Language instances into representations such as json.
    """

    class Meta:
        """
        Specify the model and fields.
        """
        model = Language
        fields = ['name']


class VoteSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Vote instances into representations such as json.
    """

    class Meta:
        """
        Specify the model and fields.
        """
        model = Vote
        fields = ['movie', 'times_rated', 'total_rating', 'final_rating',]
        

class ActorSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Actor instances into representations such as json.
    """
    movies = serializers.StringRelatedField(many=True)
    quotes = serializers.StringRelatedField(many=True)

    class Meta:
        """
        Specify the model and fields.
        """
        model = Actor
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'movies', 'quotes',]
        

class MovieSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize movie instances into representations such as json.
    """
    owner = serializers.ReadOnlyField(source='owner.user.username')
    language = LanguageSerializer(required=False)
    genres = serializers.StringRelatedField(many=True, required=False)
    cast = ActorSerializer(many=True, required=False)
    directed_by = serializers.StringRelatedField(required=False)
    quotes = serializers.StringRelatedField(many=True, required=False)
    vote = VoteSerializer(required=False)

    class Meta:
        """
        Specify the model and fields.
        """
        model = Movie
        fields = [
            'owner',
            'directed_by',
            'title',
            'language',
            'genres',
            'cast', 
            'runtime',
            'description',
            'date_released',
            'quotes',
            'vote',
        ]


class QuoteSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Quote instances into representations such as json.
    """
    by = ActorSerializer()
    movie = MovieSerializer()

    class Meta:
        """
        Specify the model and fields.
        """
        model = Quote
        fields = ['text', 'by', 'movie']


class DirectorSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Director instances into representations such as json.
    """
    movies = MovieSerializer(many=True)

    class Meta:
        """
        Specify the model and fields.
        """
        model = Director
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'movies']


class GenreSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Genre instances into representations such as json.
    """
    movies = MovieSerializer(many=True)

    class Meta:
        """
        Specify the model and fields.
        """
        model = Genre
        fields = ['name', 'movies']


# x@e2e4.email