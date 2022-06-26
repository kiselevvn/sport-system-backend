from rest_framework.generics import RetrieveAPIView

from ...serializers import EmployeeRetriveSerializer


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """"""

    serializer_class = EmployeeRetriveSerializer
