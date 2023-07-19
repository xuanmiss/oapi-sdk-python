# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .condition import Condition


class FilterInfo(object):
    _types = {
        "col": str,
        "conditions": List[Condition],
    }

    def __init__(self, d):
        self.col: Optional[str] = None
        self.conditions: Optional[List[Condition]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FilterInfoBuilder":
        return FilterInfoBuilder()


class FilterInfoBuilder(object):
    def __init__(self, filter_info: FilterInfo = FilterInfo({})) -> None:
        self._filter_info: FilterInfo = filter_info

    def col(self, col: str) -> "FilterInfoBuilder":
        self._filter_info.col = col
        return self

    def conditions(self, conditions: List[Condition]) -> "FilterInfoBuilder":
        self._filter_info.conditions = conditions
        return self

    def build(self) -> "FilterInfo":
        return self._filter_info