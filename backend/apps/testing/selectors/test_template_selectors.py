from django.db.models import Prefetch

from backend.apps.testing.models import (
    Answer,
    MediaObject,
    Question,
    TestTemplate,
)


class TestTemplateSelectors:
    """
    Набор запросов
    Шаблон тестирования
    """

    @classmethod
    def base_queryset():
        return TestTemplate.objects.all()

    @classmethod
    def all(cls):
        return TestTemplate.objects.prefetch_related(
            Prefetch(
                lookup="questions",
                queryset=Question.objects.prefetch_related(
                    Prefetch(
                        lookup="media_objects",
                        queryset=MediaObject.objects.all(),
                    ),
                    Prefetch(lookup="answers", queryset=Answer.objects.all()),
                ),
            ),
        )

    @classmethod
    def get(cls, id: int):
        return cls.all().get(pk=id)
