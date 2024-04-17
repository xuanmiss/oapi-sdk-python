# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .cost_center_version import CostCenterVersion


class SearchCostCenterResponseBody(object):
    _types = {
        "items": List[CostCenterVersion],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[CostCenterVersion]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchCostCenterResponseBodyBuilder":
        return SearchCostCenterResponseBodyBuilder()


class SearchCostCenterResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_cost_center_response_body = SearchCostCenterResponseBody()

    def items(self, items: List[CostCenterVersion]) -> "SearchCostCenterResponseBodyBuilder":
        self._search_cost_center_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "SearchCostCenterResponseBodyBuilder":
        self._search_cost_center_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "SearchCostCenterResponseBodyBuilder":
        self._search_cost_center_response_body.has_more = has_more
        return self

    def build(self) -> "SearchCostCenterResponseBody":
        return self._search_cost_center_response_body