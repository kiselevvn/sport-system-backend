from rest_framework import serializers

from backend.apps.testing.models import TestTemplate


class TestTemplateListSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = TestTemplate
        fields = "__all__"
