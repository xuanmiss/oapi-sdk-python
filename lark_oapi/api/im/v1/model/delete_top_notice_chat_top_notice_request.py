# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteTopNoticeChatTopNoticeRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.chat_id: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteTopNoticeChatTopNoticeRequestBuilder":
        return DeleteTopNoticeChatTopNoticeRequestBuilder()


class DeleteTopNoticeChatTopNoticeRequestBuilder(object):

    def __init__(self,
                 delete_top_notice_chat_top_notice_request: DeleteTopNoticeChatTopNoticeRequest = DeleteTopNoticeChatTopNoticeRequest()) -> None:
        delete_top_notice_chat_top_notice_request.http_method = HttpMethod.POST
        delete_top_notice_chat_top_notice_request.uri = "/open-apis/im/v1/chats/:chat_id/top_notice/delete_top_notice"
        delete_top_notice_chat_top_notice_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_top_notice_chat_top_notice_request: DeleteTopNoticeChatTopNoticeRequest = delete_top_notice_chat_top_notice_request

    def chat_id(self, chat_id: str) -> "DeleteTopNoticeChatTopNoticeRequestBuilder":
        self._delete_top_notice_chat_top_notice_request.chat_id = chat_id
        self._delete_top_notice_chat_top_notice_request.paths["chat_id"] = chat_id
        return self

    def build(self) -> DeleteTopNoticeChatTopNoticeRequest:
        return self._delete_top_notice_chat_top_notice_request