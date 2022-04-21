from typing import Optional

from rest_framework import status
from rest_framework.response import Response

from ..base import BaseViewsTestCase


class ImagesViewsTestCase(BaseViewsTestCase):
    base_url = '/manager/images/'
    assert_message = 'images views'

    def get(self, *, url: Optional[str] = None, **kwargs) -> Response:
        if url is None:
            url = self.base_url
        return super().get(url=url, **kwargs)

    def post(self, *, url: Optional[str] = None, **kwargs) -> Response:
        if url is None:
            url = self.base_url
        return super().post(url=url, **kwargs)

    def test_get_success(self):
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
        data_post = {
            'content': 'image_0'
        }
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_201_CREATED,
                          f'{self.assert_message} test_post_success')
        self.assertEquals(response.data['id'],
                          1,
                          f'{self.assert_message} test_post_success')

    def test_post_401_fail(self):
        data_post = {
            'content': 'image_0'
        }
        response = self.post(anonymous=True, data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_post_401_fail')

    def test_post_400_fail(self):
        data_post = {
            'not_content': 'image_0'
        }
        response = self.post(data=data_post)
        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST,
                          f'{self.assert_message} test_post_400_fail')
