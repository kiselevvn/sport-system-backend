import random

from .helpers.fake_data import (
    FEMALES_FIRST_NAMES,
    FEMALES_LAST_NAMES,
    FEMALES_SECOND_NAMES,
    MALES_FIRST_NAMES,
    MALES_LAST_NAMES,
    MALES_SECOND_NAMES,
)


def get_fake_full_male_name() -> dict:
    """
    Возвращает случайное ФИО
    """

    full_name = {
        "last_name": random.choice(MALES_LAST_NAMES),
        "first_name": random.choice(MALES_FIRST_NAMES),
        "second_name": random.choice(MALES_SECOND_NAMES),
        "gender": 0,
    }
    return full_name


def get_fake_full_female_name() -> dict:
    """
    Возвращает случайное ФИО
    """

    full_name = {
        "last_name": random.choice(FEMALES_LAST_NAMES),
        "first_name": random.choice(FEMALES_FIRST_NAMES),
        "second_name": random.choice(FEMALES_SECOND_NAMES),
        "gender": 1,
    }
    return full_name
