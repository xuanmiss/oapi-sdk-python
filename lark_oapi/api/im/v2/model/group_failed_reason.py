# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class GroupFailedReason(object):
    _types = {
        "group_id": str,
        "error_code": int,
        "error_message": str,
    }

    def __init__(self, d=None):
        self.group_id: Optional[str] = None
        self.error_code: Optional[int] = None
        self.error_message: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GroupFailedReasonBuilder":
        return GroupFailedReasonBuilder()


class GroupFailedReasonBuilder(object):
    def __init__(self) -> None:
        self._group_failed_reason = GroupFailedReason()

    def group_id(self, group_id: str) -> "GroupFailedReasonBuilder":
        self._group_failed_reason.group_id = group_id
        return self

    def error_code(self, error_code: int) -> "GroupFailedReasonBuilder":
        self._group_failed_reason.error_code = error_code
        return self

    def error_message(self, error_message: str) -> "GroupFailedReasonBuilder":
        self._group_failed_reason.error_message = error_message
        return self

    def build(self) -> "GroupFailedReason":
        return self._group_failed_reason
