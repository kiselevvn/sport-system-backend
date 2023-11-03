from rest_framework.generics import ListAPIView

from backend.apps.services.views.helpers import StandardPagination

from .....selectors import get_sportsmans
from .....serializers import (  # SportsmanShortSerializer,
    SportsmanRetriveSerializer,
)
from ..filters import SportsmansFilter


class SportsmanPageAPIView(ListAPIView):
    """
    Постраничный вывод спортсменов
    """

    # serializer_class = SportsmanShortSerializer
    serializer_class = SportsmanRetriveSerializer
    queryset = get_sportsmans()
    pagination_class = StandardPagination
    filterset_class = SportsmansFilter

    def perform_create(self, serializer):
        return super().perform_create(serializer)
