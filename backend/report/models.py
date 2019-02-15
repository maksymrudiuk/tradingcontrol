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

    store = models.ForeignKey(
        'store.Store',
        null=True,
        verbose_name=_('Асортимент'),
        on_delete=models.CASCADE)

    t_start = models.CharField(
        verbose_name=_('Початок роботи'),
        max_length=128)

    t_finish = models.CharField(
        verbose_name=_('Кінець роботи'),
        max_length=128)

    t_delta = models.CharField(
        verbose_name=_('Тривалість роботи'),
        max_length=128)

    owner = models.ForeignKey(
        'user.UserProfile',
        verbose_name=_('Власник'),
        null=True,
        on_delete=models.CASCADE)

    assortment_percent = models.SmallIntegerField(
        verbose_name=_('Наявність у %'),
        null=True)

    created_at = models.DateTimeField(_('Створений'), default=timezone.now)

    def __str__(self):
        return '%s - %s - %s - %s (%s)' % (self.store, self.owner,
                                           self.name, self.created_at, self.id)


class ReportItem(models.Model):

    class Meta:
        verbose_name = _('Товар - Звіт')
        verbose_name_plural = _('Товари - Звіт')

    goods_item = models.ForeignKey(
        'goods.Goods',
        related_name='goods_item',
        verbose_name='Товар',
        null=True,
        on_delete=models.SET_NULL)

    status = models.BooleanField(_('Знайдено?'))

    report = models.ForeignKey(
        'ReportData',
        related_name='assortment',
        verbose_name=_('Звіт'),
        blank=False,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return '(%s - %s)' % (self.goods_item.name, self.report)
