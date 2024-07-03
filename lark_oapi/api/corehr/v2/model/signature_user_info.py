# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SignatureUserInfo(object):
    _types = {
        "id": str,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SignatureUserInfoBuilder":
        return SignatureUserInfoBuilder()


class SignatureUserInfoBuilder(object):
    def __init__(self) -> None:
        self._signature_user_info = SignatureUserInfo()

    def id(self, id: str) -> "SignatureUserInfoBuilder":
        self._signature_user_info.id = id
        return self

    def build(self) -> "SignatureUserInfo":
        return self._signature_user_info