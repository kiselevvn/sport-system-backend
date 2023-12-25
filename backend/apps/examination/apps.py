from django.apps import AppConfig


class ExaminationConfig(AppConfig):
    """
    Осмотр спортсменов
    """

    default_auto_field = "django.db.models.AutoField"
    name = "backend.apps.examination"
    verbose_name = "2. Медицинские обследования"
