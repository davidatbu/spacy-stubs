from ...language import Language
from typing import Any

class MultiLanguageDefaults(Language.Defaults):
    lex_attr_getters: Any = ...
    tokenizer_exceptions: Any = ...

class MultiLanguage(Language):
    lang: str = ...
    Defaults: Any = ...