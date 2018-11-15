from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class ReportData(models.Model):

    class Meta:
        verbose_name = _('Звіт')
        verbose_name_plural = _('Звіти')

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=256)

    assortment = models.ForeignKey(
        'store.Store',
        null=True,
        verbose_name=_('Асортимент'),
        on_delete=models.CASCADE)

    owner = models.ForeignKey(
        'user.UserProfile',
        verbose_name=_('Власник'),
        null=True,
        on_delete=models.CASCADE)

    created_at = models.DateTimeField(_('Створений'), default=timezone.now)

    def __str__(self):
        return '%s' % self.name


class ReportItem(models.Model):

    class Meta:
        verbose_name = _('Товар - Звіт')
        verbose_name_plural = _('Товари - Звіт')

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=256,
        blank=True)

    status = models.CharField(
        verbose_name=_('Статус'),
        max_length=256,
        blank=True)

    report = models.ForeignKey(
        'ReportData',
        verbose_name=_('Звіт'),
        blank=False,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name

