# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class AilyKnowledgeDatatable(object):
    _types = {
        "api_name": str,
        "title": str,
    }

    def __init__(self, d=None):
        self.api_name: Optional[str] = None
        self.title: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AilyKnowledgeDatatableBuilder":
        return AilyKnowledgeDatatableBuilder()


class AilyKnowledgeDatatableBuilder(object):
    def __init__(self) -> None:
        self._aily_knowledge_datatable = AilyKnowledgeDatatable()

    def api_name(self, api_name: str) -> "AilyKnowledgeDatatableBuilder":
        self._aily_knowledge_datatable.api_name = api_name
        return self

    def title(self, title: str) -> "AilyKnowledgeDatatableBuilder":
        self._aily_knowledge_datatable.title = title
        return self

    def build(self) -> "AilyKnowledgeDatatable":
        return self._aily_knowledge_datatable