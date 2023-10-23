# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class GwResponse(object):
    _types = {
        "status_code": int,
        "header": str,
    }

    def __init__(self, d=None):
        self.status_code: Optional[int] = None
        self.header: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GwResponseBuilder":
        return GwResponseBuilder()


class GwResponseBuilder(object):
    def __init__(self) -> None:
        self._gw_response = GwResponse()

    def status_code(self, status_code: int) -> "GwResponseBuilder":
        self._gw_response.status_code = status_code
        return self

    def header(self, header: str) -> "GwResponseBuilder":
        self._gw_response.header = header
        return self

    def build(self) -> "GwResponse":
        return self._gw_response