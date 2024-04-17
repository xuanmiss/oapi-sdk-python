# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init


class FeedCardSettingFailedItem(object):
    _types = {
        "feed_card_id": str,
        "error_code": int,
        "error_message": str,
    }

    def __init__(self, d=None):
        self.feed_card_id: Optional[str] = None
        self.error_code: Optional[int] = None
        self.error_message: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FeedCardSettingFailedItemBuilder":
        return FeedCardSettingFailedItemBuilder()


class FeedCardSettingFailedItemBuilder(object):
    def __init__(self) -> None:
        self._feed_card_setting_failed_item = FeedCardSettingFailedItem()

    def feed_card_id(self, feed_card_id: str) -> "FeedCardSettingFailedItemBuilder":
        self._feed_card_setting_failed_item.feed_card_id = feed_card_id
        return self

    def error_code(self, error_code: int) -> "FeedCardSettingFailedItemBuilder":
        self._feed_card_setting_failed_item.error_code = error_code
        return self

    def error_message(self, error_message: str) -> "FeedCardSettingFailedItemBuilder":
        self._feed_card_setting_failed_item.error_message = error_message
        return self

    def build(self) -> "FeedCardSettingFailedItem":
        return self._feed_card_setting_failed_item
