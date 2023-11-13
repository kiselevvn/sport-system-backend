from django.db import models
from django.utils.translation import gettext as _

from .unit import Unit


class Indicator(models.Model):
    """
    Indicator
    Показатель
    """

    class TypeIndiactor(models.IntegerChoices):
        """
        Тип значения атрибута
        """

        INTEGER = 1, _("Целочисленный")
        FLOAT = 2, _("С плавающей точкой")

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    type_indicator = models.PositiveIntegerField(
        verbose_name=_("Type Indicator"),
        choices=TypeIndiactor.choices,
    )
    unit = models.ForeignKey(
        "examination.Unit",
        verbose_name=_("Unit"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Показатель")
        verbose_name_plural = _("Показатели")
