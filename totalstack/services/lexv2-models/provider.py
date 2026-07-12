"""Auto-wired TotalStack provider for lexv2-models."""
import importlib.util
import functools
import logging
import os

from localstack.aws.api import RequestContext, handler
from localstack.aws.api import CommonServiceException

LOG = logging.getLogger(__name__)

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_SVC = os.path.join(_ROOT, "specs", "aws", ".speclang", "assembled", "lexv2-models")

# Load models
from dataclasses import dataclass as _dc
_models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(_SVC, "models.code.py"))
_models_mod = importlib.util.module_from_spec(_models_spec)
_models_mod.dataclass = _dc
_models_spec.loader.exec_module(_models_mod)

_STORE_CLS = None
for _name, _obj in _models_mod.__dict__.items():
    if _name.endswith("Store") and isinstance(_obj, type) and _name != "type":
        _STORE_CLS = _obj
        break

# Discover handler functions
_HANDLERS = {}
for _fn in sorted(os.listdir(_SVC)):
    if not _fn.endswith(".code.py") or _fn == "models.code.py":
        continue
    _stem = _fn[:-8]
    _op = "".join(w.capitalize() for w in _stem.split("-"))
    _method = _stem.replace("-", "_")
    _hspec = importlib.util.spec_from_file_location(
        _stem, os.path.join(_SVC, _fn))
    _hmod = importlib.util.module_from_spec(_hspec)
    # Strip @dataclass from handler code (SpecLang cascade bug — applies it to functions)
    _hmod.dataclass = lambda f: f
    _hspec.loader.exec_module(_hmod)
    for _v in _hmod.__dict__.values():
        if callable(_v) and not getattr(_v, "__name__", "").startswith("_"):
            _HANDLERS[_op] = (_method, _v)
            break


class TotalStackLexv2ModelsProvider:
    """Auto-wired provider for lexv2-models."""

    def __init__(self):
        self.store = _STORE_CLS()


# Attach handler methods
def _attach_handler(op_name, method_name, fn):
    @handler(op_name, expand=False)
    def _w(self, context: RequestContext, request: dict,
           _fn=fn, _method=method_name):
        try:
            return _fn(self.store, request)
        except Exception as e:
            raise CommonServiceException(str(e)) from e
    return _w


for _op, (_method, _fn) in _HANDLERS.items():
    setattr(TotalStackLexv2ModelsProvider, _method, _attach_handler(_op, _method, _fn))
