from django.contrib.auth import get_user_model
from rest_framework import serializers


class EmployeeRetriveSerializer(serializers.ModelSerializer):
    """
    Сериализатор детального
    представления сотрудника
    """

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "second_name",
        ]
