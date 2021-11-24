from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from .models import Genre, Actor, Movie, MovieRank


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "tid",
            "name",
        )


class ActorSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                "id",
                "title",
                "poster_path",
            )

    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = (
            "tid",
            "name",
            "profile_path",
            "movies",
        )


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "poster_path",
        )


class MovieSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = "__all__"

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = "__all__"

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = (
                "id",
                "username",
            )

    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    wish_users = UserSerializer(many=True, read_only=True)
    rate_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "tid",
            "title",
            "overview",
            "release_date",
            "poster_path",
            "director",
            "rank_count",
            "rank_sum",
            "genres",
            "actors",
            "wish_users",
            "rate_users",
        )


class MovieRankSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                "id",
                "title",
                "poster_path",
            )

    movie = MovieListSerializer(read_only=True)

    class Meta:
        model = MovieRank
        fields = (
            "movie",
            "rank",
        )


class RankBodySerializer(serializers.Serializer):
    rank = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="0-5 사이 정수 입력"
    )
