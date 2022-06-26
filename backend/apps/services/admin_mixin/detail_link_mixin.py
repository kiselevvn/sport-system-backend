from django.utils.http import urlencode
from django.urls import reverse
from django.utils.html import format_html


class DetailLinkMixin:
    def detail_link(self, obj):
        print(obj._meta)
        url = reverse(
            f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change",
            kwargs={"object_id": f"{obj.id}"},
        )
        return format_html('<a href="{}">Открыть {}</a>', url)

    detail_link.short_description = "Подробнее"
