from django.db import models
from django.utils.translation import gettext as _

from .sport_type import SportType


class SportCategory(SportType):
    """
    Вид спорта
    """

    class Meta:
        verbose_name = _("Вид спорта")
        verbose_name_plural = _("Виды спорта")
