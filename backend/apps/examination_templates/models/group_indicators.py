from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DescriptionMixin,
    NameMixin,
    OrderMixin,
    ShortNameMixin,
)


class GroupIndicators(
    NameMixin,
    ShortNameMixin,
    DescriptionMixin,
):
    """
    Group of medical indicators
    Группа медецинских показателей
    """

    indicators = models.ManyToManyField("examination_templates.Indicator")

    class Meta:
        verbose_name = _("Group of medical indicators")
        verbose_name_plural = _("Group of medical indicators")
