from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UploadPhoto(models.Model):

    class Meta:
        verbose_name = _('Завантажене фото')
        verbose_name_plural = _('Завантажені фото')

    file = models.ImageField(_('Файл'))

    owner = models.ForeignKey(
        'user.UserProfile',
        verbose_name=_('Власник'),
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    created_at = models.DateTimeField(_('Завантажено'), default=timezone.now)
