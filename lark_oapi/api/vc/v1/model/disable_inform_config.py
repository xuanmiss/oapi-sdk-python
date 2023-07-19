# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .subscribe_department import SubscribeDepartment
from .subscribe_user import SubscribeUser


class DisableInformConfig(object):
    _types = {
        "if_inform": bool,
        "informed_users": List[SubscribeUser],
        "informed_depts": List[SubscribeDepartment],
    }

    def __init__(self, d):
        self.if_inform: Optional[bool] = None
        self.informed_users: Optional[List[SubscribeUser]] = None
        self.informed_depts: Optional[List[SubscribeDepartment]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DisableInformConfigBuilder":
        return DisableInformConfigBuilder()


class DisableInformConfigBuilder(object):
    def __init__(self, disable_inform_config: DisableInformConfig = DisableInformConfig({})) -> None:
        self._disable_inform_config: DisableInformConfig = disable_inform_config

    def if_inform(self, if_inform: bool) -> "DisableInformConfigBuilder":
        self._disable_inform_config.if_inform = if_inform
        return self

    def informed_users(self, informed_users: List[SubscribeUser]) -> "DisableInformConfigBuilder":
        self._disable_inform_config.informed_users = informed_users
        return self

    def informed_depts(self, informed_depts: List[SubscribeDepartment]) -> "DisableInformConfigBuilder":
        self._disable_inform_config.informed_depts = informed_depts
        return self

    def build(self) -> "DisableInformConfig":
        return self._disable_inform_config