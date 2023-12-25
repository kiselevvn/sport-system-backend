from django.db.models import Prefetch

from backend.apps.examination.models import (
    Examination,
    ResultExamination,
    ResultIndicator,
)


class ExaminationSelector:
    """ """

    @classmethod
    def all(cls):
        return Examination.objects.prefetch_related(
            Prefetch(
                lookup="results",
                queryset=ResultExamination.objects.prefetch_related(
                    Prefetch(
                        lookup="results_indicators",
                        queryset=ResultIndicator.objects.all(),
                    )
                ),
            )
        )
