from .. import about as about, util as util
from ..compat import path2str as path2str
from typing import Any, Optional

def package(input_dir: Any, output_dir: Any, meta_path: Optional[Any] = ..., create_meta: bool = ..., force: bool = ...) -> None: ...
def create_file(file_path: Any, contents: Any) -> None: ...
def generate_meta(model_path: Any, existing_meta: Any, msg: Any): ...

TEMPLATE_SETUP: Any
TEMPLATE_MANIFEST: Any
TEMPLATE_INIT: Any
