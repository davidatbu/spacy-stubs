from ...attrs import IS_CURRENCY as IS_CURRENCY, LIKE_NUM as LIKE_NUM
from .punctuation import LIST_CURRENCY as LIST_CURRENCY
from typing import Any

def like_num(text: Any): ...
def is_currency(text: Any): ...

LEX_ATTRS: Any
