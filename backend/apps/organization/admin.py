from django.contrib import admin

from . import models


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    # list_filter = ("test_template",)
    list_display = (
        "short_name",
        "address",
    )
    search_fields = (
        "full_name",
        "short_name",
        "inn",
        "kpp",
        "ogrn",
        "address",
    )


class ChildGroupInline(admin.TabularInline):
    """
    Инлайновая подгруппа
    """

    model = models.ChildGroup


@admin.register(models.EducationGroup)
class EducationGroupAdmin(admin.ModelAdmin):
    """
    Образовательная группа
    """

    inlines = (ChildGroupInline,)
    # list_filter = ("test_template",)
    # list_display = (
    #     "test_template",
    # )
