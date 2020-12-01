from ...language import Language
from typing import Any

class PersianDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    stop_words: Any = ...
    tag_map: Any = ...
    suffixes: Any = ...
    writing_system: Any = ...

class Persian(Language):
    lang: str = ...
    Defaults: Any = ...
