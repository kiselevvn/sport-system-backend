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
    "import_export",
    "puml_generator",
]

PROJECT_APPS = [
    # Справочная база NP
    "backend.apps.np",
    # Главное приложение
    "backend.src",
    # Вспомогательные функции
    "backend.apps.services",
    # Физкультурно-спортивные организации
    "backend.apps.organization",
    # Пользователи
    "backend.apps.users",
    # Рейтинговые списки
    "backend.apps.ekp",
    # Спортивные испытания
    "backend.apps.competitions",
    # Обследования
    "backend.apps.examination",
    # Тестирование
    "backend.apps.testing",
    # Рейтинговые списки
    # "backend.apps.rating",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
