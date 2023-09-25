from rest_framework.generics import CreateAPIView
from .....serializers import EmployeeCreateSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """"""

    serializer_class = EmployeeCreateSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
