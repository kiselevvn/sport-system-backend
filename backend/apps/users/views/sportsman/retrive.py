from rest_framework.generics import RetrieveAPIView
from ...serializers import SportsmanRetriveSerializer


class SportsmanRetrieveAPIView(RetrieveAPIView):
    """"""

    serializer_class = SportsmanRetriveSerializer
