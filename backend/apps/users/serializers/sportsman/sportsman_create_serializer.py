# from rest_framework import serializers
from ..group import NameFieldsSerializer, AccountFieldsSerializer
from ...services import create_sportsman_service


class SportsmanCreateSerializer(NameFieldsSerializer, AccountFieldsSerializer):
    """
    Создание спортсмена
    """

    def create(self, validated_data):
        return create_sportsman_service(**validated_data)
