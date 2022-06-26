from .enums.indicator_type import (
    INDIACTOR_SCHEMES,
)


def get_indicator_scheme(type_indicator: int):
    scheme = {}
    if type_indicator in INDIACTOR_SCHEMES:
        scheme = INDIACTOR_SCHEMES[type_indicator]["schema"].schema()
        # print(scheme)
    else:
        raise Exception("Unable to find schema!")
    return scheme
