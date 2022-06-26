from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin


class ResultTesting(DateCreatedMixin):
    """
    Результат тестирования
    """

    test = models.ForeignKey(
        "testing_templates.TestTemplate",
        verbose_name=_("Тест"),
        on_delete=models.CASCADE,
        related_name="result_testings",
    )

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="result_testings",
    )

    result_score = models.PositiveIntegerField(
        _("Кол-во баллов"), blank=True, null=True
    )

    @property
    def name(self):
        return f"{self.user} - {self.test}"

    class Meta:
        verbose_name = _("Результат тестирования")
        verbose_name_plural = _("Результаты тестирования")
        unique_together = ["test", "user"]
