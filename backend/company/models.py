from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here


class Company(models.Model):

    class Meta:
        verbose_name = _('Підриємство')
        verbose_name_plural = _('Підприємства')

    LICENSES = (
        (1, 'Стандарт'),
        (3, 'Повна'),
        (4, 'Користувацька'),
    )

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=50,
        blank=False)

    license = models.SmallIntegerField(
        verbose_name=_('Ліцензія'),
        choices=LICENSES)

    def __str__(self):
        return '%s' % self.name


class ContractorCompany(models.Model):
    class Meta:
        verbose_name = _('Контрагент')
        verbose_name_plural = _('Контрагенти')

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=150,
        blank=False)

    parent = models.ForeignKey(
        'Company',
        verbose_name=_('Підриємство власник'),
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.name, self.parent)
