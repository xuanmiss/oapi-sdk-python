# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .cancel_aily_session_run_response_body import CancelAilySessionRunResponseBody


class CancelAilySessionRunResponse(BaseResponse):
    _types = {
        "data": CancelAilySessionRunResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CancelAilySessionRunResponseBody] = None
        init(self, d, self._types)