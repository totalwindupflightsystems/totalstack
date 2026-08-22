"""Auto-wired TotalStack provider for amp."""

import importlib.util
import logging
import os

from localstack.aws.api import CommonServiceException, RequestContext, ServiceException, handler

LOG = logging.getLogger(__name__)

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_SVC = os.path.join(_ROOT, "specs", "aws", ".speclang", "assembled", "amp")

# Load models
from dataclasses import dataclass as _dc

_models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(_SVC, "models.code.py")
)
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
    _op = "".join(w[:1].upper() + w[1:] for w in _stem.split("-"))
    _method = _stem.replace("-", "_")
    _hspec = importlib.util.spec_from_file_location(_stem, os.path.join(_SVC, _fn))
    _hmod = importlib.util.module_from_spec(_hspec)
    # Strip @dataclass from handler code (SpecLang cascade bug — applies it to functions)
    _hmod.dataclass = lambda f: f
    _hspec.loader.exec_module(_hmod)
    # pick the actual handler function: prefer the conventional `handler` name,
    # else the first callable that is not a dunder or injected helper
    # (the injected no-op `dataclass` lambda used to win the scan and was
    # registered as the handler, so every op called the lambda and 500'd)
    _h = _hmod.__dict__.get("handler")
    if not callable(_h):
        for _v in _hmod.__dict__.values():
            _vname = getattr(_v, "__name__", "")
            if callable(_v) and not _vname.startswith("_") and _vname not in ("dataclass", "time", "uuid", "<lambda>"):
                _h = _v
                break
    if _h is not None:
        _HANDLERS[_op] = (_method, _h)


class TotalStackAmpProvider:
    """Auto-wired provider for amp."""

    def __init__(self):
        self.store = _STORE_CLS()


# Attach handler methods
def _attach_handler(op_name, method_name, fn):
    @handler(op_name, expand=False)
    def _w(self, context: RequestContext, request: dict, _fn=fn, _method=method_name):
        try:
            return _fn(self.store, request)
        except ServiceException:
            # already-typed service errors (proper code/status, e.g. 400s) pass through
            raise
        except Exception as e:
            # generated models' exceptions carry the AWS error code as a .code
            # attribute or as their class name; map them to a proper service error
            code = getattr(e, "code", None) or e.__class__.__name__
            raise CommonServiceException(code, str(e)) from e
    # localstack-core's create_dispatch_table resolves handlers via fn.__name__
    # (getattr(delegate, fn.__name__)); the wrapper must be named like the
    # attribute it is attached under, or every op 500s with AttributeError
    _w.__name__ = method_name
    _w.__qualname__ = method_name
    return _w


for _op, (_method, _fn) in _HANDLERS.items():
    setattr(TotalStackAmpProvider, _method, _attach_handler(_op, _method, _fn))
