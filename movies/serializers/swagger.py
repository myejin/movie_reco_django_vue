from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers


class RankBodySerializer(serializers.Serializer):
    rank = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], help_text="0-5 사이 정수 입력"
    )
