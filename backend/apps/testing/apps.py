from django.apps import AppConfig


class TestingConfig(AppConfig):
    """
    Тестирование спортсменов
    """

    default_auto_field = "django.db.models.AutoField"
    name = "backend.apps.testing"
    verbose_name = "Тестирование спортсменов"
