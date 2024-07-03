# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .convert_common_data_id_request_body import ConvertCommonDataIdRequestBody


class ConvertCommonDataIdRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.id_transform_type: Optional[int] = None
        self.id_type: Optional[str] = None
        self.feishu_user_id_type: Optional[str] = None
        self.feishu_department_id_type: Optional[str] = None
        self.request_body: Optional[ConvertCommonDataIdRequestBody] = None

    @staticmethod
    def builder() -> "ConvertCommonDataIdRequestBuilder":
        return ConvertCommonDataIdRequestBuilder()


class ConvertCommonDataIdRequestBuilder(object):

    def __init__(self) -> None:
        convert_common_data_id_request = ConvertCommonDataIdRequest()
        convert_common_data_id_request.http_method = HttpMethod.POST
        convert_common_data_id_request.uri = "/open-apis/corehr/v1/common_data/id/convert"
        convert_common_data_id_request.token_types = {AccessTokenType.TENANT}
        self._convert_common_data_id_request: ConvertCommonDataIdRequest = convert_common_data_id_request

    def id_transform_type(self, id_transform_type: int) -> "ConvertCommonDataIdRequestBuilder":
        self._convert_common_data_id_request.id_transform_type = id_transform_type
        self._convert_common_data_id_request.add_query("id_transform_type", id_transform_type)
        return self

    def id_type(self, id_type: str) -> "ConvertCommonDataIdRequestBuilder":
        self._convert_common_data_id_request.id_type = id_type
        self._convert_common_data_id_request.add_query("id_type", id_type)
        return self

    def feishu_user_id_type(self, feishu_user_id_type: str) -> "ConvertCommonDataIdRequestBuilder":
        self._convert_common_data_id_request.feishu_user_id_type = feishu_user_id_type
        self._convert_common_data_id_request.add_query("feishu_user_id_type", feishu_user_id_type)
        return self

    def feishu_department_id_type(self, feishu_department_id_type: str) -> "ConvertCommonDataIdRequestBuilder":
        self._convert_common_data_id_request.feishu_department_id_type = feishu_department_id_type
        self._convert_common_data_id_request.add_query("feishu_department_id_type", feishu_department_id_type)
        return self

    def request_body(self, request_body: ConvertCommonDataIdRequestBody) -> "ConvertCommonDataIdRequestBuilder":
        self._convert_common_data_id_request.request_body = request_body
        self._convert_common_data_id_request.body = request_body
        return self

    def build(self) -> ConvertCommonDataIdRequest:
        return self._convert_common_data_id_request