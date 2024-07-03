# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .create_aily_session_run_response_body import CreateAilySessionRunResponseBody


class CreateAilySessionRunResponse(BaseResponse):
    _types = {
        "data": CreateAilySessionRunResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[CreateAilySessionRunResponseBody] = None
        init(self, d, self._types)