from django.db.models import Prefetch

from backend.apps.examination.models import Examination, ResultExamination


class ExaminationSelector:
    """ """

    def all():
        return Examination.objects.select_related(
            "template", "event"
        ).prefetch_related(
            Prefetch(
                lookup="results", queryset=ResultExamination.objects.all()
            )
        )
