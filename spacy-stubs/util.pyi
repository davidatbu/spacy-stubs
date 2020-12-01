# from .compat import CudaStream as CudaStream, basestring_ as basestring_, cupy as cupy, import_file as import_file, path2str as path2str, unicode_ as unicode_
# from .errors import Errors as Errors, Warnings as Warnings, deprecation_warning as deprecation_warning
# from .symbols import ORTH as ORTH
# from typing import Any, Optional
#
# class registry:
#     languages: Any = ...
#     architectures: Any = ...
#     lookups: Any = ...
#     factories: Any = ...
#     displacy_colors: Any = ...
#
# def set_env_log(value: Any) -> None: ...
# def lang_class_is_loaded(lang: Any): ...
# def get_lang_class(lang: Any): ...
# def set_lang_class(name: Any, cls: Any) -> None: ...
# def get_data_path(require_exists: bool = ...): ...
# def set_data_path(path: Any) -> None: ...
# def make_layer(arch_config: Any): ...
# def ensure_path(path: Any): ...
# def load_language_data(path: Any): ...
# def get_module_path(module: Any): ...
# def load_model(name: Any, **overrides: Any): ...
# def load_model_from_link(name: Any, **overrides: Any): ...
# def load_model_from_package(name: Any, **overrides: Any): ...
# def load_model_from_path(model_path: Any, meta: bool = ..., **overrides: Any): ...
# def load_model_from_init_py(init_file: Any, **overrides: Any): ...
# def get_model_meta(path: Any): ...
# def is_package(name: Any): ...
# def get_package_path(name: Any): ...
# def is_in_jupyter(): ...
# def get_component_name(component: Any): ...
# def get_cuda_stream(require: bool = ..., non_blocking: bool = ...): ...
# def get_async(stream: Any, numpy_array: Any): ...
# def env_opt(name: Any, default: Optional[Any] = ...): ...
# def read_regex(path: Any): ...
# def compile_prefix_regex(entries: Any): ...
# def compile_suffix_regex(entries: Any): ...
# def compile_infix_regex(entries: Any): ...
# def add_lookups(default_func: Any, *lookups: Any): ...
# def update_exc(base_exceptions: Any, *addition_dicts: Any): ...
# def expand_exc(excs: Any, search: Any, replace: Any): ...
# def normalize_slice(length: Any, start: Any, stop: Any, step: Optional[Any] = ...): ...
# def minibatch(items: Any, size: int = ...) -> None: ...
# def compounding(start: Any, stop: Any, compound: Any): ...
# def stepping(start: Any, stop: Any, steps: Any): ...
# def decaying(start: Any, stop: Any, decay: Any) -> None: ...
# def minibatch_by_words(items: Any, size: Any, tuples: bool = ..., count_words: Any = ...) -> None: ...
# def itershuffle(iterable: Any, bufsize: int = ...) -> None: ...
# def filter_spans(spans: Any): ...
# def to_bytes(getters: Any, exclude: Any): ...
# def from_bytes(bytes_data: Any, setters: Any, exclude: Any): ...
# def to_disk(path: Any, writers: Any, exclude: Any): ...
# def from_disk(path: Any, readers: Any, exclude: Any): ...
# def minify_html(html: Any): ...
# def escape_html(text: Any): ...
# def use_gpu(gpu_id: Any): ...
# def fix_random_seed(seed: int = ...) -> None: ...
# def get_json_validator(schema: Any): ...
# def validate_schema(schema: Any) -> None: ...
# def validate_json(data: Any, validator: Any): ...
# def get_serialization_exclude(serializers: Any, exclude: Any, kwargs: Any): ...
#
# class SimpleFrozenDict(dict):
#     def __setitem__(self, key: Any, value: Any) -> None: ...
#     def pop(self, key: Any, default: Optional[Any] = ...) -> None: ...
#     def update(self, other: Any) -> None: ...
#
# class DummyTokenizer:
#     def to_bytes(self, **kwargs: Any): ...
#     def from_bytes(self, _bytes_data: Any, **kwargs: Any): ...
#     def to_disk(self, _path: Any, **kwargs: Any) -> None: ...
#     def from_disk(self, _path: Any, **kwargs: Any): ...
