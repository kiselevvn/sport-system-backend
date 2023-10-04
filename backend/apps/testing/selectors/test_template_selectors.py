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

    @staticmethod
    def base_queryset():
        return TestTemplate.objects.all()

    @staticmethod
    def all():
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
