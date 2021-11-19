from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

# accounts/

urlpatterns = [
    path("similar/", views.similar, name="similar"),
    path("signup/", views.signup, name="signup"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("<username>/follow/", views.follow, name="follow"),
    path("<username>/profile/", views.profile, name="profile"),
]
