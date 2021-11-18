import requests
from decouple import config
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Actor, Movie
from .serializers import GenreSerializer, ActorSerializer, MovieListSerializer, MovieSerializer

API_KEY = config("TMDB_API")


@api_view(["POST"])
def initiate_database(request):
    if not request.user.is_staff:
        return Response(
            {"error": f"{str(request.user)} 님은 접근 권한이 없습니다."}, status.HTTP_400_BAD_REQUEST
        )

    def init_genre():
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR"
        resp = requests.get(url).json()
        genres = resp["genres"]
        for genre in genres:
            data = {
                "tid": genre["id"],
                "name": genre["name"],
            }
            serializer = GenreSerializer(data=data)
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

                serializer = MovieSerializer(data=new_movie)
                if serializer.is_valid(raise_exception=True):
                    new_movie = serializer.save()
                    genres = Genre.objects.filter(tid__in=movie["genre_ids"])
                    new_movie.genres.set(genres)

    def init_actor_director():
        movies = Movie.objects.all()
        for movie in movies:
            url = f"https://api.themoviedb.org/3/movie/{movie.tid}/credits?api_key={API_KEY}&language=ko-KR"
            resp = requests.get(url).json()
            casts = resp["cast"]
            for cast in casts:
                if cast["known_for_department"] == "Acting":
                    if cast["popularity"] <= 6:
                        continue
                    actor = {
                        "tid": cast["id"],
                        "name": cast["name"],
                    }
                    if cast["profile_path"] is not None:
                        actor["profile_path"] = cast["profile_path"]
                    serializer = ActorSerializer(data=actor)
                    if serializer.is_valid(raise_exception=True):
                        actor = serializer.save()
                        actor.movies.add(movie.pk)

                elif cast["known_for_department"] == "Directing":
                    movie.director = cast["name"]
                    movie.save()

    try:
        init_genre()
        init_movie()
        init_actor_director()
        data = {
            "movie_count": Movie.objects.all().count(),
            "genre_count": Genre.objects.all().count(),
            "actor_count": Actor.objects.all().count(),
        }
        return Response({"data": data}, status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": e}, status.HTTP_500_INTERNAL_SERVER_ERROR)
