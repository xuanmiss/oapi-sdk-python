# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .i18n import I18n


class InterviewDimensionOption(object):
    _types = {
        "id": str,
        "name": I18n,
        "description": I18n,
        "score_val": int,
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[I18n] = None
        self.description: Optional[I18n] = None
        self.score_val: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewDimensionOptionBuilder":
        return InterviewDimensionOptionBuilder()


class InterviewDimensionOptionBuilder(object):
    def __init__(self) -> None:
        self._interview_dimension_option = InterviewDimensionOption()

    def id(self, id: str) -> "InterviewDimensionOptionBuilder":
        self._interview_dimension_option.id = id
        return self

    def name(self, name: I18n) -> "InterviewDimensionOptionBuilder":
        self._interview_dimension_option.name = name
        return self

    def description(self, description: I18n) -> "InterviewDimensionOptionBuilder":
        self._interview_dimension_option.description = description
        return self

    def score_val(self, score_val: int) -> "InterviewDimensionOptionBuilder":
        self._interview_dimension_option.score_val = score_val
        return self

    def build(self) -> "InterviewDimensionOption":
        return self._interview_dimension_option
