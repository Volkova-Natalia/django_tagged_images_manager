from typing import Optional

from rest_framework import status
from rest_framework.response import Response

from apps.manager.models.image import Image
from apps.manager.models.tag import Tag
from .base import BaseTagOfImageViewsTestCase


class TagsOfImageViewsTestCase(BaseTagOfImageViewsTestCase):
    base_url = '/manager/images/'
    assert_message = 'tags_of_image views'

    def get(self, *, image_id: int = 0, **kwargs) -> Response:
        return super().get(url=f'{self.base_url}{image_id}/tags/', **kwargs)

    def post(self, *, image_id: int = 0, **kwargs) -> Response:
        return super().post(url=f'{self.base_url}{image_id}/tags/', **kwargs)

    def test_get_405_fail(self):
        response = self.get()
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED,
                          f'{self.assert_message} test_post_success')

    def test_post_success(self):
        image_in_db = {
            'content': 'image_0'
        }
        tag_post = {
            'value': 'tag_0'
        }
        image = self._create_image_in_db(**image_in_db)
        response = self.post(image_id=image.id, data=tag_post)
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED,
                          f'{self.assert_message} test_post_success')
        image_new = Image.objects.get(id=image.id)
        image_new_tags = image_new.tags.all()[:]
        image_new_tags_values = list((image_new_tag.value for image_new_tag in image_new_tags))
        self.assertEquals([image_new.id, image_new.content, image_new_tags_values],
                          [image.id, image.content, [tag_post['value']]],
                          f'{self.assert_message} test_post_success')

    def test_post_401_fail(self):
        image_in_db = {
            'content': 'image_0'
        }
        tag_post = {
            'value': 'tag_0'
        }
        image = self._create_image_in_db(**image_in_db)
        response = self.post(anonymous=True, image_id=image.id, data=tag_post)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_post_401_fail')

    def test_post_404_fail(self):
        tag_post = {
            'value': 'tag_0'
        }
        response = self.post(image_id=1, data=tag_post)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_post_404_fail')

    def test_post_400_fail(self):
        image_in_db = {
            'content': 'image_0'
        }
        tag_post = {
            'not_value': 'tag_0'
        }
        image = self._create_image_in_db(**image_in_db)
        response = self.post(image_id=image.id, data=tag_post)
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST,
                          f'{self.assert_message} test_post_400_fail')

