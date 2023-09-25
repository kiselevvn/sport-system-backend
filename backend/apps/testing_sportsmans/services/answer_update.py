from django import forms
from service_objects import fields, services

from ..models import Answer


class AnswerUpdate(services.Service):
    validated_data = fields.DictField()
    question_id = forms.IntegerField()

    def process(self):
        validated_data = self.cleaned_data["validated_data"]
        question_id = self.cleaned_data["question_id"]
        instance = Answer.objects.create(
            question_id=question_id, **validated_data
        )
        instance.save()
        return instance
