from ...language import Language
from typing import Any

class CroatianDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    stop_words: Any = ...

class Croatian(Language):
    lang: str = ...
    Defaults: Any = ...
