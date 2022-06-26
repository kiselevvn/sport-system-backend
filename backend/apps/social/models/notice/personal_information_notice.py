from django.db import models
from django.utils.translation import gettext as _

from .information_notice import InformationNotice


class PersonalInformationNotice(InformationNotice):
    """
    Personal Information Notice
    Персональное информационное уведомления
    """

    user = models.ForeignKey(
        "users.User", verbose_name=_("Пользователь"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Персональное уведомления")
        verbose_name_plural = _("Персональные Уведомления")
