from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import ChatRoom, Message


class MessageSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ("username",)

    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Message
        fields = (
            "from_user",
            "to_user",
            "content",
            "created_at",
        )


class MsgSimpleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = Message
        fields = (
            "content",
            "created_at",
        )


class MsgBodySerializer(serializers.Serializer):
    content = serializers.CharField()
