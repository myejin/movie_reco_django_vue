from django.db import models
from django.conf import settings


class Genre(models.Model):
    tid = models.IntegerField()
    name = models.CharField(max_length=20)

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
    overview = models.TextField(default=False)
    release_date = models.DateTimeField(auto_now_add=True)
    poster_path = models.TextField(default=False)
    director = models.CharField(max_length=50, default=False)
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


class Rankset(models.IntegerChoices):
    ONE = 1, "1"
    TWO = 2, "3"
    THREE = 3, "3"
    FOUR = 4, "4"
    FIVE = 5, "5"


class MovieRank(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rank = models.IntegerField(default=Rankset.FIVE, choices=Rankset.choices)
