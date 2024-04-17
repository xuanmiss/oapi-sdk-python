# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .user_external import UserExternal


class CreateVisitorRequestBody(object):
    _types = {
        "user": UserExternal,
    }

    def __init__(self, d=None):
        self.user: Optional[UserExternal] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateVisitorRequestBodyBuilder":
        return CreateVisitorRequestBodyBuilder()


class CreateVisitorRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_visitor_request_body = CreateVisitorRequestBody()

    def user(self, user: UserExternal) -> "CreateVisitorRequestBodyBuilder":
        self._create_visitor_request_body.user = user
        return self

    def build(self) -> "CreateVisitorRequestBody":
        return self._create_visitor_request_body