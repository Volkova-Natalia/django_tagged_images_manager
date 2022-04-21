from typing import Optional, Any, Dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseView(APIView):
    content_type = 'application/json'

    def response_200(self, *, data: Optional[Dict[str, Any]]) -> Response:
        return Response(
            data=data,
            status=status.HTTP_200_OK,
            content_type=self.content_type
        )

    def response_201(self, *, data: Optional[Dict[str, Any]]) -> Response:
        return Response(
            data=data,
            status=status.HTTP_201_CREATED,
            content_type=self.content_type
        )

    def response_204(self) -> Response:
        return Response(
            data=None,
            status=status.HTTP_204_NO_CONTENT,
            content_type=self.content_type
        )

    def response_400(self, *, data: Optional[Dict[str, Any]]) -> Response:
        return Response(
            data=data,
            status=status.HTTP_400_BAD_REQUEST,
            content_type=self.content_type
        )

    def response_401(self) -> Response:
        return Response(
            data=None,
            status=status.HTTP_401_UNAUTHORIZED,
            content_type=self.content_type
        )

    def response_403(self) -> Response:
        return Response(
            data=None,
            status=status.HTTP_403_FORBIDDEN,
            content_type=self.content_type
        )

    def response_404(self) -> Response:
        return Response(
            data=None,
            status=status.HTTP_404_NOT_FOUND,
            content_type=self.content_type
        )
