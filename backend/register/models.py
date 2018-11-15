from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.


class RegisterKey(models.Model):

    class Meta:
        verbose_name = _("Ключ Реєстраці")
        verbose_name_plural = _("Ключі Реєстрації")

    key = models.CharField(
        verbose_name=_('Key'),
        max_length=256,
        unique=True)

    created = models.DateTimeField(
        verbose_name=_('Created'),
        default=timezone.now)

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=False,
        null=True)

    def __str__(self):
        return '%s' % self.email
