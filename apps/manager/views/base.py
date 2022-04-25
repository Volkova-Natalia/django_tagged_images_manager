from typing import Optional, Any, Dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class BaseView(APIView):
    permission_classes = (IsAuthenticated,)
    content_type = 'application/json'

    def response_201(self, *, data: Optional[Dict[str, Any]], **kwargs) -> Response:
        return Response(
            data=data,
            status=status.HTTP_201_CREATED,
            content_type=self.content_type,
            **kwargs
        )

    def response_204(self, **kwargs) -> Response:
        return Response(
            data=None,
            status=status.HTTP_204_NO_CONTENT,
            content_type=self.content_type,
            **kwargs
        )

    def response_400(self, *, data: Optional[Dict[str, Any]], **kwargs) -> Response:
        return Response(
            data=data,
            status=status.HTTP_400_BAD_REQUEST,
            content_type=self.content_type,
            **kwargs
        )

    def response_404(self, **kwargs) -> Response:
        return Response(
            data={"detail": "ErrorDetail(string='Not found.', code='not_found')"},
            status=status.HTTP_404_NOT_FOUND,
            content_type=self.content_type,
            **kwargs
        )
