from .user import User
from .managers import EmployeeBaseManager


class Employee(User):
    """
    Сотрудник
    """

    objects = EmployeeBaseManager()

    class Meta:
        proxy = True
