# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class EmailForUpdate(object):
    _types = {
        "email": str,
        "is_primary": bool,
        "is_public": bool,
        "email_usage": str,
    }

    def __init__(self, d=None):
        self.email: Optional[str] = None
        self.is_primary: Optional[bool] = None
        self.is_public: Optional[bool] = None
        self.email_usage: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmailForUpdateBuilder":
        return EmailForUpdateBuilder()


class EmailForUpdateBuilder(object):
    def __init__(self) -> None:
        self._email_for_update = EmailForUpdate()

    def email(self, email: str) -> "EmailForUpdateBuilder":
        self._email_for_update.email = email
        return self

    def is_primary(self, is_primary: bool) -> "EmailForUpdateBuilder":
        self._email_for_update.is_primary = is_primary
        return self

    def is_public(self, is_public: bool) -> "EmailForUpdateBuilder":
        self._email_for_update.is_public = is_public
        return self

    def email_usage(self, email_usage: str) -> "EmailForUpdateBuilder":
        self._email_for_update.email_usage = email_usage
        return self

    def build(self) -> "EmailForUpdate":
        return self._email_for_update
