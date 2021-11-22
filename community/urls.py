from django.urls import path
from . import views

# community/
urlpatterns = [
    path("reviews/<int:review_pk>/", views.review_update_delete, name="review_update_delete"),
    path("<int:article_pk>/reviews/", views.review_list_create, name="review_list_create"),
    path("<int:article_pk>/", views.article_update_delete, name="article_update_delete"),
    path("", views.article_list_create, name="article_list_create"),
]
