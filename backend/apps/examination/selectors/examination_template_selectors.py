from django.db.models import Prefetch

from backend.apps.examination.models import (
    ExaminationTemplate,
    GroupIndicators,
    Indicator,
)


class ExaminationTemplateSelectors:
    """ """

    def all():
        return ExaminationTemplate.objects.prefetch_related(
            Prefetch(
                lookup="groups_indicators",
                queryset=GroupIndicators.objects.prefetch_related(
                    Prefetch(
                        lookup="indicators", queryset=Indicator.objects.all()
                    )
                ),
            )
        )
