# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .i18n import I18n
from .i18n import I18n
from .org_role_update import OrgRoleUpdate


class CustomOrgUpdate(object):
    _types = {
        "object_api_name": str,
        "names": List[I18n],
        "code": str,
        "parent_id": str,
        "manager_ids": List[str],
        "description": List[I18n],
        "effective_time": str,
        "org_roles": List[OrgRoleUpdate],
    }

    def __init__(self, d=None):
        self.object_api_name: Optional[str] = None
        self.names: Optional[List[I18n]] = None
        self.code: Optional[str] = None
        self.parent_id: Optional[str] = None
        self.manager_ids: Optional[List[str]] = None
        self.description: Optional[List[I18n]] = None
        self.effective_time: Optional[str] = None
        self.org_roles: Optional[List[OrgRoleUpdate]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomOrgUpdateBuilder":
        return CustomOrgUpdateBuilder()


class CustomOrgUpdateBuilder(object):
    def __init__(self) -> None:
        self._custom_org_update = CustomOrgUpdate()

    def object_api_name(self, object_api_name: str) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.object_api_name = object_api_name
        return self

    def names(self, names: List[I18n]) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.names = names
        return self

    def code(self, code: str) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.code = code
        return self

    def parent_id(self, parent_id: str) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.parent_id = parent_id
        return self

    def manager_ids(self, manager_ids: List[str]) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.manager_ids = manager_ids
        return self

    def description(self, description: List[I18n]) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.description = description
        return self

    def effective_time(self, effective_time: str) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.effective_time = effective_time
        return self

    def org_roles(self, org_roles: List[OrgRoleUpdate]) -> "CustomOrgUpdateBuilder":
        self._custom_org_update.org_roles = org_roles
        return self

    def build(self) -> "CustomOrgUpdate":
        return self._custom_org_update
