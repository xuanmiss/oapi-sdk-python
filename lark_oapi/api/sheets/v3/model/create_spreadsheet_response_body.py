# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .spreadsheet import Spreadsheet


class CreateSpreadsheetResponseBody(object):
    _types = {
        "spreadsheet": Spreadsheet,
    }

    def __init__(self, d):
        self.spreadsheet: Optional[Spreadsheet] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateSpreadsheetResponseBodyBuilder":
        return CreateSpreadsheetResponseBodyBuilder()


class CreateSpreadsheetResponseBodyBuilder(object):
    def __init__(self, create_spreadsheet_response_body: CreateSpreadsheetResponseBody = CreateSpreadsheetResponseBody(
        {})) -> None:
        self._create_spreadsheet_response_body: CreateSpreadsheetResponseBody = create_spreadsheet_response_body

    def spreadsheet(self, spreadsheet: Spreadsheet) -> "CreateSpreadsheetResponseBodyBuilder":
        self._create_spreadsheet_response_body.spreadsheet = spreadsheet
        return self

    def build(self) -> "CreateSpreadsheetResponseBody":
        return self._create_spreadsheet_response_body