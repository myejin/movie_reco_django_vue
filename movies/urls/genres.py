from django.urls import path
from .. import views

# genres/

urlpatterns = [
    path("<int:genre_pk>/", views.movie_of_genre, name="movie_of_genre"),
    path("", views.genre_list, name="genre_list"),
]
