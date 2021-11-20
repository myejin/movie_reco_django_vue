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
                }
            },
        )
    }
    return data


article_delete_schema = {
    "204": openapi.Response(
        description="삭제 완료를 알리는 메세지가 반환됩니다.",
        examples={
            "application/json": {
                "message": "1번 게시물이 삭제되었습니다.",
            }
        },
    )
}
