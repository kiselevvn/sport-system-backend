from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin


class Question(DateCreatedMixin):
    """
    Вопрос
    """

    test = models.ForeignKey(
        "testing_templates.TestTemplate",
        verbose_name=_("Тест"),
        on_delete=models.CASCADE,
        related_name="questions",
    )

    text = models.TextField(
        verbose_name=_("Текст вопроса"), blank=True, null=True
    )

    number = models.PositiveIntegerField(
        verbose_name=_("Порядковый номер"), blank=True, null=True
    )
    win_score = models.PositiveIntegerField(
        verbose_name=_("Кол-во баллов"), blank=True, null=True
    )
    allow_incorrect_answers = models.BooleanField(
        verbose_name=_("Допускать неверные ответы"), default=False
    )

    class Meta:
        verbose_name = _("Вопрос теста")
        verbose_name_plural = _("Вопросы теста")
