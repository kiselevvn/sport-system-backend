from .employee.create import EmployeeCreateAPIView
from .employee.page import EmployeePageAPIView
from .employee.retrive import EmployeeRetrieveAPIView
from .sportsman.create import SportsmanCreateAPIView
from .sportsman.page import SportsmanPageAPIView
from .sportsman.retrive import SportsmanRetrieveAPIView

__all__ = [
    "SportsmanCreateAPIView",
    "SportsmanPageAPIView",
    "SportsmanRetrieveAPIView",
    "EmployeeRetrieveAPIView",
    "EmployeeCreateAPIView",
    "EmployeePageAPIView",
]
