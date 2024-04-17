# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class Text(object):
    _types = {
        "text": str,
        "font_weight": str,
        "font_size": int,
        "horizontal_align": str,
        "vertical_align": str,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        self.font_weight: Optional[str] = None
        self.font_size: Optional[int] = None
        self.horizontal_align: Optional[str] = None
        self.vertical_align: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TextBuilder":
        return TextBuilder()


class TextBuilder(object):
    def __init__(self) -> None:
        self._text = Text()

    def text(self, text: str) -> "TextBuilder":
        self._text.text = text
        return self

    def font_weight(self, font_weight: str) -> "TextBuilder":
        self._text.font_weight = font_weight
        return self

    def font_size(self, font_size: int) -> "TextBuilder":
        self._text.font_size = font_size
        return self

    def horizontal_align(self, horizontal_align: str) -> "TextBuilder":
        self._text.horizontal_align = horizontal_align
        return self

    def vertical_align(self, vertical_align: str) -> "TextBuilder":
        self._text.vertical_align = vertical_align
        return self

    def build(self) -> "Text":
        return self._text