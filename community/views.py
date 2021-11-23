from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Review
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from movies.models import Movie
from .schemas import *


@swagger_auto_schema(
    method="get",
    operation_description="커뮤니티의 모든 게시물 정보를 반환합니다.",
    manual_parameters=[token_param],
    responses=article_list_schema,
)
@swagger_auto_schema(
    method="post",
    operation_description="새로운 게시물을 생성합니다.",
    manual_parameters=[token_param],
    request_body=ArticleCreateSerializer,
    responses=article_res_schema(201),
)
@api_view(["GET", "POST"])
def article_list_create(request):
    def article_list():
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        data = {
            "count": len(serializer.data),
            "articles": serializer.data,
        }
        return Response(data, status.HTTP_200_OK)

    def article_create(request):
        movie = get_object_or_404(Movie, pk=request.data["movie_pk"])
        latitude = request.data["latitude"]
        longitude = request.data["longitude"]
        article = Article.objects.create(author=request.user, movie=movie, latitude=latitude, longitude=longitude)
        return Response(ArticleSerializer(article).data, status=status.HTTP_201_CREATED)

    if request.user.is_authenticated:
        if request.method == "GET":
            return article_list()
        else:
            return article_create(request)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method="put",
    operation_description="해당 게시물의 마감 여부를 변경합니다.",
    manual_parameters=[token_param],
    request_body=ArticleUpdateSerializer,
    responses=article_res_schema(200),
)
@swagger_auto_schema(
    method="delete",
    operation_description="해당 게시물을 삭제합니다.",
    manual_parameters=[token_param],
    responses=delete_schema,
)
@api_view(["PUT", "DELETE"])
def article_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user != article.author:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def article_update(request):
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def article_delete():
        article.delete()
        data = {
            "message": f"{article_pk}번 게시물이 삭제되었습니다.",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        return article_update(request)
    else:
        return article_delete()


@swagger_auto_schema(
    method="get",
    operation_description="특정 게시물의 모든 리뷰를 반환합니다.",
    manual_parameters=[token_param],
    responses=review_list_schema,
)
@swagger_auto_schema(
    method="post",
    operation_description="특정 게시물의 새로운 리뷰를 생성합니다.",
    manual_parameters=[token_param],
    request_body=ReviewBodySerializer,
    responses=review_res_schema(201),
)
@api_view(["GET", "POST"])
def review_list_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def review_list():
        reviews = article.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        data = {
            "article_id": article_pk,
            "reviews": serializer.data,
        }
        return Response(data)

    def review_create(request):
        content = request.data["content"]
        new_review = Review.objects.create(author=request.user, article=article, content=content)
        serializer = ReviewSerializer(new_review)
        data = {
            "article_id": article_pk,
            "review": serializer.data,
        }
        return Response(data, status=status.HTTP_201_CREATED)

    if request.user.is_authenticated:
        if request.method == "GET":
            return review_list()
        else:
            return review_create(request)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method="delete",
    operation_description="해당 리뷰를 삭제합니다.",
    manual_parameters=[token_param],
    responses=delete_schema,
)
@swagger_auto_schema(
    method="put",
    operation_description="리뷰의 내용을 변경합니다.",
    manual_parameters=[token_param],
    request_body=ReviewBodySerializer,
    responses=review_res_schema(200),
)
@api_view(["PUT", "DELETE"])
def review_update_delete(request, review_pk):
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    review = get_object_or_404(Review, pk=review_pk)
    if review.author != request.user:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def review_update():
        review.content = request.data["content"]
        review.save()
        serializer = ReviewSerializer(review)
        data = {
            "article_id": review.article.pk,
            "review": serializer.data,
        }
        return Response(data)

    def review_delete():
        review.delete()
        data = {
            "message": f"{review_pk}번 리뷰가 삭제되었습니다.",
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        return review_update()
    else:
        return review_delete()
