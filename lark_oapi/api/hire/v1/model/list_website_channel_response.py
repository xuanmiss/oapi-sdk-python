# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_website_channel_response_body import ListWebsiteChannelResponseBody


class ListWebsiteChannelResponse(BaseResponse):
    _types = {
        "data": ListWebsiteChannelResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListWebsiteChannelResponseBody] = None
        init(self, d, self._types)