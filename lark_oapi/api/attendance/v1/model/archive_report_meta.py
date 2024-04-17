# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class ArchiveReportMeta(object):
    _types = {
        "report_id": str,
        "report_name": str,
        "archive_rule_id": str,
        "archive_rule_name": str,
    }

    def __init__(self, d=None):
        self.report_id: Optional[str] = None
        self.report_name: Optional[str] = None
        self.archive_rule_id: Optional[str] = None
        self.archive_rule_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ArchiveReportMetaBuilder":
        return ArchiveReportMetaBuilder()


class ArchiveReportMetaBuilder(object):
    def __init__(self) -> None:
        self._archive_report_meta = ArchiveReportMeta()

    def report_id(self, report_id: str) -> "ArchiveReportMetaBuilder":
        self._archive_report_meta.report_id = report_id
        return self

    def report_name(self, report_name: str) -> "ArchiveReportMetaBuilder":
        self._archive_report_meta.report_name = report_name
        return self

    def archive_rule_id(self, archive_rule_id: str) -> "ArchiveReportMetaBuilder":
        self._archive_report_meta.archive_rule_id = archive_rule_id
        return self

    def archive_rule_name(self, archive_rule_name: str) -> "ArchiveReportMetaBuilder":
        self._archive_report_meta.archive_rule_name = archive_rule_name
        return self

    def build(self) -> "ArchiveReportMeta":
        return self._archive_report_meta
