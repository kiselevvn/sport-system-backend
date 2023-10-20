from django.utils.translation import gettext_lazy as _

from .managers import SportsmanBaseManager
from .user import User


class Sportsman(User):
    """
    Спортсмен
    """

    objects = SportsmanBaseManager()

    class Meta:
        verbose_name = _("Спортсмен")
        verbose_name_plural = _("Спортсмены")
        proxy = True
