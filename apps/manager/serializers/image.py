import base64

from rest_framework import serializers
from django.db import transaction

from apps.manager.models import Image


class ImageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'content',
            'metadata',
            'created_date',
            'tags',
        ]


class ImagePostSerializer(serializers.Serializer):
    content = serializers.CharField(
        allow_blank=False,
        required=True,
    )
    metadata = serializers.JSONField(
        required=True,
    )

    def validate(self, data):
        headers = self.context['request'].headers
        coder = headers['X-Content-Image-coder'] if 'X-Content-Image-coder' in headers else 'utf-18'
        img_base64 = data['content'].encode(coder)
        data['content'] = base64.b64decode(img_base64)
        return data

    def create(self, validated_data: dict) -> Image:
        try:
            with transaction.atomic():
                obj = Image(metadata=str(validated_data['metadata']))
                obj.save()
        except Exception:
            raise
        else:
            obj.save_file(content=validated_data['content'])

        return obj


class ImagePostResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        required=True,
    )


class ImagePutSerializer(serializers.Serializer):
    content = serializers.CharField(
        allow_blank=False,
        required=True,
    )
    metadata = serializers.JSONField(
        required=True,
    )

    def validate(self, data):
        headers = self.context['request'].headers
        coder = headers['X-Content-Image-coder'] if 'X-Content-Image-coder' in headers else 'utf-18'
        img_base64 = data['content'].encode(coder)
        data['content'] = base64.b64decode(img_base64)
        return data

    def update(self, instance: Image, validated_data: dict) -> Image:
        old_file = instance.content.name

        try:
            with transaction.atomic():
                instance.metadata = validated_data.get('metadata', instance.metadata)
                instance.save()
        except Exception:
            raise
        else:
            instance.save_file(content=validated_data['content'])
            if Image().content.storage.exists(old_file):
                Image().content.storage.delete(old_file)

        return instance
