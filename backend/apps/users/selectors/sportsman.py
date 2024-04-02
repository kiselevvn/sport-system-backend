# from django.db.models import Prefetch

from backend.apps.users.models import Sportsman

# from backend.apps.competitions.models import
# from backend.apps.examination.models import ResultExamination
# from backend.apps.testing.models import ResultTest, TestTemplate


class SportsmanSelector:
    """ """

    queryset = Sportsman.objects.all()

    @classmethod
    def all(cls):
        return cls.queryset

    # results_tests
    # results_examination
    # results_sport_competition
