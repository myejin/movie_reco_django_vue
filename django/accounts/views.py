import math
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSimpleSerializer, UserRequestSerializer, GenreUpdateSerializer
from movies.models import MovieRank, Genre, Movie
from movies.serializers import MovieListSerializer, MovieRankSerializer, GenreSerializer
from .schemas import *


@swagger_auto_schema(
    method="post",
    operation_description="새로운 유저를 생성합니다. (회원가입)",
    request_body=UserRequestSerializer,
    responses=signup_res_schema,
)
@api_view(["POST"])
def signup(request):
    if request.data.get("password") != request.data.get("password2"):
        return Response({"error": "비밀번호가 일치하지 않습니다."}, status.HTTP_400_BAD_REQUEST)

    serializer = UserSimpleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@swagger_auto_schema(
    method="get",
    operation_description="해당 유저의 팔로우/팔로잉 수 및 팔로워 데이터를 반환합니다.",
    manual_parameters=[token_param],
    responses=follow_get_schema,
)
@swagger_auto_schema(
    method="post",
    operation_description="다른 유저와 팔로우 관계를 시작/취소(토글)합니다.",
    manual_parameters=[token_param],
    responses=follow_res_schema,
)
@api_view(["GET", "POST"])
def follow(request, username):
    you = get_object_or_404(get_user_model(), username=username)

    def follow_post():
        if request.user != you:
            if you.followers.filter(pk=request.user.pk).exists():
                you.followers.remove(request.user)
                msg = f"{username} 님을 팔로우 취소했습니다."
            else:
                you.followers.add(request.user)
                msg = f"{username} 님을 팔로우했습니다."
        data = {
            "follower_count": you.followers.count(),
            "following_count": you.followings.count(),
        }
        return Response(data, status.HTTP_200_OK)
    
    def follow_get():
        serializer = UserSimpleSerializer(you.followers.all(), many=True)
        data = {
            "follower_count": you.followers.count(),
            "following_count": you.followings.count(),
            "follower_list": serializer.data,
        }
        return Response(data, status.HTTP_200_OK)

    if request.user.is_authenticated:
        if request.method == 'GET':
            return follow_get()
        else:
            return follow_post()        
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method="get",
    operation_description="당신과 패턴이 비슷한 다른 유저를 추천합니다.\n추천기준은 높은 평점을 준 영화리스트의 유사도를 기반으로 설정했습니다.",
    manual_parameters=[token_param],
    responses=similar_res_schema,
)
@api_view(["GET"])
def similar(request):
    my_like_movies = MovieRank.objects.filter(user=request.user, rank__gte=4).values("movie")
    count = math.ceil(my_like_movies.count() / 2)
    users = get_list_or_404(get_user_model())
    similar_users = []
    for user in users:
        if user == request.user:
            continue
        your_like_movies = MovieRank.objects.filter(user=user, rank__gte=4).values("movie")
        if my_like_movies.difference(your_like_movies).count() < count:
            rate_movies = list(MovieRank.objects.filter(user=user).order_by("-rank").values("movie_id"))
            for i in range(len(rate_movies)):
                movie = get_object_or_404(Movie, pk=rate_movies[i]['movie_id'])
                serializer = MovieListSerializer(movie)
                rate_movies[i]['movie_detail'] = serializer.data 

            data = {
                "user_id": user.pk,
                "username": user.username,
                "rate_movies": rate_movies,
            }
            similar_users.append(data)

    data = {
        "count": len(similar_users),
        "users": similar_users,
    }
    return Response(data, status.HTTP_200_OK)


@swagger_auto_schema(
    method="get",
    operation_description="유저의 정보를 반환합니다.\n위시리스트, 평점을 매긴 영화리스트, 선호하는 장르 정보를 포함합니다.",
    manual_parameters=[token_param],
    responses=profile_res_schema,
)
@api_view(["GET"])
def profile(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), username=username)
        rate_movies = MovieRank.objects.filter(user=user)
        data = {
            "id": user.pk,
            "username": username,
            "wish_movies": MovieListSerializer(user.wish_movies.all(), many=True).data,
            "rate_movies": MovieRankSerializer(rate_movies, many=True).data,
            "like_genres": GenreSerializer(user.like_genres.all(), many=True).data,
        }
        return Response(data, status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method="put",
    operation_description="선호하는 장르 리스트를 업데이트 합니다.",
    manual_parameters=[token_param],
    request_body=GenreUpdateSerializer,
    responses=genres_update_res_schema,
)
@api_view(["PUT"])
def genres_update(request):
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), pk=request.user.pk)
        new_genre_ids = request.data["genres"]
        old_genre_ids = user.like_genres.all().values("id")

        for genre in old_genre_ids:
            if genre["id"] not in new_genre_ids:
                user.like_genres.remove(genre["id"])
        for genre_id in new_genre_ids:
            if not user.like_genres.filter(pk=genre_id).exists():
                genre = get_object_or_404(Genre, id=genre_id)
                user.like_genres.add(genre)

        serializer = GenreSerializer(user.like_genres.all(), many=True)
        return Response({"genres": serializer.data}, status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
