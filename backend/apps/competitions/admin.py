from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin

from .models import SportCategory, SportDiscipline

# class SportDisciplineResource(resources.ModelResource):
#     class Meta:
#         model = SportDiscipline
#         use_bulk = True
#         use_transactions = True
#         import_id_fields = ["code_id"]
#         exclude = [
#             "id",
#         ]


@admin.register(SportCategory)
class SportCategoryAdmin(ImportMixin, admin.ModelAdmin):
    search_fields = ["name", "code_id"]
    list_display = ["name", "code_id"]


@admin.register(SportDiscipline)
class SportDisciplineAdmin(ImportMixin, admin.ModelAdmin):
    search_fields = ["name", "code_id"]
    list_display = ["name", "code_id"]
    list_filter = [
        "sport_category",
    ]
    # resource_class = SportTypeResource
