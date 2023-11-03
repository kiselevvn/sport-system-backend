from django.contrib.auth import get_user_model
from rest_framework import serializers


class SportsmanRetriveSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "second_name",
            "birthday",
        ]
