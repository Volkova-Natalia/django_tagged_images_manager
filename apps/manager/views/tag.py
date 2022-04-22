from rest_framework.request import Request
from rest_framework.response import Response

from apps.manager.models.tag import Tag
from apps.manager.serializers.tag import TagGetSerializer, TagPostSerializer, TagPutSerializer
from .base import BaseView


class TagsView(BaseView):
    model = Tag
    get_serializer = TagGetSerializer
    post_serializer = TagPostSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        if request.successful_authenticator is None:
            return self.response_401()
        objs = self.model.objects.all()[:]
        serializer = self.get_serializer(objs, context={'request': request}, many=True)
        return self.response_200(data=serializer.data)

    def post(self, request: Request, *args, **kwargs) -> Response:
        if request.successful_authenticator is None:
            return self.response_401()
        serializer = self.post_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            obj = serializer.save()
            response = self.response_201(
                data={
                    'value': obj.value,
                }
            )
            return response
        return self.response_400(data=serializer.errors)


class TagDetailsView(BaseView):
    model = Tag
    get_serializer = TagGetSerializer
    put_serializer = TagPutSerializer

    def _get_object(self, *, obj_value: str):
        try:
            obj = self.model.objects.get(value=obj_value)
        except self.model.DoesNotExist:
            return None
        return obj

    def get(self, request: Request, tag_value: str, *args, **kwargs) -> Response:
        if request.successful_authenticator is None:
            return self.response_401()
        obj = self._get_object(obj_value=tag_value)
        if not obj:
            return self.response_404()
        serializer = self.get_serializer(obj, context={'request': request})
        return self.response_200(data=serializer.data)

    def put(self, request: Request, tag_value: str, *args, **kwargs) -> Response:
        if request.successful_authenticator is None:
            return self.response_401()
        obj = self._get_object(obj_value=tag_value)
        if not obj:
            return self.response_404()
        serializer = self.put_serializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return self.response_204()
        return self.response_400(data=serializer.errors)

    def delete(self, request: Request, tag_value: str, *args, **kwargs) -> Response:
        if request.successful_authenticator is None:
            return self.response_401()
        obj = self._get_object(obj_value=tag_value)
        if not obj:
            return self.response_404()
        obj.delete()
        return self.response_204()
