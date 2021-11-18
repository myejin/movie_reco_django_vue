from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class UserRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()


class SimilarResponseSerializer(serializers.Serializer):
    class UserListSerializer(serializers.Serializer):
        class MovieSerializer(serializers.Serializer):
            movie_id = serializers.IntegerField()
            rank = serializers.IntegerField()

        user_id = serializers.IntegerField()
        username = serializers.CharField()
        rate_movies = serializers.ListField(child=MovieSerializer())

    count = serializers.IntegerField()
    users = serializers.ListField(child=UserListSerializer())
