# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .failed_reason import FailedReason


class UpdateChatButtonResponseBody(object):
    _types = {
        "failed_user_reasons": List[FailedReason],
    }

    def __init__(self, d=None):
        self.failed_user_reasons: Optional[List[FailedReason]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateChatButtonResponseBodyBuilder":
        return UpdateChatButtonResponseBodyBuilder()


class UpdateChatButtonResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_chat_button_response_body = UpdateChatButtonResponseBody()

    def failed_user_reasons(self, failed_user_reasons: List[FailedReason]) -> "UpdateChatButtonResponseBodyBuilder":
        self._update_chat_button_response_body.failed_user_reasons = failed_user_reasons
        return self

    def build(self) -> "UpdateChatButtonResponseBody":
        return self._update_chat_button_response_body
