from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin


class ResultQuestion(DateCreatedMixin):
    """
    Вопрос результатов тестирования
    """

    result_test = models.ForeignKey(
        "testing_sportsmans.ResultTest",
        verbose_name=_("Результат тестирования"),
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question = models.ForeignKey(
        "testing_sportsmans.Question",
        verbose_name=_("Вопрос"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Ответы на вопрос")
        verbose_name_plural = _("Ответы на вопрос")
        unique_together = ["result_test", "question"]
