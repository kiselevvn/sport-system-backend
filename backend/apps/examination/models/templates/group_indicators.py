from django.db import models
from django.utils.translation import gettext as _

from .indicator import Indicator


class GroupIndicators(models.Model):
    """
    Группа медецинских показателей
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )
    short_name = models.CharField(
        verbose_name=_("Краткое наименование"),
        max_length=50,
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Группа медецинских показателей")
        verbose_name_plural = _("Группы медецинских показателей")
