from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DateCreatedMixin,
    DescriptionMixin,
    NameMixin,
)


class Examination(NameMixin, DescriptionMixin, DateCreatedMixin):
    """
    Examination
    Обследование
    """

    template = models.ForeignKey(
        "examination.ExaminationTemplate",
        verbose_name=_("Шаблон обследования"),
        on_delete=models.CASCADE,
    )

    date = models.DateField(_("Дата обследования"), blank=True, null=True)

    event = models.ForeignKey(
        "examination.Event",
        verbose_name=_("Событие"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    # group =

    class Meta:
        verbose_name = _("Обследование")
        verbose_name_plural = _("Обследования")
