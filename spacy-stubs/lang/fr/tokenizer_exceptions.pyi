from ...symbols import LEMMA as LEMMA, ORTH as ORTH, TAG as TAG
from ..char_classes import ALPHA as ALPHA, ALPHA_LOWER as ALPHA_LOWER
from ..tokenizer_exceptions import URL_PATTERN as URL_PATTERN
from .punctuation import ELISION as ELISION, HYPHENS as HYPHENS
from typing import Any

FR_BASE_EXCEPTIONS: Any

def upper_first_letter(text: Any): ...
def lower_first_letter(text: Any): ...

token: Any
orig_elision: str
orig_hyphen: str
variants_infix: Any
TOKENIZER_EXCEPTIONS: Any
TOKEN_MATCH: Any
