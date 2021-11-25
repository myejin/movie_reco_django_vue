from django.urls import path
from ..views import init_db, movies

# movies/

urlpatterns = [
    path("<int:movie_pk>/", movies.detail, name="detail"),
    path("<int:movie_pk>/rate/", movies.rate, name="rate"),
    path("<int:movie_pk>/wish/", movies.wish, name="wish"),
    path("<str:movie_title>/", movies.search, name="search"),
    path("init/", init_db.initiate_database, name="initiate_database"),
]
