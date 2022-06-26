from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin

from .question_testing import QuestionTesting


class AnswerTesting(DateCreatedMixin):
    """
    Ответ результатов тестирования
    """

    question_testing = models.ForeignKey(
        to=QuestionTesting,
        verbose_name=_("Результат тестирования"),
        on_delete=models.CASCADE,
        related_name="answers",
    )

    answers = models.ManyToManyField(
        "testing_templates.Answer", verbose_name=_("Ответы")
    )

    class Meta:
        verbose_name = _("Ответы на вопрос")
        verbose_name_plural = _("Ответы на вопрос")
