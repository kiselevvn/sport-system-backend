from django.db import models
from django.utils.translation import gettext as _

from .unit import Unit


class Indicator(models.Model):
    """
    Показатель медицинского

    физиологические («внутренние»), физические («внешние») и психологические параметры тренировочной нагрузки   и восстановления;

    параметры качеств силы, быстроты, выносливости, гибкости и ловкости;

    функциональные параметры сердечно-сосудистой и дыхательной систем;

    биомеханические параметры спортивной техники;

    параметры размеров тела.
    """

    class ValueProperty(models.IntegerChoices):
        """
        Свойство значения
        """

        ABSOLUT = 1, _("Абсолютное")
        TOP = 2, _("Верхний порог")
        BOTTOM = 3, _("Нижний порог")

    class Type(models.IntegerChoices):
        """
        Тип значения атрибута
        """

        INTEGER = 1, _("Целочисленный")
        FLOAT = 2, _("С плавающей точкой")
        IS_NORMAL = 3, _("Является нормой")
        PERCENT = 4, _("Процент")

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    type_indicator = models.PositiveIntegerField(
        verbose_name=_("Type Indicator"),
        choices=Type.choices,
    )
    value_property_indicator = models.PositiveIntegerField(
        verbose_name=_("Type Indicator"),
        choices=ValueProperty.choices,
        blank=True,
        null=True,
    )
    category_indicator = models.ForeignKey(
        "examination.CategoryIndicators",
        verbose_name=_("Группа показателей"),
        on_delete=models.CASCADE,
        related_name="indicators",
        blank=True,
        null=True,
    )
    unit = models.ForeignKey(
        "examination.Unit",
        verbose_name=_("Unit"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    property_data = models.JSONField(
        _("Данные"),
        help_text=_("Для работы свойства, необходимо задать набор аргументов"),
        blank=True,
        null=True,
        default=dict,
    )
    property_function = models.CharField(
        _("Функция"), max_length=25, blank=True, null=True
    )
    is_property = models.BooleanField(
        _("Является вычисляемым свойством"), default=False
    )

    class Meta:
        verbose_name = _("Показатель")
        verbose_name_plural = _("Показатели")
