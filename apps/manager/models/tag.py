from django.db import models
from django.urls import reverse

from .base import BaseModel


class Tag(BaseModel):
    value = models.TextField(
        primary_key=True,
    )
    created_date = models.DateTimeField(
        null=False, blank=False, unique=False,
        auto_now_add=True,
        verbose_name='Date',
        help_text='Created date of the tag',
    )

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'tag_value': self.value})
