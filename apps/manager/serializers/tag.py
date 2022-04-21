from rest_framework.serializers import ModelSerializer

from apps.manager.models.tag import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'value',
        ]


class TagWithoutPKSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
        ]


class TagGetSerializer(TagSerializer):
    class Meta(TagSerializer.Meta):
        fields = TagSerializer.Meta.fields.copy()
        fields.append('created_date')
        fields.append('images')
        extra_kwargs = {
            'value': {
                'read_only': True,
                'required': True,
            },
            'created_date': {
                'read_only': True,
                'required': True,
            },
            'images': {
                'many': True,
                'read_only': True,
                'required': True,
            },
        }


class TagPostSerializer(TagSerializer):
    class Meta(TagSerializer.Meta):
        extra_kwargs = {
            'value': {
                'required': True,
            },
        }


class TagPutSerializer(TagWithoutPKSerializer):
    class Meta(TagWithoutPKSerializer.Meta):
        extra_kwargs = {
            'value': {
                'required': True,
            },
        }
