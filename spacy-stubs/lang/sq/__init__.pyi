from ...language import Language
from typing import Any

class AlbanianDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    stop_words: Any = ...

class Albanian(Language):
    lang: str = ...
    Defaults: Any = ...