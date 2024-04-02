from rest_framework import serializers

from backend.apps.competitions.models import SportDiscipline, SportType

from .sport_category_serializer import SportCategorySerializer
from .sport_type_serializer import SportTypeSerializer


class SportDisciplineSerializer(
    SportTypeSerializer,
    serializers.ModelSerializer,
):
    """
    Вид спорта
    """

    sport_category = SportCategorySerializer()

    class Meta:
        model = SportDiscipline
        fields = [
            "sport_category",
        ] + SportType.list_fields
