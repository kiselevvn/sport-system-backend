from django import forms
from service_objects import fields, services

from ..models import Question


class QuestionUpdate(services.Service):
    validated_data = fields.DictField()
    test_template_id = forms.IntegerField()

    def process(self):
        validated_data = self.cleaned_data["validated_data"]
        test_template_id = self.cleaned_data["test_template_id"]
        instance = Question.objects.create(
            test_template_id=test_template_id, **validated_data
        )
        instance.save()
        return instance
