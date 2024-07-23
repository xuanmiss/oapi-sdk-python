# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryLocationRequestBody(object):
    _types = {
        "code_list": List[str],
        "location_type": int,
    }

    def __init__(self, d=None):
        self.code_list: Optional[List[str]] = None
        self.location_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryLocationRequestBodyBuilder":
        return QueryLocationRequestBodyBuilder()


class QueryLocationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_location_request_body = QueryLocationRequestBody()

    def code_list(self, code_list: List[str]) -> "QueryLocationRequestBodyBuilder":
        self._query_location_request_body.code_list = code_list
        return self

    def location_type(self, location_type: int) -> "QueryLocationRequestBodyBuilder":
        self._query_location_request_body.location_type = location_type
        return self

    def build(self) -> "QueryLocationRequestBody":
        return self._query_location_request_body