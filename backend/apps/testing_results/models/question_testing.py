from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin


class QuestionTesting(DateCreatedMixin):
    """
    Вопрос результатов тестирования
    """

    result_testing = models.ForeignKey(
        to="ResultTesting",
        verbose_name=_("Результат тестирования"),
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question = models.ForeignKey(
        "testing_templates.Question", verbose_name=_("Вопрос"), on_delete=models.CASCADE
    )

    # def __str__(self):
    #     return self.

    class Meta:
        verbose_name = _("Ответы на вопрос")
        verbose_name_plural = _("Ответы на вопрос")
        unique_together = ["result_testing", "question"]
