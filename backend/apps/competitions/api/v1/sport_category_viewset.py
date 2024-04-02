from rest_framework import viewsets

from backend.apps.competitions.models import SportCategory
from backend.apps.competitions.serializers import SportCategorySerializer


class SportCategoryViewSet(viewsets.ModelViewSet):
    """ """

    serializer_class = SportCategorySerializer
    queryset = SportCategory.objects.all()
