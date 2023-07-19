# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_subregion_response_body import ListSubregionResponseBody


class ListSubregionResponse(BaseResponse):
    _types = {
        "data": ListSubregionResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[ListSubregionResponseBody] = None
        init(self, d, self._types)