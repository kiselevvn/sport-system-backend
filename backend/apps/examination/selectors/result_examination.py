from django.db.models import Count, Prefetch

from backend.apps.examination.models import ResultExamination, ResultIndicator


# Prefetch(
#     lookup="results", queryset=ResultExamination.objects.all()
# )
class ResultExaminationelector:
    """ """

    def all():
        return (
            ResultExamination.objects.select_related(
                "template", "examination", "examination", "sportsman"
            )
            .annotate(count_indicators=Count("results_indicators"))
            .prefetch_related(
                Prefetch(
                    "results_indicators",
                    queryset=ResultIndicator.objects.select_related(),
                )
            )
        )
