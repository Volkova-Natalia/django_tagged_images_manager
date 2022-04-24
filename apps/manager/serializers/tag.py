from rest_framework.serializers import ModelSerializer

from apps.manager.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'value',
        ]


class TagGetSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'value',
            'created_date',
            'images',
        ]


class TagPostSerializer(TagSerializer):
    class Meta(TagSerializer.Meta):
        extra_kwargs = {
            'value': {
                'required': True,
            },
        }


class TagPutSerializer(TagSerializer):
    class Meta(TagSerializer.Meta):
        extra_kwargs = {
            'value': {
                'required': True,
            },
        }
