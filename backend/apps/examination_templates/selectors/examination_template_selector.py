from ..models import ExaminationTemplate, Indicator, GroupIndicators
from django.db.models import Prefetch


def examination_template_selector(examination_template_id: int):

    examination_template = ExaminationTemplate.objects.prefetch_related(
        Prefetch(
            "groups_indicators",
            queryset=GroupIndicators.objects.prefetch_related(
                Prefetch(
                    "indicators",
                    queryset=Indicator.objects.select_related("unit"),
                )
            ),
        )
    )

    # TODO: check does not exist
    return examination_template.get(pk=examination_template_id)
