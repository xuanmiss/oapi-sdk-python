# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .update_tabs_chat_tab_response_body import UpdateTabsChatTabResponseBody


class UpdateTabsChatTabResponse(BaseResponse):
    _types = {
        "data": UpdateTabsChatTabResponseBody
    }

    def __init__(self, d):
        super().__init__(d)
        self.data: Optional[UpdateTabsChatTabResponseBody] = None
        init(self, d, self._types)