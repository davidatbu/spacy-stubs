from .. import about as about, util as util
from ..compat import basestring_ as basestring_, path2str as path2str, unicode_ as unicode_
from typing import Any, Optional

def info(model: Optional[Any] = ..., markdown: bool = ..., silent: bool = ...): ...
def list_models(): ...
def print_markdown(data: Any, title: Optional[Any] = ...) -> None: ...