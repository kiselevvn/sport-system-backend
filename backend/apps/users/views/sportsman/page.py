from rest_framework.generics import ListAPIView
from ...serializers import SportsmanShortSerializer
from backend.apps.services.views.helpers import StandardPagination
from ...selectors import get_sportsmans
from ..filters import SportsmansFilter


class SportsmanPageAPIView(ListAPIView):
    """
    Постраничный вывод спортсменов
    """

    serializer_class = SportsmanShortSerializer
    queryset = get_sportsmans()
    pagination_class = StandardPagination
    filterset_class = SportsmansFilter

    def perform_create(self, serializer):
        return super().perform_create(serializer)
