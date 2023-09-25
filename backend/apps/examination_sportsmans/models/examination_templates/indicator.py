from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DescriptionMixin, NameMixin

from .enum_types_indiactor import EnumTypesIndiactor
from .unit import Unit


class Indicator(NameMixin, DescriptionMixin):
    """
    Indicator
    Показатель
    """

    type_indicator = models.PositiveIntegerField(
        verbose_name=_("Type Indicator"),
        choices=EnumTypesIndiactor.choices,
    )
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Unit"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Показатель")
        verbose_name_plural = _("Показатели")
