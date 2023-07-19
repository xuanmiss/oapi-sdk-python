# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class Comments(object):
    _types = {
        "content": str,
        "created_at": int,
        "id": int,
        "user_avatar_url": str,
        "user_name": str,
        "user_id": int,
    }

    def __init__(self, d):
        self.content: Optional[str] = None
        self.created_at: Optional[int] = None
        self.id: Optional[int] = None
        self.user_avatar_url: Optional[str] = None
        self.user_name: Optional[str] = None
        self.user_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CommentsBuilder":
        return CommentsBuilder()


class CommentsBuilder(object):
    def __init__(self, comments: Comments = Comments({})) -> None:
        self._comments: Comments = comments

    def content(self, content: str) -> "CommentsBuilder":
        self._comments.content = content
        return self

    def created_at(self, created_at: int) -> "CommentsBuilder":
        self._comments.created_at = created_at
        return self

    def id(self, id: int) -> "CommentsBuilder":
        self._comments.id = id
        return self

    def user_avatar_url(self, user_avatar_url: str) -> "CommentsBuilder":
        self._comments.user_avatar_url = user_avatar_url
        return self

    def user_name(self, user_name: str) -> "CommentsBuilder":
        self._comments.user_name = user_name
        return self

    def user_id(self, user_id: int) -> "CommentsBuilder":
        self._comments.user_id = user_id
        return self

    def build(self) -> "Comments":
        return self._comments