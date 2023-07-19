# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class VcInfo(object):
    _types = {
        "unique_id": int,
        "meeting_no": int,
    }

    def __init__(self, d):
        self.unique_id: Optional[int] = None
        self.meeting_no: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "VcInfoBuilder":
        return VcInfoBuilder()


class VcInfoBuilder(object):
    def __init__(self, vc_info: VcInfo = VcInfo({})) -> None:
        self._vc_info: VcInfo = vc_info

    def unique_id(self, unique_id: int) -> "VcInfoBuilder":
        self._vc_info.unique_id = unique_id
        return self

    def meeting_no(self, meeting_no: int) -> "VcInfoBuilder":
        self._vc_info.meeting_no = meeting_no
        return self

    def build(self) -> "VcInfo":
        return self._vc_info