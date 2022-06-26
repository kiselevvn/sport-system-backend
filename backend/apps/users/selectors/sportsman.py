from backend.apps.users.models import Sportsman


def get_sportsmans():
    return Sportsman.objects.all()
