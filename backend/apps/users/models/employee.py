from django.utils.translation import gettext_lazy as _

from .managers import EmployeeBaseManager
from .user import User


class Employee(User):
    """
    Сотрудник
    """

    objects = EmployeeBaseManager()

    class Meta:
        verbose_name = _("Сотрудник")
        verbose_name_plural = _("Сотрудники")
        proxy = True
