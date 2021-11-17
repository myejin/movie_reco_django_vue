import requests
from decouple import config
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Actor, Movie
from .serializers import GenreSerializer, ActorSerializer, MovieListSerializer, MovieSerializer

API_KEY = config("TMDB_API")


def init_genre():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR"
    resp = requests.get(url).json()
    genres = resp["genres"]
    for genre in genres:
        serializer = GenreSerializer(data=genre)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


def init_movie():
    for i in range(1, 11):
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=ko-KR&region=KR&page={i}"
        resp = requests.get(url).json()
        movies = resp["results"]
        for movie in movies:
            new_movie = {}
            new_movie["tid"] = movie["id"]
            new_movie["title"] = movie["title"]
            new_movie["overview"] = movie["overview"]
            new_movie["release_date"] = movie["release_date"]
            new_movie["poster_path"] = movie["backdrop_path"]
            new_movie["genres"] = movie["genre_ids"]

            serializer = MovieSerializer(data=new_movie)
            if serializer.is_valid(raise_exception=True):
                serializer.save()


def init_actor():
    pass


@api_view(["GET"])
def initiate_database(request):
    try:
        init_genre()
        init_movie()
        init_actor()
        data = {
            "movie_count": Movie.objects.all().count(),
            "genre_count": Genre.objects.all().count(),
            "actor_count": Actor.objects.all().count(),
        }
        return Response({"data": data}, status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": e}, status.HTTP_500_INTERNAL_SERVER_ERROR)
