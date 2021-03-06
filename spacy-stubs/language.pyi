from typing import Any, Dict, Iterable, Iterator

#
# from spacy.util import minibatch as minibatch
#
# from . import about as about
# from . import util as util
# from ._ml import create_default_optimizer as create_default_optimizer
# from ._ml import link_vectors_to_models as link_vectors_to_models
# from .analysis import analyze_all_pipes as analyze_all_pipes
# from .analysis import analyze_pipes as analyze_pipes
# from .analysis import validate_attrs as validate_attrs
# from .attrs import IS_STOP as IS_STOP
# from .attrs import LANG as LANG
# from .compat import basestring_ as basestring_
# from .compat import class_types as class_types
# from .compat import is_python2 as is_python2
# from .compat import izip as izip
# from .errors import Errors as Errors
# from .errors import Warnings as Warnings
# from .errors import deprecation_warning as deprecation_warning
# from .errors import user_warning as user_warning
# from .gold import GoldParse as GoldParse
# from .lang.lex_attrs import LEX_ATTRS as LEX_ATTRS
# from .lang.lex_attrs import is_stop as is_stop
# from .lang.punctuation import TOKENIZER_INFIXES as TOKENIZER_INFIXES
# from .lang.punctuation import TOKENIZER_PREFIXES as TOKENIZER_PREFIXES
# from .lang.punctuation import TOKENIZER_SUFFIXES as TOKENIZER_SUFFIXES
# from .lang.tag_map import TAG_MAP as TAG_MAP
# from .lang.tokenizer_exceptions import TOKEN_MATCH as TOKEN_MATCH
# from .lemmatizer import Lemmatizer as Lemmatizer
# from .lookups import Lookups as Lookups
# from .scorer import Scorer as Scorer
# from .tokenizer import Tokenizer as Tokenizer
from .tokens import Doc as Doc

