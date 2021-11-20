from django.urls import path
from . import views

# community/
urlpatterns = [
    path("<int:article_pk>/", views.article_update_delete, name="article_update_delete"),
    path("", views.article_list_create, name="article_list_create"),
]
