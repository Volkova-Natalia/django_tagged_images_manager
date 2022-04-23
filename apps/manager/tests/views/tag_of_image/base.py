from typing import Optional

from apps.manager.models.image import Image
from apps.manager.models.tag import Tag
from ..base import BaseViewsTestCase
from ..utils.imagefile import ImageWithMetadata


class BaseTagOfImageViewsTestCase(BaseViewsTestCase):
    def _create_tag_in_db(self, **kwargs) -> Tag:
        tag = Tag.objects.create(**kwargs)
        tag.save()
        return tag

    def _create_image_in_db(self, filename: Optional[str] = None, **kwargs) -> Image:
        if filename is None:
            filename = self.image_0_filename
        image_with_metadata = ImageWithMetadata(filename=filename)
        data_to_db = {
            'content':  image_with_metadata.content_raw,
            'metadata': image_with_metadata.metadata,
        }
        image = Image(metadata=data_to_db['metadata'], **kwargs)
        image.save_file(content=data_to_db['content'])
        image.save()
        self.image_file_saved = image.content.name
        return image
