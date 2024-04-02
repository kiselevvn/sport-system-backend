from django.db import models
from django.utils.translation import gettext as _


class ExaminationTemplateIndicators(models.Model):
    """
    Показатель шаблона обследований
    """

    examination_template = models.ForeignKey(
        "examination.ExaminationTemplate",
        verbose_name=_("Шаблон обследования"),
        on_delete=models.CASCADE,
        related_name="examination_template_indicators",
    )
    indicator = models.ForeignKey(
        "examination.Indicator",
        verbose_name=_("Показатель"),
        on_delete=models.CASCADE,
        related_name="examination_template_indicators",
    )
    group_indicator = models.ForeignKey(
        "examination.GroupIndicators",
        verbose_name=_("Группа показателей"),
        on_delete=models.CASCADE,
        related_name="examination_template_indicators",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Показатель шаблона обследований")
        verbose_name_plural = _("Показатели шаблона обследований")
