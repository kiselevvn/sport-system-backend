from django.db.models import Prefetch

from backend.apps.examination.models import (  # Event, GroupExaminations,
    Examination,
    ResultExaminations,
)


class ExaminationSelectors:
    """ """

    def all():
        return Examination.objects.select_related(
            "template", "event"
        ).prefetch_related(
            Prefetch(
                lookup="results", queryset=ResultExaminations.objects.all()
            )
        )
