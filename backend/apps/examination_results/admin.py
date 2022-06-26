from django.contrib import admin
from .models import Examination, GroupExaminations, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupExaminations)
class GroupExaminationsAdmin(admin.ModelAdmin):
    pass
