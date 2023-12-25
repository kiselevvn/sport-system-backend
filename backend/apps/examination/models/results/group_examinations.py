from django.db import models
from django.utils.translation import gettext as _


class GroupExaminations(models.Model):
    """
    Группа обследований
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )
    examinations = models.ManyToManyField(
        "examination.Examination",
        verbose_name=_("Обследования"),
    )
    event = models.ForeignKey(
        "ekp.Event",
        verbose_name=_("Событие"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Группа обследований")
        verbose_name_plural = _("Группы обследований")
