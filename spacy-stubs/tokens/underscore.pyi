from ..errors import Errors as Errors
from typing import Any, Optional

class Underscore:
    mutable_types: Any = ...
    doc_extensions: Any = ...
    span_extensions: Any = ...
    token_extensions: Any = ...
    def __init__(self, extensions: Any, obj: Any, start: Optional[Any] = ..., end: Optional[Any] = ...) -> None: ...
    def __dir__(self): ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any): ...
    def set(self, name: Any, value: Any): ...
    def get(self, name: Any): ...
    def has(self, name: Any): ...
    @classmethod
    def get_state(cls): ...
    @classmethod
    def load_state(cls, state: Any) -> None: ...

def get_ext_args(**kwargs: Any): ...
def is_writable_attr(ext: Any): ...
