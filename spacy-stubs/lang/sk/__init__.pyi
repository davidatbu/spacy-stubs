from ...language import Language
from typing import Any

class SlovakDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tag_map: Any = ...
    stop_words: Any = ...

class Slovak(Language):
    lang: str = ...
    Defaults: Any = ...
