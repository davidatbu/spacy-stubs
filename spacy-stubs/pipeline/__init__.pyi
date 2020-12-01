from .entityruler import EntityRuler as EntityRuler
from .functions import (
    merge_entities as merge_entities,
    merge_noun_chunks as merge_noun_chunks,
    merge_subtokens as merge_subtokens,
)
from .hooks import (
    SentenceSegmenter as SentenceSegmenter,
    SimilarityHook as SimilarityHook,
)
from .morphologizer import Morphologizer as Morphologizer
from .pipes import (
    DependencyParser as DependencyParser,
    EntityLinker as EntityLinker,
    EntityRecognizer as EntityRecognizer,
    Pipe as Pipe,
    Sentencizer as Sentencizer,
    Tagger as Tagger,
    Tensorizer as Tensorizer,
    TextCategorizer as TextCategorizer,
)
