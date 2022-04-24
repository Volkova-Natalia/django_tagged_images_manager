from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.manager.models import Tag
from apps.manager.serializers import TagGetSerializer, TagPostSerializer, TagPutSerializer
from .base import BaseView


class TagsView(BaseView, ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagGetSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TagGetSerializer
        if self.action in ['create']:
            return TagPostSerializer
        if self.action in ['update']:
            return TagPutSerializer
        return super().get_serializer_class()

    def update(self, request: Request, *args, **kwargs) -> Response:
        super().update(request, *args, **kwargs)
        return self.response_204()

    def create(self, request: Request, *args, **kwargs) -> Response:
        response = super().create(request, *args, **kwargs)
        return self.response_201(data=response.data, **response.get('headers', {}))
