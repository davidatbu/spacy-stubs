from typing_extensions import Final

class Token:
    i: Final[int]
    text: Final[str]
    @property
    def head(self) -> "Token": ...
    # Spacy does a lot of runtime modification of instance attributes, dunno how to do
    # take care of that except simply assume that the dependency parsing component was
    # used
    dep_: str
