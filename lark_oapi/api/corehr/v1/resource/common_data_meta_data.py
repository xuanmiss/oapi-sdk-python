# Code generated by Lark OpenAPI.

import io
from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.const import UTF_8, CONTENT_TYPE, APPLICATION_JSON
from lark_oapi.core import JSON
from lark_oapi.core.token import verify
from lark_oapi.core.http import Transport
from lark_oapi.core.model import Config, RequestOption, RawResponse
from lark_oapi.core.utils import Files
from requests_toolbelt import MultipartEncoder
from ..model.add_enum_option_common_data_meta_data_request import AddEnumOptionCommonDataMetaDataRequest
from ..model.add_enum_option_common_data_meta_data_response import AddEnumOptionCommonDataMetaDataResponse
from ..model.edit_enum_option_common_data_meta_data_request import EditEnumOptionCommonDataMetaDataRequest
from ..model.edit_enum_option_common_data_meta_data_response import EditEnumOptionCommonDataMetaDataResponse


class CommonDataMetaData(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def add_enum_option(self, request: AddEnumOptionCommonDataMetaDataRequest,
                        option: Optional[RequestOption] = None) -> AddEnumOptionCommonDataMetaDataResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: AddEnumOptionCommonDataMetaDataResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           AddEnumOptionCommonDataMetaDataResponse)
        response.raw = resp

        return response

    async def aadd_enum_option(self, request: AddEnumOptionCommonDataMetaDataRequest,
                               option: Optional[RequestOption] = None) -> AddEnumOptionCommonDataMetaDataResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: AddEnumOptionCommonDataMetaDataResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                           AddEnumOptionCommonDataMetaDataResponse)
        response.raw = resp

        return response

    def edit_enum_option(self, request: EditEnumOptionCommonDataMetaDataRequest,
                         option: Optional[RequestOption] = None) -> EditEnumOptionCommonDataMetaDataResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 添加 content-type
        if request.body is not None:
            option.headers[CONTENT_TYPE] = f"{APPLICATION_JSON}; charset=utf-8"

        # 发起请求
        resp: RawResponse = Transport.execute(self.config, request, option)

        # 反序列化
        response: EditEnumOptionCommonDataMetaDataResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            EditEnumOptionCommonDataMetaDataResponse)
        response.raw = resp

        return response

    async def aedit_enum_option(self, request: EditEnumOptionCommonDataMetaDataRequest,
                                option: Optional[RequestOption] = None) -> EditEnumOptionCommonDataMetaDataResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: EditEnumOptionCommonDataMetaDataResponse = JSON.unmarshal(str(resp.content, UTF_8),
                                                                            EditEnumOptionCommonDataMetaDataResponse)
        response.raw = resp

        return response
