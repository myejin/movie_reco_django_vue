from drf_yasg import openapi

token_param = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    type=openapi.TYPE_STRING,
    description="JWT 타입으로 입력",
    required=True,
)
create_room_res_schema = {
    "201": openapi.Response(
        description="",
        examples={
            "application/json": {
                "room_name": "1_2",
                "messages": [],
            }
        },
    )
}
go_room_res_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
                "room_name": "1_2",
                "messages": [],
            }
        },
    ),
    "404": openapi.Response(
        description="",
        examples={
            "application/json": {
                "message": "아직 채팅방이 없습니다. POST 요청을 시도하세요.",
            }
        },
    )
}
send_msg_res_schema = {
    "201": openapi.Response(
        description="",
        examples={
            "application/json": {
                "content": "안녕하세요.",
                "created_at": "2021-11-20T15:50:48.780412Z",
            }
        },
    )
}