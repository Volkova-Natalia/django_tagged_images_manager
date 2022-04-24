from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.manager.models import Image
from apps.manager.serializers import ImageGetSerializer, ImagePostSerializer, ImagePostResponseSerializer, ImagePutSerializer
from .base import BaseView


class ImagesView(BaseView, ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageGetSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ImageGetSerializer
        if self.action in ['create']:
            return ImagePostSerializer
        if self.action in ['update']:
            return ImagePutSerializer
        return super().get_serializer_class()

    def update(self, request: Request, *args, **kwargs) -> Response:
        super().update(request, *args, **kwargs)
        return self.response_204()

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return_serializer = ImagePostResponseSerializer(instance)
        headers = self.get_success_headers(return_serializer.data)
        return self.response_201(data=return_serializer.data, **headers)
