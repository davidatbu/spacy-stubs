from doc import Doc
from typing_extensions import Final

class Span:
    doc: Final[Doc]
    start: Final[int]
    end: Final[int]
