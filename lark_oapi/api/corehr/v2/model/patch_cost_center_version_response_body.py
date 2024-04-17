# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .cost_center_version import CostCenterVersion


class PatchCostCenterVersionResponseBody(object):
    _types = {
        "version": CostCenterVersion,
    }

    def __init__(self, d=None):
        self.version: Optional[CostCenterVersion] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchCostCenterVersionResponseBodyBuilder":
        return PatchCostCenterVersionResponseBodyBuilder()


class PatchCostCenterVersionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_cost_center_version_response_body = PatchCostCenterVersionResponseBody()

    def version(self, version: CostCenterVersion) -> "PatchCostCenterVersionResponseBodyBuilder":
        self._patch_cost_center_version_response_body.version = version
        return self

    def build(self) -> "PatchCostCenterVersionResponseBody":
        return self._patch_cost_center_version_response_body