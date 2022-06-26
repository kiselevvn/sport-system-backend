from django.db import models
from django.utils.translation import gettext as _

from .information_notice import InformationNotice


class GroupInformationNotice(InformationNotice):
    """
    Group Information Notice
    Групповое информационное уведомления
    """

    users = models.ManyToManyField(
        "users.User", verbose_name=_("Пользователь"),
    )

    class Meta:
        verbose_name = _("Групповое уведомления")
        verbose_name_plural = _("Групповые Уведомления")
