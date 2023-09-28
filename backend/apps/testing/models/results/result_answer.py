from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin


class ResultAnswer(DateCreatedMixin):
    """
    Ответ результатов тестирования
    """

    result_question = models.ForeignKey(
        to="testing.ResultQuestion",
        verbose_name=_("Результат тестирования"),
        on_delete=models.CASCADE,
        related_name="answers",
    )

    answers = models.ManyToManyField(
        "testing.Answer", verbose_name=_("Ответы")
    )

    class Meta:
        verbose_name = _("Ответы на вопрос")
        verbose_name_plural = _("Ответы на вопрос")
