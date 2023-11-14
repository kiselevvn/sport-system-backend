from django.db import models
from django.utils.translation import gettext as _


class IndicatorWeight(models.Model):
    """
    Вес показателя
    """

    value = models.FloatField(_("Значение"), default=1)
    examination_template = models.ForeignKey(
        "examination.ExaminationTemplate",
        verbose_name=_("Показатель"),
        on_delete=models.CASCADE,
        related_name="indicator_weights",
    )
    indicator = models.ForeignKey(
        "examination.Indicator",
        verbose_name=_("Показатель"),
        on_delete=models.CASCADE,
        related_name="indicator_weights",
    )
    max_limit_value = models.FloatField(
        _("Максимальное значение"), blank=True, null=True
    )
    min_limit_value = models.FloatField(
        _("Минимальное значение"), blank=True, null=True
    )
    last_update_value = models.DateTimeField(
        _("Последнее обновленеие значения"), blank=True, null=True
    )
    last_update_limits = models.DateTimeField(
        _("Последнее обновленеие пределов"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Показатель")
        verbose_name_plural = _("Показатели")
