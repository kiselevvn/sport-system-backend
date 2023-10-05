from django.db import models
from django.utils.translation import gettext as _
from backend.apps.services.models import (
    DateCreatedMixin,
    DescriptionMixin,
)


class Group(DateCreatedMixin, DescriptionMixin):
    """
    Группа
    """

    level = models.IntegerField(
        _("Уровень образования группы"), help_text=_(""), default=1
    )

    сhar_code = models.CharField(_("Символьный код"), max_length=6, default="")

    is_training_started = models.BooleanField(
        _("Начат процесс обучения"), default=False
    )
    date_training_started = models.DateField(
        _("Дата начала обучения"), blank=True, null=True
    )

    is_training_completed = models.BooleanField(
        _("Процесс обучения завершен"), default=False
    )
    date_training_completed = models.DateField(
        _("Дата окончания обучения"), blank=True, null=True
    )

    is_archival = models.BooleanField(
        _("Является архивной"), blank=True, null=True
    )
    archive_date = models.DateTimeField(
        _("Дата архивации"),
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )

    @property
    def name(self):
        """
        Наименование группы
        """
        name = f"{self.level}"
        if self.сhar_code != "":
            name += f" {self.сhar_code}"
        return name

    class Meta:
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")
