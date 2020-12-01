from ..gold import GoldCorpus as GoldCorpus
from ..syntax import nonproj as nonproj
from ..util import get_lang_class as get_lang_class, load_model as load_model
from typing import Any, Optional

NEW_LABEL_THRESHOLD: int
DEP_LABEL_THRESHOLD: int
BLANK_MODEL_MIN_THRESHOLD: int
BLANK_MODEL_THRESHOLD: int

def debug_data(lang: Any, train_path: Any, dev_path: Any, tag_map_path: Optional[Any] = ..., base_model: Optional[Any] = ..., pipeline: str = ..., ignore_warnings: bool = ..., verbose: bool = ..., no_format: bool = ...) -> None: ...
