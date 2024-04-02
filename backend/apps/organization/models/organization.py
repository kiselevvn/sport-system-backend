from django.db import models
from django.utils.translation import gettext as _


class Organization(models.Model):
    """
    Организация
    """

    full_name = models.TextField(
        _("Наименование организации полное"),
        blank=True,
        null=True,
    )

    short_name = models.CharField(
        _("Краткое наименование"), max_length=250, blank=True, null=True
    )
    inn = models.CharField(_("ИНН"), max_length=20, blank=True, null=True)

    kpp = models.CharField(_("КПП"), max_length=20, blank=True, null=True)
    ogrn = models.CharField(_("ОГРН"), max_length=20, blank=True, null=True)
    address = models.TextField(_("Адрес"), blank=True, null=True)

    class Meta:
        verbose_name = _("Организация")
        verbose_name_plural = _("Организации")
