# from rest_framework import serializers
from ...services import create_employee_service
from ..group import AccountFieldsSerializer, NameFieldsSerializer


class EmployeeCreateSerializer(NameFieldsSerializer, AccountFieldsSerializer):
    """
    Создание спортсмена
    """

    def create(self, validated_data):
        return create_employee_service(**validated_data)
