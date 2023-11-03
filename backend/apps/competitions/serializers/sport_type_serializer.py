from rest_framework import serializers

from backend.apps.competitions.models import SportType


class SportTypeSerializer(serializers.ModelSerializer):
    """
    Вид спорта
    """

    is_discipline = serializers.BooleanField()
    discipline_id = serializers.CharField()
    public_id = serializers.CharField()
    get_seaseon_id = serializers.CharField()
    get_seaseon_label = serializers.CharField()
    get_propagation_id = serializers.CharField()
    get_propagation_label = serializers.CharField()
    get_development_label = serializers.CharField()
    get_extra_id = serializers.CharField()
    get_extra_label = serializers.CharField()
    get_group_id = serializers.CharField()
    get_group_label = serializers.CharField()

    class Meta:
        model = SportType
        fields = SportType.list_fields
