import os
import json
from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from .base import BaseModel
from .tag import Tag


def name_file(instance, filename):
    try:
        filename = json.loads(instance.metadata)['Filename']
        file_name = os.path.basename(filename)
        file_path = f'{os.path.dirname(filename)}/'
    except:
        file_path, file_name = '', filename
    return f'images/{file_path}{uuid4()}-{file_name}'


class Image(BaseModel):
    content = models.ImageField(
        upload_to=name_file,
        storage=default_storage,
        null=False, blank=False, unique=True,
        verbose_name='Content',
        help_text='Image',
    )
    metadata = models.JSONField(
        null=True, blank=True, unique=False,
        verbose_name='Metadata',
        help_text='Metadata of the image',
    )
    created_date = models.DateTimeField(
        null=False, blank=False, unique=False,
        auto_now_add=True,
        verbose_name='Date',
        help_text='Created date of the image',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True, default=None, unique=False,
        related_name='images', related_query_name='image',
        verbose_name='Tag',
        help_text='Tags for the image',
    )

    def __str__(self):
        return ''

    def get_absolute_url(self):
        return reverse('image-details', kwargs={'image_id': self.id})

    def save_file(self, content: str):
        temp_file = ContentFile(content)
        self.content.save('', temp_file)


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.content:
        if instance.content.storage.exists(instance.content.name):
            instance.content.storage.delete(instance.content.name)
