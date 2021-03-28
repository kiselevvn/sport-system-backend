# flake8: noqa
from .all import AllIndicatorsAPIView
from .create import CreateIndicatorAPIView
from .retrieve import RetrieveIndicatorAPIView
from .update import UpdateIndicatorAPIView
from .destroy import DestroyIndicatorAPIView

__all__ = [
    "AllIndicatorsAPIView",
    "CreateIndicatorAPIView",
    "RetrieveIndicatorAPIView",
    "UpdateIndicatorAPIView",
    "DestroyIndicatorAPIView",
]