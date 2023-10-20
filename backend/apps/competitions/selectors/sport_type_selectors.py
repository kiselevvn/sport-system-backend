# from django.db.models import Prefetch
from backend.apps.competitions.models import SportType


class SportTypeSelectors:
    """ """

    def all():
        return SportType.objects.all()
