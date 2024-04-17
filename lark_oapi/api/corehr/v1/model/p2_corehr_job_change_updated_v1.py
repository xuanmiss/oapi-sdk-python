# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .user_id import UserId


class P2CorehrJobChangeUpdatedV1Data(object):
    _types = {
        "employment_id": str,
        "target_user_id": UserId,
        "job_change_id": str,
        "transfer_mode": int,
        "transfer_type_unique_identifier": str,
        "transfer_reason_unique_identifier": str,
        "process_id": str,
        "effective_date": str,
        "status": int,
        "transfer_key": str,
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.target_user_id: Optional[UserId] = None
        self.job_change_id: Optional[str] = None
        self.transfer_mode: Optional[int] = None
        self.transfer_type_unique_identifier: Optional[str] = None
        self.transfer_reason_unique_identifier: Optional[str] = None
        self.process_id: Optional[str] = None
        self.effective_date: Optional[str] = None
        self.status: Optional[int] = None
        self.transfer_key: Optional[str] = None
        init(self, d, self._types)


class P2CorehrJobChangeUpdatedV1(EventContext):
    _types = {
        "event": P2CorehrJobChangeUpdatedV1Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2CorehrJobChangeUpdatedV1Data] = None
        init(self, d, self._types)
