from ...symbols import AUX as AUX, NOUN as NOUN, PRON as PRON, PROPN as PROPN, VERB as VERB
from typing import Any

def noun_chunks(obj: Any) -> None: ...
def is_verb_token(token: Any): ...
def next_token(token: Any): ...
def noun_bounds(doc: Any, root: Any, np_left_deps: Any, np_right_deps: Any, stop_deps: Any): ...

SYNTAX_ITERATORS: Any
