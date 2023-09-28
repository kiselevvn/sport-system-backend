from ..models import TestTemplate


class TestTemplateSelector:
    """
    Набор запросов
    Шаблон тестирования
    """

    @staticmethod
    def base_queryset():
        return TestTemplate.objects.all()
