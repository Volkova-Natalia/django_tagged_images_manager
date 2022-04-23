from rest_framework.request import Request
from rest_framework.response import Response

from apps.manager.models.image import Image
from apps.manager.serializers.image import ImageGetSerializer, ImagePostSerializer, ImagePutSerializer
from .base import BaseView


class ImagesView(BaseView):
    model = Image
    get_serializer = ImageGetSerializer
    post_serializer = ImagePostSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        objs = self.model.objects.all()[:]
        serializer = self.get_serializer(objs, context={'request': request}, many=True)
        return self.response_200(data=serializer.data)

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.post_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            obj = serializer.save()
            response = self.response_201(
                data={
                    'id': obj.id,
                }
            )
            return response
        return self.response_400(data=serializer.errors)


class ImageDetailsView(BaseView):
    model = Image
    get_serializer = ImageGetSerializer
    put_serializer = ImagePutSerializer

    def _get_object(self, *, obj_id: int):
        try:
            obj = self.model.objects.get(id=obj_id)
        except self.model.DoesNotExist:
            return None
        return obj

    def get(self, request: Request, image_id: int, *args, **kwargs) -> Response:
        obj = self._get_object(obj_id=image_id)
        if not obj:
            return self.response_404()
        serializer = self.get_serializer(obj, context={'request': request})
        return self.response_200(data=serializer.data)

    def put(self, request: Request, image_id: int, *args, **kwargs) -> Response:
        obj = self._get_object(obj_id=image_id)
        if not obj:
            return self.response_404()
        serializer = self.put_serializer(obj, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return self.response_204()
        return self.response_400(data=serializer.errors)

    def delete(self, request: Request, image_id: int, *args, **kwargs) -> Response:
        obj_count, obj = self.model.objects.filter(id=image_id).delete()
        if obj_count == 0:
            return self.response_404()
        return self.response_204()
