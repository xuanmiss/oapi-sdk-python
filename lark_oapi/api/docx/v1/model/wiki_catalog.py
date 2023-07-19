# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class WikiCatalog(object):
    _types = {
        "wiki_token": str,
    }

    def __init__(self, d):
        self.wiki_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WikiCatalogBuilder":
        return WikiCatalogBuilder()


class WikiCatalogBuilder(object):
    def __init__(self, wiki_catalog: WikiCatalog = WikiCatalog({})) -> None:
        self._wiki_catalog: WikiCatalog = wiki_catalog

    def wiki_token(self, wiki_token: str) -> "WikiCatalogBuilder":
        self._wiki_catalog.wiki_token = wiki_token
        return self

    def build(self) -> "WikiCatalog":
        return self._wiki_catalog