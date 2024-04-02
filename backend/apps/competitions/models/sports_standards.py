from django.db import models
from django.utils.translation import gettext as _


class SportsStandards(models.Models):
    """
    Спортивный норматив
    """

    class Meta:
        verbose_name = _("Спортивная дисциплина")
        verbose_name_plural = _("Спортивные дисциплина")
