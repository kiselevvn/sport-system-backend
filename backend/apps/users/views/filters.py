from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters


class SportsmansFilter(filters.FilterSet):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "second_name",
            "username",
            "email",
            "id",
        ]


class EmployeeFilter(filters.FilterSet):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "second_name",
            "username",
            "email",
            "id",
        ]
