from .errors import Errors as Errors
from .lookups import Lookups as Lookups
from .symbols import ADJ as ADJ, NOUN as NOUN, PROPN as PROPN, PUNCT as PUNCT, VERB as VERB
from typing import Any, Optional

class Lemmatizer:
    @classmethod
    def load(cls, *args: Any, **kwargs: Any) -> None: ...
    lookups: Any = ...
    def __init__(self, lookups: Any, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, string: Any, univ_pos: Any, morphology: Optional[Any] = ...): ...
    def is_base_form(self, univ_pos: Any, morphology: Optional[Any] = ...): ...
    def noun(self, string: Any, morphology: Optional[Any] = ...): ...
    def verb(self, string: Any, morphology: Optional[Any] = ...): ...
    def adj(self, string: Any, morphology: Optional[Any] = ...): ...
    def det(self, string: Any, morphology: Optional[Any] = ...): ...
    def pron(self, string: Any, morphology: Optional[Any] = ...): ...
    def adp(self, string: Any, morphology: Optional[Any] = ...): ...
    def num(self, string: Any, morphology: Optional[Any] = ...): ...
    def punct(self, string: Any, morphology: Optional[Any] = ...): ...
    def lookup(self, string: Any, orth: Optional[Any] = ...): ...
    def lemmatize(self, string: Any, index: Any, exceptions: Any, rules: Any): ...
