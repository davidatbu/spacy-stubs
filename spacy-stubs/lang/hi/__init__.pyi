from ...language import Language
from typing import Any

class HindiDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    stop_words: Any = ...

class Hindi(Language):
    lang: str = ...
    Defaults: Any = ...
