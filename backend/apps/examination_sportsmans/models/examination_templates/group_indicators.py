from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DescriptionMixin,
    NameMixin,
    OrderMixin,
    ShortNameMixin,
)

from .indicator import Indicator


class GroupIndicators(
    NameMixin,
    ShortNameMixin,
    DescriptionMixin,
):
    """
    Group of medical indicators
    Группа медецинских показателей
    """

    indicators = models.ManyToManyField(Indicator, verbose_name=_("Показатели"))

    class Meta:
        verbose_name = _("Группа медецинских показателей")
        verbose_name_plural = _("Группы медецинских показателей")
