from typing import Optional

from apps.manager.models.image import Image
from ..base import BaseViewsTestCase
from ..utils.imagefile import ImageWithMetadata


class BaseImageViewsTestCase(BaseViewsTestCase):
    image_0_filename = 'apps/manager/tests/test_0.png'
    image_1_filename = 'apps/manager/tests/test_1.png'
    image_file_saved = 'path_to_image_file_in_storage'

    def tearDown(self):
        if Image().content.storage.exists(self.image_file_saved):
            Image().content.storage.delete(self.image_file_saved)
        super().tearDown()

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
