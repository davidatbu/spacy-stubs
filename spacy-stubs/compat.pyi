import copyreg as copy_reg
import cupy
import cPickle as pickle
from cupy.cuda.stream import Stream as CudaStream
from thinc.neural.optimizers import Adam as Optimizer
from thinc.neural.util import copy_array
from typing import Any, Optional

pickle = pickle
copy_reg = copy_reg
CudaStream = CudaStream
cupy = cupy
copy_array = copy_array
izip: Any
is_windows: Any
is_linux: Any
is_osx: Any
is_python2: Any
is_python3: Any
is_python_pre_3_5: Any
bytes_ = str
unicode_ = unicode
basestring_ = basestring
input_ = raw_input
path2str: Any
class_types: Any
bytes_ = bytes
unicode_ = str
basestring_ = str
input_ = input

def b_to_str(b_str: Any): ...
def symlink_to(orig: Any, dest: Any) -> None: ...
def symlink_remove(link: Any) -> None: ...
def is_config(python2: Optional[Any] = ..., python3: Optional[Any] = ..., windows: Optional[Any] = ..., linux: Optional[Any] = ..., osx: Optional[Any] = ...): ...
def import_file(name: Any, loc: Any): ...
def unescape_unicode(string: Any): ...
