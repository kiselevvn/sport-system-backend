from django.db import models
from django.utils.translation import gettext as _


class ResultIndicator(models.Model):
    """
    Результат показателя
    """

    value = models.FloatField(_("Значение"))
    result_examination = models.ForeignKey(
        "examination.ResultExamination",
        verbose_name=_("Обследование"),
        on_delete=models.CASCADE,
        related_name="results_indicators",
    )
    group_indicators = models.ForeignKey(
        "examination.GroupIndicators",
        verbose_name=_("Группа показателя"),
        on_delete=models.CASCADE,
        related_name="results_indicators",
    )
    indicator = models.ForeignKey(
        "examination.Indicator",
        verbose_name=_("Показатель"),
        on_delete=models.CASCADE,
        related_name="results_indicators",
    )
    result = models.JSONField(
        _("результат обследования"), blank=True, null=True
    )

    def save_result_value(self, commit=True):
        new_value = None
        if self.indicator in (
            self.indicator.Type.FLOAT,
            self.indicator.Type.INTEGER,
        ):
            new_value = self.result["value"]
        if self.value == new_value:
            return False, None
        self.value = new_value
        self.save()
        return True, self

    class Meta:
        verbose_name = _("Результат показателя")
        verbose_name_plural = _("Результат показателей")
