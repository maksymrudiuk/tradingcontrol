from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Goods(models.Model):

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товари')

    CATEGORY = (
        (1, 'Морозиво'),
        (3, 'Масло'),
        (4, 'Заморожені продукти'),
        (5, 'Заморожені ягоди перетерті з цукром'),
        (6, 'Заморожене тісто'),
        (7, 'Глазуровані сирки'),
        (8, 'Заморожена картопля та картопляні вироби'),
        (9, 'Заморожені напівфабрикати'),
        (10, 'Вафельні продукти'),
    )

    name = models.CharField(
        verbose_name=_('Назва'),
        max_length=256)

    image = models.ImageField(_('Зображення'))

    bar_code = models.CharField(
        verbose_name=_('Штрих Код'),
        max_length=100)

    category = models.SmallIntegerField(
        verbose_name=_('Категорія'),
        choices=CATEGORY,
        default=None)

    def __str__(self):
        return '%s' % self.name
