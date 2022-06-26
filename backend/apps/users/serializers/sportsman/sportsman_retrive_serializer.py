from rest_framework import serializers
from django.contrib.auth import get_user_model


class SportsmanRetriveSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "second_name",
        ]
