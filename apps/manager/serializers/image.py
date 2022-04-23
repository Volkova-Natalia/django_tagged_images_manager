import base64

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.manager.models.image import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'content',
            'metadata',
            'tags',
        ]


class ImageWithoutPKSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'content',
            'metadata',
            'tags',
        ]


class ImageGetSerializer(ImageSerializer):
    class Meta(ImageSerializer.Meta):
        fields = ImageSerializer.Meta.fields.copy()
        fields.append('created_date')
        extra_kwargs = {
            'id': {
                'read_only': True,
                'required': True,
            },
            'content': {
                'read_only': True,
                'required': True,
            },
            'metadata': {
                'read_only': True,
                'required': True,
            },
            'created_date': {
                'read_only': True,
                'required': True,
            },
            'tags': {
                'many': True,
                'read_only': True,
                'required': True,
            },
        }


class ImagePostSerializer(serializers.Serializer):
    content = serializers.CharField(
        allow_blank=False,
        required=True,
    )
    metadata = serializers.JSONField(
        required=True,
    )

    def create(self, validated_data: dict) -> Image:
        headers = self.context['request'].headers
        coder = headers['X-Content-Image-coder'] if 'X-Content-Image-coder' in headers else 'utf-18'
        img_base64 = validated_data['content'].encode(coder)
        img_byte = base64.b64decode(img_base64)

        obj = Image(metadata=str(validated_data['metadata']))
        obj.save_file(content=img_byte)
        obj.save()
        return obj


class ImagePutSerializer(serializers.Serializer):
    content = serializers.CharField(
        allow_blank=False,
        required=True,
    )
    metadata = serializers.JSONField(
        required=True,
    )

    def update(self, instance: Image, validated_data: dict) -> Image:
        headers = self.context['request'].headers
        coder = headers['X-Content-Image-coder'] if 'X-Content-Image-coder' in headers else 'utf-18'
        img_base64 = validated_data['content'].encode(coder)
        img_byte = base64.b64decode(img_base64)

        old_file = instance.content.name

        instance.metadata = validated_data.get('metadata', instance.metadata)
        instance.save_file(content=img_byte)
        instance.save()

        if Image().content.storage.exists(old_file):
            Image().content.storage.delete(old_file)
        return instance
