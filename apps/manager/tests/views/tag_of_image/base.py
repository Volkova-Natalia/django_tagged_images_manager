from typing import Optional

from apps.manager.models.image import Image
from apps.manager.models.tag import Tag
from ..base import BaseViewsTestCase


class BaseTagOfImageViewsTestCase(BaseViewsTestCase):
    def _create_tag_in_db(self, **kwargs) -> Tag:
        tag = Tag.objects.create(**kwargs)
        tag.save()
        return tag

    def _create_image_in_db(self, *, tag: Optional[Tag] = None, **kwargs) -> Image:
        image = Image.objects.create(**kwargs)
        image.save()
        image.tags.add(tag)
        return image
