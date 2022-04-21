from django.db import models

from .base import BaseModel


class Tag(BaseModel):
    value = models.TextField(
        primary_key=True,
    )
    created_date = models.DateTimeField(
        null=False, blank=False, unique=False,
        auto_now_add=True,
        verbose_name='Date',
        help_text='Created date of the tag'
    )
