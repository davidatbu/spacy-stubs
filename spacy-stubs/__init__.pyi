# from . import pipeline as pipeline
# from .glossary import explain as explain
# from thinc.neural.util import prefer_gpu as prefer_gpu, require_gpu as require_gpu
from typing import List

from .language import Language
from .language import component as component

# from .util import registry as registry

def load(
    name: str,
    disable: List[str] = []
    # **overrides: Any
) -> Language: ...

# def blank(name: Any, **kwargs: Any): ...
# def info(model: Optional[Any] = ..., markdown: bool = ..., silent: bool = ...): ...
