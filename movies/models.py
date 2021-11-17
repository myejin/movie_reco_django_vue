from django.db import models


class Genre(models.Model):
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
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return f"{self.pk}: {self.title}"
