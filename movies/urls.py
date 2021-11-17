from django.urls import path
from . import views

urlpatterns = [
    path("init/", views.initiate_database, name="initiate_database"),
]
