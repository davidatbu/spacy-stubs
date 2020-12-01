from .converters import conll_ner2json as conll_ner2json, conllu2json as conllu2json, iob2json as iob2json, ner_jsonl2json as ner_jsonl2json
from typing import Any, Optional

CONVERTERS: Any
FILE_TYPES: Any
FILE_TYPES_STDOUT: Any

def convert(input_file: Any, output_dir: str = ..., file_type: str = ..., n_sents: int = ..., seg_sents: bool = ..., model: Optional[Any] = ..., morphology: bool = ..., converter: str = ..., lang: Optional[Any] = ...) -> None: ...
def autodetect_ner_format(input_data: Any): ...
