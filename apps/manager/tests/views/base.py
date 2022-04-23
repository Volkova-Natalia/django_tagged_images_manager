from typing import Optional, Any, Dict

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from rest_framework.response import Response


class BaseViewsTestCase(TestCase):
    content_type = 'application/json'

    registered_user_data = {
        'username': 'registered_user_username',
        'password': 'registered_user_password'
    }
    registered_user = None

    registered_client: Client = None
    anonymous_client: Client = None

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.anonymous_client = Client()
        if cls.registered_user is None:
            cls.registered_user = User.objects.create_user(**cls.registered_user_data)
            cls.registered_user.save()

    def setUp(self):
        super().setUp()
        self.registered_client = Client()
        self.registered_client.login(**self.registered_user_data)

    def tearDown(self):
        self.registered_client.logout()
        super().tearDown()

    def get(self, *, anonymous=False, url='', **kwargs) -> Response:
        client = self.anonymous_client if anonymous else self.registered_client
        return client.get(
            path=url,
            content_type=self.content_type,
            HTTP_ACCEPT=self.content_type,
            **kwargs
        )

    def post(self, *, anonymous=False, url='', data: Optional[Dict[str, Any]] = None, **kwargs) -> Response:
        client = self.anonymous_client if anonymous else self.registered_client
        return client.post(
            path=url,
            data=data,
            content_type=self.content_type,
            HTTP_ACCEPT=self.content_type,
            **kwargs
        )

    def put(self, *, anonymous=False, url='', data: Optional[Dict[str, Any]] = None, **kwargs) -> Response:
        client = self.anonymous_client if anonymous else self.registered_client
        return client.put(
            path=url,
            data=data,
            content_type=self.content_type,
            HTTP_ACCEPT=self.content_type,
            **kwargs
        )

    def delete(self, *, anonymous=False, url='', **kwargs) -> Response:
        client = self.anonymous_client if anonymous else self.registered_client
        return client.delete(
            path=url,
            content_type=self.content_type,
            HTTP_ACCEPT=self.content_type,
            **kwargs
        )
