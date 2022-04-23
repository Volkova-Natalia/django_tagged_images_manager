import json

from rest_framework import status
from rest_framework.response import Response

from apps.manager.models.image import Image
from .base import BaseImageViewsTestCase
from ..utils.imagefile import ImageWithMetadata


class ImageDetailsViewsTestCase(BaseImageViewsTestCase):
    base_url = '/manager/images/'
    assert_message = 'image details views'

    def get(self, *, image_id: int = 0, **kwargs) -> Response:
        return super().get(url=f'{self.base_url}{image_id}', **kwargs)

    def put(self, *, image_id: int = 0, **kwargs) -> Response:
        my_headers = {
            'HTTP_X_Content_Image_coder': 'utf-8',
        }
        return super().put(url=f'{self.base_url}{image_id}', **my_headers, **kwargs)

    def delete(self, *, image_id: int = 0, **kwargs) -> Response:
        return super().delete(url=f'{self.base_url}{image_id}', **kwargs)

    def test_get_success(self):
        data_in_db = {
            'content': 'image_0'
        }
        image = self._create_image_in_db(**data_in_db)
        response = self.get(image_id=image.id)
        self.assertEquals(response.status_code,
                          status.HTTP_200_OK,
                          f'{self.assert_message} test_get_success')
        self.assertEquals([response.data['id'], response.data['content'], response.data['tags']],
                          [image.id, image.content, []],
                          f'{self.assert_message} test_get_success')

    def test_get_401_fail(self):
        data_in_db = {
            'content': 'image_0'
        }
        image = self._create_image_in_db(**data_in_db)
        response = self.get(anonymous=True, image_id=image.id)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_get_401_fail')

    def test_get_404_fail(self):
        response = self.get(image_id=1)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_get_404_fail')

    def test_put_success(self):
        image = self._create_image_in_db(filename=self.image_0_filename)
        data_put = ImageWithMetadata(filename=self.image_1_filename).data
        response = self.put(image_id=image.id, data=data_put)
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT,
                          f'{self.assert_message} test_put_success')
        self.assertEquals(Image.objects.count(),
                          1,
                          f'{self.assert_message} test_put_success')
        image_new = Image.objects.get(id=image.id)
        from PIL import Image as PILImage
        img_new = PILImage.open(image_new.content.path)
        img_new.show()
        self.image_file_saved = image_new.content.path
        self.assertEquals([image_new.id, image_new.tags],
                          [image.id, image.tags],
                          f'{self.assert_message} test_put_success')
        if json.loads(data_put['metadata'])['ImageFormat'] == 'PNG':
            self.assertEquals(data_put['content'],
                              data_put['content'],
                              f'{self.assert_message} test_post_success')

    def test_put_401_fail(self):
        image = self._create_image_in_db(filename=self.image_0_filename)
        data_put = ImageWithMetadata(filename=self.image_1_filename).data
        response = self.put(anonymous=True, image_id=image.id, data=data_put)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_put_401_fail')

    def test_put_404_fail(self):
        data_put = ImageWithMetadata(filename=self.image_1_filename).data
        response = self.put(image_id=1, data=data_put)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_put_404_fail')

    def test_delete_success(self):
        data_in_db = {
            'content': 'image_0'
        }
        image = self._create_image_in_db(**data_in_db)
        response = self.delete(image_id=image.id)
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT,
                          f'{self.assert_message} test_delete_success')
        self.assertEquals(Image.objects.count(),
                          0,
                          f'{self.assert_message} test_delete_success')

    def test_delete_401_fail(self):
        data_in_db = {
            'content': 'image_0'
        }
        image = self._create_image_in_db(**data_in_db)
        response = self.delete(anonymous=True, image_id=image.id)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_delete_401_fail')

    def test_delete_404_fail(self):
        response = self.delete(image_id=1)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_delete_404_fail')

