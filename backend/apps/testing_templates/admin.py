from django.contrib import admin
from .models import Test, Question, Answer, ResultTesting,QuestionTesting,AnswerTesting
from django.utils.http import urlencode
from django.urls import reverse
from django.utils.html import format_html
from backend.apps.services.admin_mixin.detail_link_mixin import DetailLinkMixin

class QuestionInline(admin.TabularInline):
    model = Question


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("slug", "is_open", "is_published","questions_link","result_testing_link","date_created")
    inlines = [
        QuestionInline,
    ]

    def questions_link(self, obj):
        count = obj.questions.count()
        if count == 0:
            return format_html('Открыть {}', count)
        url = (
            reverse("admin:testing_question_changelist")
            + "?"
            + urlencode({"test__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    questions_link.short_description = "Вопросы теста"

    def result_testing_link(self, obj):
        count = obj.result_testings.count()
        if count == 0:
            return format_html('Открыть {}', count)
        url = (
            reverse("admin:testing_question_changelist")
            + "?"
            + urlencode({"test__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    result_testing_link.short_description = "Результаты тестирования"

class AnswerInline(admin.StackedInline):
    model = Answer
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by("number")

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ("test", )
    list_display = ("text", "number", "answers_link","date_created")
    inlines = [
        AnswerInline,
    ]

    def answers_link(self, obj):
        count = obj.answers.count()
        if count == 0:
            return format_html('Открыть {}', count)
        url = (
            reverse("admin:testing_answer_changelist")
            + "?"
            + urlencode({"question__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">Открыть {}</a>', url, count)

    answers_link.short_description = "Варианты ответа"

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_filter = ("question", )
    list_display = ("text", "number")


@admin.register(ResultTesting)
class ResultTestingAdmin(admin.ModelAdmin,DetailLinkMixin):
    list_filter = ("test", )
    list_display = ("test", "user","result_score","date_created")
