# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class QueryTaskRequestBody(object):
    _types = {
        "commit_start_time": int,
        "commit_end_time": int,
        "rule_id": int,
        "user_id": str,
        "page_token": str,
        "page_size": int,
    }

    def __init__(self, d=None):
        self.commit_start_time: Optional[int] = None
        self.commit_end_time: Optional[int] = None
        self.rule_id: Optional[int] = None
        self.user_id: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QueryTaskRequestBodyBuilder":
        return QueryTaskRequestBodyBuilder()


class QueryTaskRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._query_task_request_body = QueryTaskRequestBody()

    def commit_start_time(self, commit_start_time: int) -> "QueryTaskRequestBodyBuilder":
        self._query_task_request_body.commit_start_time = commit_start_time
        return self

    def commit_end_time(self, commit_end_time: int) -> "QueryTaskRequestBodyBuilder":
        self._query_task_request_body.commit_end_time = commit_end_time
        return self

    def rule_id(self, rule_id: int) -> "QueryTaskRequestBodyBuilder":
        self._query_task_request_body.rule_id = rule_id
        return self

    def user_id(self, user_id: str) -> "QueryTaskRequestBodyBuilder":
        self._query_task_request_body.user_id = user_id
        return self

    def page_token(self, page_token: str) -> "QueryTaskRequestBodyBuilder":
        self._query_task_request_body.page_token = page_token
        return self

    def page_size(self, page_size: int) -> "QueryTaskRequestBodyBuilder":
        self._query_task_request_body.page_size = page_size
        return self

    def build(self) -> "QueryTaskRequestBody":
        return self._query_task_request_body