from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import ChatRoom, Message


class MessageSerializer(serializers.ModelSerializer):
    class ChatRoomSerializer(serializers.ModelSerializer):
        class Meta:
            model = ChatRoom
            fields = ("name",)
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ("username",)
    
    room = ChatRoomSerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = (
            "room",
            "author",
            "content",
            "created_at",
        )

class MsgSimpleSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Message
        fields = (
            "content",
            "created_at",
        )

class MsgBodySerializer(serializers.Serializer):
    content = serializers.CharField()
