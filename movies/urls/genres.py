from django.urls import path
from ..views import genres

# genres/

urlpatterns = [
    path("<int:genre_pk>/movies/", genres.movie_of_genre, name="movie_of_genre"),
    path("", genres.genre_list, name="genre_list"),
]
