# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .id_name_object import IdNameObject
from .id_name_object import IdNameObject
from .data_permission import DataPermission
from .business_management_scope import BusinessManagementScope


class PermissionCollection(object):
    _types = {
        "feature_permissions": List[IdNameObject],
        "management_permissions": List[IdNameObject],
        "data_permissions": List[DataPermission],
        "business_management_scopes": List[BusinessManagementScope],
    }

    def __init__(self, d=None):
        self.feature_permissions: Optional[List[IdNameObject]] = None
        self.management_permissions: Optional[List[IdNameObject]] = None
        self.data_permissions: Optional[List[DataPermission]] = None
        self.business_management_scopes: Optional[List[BusinessManagementScope]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PermissionCollectionBuilder":
        return PermissionCollectionBuilder()


class PermissionCollectionBuilder(object):
    def __init__(self) -> None:
        self._permission_collection = PermissionCollection()

    def feature_permissions(self, feature_permissions: List[IdNameObject]) -> "PermissionCollectionBuilder":
        self._permission_collection.feature_permissions = feature_permissions
        return self

    def management_permissions(self, management_permissions: List[IdNameObject]) -> "PermissionCollectionBuilder":
        self._permission_collection.management_permissions = management_permissions
        return self

    def data_permissions(self, data_permissions: List[DataPermission]) -> "PermissionCollectionBuilder":
        self._permission_collection.data_permissions = data_permissions
        return self

    def business_management_scopes(self, business_management_scopes: List[
        BusinessManagementScope]) -> "PermissionCollectionBuilder":
        self._permission_collection.business_management_scopes = business_management_scopes
        return self

    def build(self) -> "PermissionCollection":
        return self._permission_collection