# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class OpenapiLogDetail(object):
    _types = {
        "path": str,
        "method": str,
        "query_param": str,
        "payload": str,
        "status_code": int,
        "response": str,
    }

    def __init__(self, d=None):
        self.path: Optional[str] = None
        self.method: Optional[str] = None
        self.query_param: Optional[str] = None
        self.payload: Optional[str] = None
        self.status_code: Optional[int] = None
        self.response: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "OpenapiLogDetailBuilder":
        return OpenapiLogDetailBuilder()


class OpenapiLogDetailBuilder(object):
    def __init__(self) -> None:
        self._openapi_log_detail = OpenapiLogDetail()

    def path(self, path: str) -> "OpenapiLogDetailBuilder":
        self._openapi_log_detail.path = path
        return self

    def method(self, method: str) -> "OpenapiLogDetailBuilder":
        self._openapi_log_detail.method = method
        return self

    def query_param(self, query_param: str) -> "OpenapiLogDetailBuilder":
        self._openapi_log_detail.query_param = query_param
        return self

    def payload(self, payload: str) -> "OpenapiLogDetailBuilder":
        self._openapi_log_detail.payload = payload
        return self

    def status_code(self, status_code: int) -> "OpenapiLogDetailBuilder":
        self._openapi_log_detail.status_code = status_code
        return self

    def response(self, response: str) -> "OpenapiLogDetailBuilder":
        self._openapi_log_detail.response = response
        return self

    def build(self) -> "OpenapiLogDetail":
        return self._openapi_log_detail