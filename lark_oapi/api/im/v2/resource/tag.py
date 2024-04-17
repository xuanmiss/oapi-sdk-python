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
from ..model.create_tag_request import CreateTagRequest
from ..model.create_tag_response import CreateTagResponse
from ..model.patch_tag_request import PatchTagRequest
from ..model.patch_tag_response import PatchTagResponse


class Tag(object):
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def create(self, request: CreateTagRequest, option: Optional[RequestOption] = None) -> CreateTagResponse:
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
        response: CreateTagResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateTagResponse)
        response.raw = resp

        return response

    async def acreate(self, request: CreateTagRequest, option: Optional[RequestOption] = None) -> CreateTagResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: CreateTagResponse = JSON.unmarshal(str(resp.content, UTF_8), CreateTagResponse)
        response.raw = resp

        return response

    def patch(self, request: PatchTagRequest, option: Optional[RequestOption] = None) -> PatchTagResponse:
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
        response: PatchTagResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchTagResponse)
        response.raw = resp

        return response

    async def apatch(self, request: PatchTagRequest, option: Optional[RequestOption] = None) -> PatchTagResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取 token
        verify(self.config, request, option)

        # 发起请求
        resp: RawResponse = await Transport.aexecute(self.config, request, option)

        # 反序列化
        response: PatchTagResponse = JSON.unmarshal(str(resp.content, UTF_8), PatchTagResponse)
        response.raw = resp

        return response