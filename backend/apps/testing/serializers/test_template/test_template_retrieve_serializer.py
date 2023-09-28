from rest_framework import serializers

from backend.apps.testing.models import (
    Answer,
    MediaObject,
    Question,
    TestTemplate,
)


class MediaObjectTestTemplateRetrieveSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = MediaObject
        fields = "__all__"


class AnswerTestTemplateRetrieveSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = Answer
        fields = "__all__"


class QuestionTestTemplateRetrieveSerializer(serializers.ModelSerializer):
    """"""

    answers = AnswerTestTemplateRetrieveSerializer(
        many=True,
    )
    media_objects = MediaObjectTestTemplateRetrieveSerializer(
        many=True,
    )

    class Meta:
        model = Question
        fields = "__all__"


class TestTemplateRetrieveSerializer(serializers.ModelSerializer):
    """"""

    questions = QuestionTestTemplateRetrieveSerializer(
        many=True,
    )

    class Meta:
        model = TestTemplate
        fields = "__all__"
