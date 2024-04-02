from django.db import models
from django.utils.translation import gettext as _


class SportResult(models.Model):
    """
    Спортивный результат
    """

    # sportsman =
    # sport_competition =
    sport_competition = models.ForeignKey(
        "competitions.User", verbose_name=_("Спортивное испытание")
    )
    sportsman = models.ForeignKey(
        "users.User",
        verbose_name=_("Спортсмен"),
        related_name="results_sport_competition",
    )

    class Meta:
        verbose_name = _("Спортивный результат")
        verbose_name_plural = _("Спортивные результаты")
