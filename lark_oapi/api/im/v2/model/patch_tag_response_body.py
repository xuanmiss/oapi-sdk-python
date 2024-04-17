# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .tag_info import TagInfo
from .patch_tag_fail_reason import PatchTagFailReason


class PatchTagResponseBody(object):
    _types = {
        "tag_info": TagInfo,
        "patch_tag_fail_reason": PatchTagFailReason,
    }

    def __init__(self, d=None):
        self.tag_info: Optional[TagInfo] = None
        self.patch_tag_fail_reason: Optional[PatchTagFailReason] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchTagResponseBodyBuilder":
        return PatchTagResponseBodyBuilder()


class PatchTagResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_tag_response_body = PatchTagResponseBody()

    def tag_info(self, tag_info: TagInfo) -> "PatchTagResponseBodyBuilder":
        self._patch_tag_response_body.tag_info = tag_info
        return self

    def patch_tag_fail_reason(self, patch_tag_fail_reason: PatchTagFailReason) -> "PatchTagResponseBodyBuilder":
        self._patch_tag_response_body.patch_tag_fail_reason = patch_tag_fail_reason
        return self

    def build(self) -> "PatchTagResponseBody":
        return self._patch_tag_response_body
