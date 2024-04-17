# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.model import BaseRequest
from lark_oapi.core.enum import HttpMethod, AccessTokenType


class GetVerificationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "GetVerificationRequestBuilder":
        return GetVerificationRequestBuilder()


class GetVerificationRequestBuilder(object):

    def __init__(self) -> None:
        get_verification_request = GetVerificationRequest()
        get_verification_request.http_method = HttpMethod.GET
        get_verification_request.uri = "/open-apis/verification/v1/verification"
        get_verification_request.token_types = {AccessTokenType.TENANT}
        self._get_verification_request: GetVerificationRequest = get_verification_request

    def build(self) -> GetVerificationRequest:
        return self._get_verification_request