from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Genre
from ..serializers import (
    GenreSerializer,
    MovieListSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from ..schemas import genre_list_schema, movie_of_genre_schema


@swagger_auto_schema(
    method="get",
    operation_description="모든 영화장르 정보를 반환합니다.",
    responses=genre_list_schema,
)
@api_view(["GET"])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response({"genres": serializer.data}, status.HTTP_200_OK)


@swagger_auto_schema(
    method="get",
    operation_description="특정 장르의 모든 영화를 반환합니다.",
    responses=movie_of_genre_schema,
)
@api_view(["GET"])
def movie_of_genre(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    movies = genre.movies.all()
    serializer = MovieListSerializer(movies, many=True)
    data = {
        "genre_name": genre.name,
        "movies": serializer.data,
    }
    return Response(data, status.HTTP_200_OK)
