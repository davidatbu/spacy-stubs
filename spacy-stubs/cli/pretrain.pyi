from .. import util as util
from .._ml import Tok2Vec as Tok2Vec, chain as chain, create_default_optimizer as create_default_optimizer, flatten as flatten, get_cossim_loss as get_cossim_loss, masked_language_model as masked_language_model
from ..attrs import HEAD as HEAD, ID as ID
from ..errors import Errors as Errors
from ..tokens import Doc as Doc
from typing import Any, Optional

def pretrain(texts_loc: Any, vectors_model: Any, output_dir: Any, width: int = ..., conv_depth: int = ..., bilstm_depth: int = ..., cnn_pieces: int = ..., sa_depth: int = ..., use_chars: bool = ..., cnn_window: int = ..., embed_rows: int = ..., loss_func: str = ..., use_vectors: bool = ..., dropout: float = ..., n_iter: int = ..., batch_size: int = ..., max_length: int = ..., min_length: int = ..., seed: int = ..., n_save_every: Optional[Any] = ..., init_tok2vec: Optional[Any] = ..., epoch_start: Optional[Any] = ...) -> None: ...
def make_update(model: Any, docs: Any, optimizer: Any, drop: float = ..., objective: str = ...): ...
def make_docs(nlp: Any, batch: Any, min_length: Any, max_length: Any): ...
def get_vectors_loss(ops: Any, docs: Any, prediction: Any, objective: str = ...): ...
def create_pretraining_model(nlp: Any, tok2vec: Any): ...

class ProgressTracker:
    loss: float = ...
    prev_loss: float = ...
    nr_word: int = ...
    words_per_epoch: Any = ...
    frequency: Any = ...
    last_time: Any = ...
    last_update: int = ...
    epoch_loss: float = ...
    def __init__(self, frequency: int = ...) -> None: ...
    def update(self, epoch: Any, loss: Any, docs: Any): ...