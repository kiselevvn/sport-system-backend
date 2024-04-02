from datetime import datetime, timedelta
from random import randrange


class DateManager:

    @classmethod
    def random_date(cls, start: datetime, end: datetime) -> datetime:
        """
        Возвращает случайную дату
        в указанном периоде
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    @classmethod
    def random_date_year(cls, year: str) -> datetime:
        """
        Возвращает случайную дату
        за указанный год
        """
        d1 = datetime.strptime(f"1/1/{str(year)} 6:30", "%d/%m/%Y %H:%M")
        d2 = datetime.strptime(f"31/12/{str(year)} 6:30", "%d/%m/%Y %H:%M")
        return cls.random_date(d1, d2)
