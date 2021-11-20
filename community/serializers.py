from django.contrib.auth import get_user_model
from rest_framework import serializers
from movies.models import Movie
from .models import Article


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

    class Meta:
        model = Article
        fields = (
            "id",
            "author",
            "movie",
            "position",
            "is_finished",
        )


class ArticleCreateSerializer(serializers.Serializer):
    movie_pk = serializers.IntegerField()
    position = serializers.CharField()


class ArticleUpdateSerializer(serializers.Serializer):
    is_finished = serializers.BooleanField(default=False)
