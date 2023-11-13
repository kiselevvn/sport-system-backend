from django.db import models
from django.utils.translation import gettext as _


class ResultExamination(models.Model):
    """
    Результат обследования
    """

    template = models.ForeignKey(
        "examination.ExaminationTemplate",
        verbose_name=_("Обследование"),
        on_delete=models.CASCADE,
        related_name="results_indicators",
    )
    examination = models.ForeignKey(
        "examination.Examination",
        verbose_name=_("Обследование"),
        on_delete=models.CASCADE,
        related_name="results",
    )
    sportsman = models.ForeignKey(
        "users.User",
        verbose_name=_("Спортсмен"),
        on_delete=models.CASCADE,
        related_name="results_examination",
    )
    result = models.JSONField(
        _("результат обследования"), blank=True, null=True
    )
    date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата проведения")
    )

    class Meta:
        verbose_name = _("Результат обследования")
        verbose_name_plural = _("Результат обследований")
