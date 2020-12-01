from .. import about as about, util as util
from .._ml import create_default_optimizer as create_default_optimizer
from ..attrs import CLUSTER as CLUSTER, IS_OOV as IS_OOV, LANG as LANG, PROB as PROB
from ..compat import path2str as path2str
from ..gold import GoldCorpus as GoldCorpus
from typing import Any, Optional

def train(lang: Any, output_path: Any, train_path: Any, dev_path: Any, raw_text: Optional[Any] = ..., base_model: Optional[Any] = ..., pipeline: str = ..., replace_components: bool = ..., vectors: Optional[Any] = ..., width: int = ..., conv_depth: int = ..., cnn_window: int = ..., cnn_pieces: int = ..., use_chars: bool = ..., bilstm_depth: int = ..., embed_rows: int = ..., n_iter: int = ..., n_early_stopping: Optional[Any] = ..., n_examples: int = ..., use_gpu: int = ..., version: str = ..., meta_path: Optional[Any] = ..., init_tok2vec: Optional[Any] = ..., parser_multitasks: str = ..., entity_multitasks: str = ..., noise_level: float = ..., orth_variant_level: float = ..., eval_beam_widths: str = ..., gold_preproc: bool = ..., learn_tokens: bool = ..., textcat_multilabel: bool = ..., textcat_arch: str = ..., textcat_positive_label: Optional[Any] = ..., tag_map_path: Optional[Any] = ..., verbose: bool = ..., debug: bool = ...): ...
