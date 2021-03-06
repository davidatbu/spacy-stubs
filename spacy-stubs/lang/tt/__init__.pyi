from ...language import Language
from typing import Any

class TatarDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    infixes: Any = ...
    stop_words: Any = ...

class Tatar(Language):
    lang: str = ...
    Defaults: Any = ...
