from rest_framework import status
from rest_framework.response import Response

from apps.manager.models.image import Image
from apps.manager.models.tag import Tag
from .base import BaseTagOfImageViewsTestCase


class TagOfImageDetailsViewsTestCase(BaseTagOfImageViewsTestCase):
    base_url = '/manager/images/'
    assert_message = 'tag_of_image details views'

    def get(self, *, image_id: int = 0, tag_value: str = '', **kwargs) -> Response:
        return super().get(url=f'{self.base_url}{image_id}/tags/{tag_value}', **kwargs)

    def put(self, *, image_id: int = 0, tag_value: str = '', **kwargs) -> Response:
        return super().put(url=f'{self.base_url}{image_id}/tags/{tag_value}', **kwargs)

    def delete(self, *, image_id: int = 0, tag_value: str = '', **kwargs) -> Response:
        return super().delete(url=f'{self.base_url}{image_id}/tags/{tag_value}', **kwargs)

    def test_get_405_fail(self):
        response = self.get()
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED,
                          f'{self.assert_message} test_get_405_fail')

    def test_put_success(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag_put = {
            'value': 'tag_0_new'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        image = self._create_image_in_db(filename=self.image_0_filename, tag=tag)
        response = self.put(image_id=image.id, tag_value=tag.value, data=tag_put)
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT,
                          f'{self.assert_message} test_put_success')
        image_new = Image.objects.get(id=image.id)
        image_new_tags = image_new.tags.all()[:]
        image_new_tags_values = list((image_new_tag.value for image_new_tag in image_new_tags))
        self.assertEquals([image_new.id, image_new.content, image_new_tags_values],
                          [image.id, image.content, [tag_put['value']]],
                          f'{self.assert_message} test_put_success')
        self.assertTrue(Tag.objects.filter(value=tag.value).exists(),
                        f'{self.assert_message} test_put_success')


    def test_put_401_fail(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag_put = {
            'value': 'tag_0_new'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        image = self._create_image_in_db(filename=self.image_0_filename, tag=tag)
        response = self.put(anonymous=True, image_id=image.id, tag_value=tag.value, data=tag_put)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_put_401_fail')

    def test_put_404_fail_image(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag_put = {
            'value': 'tag_0_new'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        response = self.put(image_id=1, tag_value=tag.value, data=tag_put)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_put_404_fail_image')

    def test_put_404_fail_tag(self):
        tag_put = {
            'value': 'tag_0_new'
        }
        image = self._create_image_in_db(filename=self.image_0_filename)
        response = self.put(image_id=image.id, tag_value='AAA', data=tag_put)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_put_404_fail_tag')

    def test_put_400_fail(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag_put = {
            'not_value': 'tag_0_new'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        image = self._create_image_in_db(filename=self.image_0_filename, tag=tag)
        response = self.put(image_id=image.id, tag_value=tag.value, data=tag_put)
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST,
                          f'{self.assert_message} test_put_400_fail')

    def test_delete_success(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        image = self._create_image_in_db(filename=self.image_0_filename, tag=tag)
        response = self.delete(image_id=image.id, tag_value=tag.value)
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT,
                          f'{self.assert_message} test_delete_success')
        image_new = Image.objects.get(id=image.id)
        image_new_tags = image_new.tags.all()[:]
        self.assertEquals(len(image_new_tags),
                          0,
                          f'{self.assert_message} test_delete_success')
        self.assertEquals(Tag.objects.count(),
                          1,
                          f'{self.assert_message} test_delete_success')

    def test_delete_401_fail(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        image = self._create_image_in_db(filename=self.image_0_filename, tag=tag)
        response = self.delete(anonymous=True, image_id=image.id, tag_value=tag.value)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_delete_401_fail')

    def test_delete_404_fail_image(self):
        tag_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**tag_in_db)
        response = self.delete(image_id=1, tag_value=tag.value)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_delete_404_fail_image')

    def test_delete_404_fail_tag(self):
        image = self._create_image_in_db(filename=self.image_0_filename)
        response = self.delete(image_id=image.id, tag_value='AAA')
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_delete_404_fail_tag')
