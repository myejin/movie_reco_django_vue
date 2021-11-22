from django.urls import path

from . import views

urlpatterns = [
    path("<str:username>/room/", views.chat_room, name="chat_room"),
    path("<str:username>/", views.send_message, name="send_message"),
]
