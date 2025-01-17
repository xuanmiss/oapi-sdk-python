# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class BuiltinAction(object):
    _types = {
        "builtin_action_type": str,
        "enable": bool,
        "action_status": str,
        "extra": str,
    }

    def __init__(self, d=None):
        self.builtin_action_type: Optional[str] = None
        self.enable: Optional[bool] = None
        self.action_status: Optional[str] = None
        self.extra: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BuiltinActionBuilder":
        return BuiltinActionBuilder()


class BuiltinActionBuilder(object):
    def __init__(self) -> None:
        self._builtin_action = BuiltinAction()

    def builtin_action_type(self, builtin_action_type: str) -> "BuiltinActionBuilder":
        self._builtin_action.builtin_action_type = builtin_action_type
        return self

    def enable(self, enable: bool) -> "BuiltinActionBuilder":
        self._builtin_action.enable = enable
        return self

    def action_status(self, action_status: str) -> "BuiltinActionBuilder":
        self._builtin_action.action_status = action_status
        return self

    def extra(self, extra: str) -> "BuiltinActionBuilder":
        self._builtin_action.extra = extra
        return self

    def build(self) -> "BuiltinAction":
        return self._builtin_action
