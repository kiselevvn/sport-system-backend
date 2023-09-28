from service_objects import fields, services

from ..models import TestTemplate


class TestTemplateCreate(services.Service):
    validated_data = fields.DictField()
    # instance = fields.ModelField(QuestionnaireResult)

    def process(self):
        validated_data = self.cleaned_data["validated_data"]
        instance = TestTemplate.objects.create(**validated_data)
        instance.save()
        return instance
