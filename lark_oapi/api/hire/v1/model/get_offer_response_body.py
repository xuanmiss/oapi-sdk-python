# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .offer import Offer


class GetOfferResponseBody(object):
    _types = {
        "offer": Offer,
    }

    def __init__(self, d):
        self.offer: Optional[Offer] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetOfferResponseBodyBuilder":
        return GetOfferResponseBodyBuilder()


class GetOfferResponseBodyBuilder(object):
    def __init__(self, get_offer_response_body: GetOfferResponseBody = GetOfferResponseBody({})) -> None:
        self._get_offer_response_body: GetOfferResponseBody = get_offer_response_body

    def offer(self, offer: Offer) -> "GetOfferResponseBodyBuilder":
        self._get_offer_response_body.offer = offer
        return self

    def build(self) -> "GetOfferResponseBody":
        return self._get_offer_response_body