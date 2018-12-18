from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):

    class Meta:
        verbose_name = _("Користувач")
        verbose_name_plural = _("Користувачі")

    ROLES = (
        (1, 'Агент'),
        (3, 'Директор'),
    )

    user_photo = models.ImageField(verbose_name=_('Фото'), blank=True)

    phone = models.CharField(
        verbose_name=_('Телефон'),
        max_length=50,
        blank=True)

    company = models.ForeignKey(
        'company.ContractorCompany',
        related_name='company_staff',
        verbose_name=_('Контрагент'),
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    role = models.SmallIntegerField(
        verbose_name=_('Посада'),
        null=True,
        blank=True,
        choices=ROLES)

    def __str__(self):
        return self.get_short_name()

    @property
    def admin_list_display(self):
        return self._get_short_name()

    @property
    def isDirector(self):
        return self.role == 3

    @property
    def isAgent(self):
        return self.role == 1

    def get_short_name(self):
        return self.username


class UserGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _('Група')
        verbose_name_plural = _('Групи')
