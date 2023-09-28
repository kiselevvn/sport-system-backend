from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DateCreatedMixin,
    DescriptionMixin,
    NameMixin,
)


class ResultExaminations(NameMixin, DescriptionMixin, DateCreatedMixin):
    """
    Event
    Группа обследований
    """

    examination = models.ForeignKey(
        "examination.Examination",
        verbose_name=_("Обследование"),
        on_delete=models.CASCADE,
    )
    sportsman = models.ForeignKey(
        "users.User", verbose_name=_("Спортсмен"), on_delete=models.CASCADE
    )
    result = models.JSONField(
        _("результат обследования"), blank=True, null=True
    )

    class Meta:
        verbose_name = _("Группа обследований")
        verbose_name_plural = _("Группы обследований")
