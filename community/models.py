from django.contrib.auth import get_user_model
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="reviews")
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.content[:5]}"
