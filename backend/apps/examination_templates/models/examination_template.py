from django.db import models
from django.utils.translation import gettext as _
from backend.apps.services.models import (
    NameMixin,
    ShortNameMixin,
    DescriptionMixin,
    OrderMixin,
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

    class Meta:
        verbose_name = _("Group of medical indicators")
        verbose_name_plural = _("Group of medical indicators")


class ExaminationTemplate(NameMixin, DescriptionMixin):
    """
    Medical Examination Template
    Шаблоны Медицинских Обследований
    """

    class Meta:
        verbose_name = _("Medical Examination Template")
        verbose_name_plural = _("Medical Examination Template's")


class ExaminationTemplateAndGroupIndicatorsMTM(OrderMixin):
    """
    Many to Many
    Medical Examination And Group Indicators
    """

    examination_template = models.ForeignKey(
        "examination_templates.ExaminationTemplate",
        verbose_name=_("Medical Examination Template"),
        on_delete=models.CASCADE,
    )
    group_indicators = models.ForeignKey(
        "examination_templates.GroupIndicators",
        verbose_name=_("Group Medical Indicators"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _(
            "Medical Examination And Group Medical Indicators MTM"
        )
        verbose_name_plural = _(
            "Medical Examination And Group Medical Indicators MTM"
        )
        unique_together = [["examination_template", "group_indicators"]]

    def __str__(self):
        return self.name


class GroupIndicatorsAndIndicatorMTM(OrderMixin):
    """
    Many to Many
    Group Medical Indicators And Medical Indicator
    """

    indicator = models.ForeignKey(
        "examination_templates.Indicator",
        verbose_name=_("Medical Examination Template"),
        on_delete=models.CASCADE,
    )
    group_indicators = models.ForeignKey(
        "examination_templates.GroupIndicators",
        verbose_name=_("Group Medical Indicators"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Medical Examination And Group Indicators MTM")
        verbose_name_plural = _("Medical Examination And Group Indicators MTM")
        unique_together = [["group_indicators", "indicator"]]
