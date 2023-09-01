import uuid

from django.db.models import Q, QuerySet
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser, User
from django.db import models
from django.urls import reverse

from conf.settings import LETTER_ATTACHMENT_DIR, MAX_LETTER_ATTACHMENT_SIZE


class UUIDMixin(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LettersManager(models.Manager):

    def my_letters(self, user: AbstractBaseUser | AnonymousUser) -> QuerySet:
        """Return  a list of letters where the user is an quthor or an addressee."""
        return self.get_queryset().filter(Q(author=user) | Q(addressee=user))


class Letter(UUIDMixin, TimeStampedMixin):
    """Basically a message from one user to other(s), but has minimal limits for size and delivery time."""

    author = models.ForeignKey(
        User,
        # default=User.objects.get(id=1),  # replace with get_or_create()
        on_delete=models.CASCADE,  # replace with default
        related_name='sent_letters',
    )
    addressee = models.ForeignKey(
        User,
        # default=User.objects.get(id=1),
        on_delete=models.CASCADE,
        related_name='received_letters',
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    text = models.TextField(
        max_length=10240,
        blank=True,
        null=True,
    )

    objects = LettersManager()

    def __str__(self) -> str:
        return f'{self.id}: {self.title}'

    def get_absolute_url(self) -> str:
        return reverse('letter-detail', kwargs={'pk': self.pk})


class Attachment(UUIDMixin, TimeStampedMixin):
    """Attachments that user can add to his letters. Photos mostly."""

    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file_body = models.FileField(
        upload_to=LETTER_ATTACHMENT_DIR,
        max_length=MAX_LETTER_ATTACHMENT_SIZE,
    )

