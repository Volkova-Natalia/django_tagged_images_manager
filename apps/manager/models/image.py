from django.db import models

from .base import BaseModel
from .tag import Tag


class Image(BaseModel):
    content = models.TextField(
        null=False, blank=False, unique=False,
        verbose_name='Content', help_text='Image',
    )
    created_date = models.DateTimeField(
        null=False, blank=False, unique=False,
        auto_now_add=True,
        verbose_name='Date',
        help_text='Created date of the image'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True, default=None, unique=False,
        related_name='images', related_query_name='image',
        verbose_name='Tag', help_text='Tags for the image',
    )