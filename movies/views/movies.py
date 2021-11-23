from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Movie, MovieRank
from ..serializers import (
    RankBodySerializer,
    MovieSerializer
)

from drf_yasg.utils import swagger_auto_schema
from ..schemas import token_param, msg_res_schema, rate_post_schema, rate_del_schema


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
    responses=rate_post_schema,
)
@swagger_auto_schema(
    method="delete",
    operation_description="해당 영화에 대한 평점을 철회합니다.",
    manual_parameters=[token_param],
    responses=rate_del_schema,
)
@api_view(["POST", "DELETE"])
def rate(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)

        if request.method == "DELETE":
            movie_rank = get_object_or_404(MovieRank, user=request.user, movie=movie)
            movie_rank.delete()
            data = {
                "msg": f"{movie.title} 에 대한 리뷰가 삭제되었습니다.",
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            if movie.rate_users.filter(pk=request.user.pk).exists():
                movie_rank = get_object_or_404(MovieRank, user=request.user, movie=movie)
                old_rank, movie_rank.rank = movie_rank.rank, request.data["rank"]
                movie_rank.save()
                movie.rank_sum += movie_rank.rank - old_rank
                movie.save()
            else:
                MovieRank.objects.create(user=request.user, movie=movie, rank=request.data["rank"])
                movie.rank_count += 1
                movie.rank_sum += request.data["rank"]
                movie.save()
            data = {
                "rank_count": movie.rank_count,
                "rank_sum": movie.rank_sum,
            }
            return Response(data, status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method="get",
    operation_description="특정 영화의 정보를 반환합니다.",
    manual_parameters=[token_param],
    # responses=msg_res_schema("쇼생크 탈출 이(가) 위시리스트에 추가되었습니다."),
)
@api_view(["GET"])
def detail(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
    