# from .tokens.underscore import Underscore as Underscore
# from .vocab import Vocab as Vocab
#
# ENABLE_PIPELINE_ANALYSIS: bool
#
# class BaseDefaults:
#     @classmethod
#     def create_lemmatizer(
#         cls, nlp: Optional[Any] = ..., lookups: Optional[Any] = ...
#     ): ...
#     @classmethod
#     def create_lookups(cls, nlp: Optional[Any] = ...): ...
#     @classmethod
#     def create_vocab(cls, nlp: Optional[Any] = ...): ...
#     @classmethod
#     def create_tokenizer(cls, nlp: Optional[Any] = ...): ...
#     pipe_names: Any = ...
#     token_match: Any = ...
#     prefixes: Any = ...
#     suffixes: Any = ...
#     infixes: Any = ...
#     tag_map: Any = ...
#     tokenizer_exceptions: Any = ...
#     stop_words: Any = ...
#     morph_rules: Any = ...
#     lex_attr_getters: Any = ...
#     syntax_iterators: Any = ...
#     resources: Any = ...
#     writing_system: Any = ...
#     single_orth_variants: Any = ...
#     paired_orth_variants: Any = ...
#
class Language:
    # Defaults: Any = ...

    lang: str = ...

    #     factories: Any = ...
    #     vocab: Any = ...
    #     tokenizer: Any = ...
    #     pipeline: Any = ...
    #     max_length: Any = ...
    #     def __init__(
    #         self,
    #         vocab: bool = ...,
    #         make_doc: bool = ...,
    #         max_length: Any = ...,
    #         meta: Any = ...,
    #         **kwargs: Any
    #     ) -> None: ...
    #     @property
    #     def path(self): ...
    @property
    def meta(self) -> Dict[str, Any]: ...
    #     @meta.setter
    #     def meta(self, value: Any) -> None: ...
    #     @property
    #     def tensorizer(self): ...
    #     @property
    #     def tagger(self): ...
    #     @property
    #     def parser(self): ...
    #     @property
    #     def entity(self): ...
    #     @property
    #     def linker(self): ...
    #     @property
    #     def matcher(self): ...
    #     @property
    #     def pipe_names(self): ...
    #     @property
    #     def pipe_factories(self): ...
    #     @property
    #     def pipe_labels(self): ...
    #     def get_pipe(self, name: Any): ...
    #     def create_pipe(self, name: Any, config: Any = ...): ...
    #     def add_pipe(
    #         self,
    #         component: Any,
    #         name: Optional[Any] = ...,
    #         before: Optional[Any] = ...,
    #         after: Optional[Any] = ...,
    #         first: Optional[Any] = ...,
    #         last: Optional[Any] = ...,
    #     ) -> None: ...
    #     def has_pipe(self, name: Any): ...
    #     def replace_pipe(self, name: Any, component: Any) -> None: ...
    #     def rename_pipe(self, old_name: Any, new_name: Any) -> None: ...
    #     def remove_pipe(self, name: Any): ...
    def __call__(
        self,
        text: str,
        disable: List[str] = [],
        # component_cfg: Optional[Any] = ...
    ) -> Doc: ...
    #     def disable_pipes(self, *names: Any): ...
    #     def make_doc(self, text: Any): ...
    #     def update(
    #         self,
    #         docs: Any,
    #         golds: Any,
    #         drop: float = ...,
    #         sgd: Optional[Any] = ...,
    #         losses: Optional[Any] = ...,
    #         component_cfg: Optional[Any] = ...,
    #     ) -> None: ...
    #     def rehearse(
    #         self,
    #         docs: Any,
    #         sgd: Optional[Any] = ...,
    #         losses: Optional[Any] = ...,
    #         config: Optional[Any] = ...,
    #     ): ...
    #     def preprocess_gold(self, docs_golds: Any) -> None: ...
    #     def begin_training(
    #         self,
    #         get_gold_tuples: Optional[Any] = ...,
    #         sgd: Optional[Any] = ...,
    #         component_cfg: Optional[Any] = ...,
    #         **cfg: Any
    #     ): ...
    #     def resume_training(self, sgd: Optional[Any] = ..., **cfg: Any): ...
    #     def evaluate(
    #         self,
    #         docs_golds: Any,
    #         verbose: bool = ...,
    #         batch_size: int = ...,
    #         scorer: Optional[Any] = ...,
    #         component_cfg: Optional[Any] = ...,
    #     ): ...
    #     def use_params(self, params: Any, **cfg: Any) -> None: ...
    def pipe(
        self,
        texts: Iterable[str],
        as_tuples: bool = ...,
        n_threads: int = ...,
        batch_size: int = ...,
        disable: Any = ...,
        cleanup: bool = ...,
        # component_cfg: Optional[Any] = ...,
        n_process: int = ...,
    ) -> Iterator[Doc]: ...

#     def to_disk(self, path: Any, exclude: Any = ..., disable: Optional[Any] = ...): ...
#     def from_disk(
#         self, path: Any, exclude: Any = ..., disable: Optional[Any] = ...
#     ): ...
#     def to_bytes(
#         self, exclude: Any = ..., disable: Optional[Any] = ..., **kwargs: Any
#     ): ...
#     def from_bytes(
#         self,
#         bytes_data: Any,
#         exclude: Any = ...,
#         disable: Optional[Any] = ...,
#         **kwargs: Any
#     ): ...
#
# class component:
#     name: Any = ...
#     assigns: Any = ...
#     requires: Any = ...
#     retokenizes: Any = ...
#     def __init__(
#         self,
#         name: Optional[Any] = ...,
#         assigns: Any = ...,
#         requires: Any = ...,
#         retokenizes: bool = ...,
#     ) -> None: ...
#     def __call__(self, *args: Any, **kwargs: Any): ...
#
# class DisabledPipes(list):
#     nlp: Any = ...
#     names: Any = ...
#     original_pipeline: Any = ...
#     def __init__(self, nlp: Any, *names: Any) -> None: ...
#     def __enter__(self): ...
#     def __exit__(self, *args: Any) -> None: ...
#     def restore(self) -> None: ...
#
# class _Sender:
#     data: Any = ...
#     queues: Any = ...
#     chunk_size: Any = ...
#     count: int = ...
#     def __init__(self, data: Any, queues: Any, chunk_size: Any) -> None: ...
#     def send(self) -> None: ...
#     def step(self) -> None: ...
