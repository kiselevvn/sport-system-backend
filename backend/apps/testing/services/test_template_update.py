from django import forms
from service_objects import fields, services

from ..models import TestTemplate


class TestTemplateUpdate(services.Service):
    validated_data = fields.DictField()
    id = forms.IntegerField(required=False)
    instance = fields.ModelField(TestTemplate, required=False)

    def process(self):
        assert ("id" in self.cleaned_data) or (
            "validated_data" in self.cleaned_data
        ), "Невозможно получить instance для выполнения обновления"
        validated_data = self.cleaned_data["validated_data"]
        if "instance" in self.cleaned_data:
            instance = self.cleaned_data["instance"]
        else:
            instance = TestTemplate.objects.get(pk=id)
        instance.update(**validated_data)
        # instance.save()
        return instance
