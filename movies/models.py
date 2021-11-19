from django.db import models
from django.conf import settings


class Genre(models.Model):
    tid = models.IntegerField()
    name = models.CharField(max_length=20)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_genres")

    def __str__(self):
        return f"{self.pk}: {self.name}"


class Actor(models.Model):
    tid = models.IntegerField()
    name = models.CharField(max_length=30)
    profile_path = models.TextField(default=False)

    def __str__(self):
        return f"{self.pk}: {self.name}"


class Movie(models.Model):
    tid = models.IntegerField()
    title = models.CharField(max_length=50)
    overview = models.TextField(default="")
    release_date = models.DateTimeField(auto_now_add=True)
    poster_path = models.TextField(default="")
    director = models.CharField(max_length=50, default="")
    rate_user_count = models.IntegerField(default=0)
    total_rank = models.IntegerField(default=0)

    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")
    wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="wish_movies")
    rate_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="rate_movies", through="MovieRank"
    )

    def __str__(self):
        return f"{self.pk}: {self.title}"


class MovieRank(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rank = models.IntegerField(default=5, choices=list(zip(range(1, 6), range(1, 6))))
