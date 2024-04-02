from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from . import models


@admin.register(models.ResultAnswer)
class ResultAnswerAdmin(admin.ModelAdmin):
    list_display = ("result_question", "date_created")


@admin.register(models.ResultQuestion)
class ResultQuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "result_answers_link")

    def result_answers_link(self, obj):
        count = obj.answers.count()
        if count == 0:
            return format_html("Открыть {}", count)
        url = (
            reverse("admin:testing_resultanswer_changelist")
            + "?"
            + urlencode({"result_question_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    result_answers_link.short_description = "Ответы"


@admin.register(models.ResultTest)
class ResultTestAdmin(admin.ModelAdmin):
    list_filter = ("test_template",)
    list_display = (
        "test_template",
        "user",
        "result_score",
        "date",
        "date_created",
        "result_question_link",
    )

    def result_question_link(self, obj):
        count = obj.questions.count()
        if count == 0:
            return format_html("Открыть {}", count)
        url = (
            reverse("admin:testing_resultquestion_changelist")
            + "?"
            + urlencode({"result_test_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    result_question_link.short_description = "Ответы"


class QuestionInline(admin.TabularInline):
    model = models.Question


@admin.register(models.TestTemplate)
class TestTemplateAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "is_open",
        "is_published",
        "questions_link",
        "result_test_link",
    )
    inlines = [
        QuestionInline,
    ]

    def questions_link(self, obj):
        count = obj.questions.count()
        if count == 0:
            return format_html("Открыть {}", count)
        url = (
            reverse("admin:testing_question_changelist")
            + "?"
            + urlencode({"test_template__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    questions_link.short_description = "Вопросы теста"

    def result_test_link(self, obj):
        count = obj.results_tests.count()
        if count == 0:
            return format_html("Открыть {}", count)
        url = (
            reverse("admin:testing_question_changelist")
            + "?"
            + urlencode({"test_template__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    result_test_link.short_description = "Результаты тестирования"


class AnswerInline(admin.StackedInline):
    model = models.Answer

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by("number")


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ("test_template",)
    list_display = (
        "text",
        "number",
        "answers_link",
    )
    inlines = [
        AnswerInline,
    ]

    def answers_link(self, obj):
        count = obj.answers.count()
        if count == 0:
            return format_html("Открыть {}", count)
        url = (
            reverse("admin:testing_answer_changelist")
            + "?"
            + urlencode({"question__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    answers_link.short_description = "Варианты ответа"


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_filter = ("question",)
    list_display = ("text", "number")
