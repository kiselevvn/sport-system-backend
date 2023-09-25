from rest_framework.generics import CreateAPIView

from .....serializers import SportsmanCreateSerializer


class SportsmanCreateAPIView(CreateAPIView):
    """"""

    serializer_class = SportsmanCreateSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
