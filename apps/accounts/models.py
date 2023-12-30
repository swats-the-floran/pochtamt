import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, UUIDMixin, TimeStampedMixin):

    class GenderChoices(models.TextChoices):
        MALE = 'M', _('Мужской')
        FEMALE = 'F', _('Женский')

    gender = models.CharField(max_length=1, choices=GenderChoices.choices, null=True, blank=True)
    profile_image = models.ImageField(max_length=255, upload_to='profile_images/', null=True, blank=True)

    friends = models.ManyToManyField('self', null=True, blank=True)

