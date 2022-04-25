import json
from typing import Optional

from rest_framework import status
from rest_framework.response import Response

from apps.manager.models import Image
from .base import BaseImageViewsTestCase
from apps.manager.tests.views.utils.imagefile import ImageWithMetadata


class ImagesViewsTestCase(BaseImageViewsTestCase):
    base_url = '/manager/images/'
    assert_message = 'images views'

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

    def test_get_success(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        image = self._create_image_in_db(filename=self.image_0_filename, tag=tag)
        response = self.get()
        self.assertEquals(response.status_code,
                          status.HTTP_200_OK,
                          f'{self.assert_message} test_get_success')
        self.assertEquals([response.data[0]['id'], response.data[0]['tags']],
                          [image.id, [tag_in_db['value']]],
                          f'{self.assert_message} test_get_success')
        self.assertTrue(response.data[0]['content'].endswith(image.content.url),
                        f'{self.assert_message} test_get_success')

    def test_get_401_fail(self):
        response = self.get(anonymous=True)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_get_401_fail')

    def test_post_success(self):
        data_post = ImageWithMetadata(filename=self.image_0_filename).data
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED,
                          f'{self.assert_message} test_post_success')
        image_new = Image.objects.get(id=response.data['id'])
        self.image_file_saved = image_new.content.name
        self.assertEquals(image_new.metadata,
                          data_post['metadata'],
                          f'{self.assert_message} test_post_success')
        if json.loads(data_post['metadata'])['ImageFormat'] == 'PNG':
            data_saved = ImageWithMetadata(filename=image_new.content.path).data
            self.assertEquals(data_saved['content'],
                              data_post['content'],
                              f'{self.assert_message} test_post_success')

    def test_post_401_fail(self):
        data_post = ImageWithMetadata(filename=self.image_0_filename).data
        response = self.post(anonymous=True, data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_post_401_fail')

    def test_post_400_fail_content(self):
        image_with_metadata = ImageWithMetadata(filename=self.image_0_filename)
        data_post = {
            'not_content':  image_with_metadata.content,
            'metadata': image_with_metadata.metadata,
        }
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST,
                          f'{self.assert_message} test_post_400_fail_content')

    def test_post_400_fail_metadata(self):
        image_with_metadata = ImageWithMetadata(filename=self.image_0_filename)
        data_post = {
            'content':  image_with_metadata.content,
            'not_metadata': image_with_metadata.metadata,
        }
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST,
                          f'{self.assert_message} test_post_400_fail_metadata')
