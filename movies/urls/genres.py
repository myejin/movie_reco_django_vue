from django.urls import path
from ..views import genre

# genres/

urlpatterns = [
    path("<int:genre_pk>/movies/", genre.movie_of_genre, name="movie_of_genre"),
    path("", genre.genre_list, name="genre_list"),
]
