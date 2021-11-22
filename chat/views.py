from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .schemas import *
from .models import ChatRoom, Message
from .serializers import MessageSerializer, MsgSimpleSerializer, MsgBodySerializer


@swagger_auto_schema(
    method="get",
    operation_description="채팅방 이름과 주고받은 메세지를 반환합니다.",
    manual_parameters=[token_param],
    responses=go_room_res_schema,
)
@swagger_auto_schema(
    method="post",
    operation_description="새로운 채팅방을 생성 후 채팅방 이름와 주고받은 메세지를 반환합니다.",
    manual_parameters=[token_param],
    responses=create_room_res_schema,
)
@api_view(["GET", "POST"])
def chat_room(request, username):
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    me = request.user
    you = get_object_or_404(get_user_model(), username=username)

    def create_room():
        if me.pk < you.pk:
            name = f"{me.pk}_{you.pk}"
        else:
            name = f"{you.pk}_{me.pk}"
        room = ChatRoom.objects.filter(name=name)
        if room:
            return Response({"message": "이미 채팅방이 존재합니다."}, status.HTTP_400_BAD_REQUEST)
        room = ChatRoom.objects.create(name=name)
        data = {
            "room_name": room.name,
            "messages": [],
        }
        return Response(data, status.HTTP_201_CREATED)

    def go_room():
        if me.pk < you.pk:
            room = ChatRoom.objects.filter(name=f"{me.pk}_{you.pk}")
        else:
            room = ChatRoom.objects.filter(name=f"{you.pk}_{me.pk}")
        if not room:
            return Response({"message": "아직 채팅방이 없습니다. POST 요청을 시도하세요."}, status.HTTP_404_NOT_FOUND)
        else:
            room = room[0]
            messages = Message.objects.filter(room=room)
            serializer = MessageSerializer(messages, many=True)
            data = {"room_name": room.name, "messages": serializer.data}
            return Response(data, status.HTTP_200_OK)

    if request.method == "GET":
        return go_room()
    else:
        return create_room()


@swagger_auto_schema(
    method="post",
    operation_description="새로운 메세지를 생성하고, 받는 유저에게 알람을 전달합니다.",
    manual_parameters=[token_param],
    request_body=MsgBodySerializer,
    responses=send_msg_res_schema,
)
@api_view(["POST"])
def send_message(request, username):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), username=username)
        if me.pk < you.pk:
            name = f"{me.pk}_{you.pk}"
        else:
            name = f"{you.pk}_{me.pk}"
        room = get_object_or_404(ChatRoom, name=name)
        msg = Message.objects.create(
            room=room, from_user=me, to_user=you, content=request.data["content"]
        )
        serializer = MsgSimpleSerializer(msg)
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
