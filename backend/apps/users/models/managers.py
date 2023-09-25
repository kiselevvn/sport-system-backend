from django.db import models


class SportsmanBaseManager(models.Manager):
    """
    Менеджер Спортсменов
    """

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(is_sportsman=True)


class EmployeeBaseManager(models.Manager):
    """
    Менеджер ссотрудников
    """

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(is_employee=True)
