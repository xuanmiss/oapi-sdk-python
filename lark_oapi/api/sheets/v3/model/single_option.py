# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .data_validation_value import DataValidationValue
from .option_properties import OptionProperties


class SingleOption(object):
    _types = {
        "type": str,
        "range": str,
        "data_validation_values": List[DataValidationValue],
        "properties": OptionProperties,
    }

    def __init__(self, d):
        self.type: Optional[str] = None
        self.range: Optional[str] = None
        self.data_validation_values: Optional[List[DataValidationValue]] = None
        self.properties: Optional[OptionProperties] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SingleOptionBuilder":
        return SingleOptionBuilder()


class SingleOptionBuilder(object):
    def __init__(self, single_option: SingleOption = SingleOption({})) -> None:
        self._single_option: SingleOption = single_option

    def type(self, type: str) -> "SingleOptionBuilder":
        self._single_option.type = type
        return self

    def range(self, range: str) -> "SingleOptionBuilder":
        self._single_option.range = range
        return self

    def data_validation_values(self, data_validation_values: List[DataValidationValue]) -> "SingleOptionBuilder":
        self._single_option.data_validation_values = data_validation_values
        return self

    def properties(self, properties: OptionProperties) -> "SingleOptionBuilder":
        self._single_option.properties = properties
        return self

    def build(self) -> "SingleOption":
        return self._single_option