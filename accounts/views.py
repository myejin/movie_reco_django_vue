from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserRequestSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method="post",
    operation_description="새로운 유저를 생성합니다. (회원가입)",
    request_body=UserRequestSerializer,
    responses={201: openapi.Response("회원가입 완료 후 username을 반환합니다.", UserSerializer)},
)
@api_view(["POST"])
def signup(request):
    if request.data.get("password") != request.data.get("password2"):
        return Response({"error": "비밀번호가 일치하지 않습니다."}, status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
