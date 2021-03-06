from ...language import Language
from typing import Any

class UrduDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    tag_map: Any = ...
    stop_words: Any = ...
    suffixes: Any = ...
    writing_system: Any = ...

class Urdu(Language):
    lang: str = ...
    Defaults: Any = ...
