from ...language import Language
from typing import Any

class SwedishDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...
    morph_rules: Any = ...
    tag_map: Any = ...
    infixes: Any = ...
    suffixes: Any = ...
    stop_words: Any = ...
    syntax_iterators: Any = ...

class Swedish(Language):
    lang: str = ...
    Defaults: Any = ...
