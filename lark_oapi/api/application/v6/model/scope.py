# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Scope(object):
    _types = {
        "scope_name": str,
        "grant_status": int,
    }

    def __init__(self, d):
        self.scope_name: Optional[str] = None
        self.grant_status: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScopeBuilder":
        return ScopeBuilder()


class ScopeBuilder(object):
    def __init__(self, scope: Scope = Scope({})) -> None:
        self._scope: Scope = scope

    def scope_name(self, scope_name: str) -> "ScopeBuilder":
        self._scope.scope_name = scope_name
        return self

    def grant_status(self, grant_status: int) -> "ScopeBuilder":
        self._scope.grant_status = grant_status
        return self

    def build(self) -> "Scope":
        return self._scope