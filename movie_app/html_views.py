from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie


class MovieList(APIView):
    """
    A view to return a HTML response of all movies
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movie_app/movie_list.html'

    def get(self, request):
        queryset = Movie.objects.all()
        return Response({'movies': queryset})


class MovieDetail(APIView):
    """
    A view to return a HTML response of a movie
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'movie_app/movie_detail.html'

    def get(self, request, pk):
        queryset = Movie.objects.get(id=pk)
        return Response({'movie': queryset})
