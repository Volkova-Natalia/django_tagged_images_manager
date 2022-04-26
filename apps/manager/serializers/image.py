import base64

from rest_framework import serializers

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
        """
        A bad situation is possible:
        1. obj (field 'metadata') will be saved to db successfully
        2. image file will be saved to storage successfully
        3. updating of the obj in db (field 'content') will fail

        As a result:
        1. obj from db will de removed - successfully (a transaction will rollback)
        2. image file will be in storage

        It is not possible to solve the issue here, you should have garbage collector for the unused files.
        """
        obj = Image(metadata=str(validated_data['metadata']))
        obj.save()
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
        """
        A bad situation is possible:
        1. instance (field 'metadata') will be updated in db successfully
        2. image file will be saved to storage successfully
        3. updating of the instance in db (field 'content') will fail

        As a result:
        1. instance from db will rollback - successfully (a transaction will rollback)
        2. image file will be in storage

        It is not possible to solve the issue here, you should have garbage collector for the unused files.
        """
        old_file = instance.content.name

        instance.metadata = validated_data.get('metadata', instance.metadata)
        instance.save()
        instance.save_file(content=validated_data['content'])
        if Image().content.storage.exists(old_file):
            Image().content.storage.delete(old_file)

        return instance
