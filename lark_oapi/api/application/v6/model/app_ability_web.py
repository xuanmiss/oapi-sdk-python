# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AppAbilityWeb(object):
    _types = {
        "enable": bool,
        "pc_url": str,
        "pc_new_page_open_mode": str,
        "mobile_url": str,
    }

    def __init__(self, d=None):
        self.enable: Optional[bool] = None
        self.pc_url: Optional[str] = None
        self.pc_new_page_open_mode: Optional[str] = None
        self.mobile_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppAbilityWebBuilder":
        return AppAbilityWebBuilder()


class AppAbilityWebBuilder(object):
    def __init__(self) -> None:
        self._app_ability_web = AppAbilityWeb()

    def enable(self, enable: bool) -> "AppAbilityWebBuilder":
        self._app_ability_web.enable = enable
        return self

    def pc_url(self, pc_url: str) -> "AppAbilityWebBuilder":
        self._app_ability_web.pc_url = pc_url
        return self

    def pc_new_page_open_mode(self, pc_new_page_open_mode: str) -> "AppAbilityWebBuilder":
        self._app_ability_web.pc_new_page_open_mode = pc_new_page_open_mode
        return self

    def mobile_url(self, mobile_url: str) -> "AppAbilityWebBuilder":
        self._app_ability_web.mobile_url = mobile_url
        return self

    def build(self) -> "AppAbilityWeb":
        return self._app_ability_web