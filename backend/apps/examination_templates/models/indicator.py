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

    # @property
    # def schema(self):
    #     schema = self.get_pydantic_schema()
    #     return schema

    # def get_pydantic_schema(self):
    #     scheme = {}
    #     if type_indicator in INDIACTOR_SCHEMES:
    #         scheme = INDIACTOR_SCHEMES[type_indicator]["schema"].schema()
    #         # print(scheme)
    #     else:
    #         raise Exception("Unable to find schema!")
    #     return scheme

    class Meta:
        verbose_name = _("Medical Indicator")
        verbose_name_plural = _("Medical Indicator's")
