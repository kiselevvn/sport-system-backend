from rest_framework import serializers

from backend.apps.testing_sportsmans.models import TestTemplate


class TestTemplateListSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = TestTemplate
        fields = "__all__"
