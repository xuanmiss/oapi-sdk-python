# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Agency(object):
    _types = {
        "id": str,
        "name": str,
        "contactor_id": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.contactor_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AgencyBuilder":
        return AgencyBuilder()


class AgencyBuilder(object):
    def __init__(self, agency: Agency = Agency({})) -> None:
        self._agency: Agency = agency

    def id(self, id: str) -> "AgencyBuilder":
        self._agency.id = id
        return self

    def name(self, name: str) -> "AgencyBuilder":
        self._agency.name = name
        return self

    def contactor_id(self, contactor_id: str) -> "AgencyBuilder":
        self._agency.contactor_id = contactor_id
        return self

    def build(self) -> "Agency":
        return self._agency