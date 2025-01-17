# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext


class P2CorehrDepartmentDeletedV1Data(object):
    _types = {
        "department_id": str,
        "code": str,
    }

    def __init__(self, d=None):
        self.department_id: Optional[str] = None
        self.code: Optional[str] = None
        init(self, d, self._types)


class P2CorehrDepartmentDeletedV1(EventContext):
    _types = {
        "event": P2CorehrDepartmentDeletedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrDepartmentDeletedV1Data] = None
        init(self, d, self._types)
