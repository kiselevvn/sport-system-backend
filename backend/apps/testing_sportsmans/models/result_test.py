from django.db import models
from django.utils.translation import gettext as _

from backend.apps.services.models import DateCreatedMixin


class ResultTest(DateCreatedMixin):
    """
    Результат тестирования
    """

    test = models.ForeignKey(
        "testing_sportsmans.TestTemplate",
        verbose_name=_("Тест"),
        on_delete=models.CASCADE,
        related_name="result_tests",
    )

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="result_tests",
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
