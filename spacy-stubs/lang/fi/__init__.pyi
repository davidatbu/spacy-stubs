from ...language import Language
from typing import Any

class FinnishDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    infixes: Any = ...
    suffixes: Any = ...
    tokenizer_exceptions: Any = ...
    stop_words: Any = ...

class Finnish(Language):
    lang: str = ...
    Defaults: Any = ...
