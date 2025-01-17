# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .id_info import IdInfo


class ConvertCommonDataIdResponseBody(object):
    _types = {
        "items": List[IdInfo],
    }

    def __init__(self, d=None):
        self.items: Optional[List[IdInfo]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ConvertCommonDataIdResponseBodyBuilder":
        return ConvertCommonDataIdResponseBodyBuilder()


class ConvertCommonDataIdResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._convert_common_data_id_response_body = ConvertCommonDataIdResponseBody()

    def items(self, items: List[IdInfo]) -> "ConvertCommonDataIdResponseBodyBuilder":
        self._convert_common_data_id_response_body.items = items
        return self

    def build(self) -> "ConvertCommonDataIdResponseBody":
        return self._convert_common_data_id_response_body
