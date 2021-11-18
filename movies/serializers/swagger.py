from rest_framework import serializers
from ..models import Genre, Movie


class GenreRequestSerializer(serializers.Serializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = "__all__"

    genres = serializers.ListField(child=GenreSerializer())


class MovieOfGenreResponseSerializer(serializers.Serializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                "id",
                "title",
                "poster_path",
            )

    genre_name = serializers.CharField()
    movies = serializers.ListField(child=MovieListSerializer())
