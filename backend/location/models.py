from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class City(models.Model):

    class Meta:
        verbose_name = _('Місто')
        verbose_name_plural = _('Міста')

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=50
    )

    def __str__(self):
        return '%s' % self.name


class Region(models.Model):

    class Meta:
        verbose_name = _('Район')
        verbose_name_plural = _('Райони')

    city = models.ForeignKey(
        'location.City',
        related_name='city',
        verbose_name=_('Місто'),
        on_delete=models.CASCADE)

    region = models.CharField(
        verbose_name=_('Район'),
        max_length=256)

    def __str__(self):
        return '%s, %s' % (self.city, self.region)


class Route(models.Model):

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршрути"

    agent = models.ForeignKey(
        'user.UserProfile',
        related_name='agent',
        verbose_name=_('Агент'),
        on_delete=models.CASCADE)

    route_region = models.ForeignKey(
        'location.Region',
        related_name='route_region',
        verbose_name=_('Район'),
        on_delete=models.CASCADE)

    created = models.DateTimeField(
        verbose_name=_('Створено'),
        default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.agent, self.route_region)
