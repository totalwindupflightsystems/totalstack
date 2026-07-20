"""
Test inputs loader for aws-shape-validator.
Loads per-service test input dicts from development/test_inputs/<service>.py.

Usage:
    from test_inputs import load_test_inputs
    inputs = load_test_inputs('acm')
    # Returns {'RequestCertificate': {...}, ...}
"""
import importlib


def _module_name(service: str) -> str:
    """Convert service name to module name (hyphens -> underscores)."""
    return service.replace('-', '_')


def load_test_inputs(service: str) -> dict:
    """Load TEST_INPUTS dict for a service. Returns empty dict if not found."""
    mod_name = _module_name(service)
    try:
        mod = importlib.import_module(f'test_inputs.{mod_name}')
        return getattr(mod, 'TEST_INPUTS', {})
    except ModuleNotFoundError:
        return {}
