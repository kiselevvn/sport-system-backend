# Универсальная система система спортивного отбора #

## Зависимости ##

* [Python 3.7.3](https://www.python.org/downloads/) 
* [Poetry](https://python-poetry.org/docs/#installation) паетный менеджер
* База данных [Postgres](https://www.postgresql.org/download/)

## Подготовка и запуск приложения ##

Клонировать

Установка зависимостей Python:

```cmd
poetry install
```

Применение миграций миграций к базе:

```cmd
poetry run task migrate
```

```env
DEBUG=true
SITE_DOMAIN="*"
SECRET_KEY=""
DATABASE_URL=""
```

## Список справочников ##

* [Реестр открытых данных](https://sportrf.gov.ru/nsi)
* [Реестр видов спорта](https://www.minsport.gov.ru/activity/government-regulation/priznanie-vidov-sporta-i-sportivnyh-discziplin-vserossijskij-reestr-vidov-sporta/)
* [Перечни физкультурно-спортивных организаций](https://www.minsport.gov.ru/activity/mass-sport/perechni-fizkulturno-sportivnyh-organizaczij/)


https://sportrf.gov.ru/