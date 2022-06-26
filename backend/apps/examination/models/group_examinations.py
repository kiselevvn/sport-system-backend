from django.db import models
from django.utils.translation import gettext as _
from backend.apps.services.models import (
    NameMixin,
    DescriptionMixin,
    DateCreatedMixin,
)


class GroupExaminations(NameMixin, DescriptionMixin, DateCreatedMixin):
    """
    Event
    Группа обследований
    """

    examinations = models.ManyToManyField(
        "examination.Examination",
        verbose_name=_("Обследования"),
    )

    class Meta:
        verbose_name = _("Группа обследований")
        verbose_name_plural = _("Группы обследований")
