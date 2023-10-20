from django.contrib import admin
from import_export import resources
from import_export.admin import ImportMixin

from .models import SportType


class SportTypeResource(resources.ModelResource):
    class Meta:
        model = SportType
        use_bulk = True
        use_transactions = True
        import_id_fields = ["code_id"]
        exclude = [
            "id",
        ]


@admin.register(SportType)
class SportTypeAdmin(ImportMixin, admin.ModelAdmin):
    search_fields = ["name", "code_id"]
    list_display = ["name", "code_id"]
    resource_class = SportTypeResource
