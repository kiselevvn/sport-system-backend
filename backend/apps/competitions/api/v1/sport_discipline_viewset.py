from rest_framework import viewsets

from backend.apps.competitions.models import SportDiscipline
from backend.apps.competitions.serializers import SportDisciplineSerializer


class SportDisciplineViewSet(viewsets.ModelViewSet):
    """ """

    serializer_class = SportDisciplineSerializer
    queryset = SportDiscipline.objects.all().select_related("sport_category")
