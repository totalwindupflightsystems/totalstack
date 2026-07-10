"""Auto-wire all TotalStack services into LocalStack's HTTP gateway.

One-shot: discovers all services, creates provider modules,
patches LocalStack's routing, and removes skip markers from E2E tests.
"""
import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSEMBLED = ROOT / "specs" / "aws" / ".speclang" / "assembled"
TOTALSTACK_SERVICES = ROOT / "totalstack" / "services"
PROVIDERS_PY = ROOT / "totalstack" / "providers.py"
LS_PROVIDERS = ROOT / "localstack-core" / "localstack" / "services" / "providers.py"

# Skip: LocalStack ASF services that already have real providers
SKIP = {
    'acm',  # already wired
    'dynamodb',  # forward_request to JVM
    'ec2',
    'ecs',
    'eks',
    'elasticache',
    'emr',
    'glue',
    'iam',
    'kafka',
    'kinesis',
    'kms',
    'lambda',
    'logs',
    'rds',
    'redshift',
    's3',
    'sagemaker',
    'ssm',
    'sns',
    'sqs',
    'wafv2',
}


def pascal(svc: str) -> str:
    """'application-autoscaling' → 'ApplicationAutoscaling'"""
    return "".join(w.capitalize() for w in svc.replace("-", " ").split())


def discover_services() -> list:
    return sorted(
        d.name for d in ASSEMBLED.iterdir()
        if d.is_dir() and not d.name.startswith("_")
        and (d / "models.code.py").exists()
    )


def generate_provider(svc: str) -> str:
    """Generate a generic auto-wiring provider.py for one service."""
    p = pascal(svc)
    return f'''"""Auto-wired TotalStack provider for {svc}."""
import importlib.util
import functools
import logging
import os

from localstack.aws.api import RequestContext, handler
from localstack.aws.api import CommonServiceException

LOG = logging.getLogger(__name__)

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_SVC = os.path.join(_ROOT, "specs", "aws", ".speclang", "assembled", "{svc}")

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
_HANDLERS = {{}}
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


class TotalStack{p}Provider:
    """Auto-wired provider for {svc}."""

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
    setattr(TotalStack{p}Provider, _method, _attach_handler(_op, _method, _fn))
'''


def generate_providers_py(services: list) -> str:
    lines = [
        '"""TotalStack service providers — auto-generated wiring."""',
        "from localstack.services.plugins import Service, aws_provider",
        "",
    ]
    for svc in sorted(services):
        if svc in SKIP:
            continue
        p = pascal(svc)
        snake = svc.replace("-", "_")
        lines.append(f'''
@aws_provider(api="{svc}", name="totalstack")
def {snake}_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.{svc}.provider import TotalStack{p}Provider
    provider = TotalStack{p}Provider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)
''')
    return "\n".join(lines)


def patch_ls_providers():
    content = LS_PROVIDERS.read_text()
    marker = "# TotalStack providers"
    if marker in content:
        return  # already patched
    LS_PROVIDERS.write_text(
        content.rstrip() + "\n\n# TotalStack providers\n"
        "from totalstack.providers import *  # noqa: F401, F403\n"
    )


def fix_e2e_skip_markers(services: list):
    """Remove the module-level pytestmark skip from E2E test files
    so all tests actually run instead of skipping themselves."""
    tests_dir = ASSEMBLED / "_tests"
    fixed = 0
    for svc in services:
        e2e_path = tests_dir / f"test_{svc}_e2e.py"
        if not e2e_path.exists():
            continue
        content = e2e_path.read_text()
        if "provider not yet wired" in content or "not yet wired into" in content:
            # Replace the skip reason — remove pytestmark skip, keep boto3 check
            lines = content.split("\n")
            new_lines = []
            skip_block = False
            for line in lines:
                if "pytestmark = pytest.mark.skipif" in line and (
                    "wired" in line or "available" in line):
                    skip_block = True
                    continue
                if skip_block and line.strip() == "":
                    skip_block = False
                    continue
                if not skip_block:
                    new_lines.append(line)
            e2e_path.write_text("\n".join(new_lines))
            fixed += 1
            print(f"  ✓ unfroze {svc} E2E tests")
    print(f"\nUnfroze {fixed} E2E test files")


def main():
    print("=== TotalStack Auto-Wiring ===\n")
    services = discover_services()
    to_wire = [s for s in services if s not in SKIP]
    print(f"Wiring {len(to_wire)} services (skipping {len(services) - len(to_wire)} ASF/moto)\n")

    # Generate providers
    for svc in sorted(to_wire):
        svc_dir = TOTALSTACK_SERVICES / svc
        svc_dir.mkdir(parents=True, exist_ok=True)
        (svc_dir / "__init__.py").write_text("")
        (svc_dir / "provider.py").write_text(generate_provider(svc))
        print(f"  ✓ {svc}")

    # Generate providers.py registry
    PROVIDERS_PY.write_text(generate_providers_py(services))
    print(f"\n✓ Wrote providers.py")

    # Patch LocalStack
    patch_ls_providers()
    print(f"✓ Patched LocalStack routing")

    # Unfreeze E2E skip markers
    print()
    fix_e2e_skip_markers(services)

    print(f"\n=== Done: {len(to_wire)} services wired ===\n")
    print("Start localstack:    localstack start")
    print("Run E2E tests:       .venv/bin/python -m pytest specs/aws/.speclang/assembled/_tests/test_*e2e*.py -q")


if __name__ == "__main__":
    main()
