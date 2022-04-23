import os
import json
from typing import Optional

from rest_framework import status
from rest_framework.response import Response
from PIL import Image as PILImage

from apps.manager.models.image import Image
from ..base import BaseViewsTestCase
from ..utils.imagefile import ImageWithMetadata


class ImagesViewsTestCase(BaseViewsTestCase):
    base_url = '/manager/images/'
    assert_message = 'images views'
    image_filename = 'apps/manager/tests/test_0.png'
    image_file_saved = ''

    def tearDown(self):
        if os.path.exists(self.image_file_saved):
            os.remove(self.image_file_saved)
        super().tearDown()

    def get(self, *, url: Optional[str] = None, **kwargs) -> Response:
        if url is None:
            url = self.base_url
        return super().get(url=url, **kwargs)

    def post(self, *, url: Optional[str] = None, **kwargs) -> Response:
        if url is None:
            url = self.base_url
        my_headers = {
            'HTTP_X_Content_Image_coder': 'utf-8',
        }
        return super().post(url=url, **my_headers, **kwargs)

    def _create_image_in_db(self, **kwargs) -> Image:
        image_with_metadata = ImageWithMetadata(filename=self.image_filename)
        data_to_db = {
            'content':  image_with_metadata.content_raw,
            'metadata': image_with_metadata.metadata,
        }
        image = Image(metadata=data_to_db['metadata'], **kwargs)
        image.save_file(content=data_to_db['content'])
        image.save()
        self.image_file_saved = image.content.path
        return image

    def test_get_success(self):
        image = self._create_image_in_db()
        response = self.get()
        self.assertEquals(response.status_code,
                          status.HTTP_200_OK,
                          f'{self.assert_message} test_get_success')

    def test_get_401_fail(self):
        response = self.get(anonymous=True)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_get_401_fail')

    def test_post_success(self):
        data_post = ImageWithMetadata(filename=self.image_filename).data
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED,
                          f'{self.assert_message} test_post_success')
        self.assertEquals(response.data['id'],
                          1,
                          f'{self.assert_message} test_post_success')
        image_new = Image.objects.get(id=response.data['id'])
        self.image_file_saved = image_new.content.path
        img_new = PILImage.open(image_new.content.path)
        img_new.show()
        self.assertEquals(image_new.metadata,
                          data_post['metadata'],
                          f'{self.assert_message} test_post_success')
        data_saved = ImageWithMetadata(filename=self.image_filename).data
        if json.loads(data_post['metadata'])['ImageFormat'] == 'PNG':
            self.assertEquals(data_saved['content'],
                              data_post['content'],
                              f'{self.assert_message} test_post_success')

    def test_post_401_fail(self):
        data_post = ImageWithMetadata(filename=self.image_filename).data
        response = self.post(anonymous=True, data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_post_401_fail')

    def test_post_400_fail_content(self):
        image_with_metadata = ImageWithMetadata(filename=self.image_filename)
        data_post = {
            'not_content':  image_with_metadata.content,
            'metadata': image_with_metadata.metadata,
        }
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST,
                          f'{self.assert_message} test_post_400_fail_content')

    def test_post_400_fail_metadata(self):
        image_with_metadata = ImageWithMetadata(filename=self.image_filename)
        data_post = {
            'content':  image_with_metadata.content,
            'not_metadata': image_with_metadata.metadata,
        }
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST,
                          f'{self.assert_message} test_post_400_fail_metadata')
