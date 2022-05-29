from app1.models import Movie
from rest_framework.decorators import api_view
from app1.api.serializers import MovieSerializer
from rest_framework.response import Response

@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    serializer =  MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)