from django.db import models
from django.utils.translation import gettext as _


class Examination(models.Model):
    """
    Обследование
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )

    # group =

    class Meta:
        verbose_name = _("Обследование")
        verbose_name_plural = _("Обследования")
