from rest_framework.generics import ListAPIView

from backend.apps.services.views.helpers import StandardPagination

from ...selectors import get_employees
from ...serializers import EmployeeShortSerializer
from ..filters import EmployeeFilter


class EmployeePageAPIView(ListAPIView):
    """
    Постраничный вывод спортсменов
    """

    serializer_class = EmployeeShortSerializer
    queryset = get_employees()
    pagination_class = StandardPagination
    filterset_class = EmployeeFilter

    def perform_create(self, serializer):
        return super().perform_create(serializer)
