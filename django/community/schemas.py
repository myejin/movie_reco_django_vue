from drf_yasg import openapi

token_param = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    type=openapi.TYPE_STRING,
    description="JWT 타입으로 입력",
    required=True,
)
article_list_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "count": 0,
                "articles": [],
            }
        },
    )
}


def article_res_schema(status_code):
    data = {
        f"{status_code}": openapi.Response(
            description="",
            examples={
                "application/json": {
                    "id": 1,
                    "author": {"username": "user1"},
                    "movie": {"id": 1, "title": "쇼생크 탈출"},
                    "position": "",
                    "is_finished": False,
                    "created_at": "2021-11-22 16:57:08",
                    "updated_at": "2021-11-22 16:57:10",
                }
            },
        )
    }
    return data


delete_schema = {
    "204": openapi.Response(
        description="삭제완료 메세지(`message`)를 반환됩니다.",
    )
}
review_list_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "article_id": 1,
                "reviews": [
                    {
                        "id": 1,
                        "author": {"username": "user1"},
                        "content": "이거 짱 잼임",
                        "created_at": "2021-11-22 16:57:08",
                        "updated_at": "2021-11-22 16:57:10",
                    }
                ],
            }
        },
    )
}


def review_res_schema(status_code):
    data = {
        f"{status_code}": openapi.Response(
            description="",
            examples={
                "application/json": {
                    "article_id": 1,
                    "review": {
                        "id": 1,
                        "author": {"username": "user1"},
                        "content": "이거 짱 잼임",
                        "created_at": "2021-11-22 16:57:08",
                        "updated_at": "2021-11-22 16:57:10",
                    },
                }
            },
        )
    }
    return data
