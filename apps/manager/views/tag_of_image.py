from rest_framework.request import Request
from rest_framework.response import Response

from apps.manager.models import Image
from apps.manager.models import Tag
from apps.manager.serializers import TagPostSerializer, TagPutSerializer
from .base import BaseView


class TagsOfImageView(BaseView):
    post_serializer = TagPostSerializer

    def _get_image(self, *, image_id: int):
        try:
            image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return None
        return image

    def _get_tag(self, *, tag_value: str):
        try:
            tag = Tag.objects.get(value=tag_value)
        except Tag.DoesNotExist:
            return None
        return tag

    def post(self, request: Request, image_id: int, *args, **kwargs) -> Response:
        image = self._get_image(image_id=image_id)
        if not image:
            return self.response_404()
        serializer = self.post_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            tag = self._get_tag(tag_value=serializer.validated_data['value'])
            if not tag:
                tag = serializer.save()
            image.tags.add(tag)
            response = self.response_201(
                data={
                    'id': image.id,
                }
            )
            return response
        return self.response_400(data=serializer.errors)


class TagOfImageDetailsView(BaseView):
    put_serializer = TagPutSerializer

    def _get_image(self, *, image_id: int):
        try:
            image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return None
        return image

    def _get_tag(self, *, tag_value: str):
        try:
            tag = Tag.objects.get(value=tag_value)
        except Tag.DoesNotExist:
            return None
        return tag

    def put(self, request: Request, image_id: int, tag_value: str, *args, **kwargs) -> Response:
        image = self._get_image(image_id=image_id)
        if not image:
            return self.response_404()
        tag = self._get_tag(tag_value=tag_value)
        if not tag:
            return self.response_404()
        serializer = self.put_serializer(tag, data=request.data, context={'request': request})
        if serializer.is_valid():
            image.tags.remove(tag)
            tag_new = self._get_tag(tag_value=serializer.validated_data['value'])
            if not tag_new:
                tag_new = serializer.save()
            image.tags.add(tag_new)
            return self.response_204()
        return self.response_400(data=serializer.errors)

    def delete(self, request: Request, image_id: int, tag_value: str, *args, **kwargs) -> Response:
        image = self._get_image(image_id=image_id)
        if not image:
            return self.response_404()
        tag = self._get_tag(tag_value=tag_value)
        if not tag:
            return self.response_404()
        image.tags.remove(tag)
        return self.response_204()
