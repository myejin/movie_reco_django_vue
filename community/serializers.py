from django.contrib.auth import get_user_model
from rest_framework import serializers
from movies.models import Movie
from .models import Article, Review


class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ("username",)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                "id",
                "title",
            )

    author = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "author",
            "movie",
            "position",
            "is_finished",
            "created_at",
            "updated_at",
        )


class ArticleCreateSerializer(serializers.Serializer):
    movie_pk = serializers.IntegerField()
    position = serializers.CharField()


class ArticleUpdateSerializer(serializers.Serializer):
    is_finished = serializers.BooleanField(default=False)


class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ("username",)

    author = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "author",
            "content",
            "created_at",
            "updated_at",
        )


class ReviewBodySerializer(serializers.Serializer):
    content = serializers.CharField()
