from django.urls import path
from ..views import init_db, movie

# movies/

urlpatterns = [
    path("<int:movie_pk>/rate/", movie.rate, name="rate"),
    path("<int:movie_pk>/wish/", movie.wish, name="wish"),
    path("init/", init_db.initiate_database, name="initiate_database"),
]
