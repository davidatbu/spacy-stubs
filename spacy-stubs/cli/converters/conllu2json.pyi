from ...gold import iob_to_biluo as iob_to_biluo
from typing import Any, Optional

def conllu2json(input_data: Any, n_sents: int = ..., use_morphology: bool = ..., lang: Optional[Any] = ..., **_: Any): ...
def is_ner(tag: Any): ...
def read_conllx(input_data: Any, use_morphology: bool = ..., n: int = ...) -> None: ...
def simplify_tags(iob: Any): ...
def generate_sentence(sent: Any, has_ner_tags: Any): ...
def create_doc(sentences: Any, id: Any): ...
