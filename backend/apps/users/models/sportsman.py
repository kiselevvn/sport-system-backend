from .user import User
from .managers import SportsmanBaseManager


class Sportsman(User):
    """
    Спортсмен
    """

    objects = SportsmanBaseManager()

    class Meta:
        proxy = True
