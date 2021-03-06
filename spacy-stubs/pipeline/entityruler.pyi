from ..compat import basestring_ as basestring_
from ..errors import Errors as Errors
from ..language import component as component
from ..matcher import Matcher as Matcher, PhraseMatcher as PhraseMatcher
from ..tokens import Doc as Doc, Span as Span
from ..util import ensure_path as ensure_path, from_disk as from_disk, to_disk as to_disk
from typing import Any, Optional

DEFAULT_ENT_ID_SEP: str

class EntityRuler:
    nlp: Any = ...
    overwrite: Any = ...
    token_patterns: Any = ...
    phrase_patterns: Any = ...
    matcher: Any = ...
    phrase_matcher_attr: Any = ...
    phrase_matcher: Any = ...
    ent_id_sep: Any = ...
    def __init__(self, nlp: Any, phrase_matcher_attr: Optional[Any] = ..., validate: bool = ..., **cfg: Any) -> None: ...
    @classmethod
    def from_nlp(cls, nlp: Any, **cfg: Any): ...
    def __len__(self): ...
    def __contains__(self, label: Any): ...
    def __call__(self, doc: Any): ...
    @property
    def labels(self): ...
    @property
    def ent_ids(self): ...
    @property
    def patterns(self): ...
    def add_patterns(self, patterns: Any) -> None: ...
    def from_bytes(self, patterns_bytes: Any, **kwargs: Any): ...
    def to_bytes(self, **kwargs: Any): ...
    def from_disk(self, path: Any, **kwargs: Any): ...
    def to_disk(self, path: Any, **kwargs: Any): ...
