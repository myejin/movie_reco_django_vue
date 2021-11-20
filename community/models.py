from django.db import models
from django.conf import settings
from movies.models import Movie


class Article(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles"
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="articles")
    position = models.CharField(max_length=100, default="")
    is_finished = models.BooleanField(default=False)
