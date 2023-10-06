from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from .mixins import DateCreatedMixin


class ImportFromFile(DateCreatedMixin):
    """
    Импорт данных из файла
    """

    class ImportStatus(models.IntegerChoices):
        ERROR = 0, _("Ошибка импорта")
        SUCCESS = 1, _("Успешный импорт")

    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="imported_files",
    )
    file = models.FileField(verbose_name=_("Файл"), blank=True, null=True)
    status = models.IntegerField(
        verbose_name=_("Статус"),
        blank=True,
        null=True,
        choices=ImportStatus.choices,
    )

    class Meta:
        abstract = True
