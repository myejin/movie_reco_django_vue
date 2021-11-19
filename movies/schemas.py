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
                "tid": 80,
                "name": "모험",
            }
        },
    )
}

movie_of_genre_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "genre_name": "모험",
                "movies": [
                    {
                        "id": 1,
                        "title": "쇼생크 탈출",
                        "poster_path": "poster.jpg",
                    },
                ],
            }
        },
    )
}
init_schema = {
    "200": openapi.Response(
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
