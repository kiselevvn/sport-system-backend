from django.contrib import admin
from . import models


@admin.register(models.ExaminationTemplate)
class ExaminationTemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GroupIndicators)
class GroupIndicatorsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Examination)
class ExaminationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GroupExaminations)
class GroupExaminationsAdmin(admin.ModelAdmin):
    pass
