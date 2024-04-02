from rest_framework import serializers

from backend.apps.competitions.models import SportCategory

from .sport_type_serializer import SportTypeSerializer


class SportCategorySerializer(
    SportTypeSerializer,
    serializers.ModelSerializer,
):
    """
    Вид спорта
    """

    class Meta:
        model = SportCategory
        fields = "__all__"
