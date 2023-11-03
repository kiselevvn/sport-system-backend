from rest_framework import serializers

from ...services import create_sportsman_service
from ..group import AccountFieldsSerializer, NameFieldsSerializer


class SportsmanCreateSerializer(NameFieldsSerializer, AccountFieldsSerializer):
    """
    Создание спортсмена
    """

    birthday = serializers.DateField(required=False, default=None)

    def create(self, validated_data):
        return create_sportsman_service(**validated_data)
