DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "djoser",
    "drf_yasg",
    "puml_generator",
]

PROJECT_APPS = [
    # Главное приложение
    "backend.src",
    # Вспомогательные функции
    "backend.apps.services",
    # Пользователи
    "backend.apps.users",
    # Социальный модуль
    "backend.apps.social",
    # Шаблоны обследований
    # "backend.apps.examination_templates",
    # # Обследования
    # "backend.apps.examination_results",
    "backend.apps.examination_sportsmans",
    # # Шаблоны тестирования
    # "backend.apps.testing_templates",
    # # Тестирование
    # "backend.apps.testing_results",
    "backend.apps.testing_sportsmans",
    # Рейтинговые списки
    "backend.apps.rating",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
