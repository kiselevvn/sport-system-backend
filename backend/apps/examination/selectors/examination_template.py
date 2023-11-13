from django.db.models import Prefetch

from backend.apps.examination.models import (
    ExaminationTemplate,
    GroupIndicators,
    Indicator,
)


class ExaminationTemplateSelector:
    """ """

    def all():
        return ExaminationTemplate.objects.prefetch_related(
            Prefetch(
                lookup="groups_indicators",
                queryset=GroupIndicators.objects.prefetch_related(
                    Prefetch(
                        lookup="indicators",
                        queryset=Indicator.objects.select_related("unit"),
                    )
                ),
            )
        )
