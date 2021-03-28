from django.db import models
from django.utils.translation import gettext as _
from backend.apps.examination_templates.enums import TypeIndiactor
from backend.apps.services.models import NameMixin, DescriptionMixin
from backend.apps.examination_templates.services import (
    DICT_OF_INDIACTOR_SCHEMES,
)


class Indicator(NameMixin, DescriptionMixin):
    """
    Medical Indicator
    Медицинский показатель
    """

    type_indicator = models.PositiveIntegerField(
        verbose_name=_("Type Medical Indicator"),
        choices=TypeIndiactor.choices,
    )
    unit = models.ForeignKey(
        "examination_templates.Unit",
        verbose_name=_("Unit"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @property
    def schema(self):
        schema = self.get_pydantic_schema()
        return schema

    def get_pydantic_schema(self):
        if self.type_indicator in DICT_OF_INDIACTOR_SCHEMES:
            scheme = DICT_OF_INDIACTOR_SCHEMES[self.type_indicator][
                "schema"
            ].schema_json()
        else:
            raise Exception("Unable to find schema!")
        return scheme

    class Meta:
        verbose_name = _("Medical Indicator")
        verbose_name_plural = _("Medical Indicator's")