from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _


class ImportFromFile(models.Model):
    """
    Импорт данных из файла
    """

    class ImportTypes(models.IntegerChoices):
        """
        Тип сущности
        """

    class ImportStatus(models.IntegerChoices):
        # ERROR = 0, _("")
        ERROR = 1, _("Ошибка импорта")
        SUCCESS = 2, _("Успешный импорт")

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
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )

    class Meta:
        abstract = True
