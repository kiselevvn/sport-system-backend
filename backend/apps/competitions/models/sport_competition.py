from django.db import models
from django.utils.translation import gettext as _


class SportCompetition(models.Model):
    """
    Спортивное испытание
    """

    # sport_competition =

    class Meta:
        verbose_name = _("Спортивное испытание")
        verbose_name_plural = _("Спортивные испытания")
