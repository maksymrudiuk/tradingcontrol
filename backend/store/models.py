from django.db import models
from django.utils.translation import gettext as _


class Store(models.Model):

    class Meta:
        verbose_name = _("Торгова точка")
        verbose_name_plural = _("Торгові точки")

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=256)

    address = models.CharField(
        verbose_name=_('Адреса'),
        max_length=256)

    goods = models.ManyToManyField('goods.Goods', through='GoodsInStore')

    lat = models.FloatField(
        verbose_name=_('Широта'),
        blank=True,
        null=True)

    lon = models.FloatField(
        verbose_name=_('Довгота'),
        blank=True,
        null=True)

    def __str__(self):
        return '%s  %s' % (self.name, self.get_short_address())

    def get_short_address(self):
        return ' '.join(self.address.split(',')[0:2])


class GoodsInStore(models.Model):

    class Meta:
        verbose_name = _("Торгова точка - Товар")
        verbose_name_plural = _("Торгові точки - Товари")

    store = models.ForeignKey(
        "Store",
        verbose_name=_("Торгова точка"),
        on_delete=models.CASCADE)

    goods = models.ForeignKey(
        "goods.Goods",
        verbose_name=_("Товар"),
        on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.goods, self.store)
