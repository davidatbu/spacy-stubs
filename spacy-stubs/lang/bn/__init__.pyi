from ...language import Language
from typing import Any

class BengaliDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    tag_map: Any = ...
    stop_words: Any = ...
    prefixes: Any = ...
    suffixes: Any = ...
    infixes: Any = ...

class Bengali(Language):
    lang: str = ...
    Defaults: Any = ...
