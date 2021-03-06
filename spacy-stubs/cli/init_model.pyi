from ..errors import Errors as Errors, Warnings as Warnings, user_warning as user_warning
from ..util import ensure_path as ensure_path, get_lang_class as get_lang_class
from ..vectors import Vectors as Vectors
from typing import Any, Optional

DEFAULT_OOV_PROB: int

def init_model(lang: Any, output_dir: Any, freqs_loc: Optional[Any] = ..., clusters_loc: Optional[Any] = ..., jsonl_loc: Optional[Any] = ..., vectors_loc: Optional[Any] = ..., prune_vectors: int = ..., vectors_name: Optional[Any] = ..., model_name: Optional[Any] = ...): ...
def open_file(loc: Any): ...
def read_attrs_from_deprecated(freqs_loc: Any, clusters_loc: Any): ...
def create_model(lang: Any, lex_attrs: Any, name: Optional[Any] = ...): ...
def add_vectors(nlp: Any, vectors_loc: Any, prune_vectors: Any, name: Optional[Any] = ...) -> None: ...
def read_vectors(vectors_loc: Any): ...
def read_freqs(freqs_loc: Any, max_length: int = ..., min_doc_freq: int = ..., min_freq: int = ...): ...
def read_clusters(clusters_loc: Any): ...
