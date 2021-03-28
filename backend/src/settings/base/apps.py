DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "djoser",
    "corsheaders",
    "rest_framework",
    "drf_yasg",
]

PROJECT_APPS = [
    "backend.apps.services",
    "backend.apps.users",
    "backend.apps.examination_templates",
]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
