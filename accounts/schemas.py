from drf_yasg import openapi

token_param = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    type=openapi.TYPE_STRING,
    description="JWT 타입으로 입력",
    required=True,
)

signup_res_schema = {
    "201": openapi.Response(
        description="회원가입 완료 후 username을 반환합니다.",
        examples={
            "application/json": {
                "username": "user1",
            }
        },
    )
}

follow_res_schema = {
    "200": openapi.Response(
        description="해당 유저의 팔로워/팔로잉 수를 반환합니다.",
        examples={
            "application/json": {
                "follower_count": 100000,
                "following_count": 1,
            }
        },
    )
}
follow_get_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "follower_count": 100000,
                "following_count": 1,
                "follower_list": [
                    { "username": "user1" }
                ],
            }
        },
    )
}

similar_res_schema = {
    "200": openapi.Response(
        description="영화(rate_movies)는 평점이 높은 순으로 반환됩니다.",
        examples={
            "application/json": {
                "count": 1,
                "users": [
                    {
                        "user_id": 1,
                        "username": "user1",
                        "rate_movies": [
                            {"movie_id": 1, "rank": 5},
                            {"movie_id": 2, "rank": 3},
                        ],
                    }
                ],
            }
        },
    )
}
profile_res_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "id": 7,
                "username": "user1",
                "wish_movies": [
                    {"id": 2, "title": "해리포터", "poster_path": "/poster2.jpg"},
                ],
                "rate_movies": [
                    {
                        "id": 1,
                        "movie": {
                            "id": 1,
                            "title": "쇼생크 탈출",
                            "poster_path": "/poster1.jpg",
                        },
                        "rank": 4,
                    },
                ],
                "like_genres": [
                    {"id": 1, "name": "모험"},
                ],
            }
        },
    )
}
genres_update_res_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "message": "선호하는 장르 리스트를 수정했습니다.",
            }
        },
    )
}
