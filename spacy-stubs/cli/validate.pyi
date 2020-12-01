from .. import about as about
from ..compat import path2str as path2str
from ..util import get_data_path as get_data_path
from typing import Any

def validate() -> None: ...
def get_model_links(compat: Any): ...
def get_model_pkgs(compat: Any, all_models: Any): ...
def get_model_row(compat: Any, name: Any, data: Any, msg: Any, model_type: str = ...): ...
def is_model_path(model_path: Any): ...
def is_compat(compat: Any, name: Any, version: Any): ...
def reformat_version(version: Any): ...
