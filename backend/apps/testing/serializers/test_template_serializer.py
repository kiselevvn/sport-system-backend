from rest_framework.serializers import ModelSerializer

from backend.apps.testing.models import (
    Answer,
    MediaObject,
    Question,
    TestTemplate,
)


class AnswerTestTemplateSerializer(ModelSerializer):
    """
    Ответ
    """

    class Meta:
        model = Answer
        fields = "__all__"


class MediaObjectTestTemplateSerializer(ModelSerializer):
    """
    Медиа объект
    """

    class Meta:
        model = MediaObject
        fields = "__all__"


class QuestionTestTemplateSerializer(ModelSerializer):
    """
    Вопрос
    """

    answers = AnswerTestTemplateSerializer(many=True, read_only=True)
    media_objects = MediaObjectTestTemplateSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Question
        fields = "__all__"


class TestTemplateSerializer(ModelSerializer):
    """
    Шаблон тестирования
    """

    questions = QuestionTestTemplateSerializer(many=True, read_only=True)

    class Meta:
        model = TestTemplate
        fields = "__all__"
