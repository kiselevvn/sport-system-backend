from .employee import (
    EmployeeCreateSerializer,
    EmployeeRetriveSerializer,
    EmployeeShortSerializer,
)
from .sportsman import (
    SportsmanCreateSerializer,
    SportsmanRetriveSerializer,
    SportsmanShortSerializer,
)

__all__ = [
    "SportsmanCreateSerializer",
    "SportsmanShortSerializer",
    "SportsmanRetriveSerializer",
    "EmployeeCreateSerializer",
    "EmployeeShortSerializer",
    "EmployeeRetriveSerializer",
]
