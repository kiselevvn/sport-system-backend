from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DateCreatedMixin,
    DescriptionMixin,
    NameMixin,
)


class ResultIndicator(NameMixin, DescriptionMixin, DateCreatedMixin):
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
    result = models.JSONField(
        _("результат обследования"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Результат показателя")
        verbose_name_plural = _("Результат показателей")
