from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from .models import Movie
from rest_framework.response import Response
from .serializers import MovieSerializer


@api_view(["GET"])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET", "PATCH", "DELETE"])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "GET":
        serializer = MovieSerializer(movie)  # serializer는 JSON으로 변환해주는 것이라 생각하면 된다.
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = MovieSerializer(data=request.data, instance=movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Movie Edited!"})
    else:
        movie.delete()
        return Response({"message": "Movie deleted!"})


@api_view(["POST"])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
