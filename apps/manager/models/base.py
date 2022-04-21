from django.db import models
from django.forms.models import model_to_dict


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = models.Manager

    def to_dict(self, *, fields=None, exclude=None):
        return model_to_dict(instance=self, fields=fields, exclude=exclude)
