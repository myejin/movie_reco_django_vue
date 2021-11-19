from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Movie, MovieRank
from ..serializers import (
    RankBodySerializer,
)

from drf_yasg.utils import swagger_auto_schema
from ..schemas import token_param, msg_res_schema


@swagger_auto_schema(
    method="post",
    operation_description="해당 영화를 위시리스트에 추가/제거(토글)합니다.",
    manual_parameters=[token_param],
    responses=msg_res_schema("쇼생크 탈출 이(가) 위시리스트에 추가되었습니다."),
)
@api_view(["POST"])
def wish(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.wish_users.filter(pk=request.user.pk).exists():
            movie.wish_users.remove(request.user)
            msg = f"{movie.title} 이(가) 위시리스트에서 삭제되었습니다."
        else:
            movie.wish_users.add(request.user)
            msg = f"{movie.title} 이(가) 위시리스트에 추가되었습니다."
        return Response({"message": msg}, status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method="post",
    operation_description="해당 영화의 평점(1-5 사이 정수)를 추가/수정합니다.",
    manual_parameters=[token_param],
    request_body=RankBodySerializer,
    responses=msg_res_schema("평점을 등록했습니다."),
)
@api_view(["POST"])
def rate(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.rate_users.filter(pk=request.user.pk).exists():
            movie_rank = get_object_or_404(MovieRank, user=request.user, movie=movie)
            movie_rank.rank = request.data["rank"]
            movie_rank.save()
            msg = "평점을 변경했습니다."
        else:
            MovieRank.objects.create(user=request.user, movie=movie, rank=request.data["rank"])
            msg = "평점을 등록했습니다."
        return Response({"message": msg}, status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
