# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType
from .add_enum_option_common_data_meta_data_request_body import AddEnumOptionCommonDataMetaDataRequestBody


class AddEnumOptionCommonDataMetaDataRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[AddEnumOptionCommonDataMetaDataRequestBody] = None

    @staticmethod
    def builder() -> "AddEnumOptionCommonDataMetaDataRequestBuilder":
        return AddEnumOptionCommonDataMetaDataRequestBuilder()


class AddEnumOptionCommonDataMetaDataRequestBuilder(object):

    def __init__(self) -> None:
        add_enum_option_common_data_meta_data_request = AddEnumOptionCommonDataMetaDataRequest()
        add_enum_option_common_data_meta_data_request.http_method = HttpMethod.POST
        add_enum_option_common_data_meta_data_request.uri = "/open-apis/corehr/v1/common_data/meta_data/add_enum_option"
        add_enum_option_common_data_meta_data_request.token_types = {AccessTokenType.TENANT}
        self._add_enum_option_common_data_meta_data_request: AddEnumOptionCommonDataMetaDataRequest = add_enum_option_common_data_meta_data_request

    def client_token(self, client_token: str) -> "AddEnumOptionCommonDataMetaDataRequestBuilder":
        self._add_enum_option_common_data_meta_data_request.client_token = client_token
        self._add_enum_option_common_data_meta_data_request.add_query("client_token", client_token)
        return self

    def request_body(self,
                     request_body: AddEnumOptionCommonDataMetaDataRequestBody) -> "AddEnumOptionCommonDataMetaDataRequestBuilder":
        self._add_enum_option_common_data_meta_data_request.request_body = request_body
        self._add_enum_option_common_data_meta_data_request.body = request_body
        return self

    def build(self) -> AddEnumOptionCommonDataMetaDataRequest:
        return self._add_enum_option_common_data_meta_data_request