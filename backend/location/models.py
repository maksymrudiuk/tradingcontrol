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

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=256,
        null=True)

    agent = models.ForeignKey(
        'user.UserProfile',
        related_name='agent',
        verbose_name=_('Агент'),
        null=True,
        on_delete=models.CASCADE)

    route_item = models.ManyToManyField('store.Store', through='AgentStore')

    created = models.DateTimeField(
        verbose_name=_('Створено'),
        default=timezone.now)

    def __str__(self):
        return '%s - %s %s' % (self.name,
                               self.agent.first_name,
                               self.agent.last_name)


class AgentStore(models.Model):

    class Meta:
        verbose_name = _('Агент - Торгова точка')
        verbose_name = _('Агенти - Торгові точки')

    agent_store = models.ForeignKey(
        'store.Store',
        related_name='agent_store',
        verbose_name=_('Торгова точка'),
        on_delete=models.CASCADE)

    route = models.ForeignKey(
        'Route',
        related_name='route',
        verbose_name=_('Маршрут'),
        on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.route, self.agent_store)
