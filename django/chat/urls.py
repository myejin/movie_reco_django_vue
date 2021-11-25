from django.urls import path

from . import views

# chat/

urlpatterns = [
    path("rooms/", views.my_room_list, name="my_room_list"),
    path("<str:username>/room/", views.chat_room, name="chat_room"),
    path("<str:username>/", views.send_message, name="send_message"),
]
