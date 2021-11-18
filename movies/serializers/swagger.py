from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers, validators
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


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()


class RankBodySerializer(serializers.Serializer):
    rank = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="0-5 사이 정수 입력"
    )
