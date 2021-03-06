from ...language import Language
from typing import Any

class LithuanianDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    stop_words: Any = ...
    tag_map: Any = ...
    morph_rules: Any = ...

class Lithuanian(Language):
    lang: str = ...
    Defaults: Any = ...
