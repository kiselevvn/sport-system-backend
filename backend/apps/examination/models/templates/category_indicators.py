from django.db import models
from django.utils.translation import gettext as _

from .indicator import Indicator


class CategoryIndicators(models.Model):
    """
    Категория медецинских показателей
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Категория медецинских показателей")
        verbose_name_plural = _("Категории медецинских показателей")
