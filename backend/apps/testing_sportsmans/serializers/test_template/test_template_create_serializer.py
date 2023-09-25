from rest_framework import serializers

from backend.apps.testing_sportsmans.models import TestTemplate


class TestTemplateCreateSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = TestTemplate
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     validated_data["user"] = self.context["request"].user
    #     return QuestionnaireResultInfoUpdate.execute(
    #         {"instance": instance, "validated_data": validated_data}
    #     )

    # def create(self, validated_data):
    #     # validated_data["user"] = self.context["request"].user
    #     return TestTemplateCreate.execute({"validated_data": validated_data})
