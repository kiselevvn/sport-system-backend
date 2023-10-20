from rest_framework.serializers import ModelSerializer

from backend.apps.competitions.models import SportType


class SportTypeSerializer(ModelSerializer):
    """
    Вид спорта
    """

    class Meta:
        model = SportType
        # fields = ["id", ]
        fields = "__all__"
