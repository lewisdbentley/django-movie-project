from rest_framework import serializers
from .models import Movie, Director, Genre, Language, Actor, Quote, Review, Profile, Vote
from django.contrib.auth.models import User



class ProfileSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Profile instances into representations such as json.
    """
    
    class Meta:
        """
        Specify the model and fields.
        """
        model = Profile
        fields = ['user', 'bio']


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


class DirectorSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Director instances into representations such as json.
    """
    
    class Meta:
        """
        Specify the model and fields.
        """
        model = Director
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class GenreSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Genre instances into representations such as json.
    """

    class Meta:
        """
        Specify the model and fields.
        """
        model = Genre
        fields = ['name',]


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


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Review instances into representations such as json.
    """

    class Meta:
        """
        Specify the model and fields.
        """
        model = Review
        fields = ['owner', 'title', 'text']


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


class MovieSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize movie instances into representations such as json.
    """
    genres = GenreSerializer(read_only=True, many=True)
    cast = ActorSerializer(read_only=True, many=True)
    language = LanguageSerializer(read_only=True)
    directed_by = DirectorSerializer(read_only=True)
    quotes = serializers.StringRelatedField(many=True, required=False)
    reviews = ReviewSerializer(read_only=True, many=True)
    vote = VoteSerializer(read_only=True)

    class Meta:
        """
        Specify the model and fields.
        """
        model = Movie
        fields = [
            'directed_by',
            'title',
            'language',
            'genres',
            'cast', 
            'runtime',
            'description',
            'date_released',
            'quotes',
            'reviews',
            'vote',
        ]


class QuoteSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Quote instances into representations such as json.
    """
    by = ActorSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        """
        Specify the model and fields.
        """
        model = Quote
        fields = ['text', 'by', 'movie']
    

class ActorSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize Actor instances into representations such as json.
    """
    quotes = QuoteSerializer(read_only=True)

    class Meta:
        """
        Specify the model and fields.
        """
        model = Actor
        fields = ['first_name', 'last_name', 'quotes', 'date_of_birth', 'date_of_death',]


# x@e2e4.email