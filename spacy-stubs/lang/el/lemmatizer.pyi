from ...lemmatizer import Lemmatizer as Lemmatizer
from typing import Any

class GreekLemmatizer(Lemmatizer):
    def lemmatize(self, string: Any, index: Any, exceptions: Any, rules: Any): ...
