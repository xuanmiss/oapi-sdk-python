# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .create_app_request_body import CreateAppRequestBody


class CreateAppRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.request_body: Optional[CreateAppRequestBody] = None

    @staticmethod
    def builder() -> "CreateAppRequestBuilder":
        return CreateAppRequestBuilder()


class CreateAppRequestBuilder(object):

    def __init__(self, create_app_request: CreateAppRequest = CreateAppRequest()) -> None:
        create_app_request.http_method = HttpMethod.POST
        create_app_request.uri = "/open-apis/search/v2/app"
        create_app_request.token_types = {AccessTokenType.USER}
        self._create_app_request: CreateAppRequest = create_app_request

    def user_id_type(self, user_id_type: str) -> "CreateAppRequestBuilder":
        self._create_app_request.user_id_type = user_id_type
        self._create_app_request.queries["user_id_type"] = str(user_id_type)
        return self

    def page_size(self, page_size: int) -> "CreateAppRequestBuilder":
        self._create_app_request.page_size = page_size
        self._create_app_request.queries["page_size"] = str(page_size)
        return self

    def page_token(self, page_token: str) -> "CreateAppRequestBuilder":
        self._create_app_request.page_token = page_token
        self._create_app_request.queries["page_token"] = str(page_token)
        return self

    def request_body(self, request_body: CreateAppRequestBody) -> "CreateAppRequestBuilder":
        self._create_app_request.request_body = request_body
        self._create_app_request.body = request_body
        return self

    def build(self) -> CreateAppRequest:
        return self._create_app_request