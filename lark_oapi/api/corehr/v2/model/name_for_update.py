# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class NameForUpdate(object):
    _types = {
        "full_name": str,
        "first_name": str,
        "middle_name": str,
        "name_primary": str,
        "local_first_name": str,
        "local_middle_name": str,
        "local_primary": str,
        "custom_local_name": str,
        "custom_western_name": str,
        "country_region": str,
        "name_type": str,
    }

    def __init__(self, d=None):
        self.full_name: Optional[str] = None
        self.first_name: Optional[str] = None
        self.middle_name: Optional[str] = None
        self.name_primary: Optional[str] = None
        self.local_first_name: Optional[str] = None
        self.local_middle_name: Optional[str] = None
        self.local_primary: Optional[str] = None
        self.custom_local_name: Optional[str] = None
        self.custom_western_name: Optional[str] = None
        self.country_region: Optional[str] = None
        self.name_type: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "NameForUpdateBuilder":
        return NameForUpdateBuilder()


class NameForUpdateBuilder(object):
    def __init__(self) -> None:
        self._name_for_update = NameForUpdate()

    def full_name(self, full_name: str) -> "NameForUpdateBuilder":
        self._name_for_update.full_name = full_name
        return self

    def first_name(self, first_name: str) -> "NameForUpdateBuilder":
        self._name_for_update.first_name = first_name
        return self

    def middle_name(self, middle_name: str) -> "NameForUpdateBuilder":
        self._name_for_update.middle_name = middle_name
        return self

    def name_primary(self, name_primary: str) -> "NameForUpdateBuilder":
        self._name_for_update.name_primary = name_primary
        return self

    def local_first_name(self, local_first_name: str) -> "NameForUpdateBuilder":
        self._name_for_update.local_first_name = local_first_name
        return self

    def local_middle_name(self, local_middle_name: str) -> "NameForUpdateBuilder":
        self._name_for_update.local_middle_name = local_middle_name
        return self

    def local_primary(self, local_primary: str) -> "NameForUpdateBuilder":
        self._name_for_update.local_primary = local_primary
        return self

    def custom_local_name(self, custom_local_name: str) -> "NameForUpdateBuilder":
        self._name_for_update.custom_local_name = custom_local_name
        return self

    def custom_western_name(self, custom_western_name: str) -> "NameForUpdateBuilder":
        self._name_for_update.custom_western_name = custom_western_name
        return self

    def country_region(self, country_region: str) -> "NameForUpdateBuilder":
        self._name_for_update.country_region = country_region
        return self

    def name_type(self, name_type: str) -> "NameForUpdateBuilder":
        self._name_for_update.name_type = name_type
        return self

    def build(self) -> "NameForUpdate":
        return self._name_for_update
