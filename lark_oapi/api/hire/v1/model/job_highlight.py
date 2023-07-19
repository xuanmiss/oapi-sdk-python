# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class JobHighlight(object):
    _types = {
        "id": str,
        "zh_name": str,
        "en_name": str,
    }

    def __init__(self, d):
        self.id: Optional[str] = None
        self.zh_name: Optional[str] = None
        self.en_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobHighlightBuilder":
        return JobHighlightBuilder()


class JobHighlightBuilder(object):
    def __init__(self, job_highlight: JobHighlight = JobHighlight({})) -> None:
        self._job_highlight: JobHighlight = job_highlight

    def id(self, id: str) -> "JobHighlightBuilder":
        self._job_highlight.id = id
        return self

    def zh_name(self, zh_name: str) -> "JobHighlightBuilder":
        self._job_highlight.zh_name = zh_name
        return self

    def en_name(self, en_name: str) -> "JobHighlightBuilder":
        self._job_highlight.en_name = en_name
        return self

    def build(self) -> "JobHighlight":
        return self._job_highlight