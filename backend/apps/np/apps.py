from django.apps import AppConfig


class NpConfig(AppConfig):
    """
    Справочная база NP
    """

    default_auto_field = "django.db.models.AutoField"
    name = "backend.apps.np"
    verbose_name = "Справочник"
