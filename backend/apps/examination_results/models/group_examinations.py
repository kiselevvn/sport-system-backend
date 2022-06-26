from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import (
    DateCreatedMixin,
    DescriptionMixin,
    NameMixin,
)


class GroupExaminations(NameMixin, DescriptionMixin, DateCreatedMixin):
    """
    Event
    Группа обследований
    """

    examinations = models.ManyToManyField(
        "examination_results.Examination",
        verbose_name=_("Обследования"),
    )

    class Meta:
        verbose_name = _("Группа обследований")
        verbose_name_plural = _("Группы обследований")
