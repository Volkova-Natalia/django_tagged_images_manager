from rest_framework import status
from rest_framework.response import Response

from apps.manager.models.tag import Tag
from ..base import BaseViewsTestCase


class TagDetailsViewsTestCase(BaseViewsTestCase):
    base_url = '/manager/tags/'
    assert_message = 'tag details views'

    def get(self, *, tag_value: str = '', **kwargs) -> Response:
        return super().get(url=f'{self.base_url}{tag_value}', **kwargs)

    def put(self, *, tag_value: str = '', **kwargs) -> Response:
        return super().put(url=f'{self.base_url}{tag_value}', **kwargs)

    def delete(self, *, tag_value: str = '', **kwargs) -> Response:
        return super().delete(url=f'{self.base_url}{tag_value}', **kwargs)

    def _create_tag_in_db(self, **kwargs) -> Tag:
        tag = Tag.objects.create(**kwargs)
        tag.save()
        return tag

    def test_get_success(self):
        data_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**data_in_db)
        response = self.get(tag_value=tag.value)
        self.assertEquals(response.status_code,
                          status.HTTP_200_OK,
                          f'{self.assert_message} test_get_success')
        self.assertEquals([response.data['value'], response.data['images']],
                          [tag.value, []],
                          f'{self.assert_message} test_get_success')

    def test_get_401_fail(self):
        data_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**data_in_db)
        response = self.get(anonymous=True, tag_value=tag.value)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_get_401_fail')

    def test_get_404_fail(self):
        response = self.get(tag_value='AAA')
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_get_404_fail')

    def test_put_success(self):
        data_in_db = {
            'value': 'tag_0'
        }
        data_put = {
            'value': 'tag_0_new'
        }
        tag = self._create_tag_in_db(**data_in_db)
        response = self.put(tag_value=tag.value, data=data_put)
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT,
                          f'{self.assert_message} test_put_success')
        tag_new = Tag.objects.get(value=tag.value)
        self.assertEquals([tag_new.value, tag_new.images],
                          [tag.value, tag.images],
                          f'{self.assert_message} test_put_success')

    def test_put_401_fail(self):
        data_in_db = {
            'value': 'tag_0'
        }
        data_put = {
            'value': 'tag_0_new'
        }
        tag = self._create_tag_in_db(**data_in_db)
        response = self.put(anonymous=True, tag_value=tag.value, data=data_put)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_put_401_fail')

    def test_put_404_fail(self):
        data_put = {
            'value': 'tag_0_new'
        }
        response = self.put(tag_value='AAA', data=data_put)
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_put_404_fail')

    def test_delete_success(self):
        data_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**data_in_db)
        response = self.delete(tag_value=tag.value)
        self.assertEquals(response.status_code,
                          status.HTTP_204_NO_CONTENT,
                          f'{self.assert_message} test_delete_success')
        self.assertEquals(Tag.objects.count(),
                          0,
                          f'{self.assert_message} test_delete_success')

    def test_delete_401_fail(self):
        data_in_db = {
            'value': 'tag_0'
        }
        tag = self._create_tag_in_db(**data_in_db)
        response = self.delete(anonymous=True, tag_value=tag.value)
        self.assertEquals(response.status_code,
                          status.HTTP_401_UNAUTHORIZED,
                          f'{self.assert_message} test_delete_401_fail')

    def test_delete_404_fail(self):
        response = self.delete(tag_value='AAA')
        self.assertEquals(response.status_code,
                          status.HTTP_404_NOT_FOUND,
                          f'{self.assert_message} test_delete_404_fail')

