# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class SignatureEnumInfoLabel(object):
    _types = {
        "zh": str,
        "en": str,
    }

    def __init__(self, d=None):
        self.zh: Optional[str] = None
        self.en: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SignatureEnumInfoLabelBuilder":
        return SignatureEnumInfoLabelBuilder()


class SignatureEnumInfoLabelBuilder(object):
    def __init__(self) -> None:
        self._signature_enum_info_label = SignatureEnumInfoLabel()

    def zh(self, zh: str) -> "SignatureEnumInfoLabelBuilder":
        self._signature_enum_info_label.zh = zh
        return self

    def en(self, en: str) -> "SignatureEnumInfoLabelBuilder":
        self._signature_enum_info_label.en = en
        return self

    def build(self) -> "SignatureEnumInfoLabel":
        return self._signature_enum_info_label