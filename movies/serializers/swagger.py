from rest_framework import serializers
from ..models import Genre


class GenreRequestSerializer(serializers.Serializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = "__all__"

    genres = serializers.ListField(child=GenreSerializer())
