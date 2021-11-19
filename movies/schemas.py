from drf_yasg import openapi

token_param = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    type=openapi.TYPE_STRING,
    description="JWT 타입으로 입력",
    required=True,
)


def msg_res_schema(msg):
    schema = {
        "200": openapi.Response(
            description="",
            examples={
                "application/json": {
                    "message": msg,
                }
            },
        )
    }
    return schema


genre_list_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "id": 1,
                "tid": 28,
                "name": "액션",
            }
        },
    )
}

movie_of_genre_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "genre_name": "액션",
                "movies": [
                    {
                        "id": 11,
                        "title": "다크 나이트",
                        "poster_path": "poster.jpg",
                    },
                ],
            }
        },
    )
}
init_schema = {
    "201": openapi.Response(
        description="",
        examples={
            "application/json": {
                "movie_count": 200,
                "genre_count": 19,
                "actor_count": 749,
            }
        },
    )
}
rate_schema = {
    "201": openapi.Response(
        description="평점 개수와 총합으로 평균 평점을 구할 수 있습니다.",
        examples={
            "application/json": {"rank_count": 3, "rank_sum": 10},
        },
    )
}
