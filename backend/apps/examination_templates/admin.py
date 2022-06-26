from django.contrib import admin
from .models import ExaminationTemplate, Unit, Indicator, GroupIndicators


@admin.register(ExaminationTemplate)
class ExaminationTemplateAdmin(admin.ModelAdmin):
    pass

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    pass

@admin.register(GroupIndicators)
class GroupIndicatorsAdmin(admin.ModelAdmin):
    pass