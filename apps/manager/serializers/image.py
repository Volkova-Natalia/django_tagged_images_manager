from rest_framework.serializers import ModelSerializer

from apps.manager.models.image import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'content',
            'tags',
        ]


class ImageWithoutPKSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'content',
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


class ImagePostSerializer(ImageWithoutPKSerializer):
    class Meta(ImageWithoutPKSerializer.Meta):
        extra_kwargs = {
            'content': {
                'required': True,
            },
        }


class ImagePutSerializer(ImageWithoutPKSerializer):
    class Meta(ImageWithoutPKSerializer.Meta):
        extra_kwargs = {
            'content': {
                'required': False,
            },
        }
