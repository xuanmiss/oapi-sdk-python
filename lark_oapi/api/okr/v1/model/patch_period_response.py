# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .patch_period_response_body import PatchPeriodResponseBody


class PatchPeriodResponse(BaseResponse):
    _types = {
        "data": PatchPeriodResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[PatchPeriodResponseBody] = None
        init(self, d, self._types)