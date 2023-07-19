# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AclScope(object):
    _types = {
        "type": str,
        "user_id": str,
    }

    def __init__(self, d):
        self.type: Optional[str] = None
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AclScopeBuilder":
        return AclScopeBuilder()


class AclScopeBuilder(object):
    def __init__(self, acl_scope: AclScope = AclScope({})) -> None:
        self._acl_scope: AclScope = acl_scope

    def type(self, type: str) -> "AclScopeBuilder":
        self._acl_scope.type = type
        return self

    def user_id(self, user_id: str) -> "AclScopeBuilder":
        self._acl_scope.user_id = user_id
        return self

    def build(self) -> "AclScope":
        return self._acl_scope