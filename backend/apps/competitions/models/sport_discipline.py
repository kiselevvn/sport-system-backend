from django.db import models
from django.utils.translation import gettext as _

from .sport_type import SportType


class SportDiscipline(SportType):
    """
    Вид спорта
    """

    sport_category = models.ForeignKey(
        "competitions.SportCategory",
        verbose_name=_("Вид спорта"),
        on_delete=models.CASCADE,
        related_name="sport_disciplines",
    )

    class Meta:
        verbose_name = _("Спортивная дисциплина")
        verbose_name_plural = _("Спортивные дисциплина")
