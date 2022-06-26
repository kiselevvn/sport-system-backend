from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from backend.apps.services.admin_mixin.detail_link_mixin import DetailLinkMixin

from .models import AnswerTesting, QuestionTesting, ResultTesting


@admin.register(ResultTesting)
class ResultTestingAdmin(admin.ModelAdmin, DetailLinkMixin):
    list_filter = ("test", )
    list_display = ("test", "user","result_score","date_created")
