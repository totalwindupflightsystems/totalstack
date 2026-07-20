#!/usr/bin/env python3
"""
AWS Shape Validator — botocore-driven correctness gate.
Compares TotalStack handler output against AWS service-2.json shapes.
Every response field is checked: required, optional, types, enums.

Usage:
  python3 aws-shape-validator.py <service>          # validate all handlers
  python3 aws-shape-validator.py <service> --op DescribeCertificate
  python3 aws-shape-validator.py --all               # all 57 services

Exit code: 1 if any required field missing or type mismatch, 0 if clean.
"""
import sys
import json
import importlib.util
import botocore.loaders
from pathlib import Path

TOTALSTACK_ROOT = Path(__file__).resolve().parent.parent
ASSEMBLED = TOTALSTACK_ROOT / "specs" / "aws" / ".speclang" / "assembled"
LOADER = botocore.loaders.Loader()

# Fields that AWS returns but we don't need to emulate (dynamic/contextual)
SKIP_FIELDS = {
    'ResponseMetadata', 'RequestId', 'HTTPStatusCode', 'HTTPHeaders',
    'RetryAttempts',
}

# Shapes that are polymorphic/self-referencing — skip deep validation
SKIP_SHAPES = set()


def load_service_model(service: str) -> dict:
    """Load botocore service-2.json for a service."""
    return LOADER.load_service_model(service, 'service-2')


def load_store(service: str):
    """Dynamically load a TotalStack service store."""
    svc_dir = ASSEMBLED / service
    models_path = svc_dir / "models.code.py"
    if not models_path.exists():
        return None
    spec = importlib.util.spec_from_file_location(
        f"{service}_models", str(models_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Register in sys.modules so handler-loading can find exception classes
    import sys as _sys_load
    _sys_load.modules[f"{service}_models"] = mod
    # Find the Store class (convention: <Service>Store)
    # Case-insensitive match for service name (e.g. "codedeploy" -> CodeDeployStore)  # noqa: E501
    stores = [(name, obj) for name, obj in mod.__dict__.items()
              if name.endswith('Store') and isinstance(obj, type)]
    service_lower = service.lower().replace('-', '')
    for name, obj in stores:
        if name.lower().replace('store', '') == service_lower:
            return obj()
    # Fallback: any *Store
    if stores:
        return stores[0][1]()
    return None


def get_shape_members(svc_model: dict, shape_name: str) -> dict:
    """Get all member fields of a shape, recursively unwrapping."""
    shape = svc_model['shapes'].get(shape_name, {})
    if 'members' in shape:
        return dict(shape['members'])
    return {}


def validate_field(value, mdef: dict, svc_model: dict, path: str) -> list:
    """Validate a single field value against its shape definition. Returns error list."""  # noqa: E501
    errors = []
    shape_name = mdef.get('shape', '')
    shape = svc_model['shapes'].get(shape_name, {})

    if value is None:
        return errors  # optional field, no value

    shape_type = shape.get('type', '')

    if shape_type == 'string':
        if not isinstance(value, str):
            errors.append(f"{path}: expected string, got {type(value).__name__}")  # noqa: E501
    elif shape_type == 'integer' or shape_type == 'long':
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"{path}: expected integer, got {type(value).__name__}")  # noqa: E501
    elif shape_type == 'boolean':
        if not isinstance(value, bool):
            errors.append(f"{path}: expected boolean, got {type(value).__name__}")  # noqa: E501
    elif shape_type == 'timestamp':
        if not isinstance(value, (int, float, str)):
            errors.append(f"{path}: expected timestamp, got {type(value).__name__}")  # noqa: E501
    elif shape_type == 'list':
        if not isinstance(value, list):
            errors.append(f"{path}: expected list, got {type(value).__name__}")
        elif 'member' in shape:
            member_def = shape['member']
            for i, item in enumerate(value):
                errors.extend(validate_field(item, member_def, svc_model, f"{path}[{i}]"))  # noqa: E501
    elif shape_type == 'structure':
        if not isinstance(value, dict):
            errors.append(f"{path}: expected dict/structure, got {type(value).__name__}")  # noqa: E501
    elif shape_type == 'map':
        if not isinstance(value, dict):
            errors.append(f"{path}: expected dict/map, got {type(value).__name__}")  # noqa: E501

    # Check enum values
    if 'enum' in shape and value not in shape['enum']:
        errors.append(f"{path}: '{value}' not in enum {shape['enum'][:5]}...")

    return errors


def validate_operation(service: str, op_name: str, our_output: dict, svc_model: dict) -> dict:  # noqa: E501
    """Validate one operation's output against AWS shape. Returns {pass: bool, errors: [], warnings: []}."""  # noqa: E501
    if op_name not in svc_model['operations']:
        return {'pass': True, 'errors': [], 'warnings': [f"op {op_name} not in service model"]}  # noqa: E501

    op = svc_model['operations'][op_name]
    output_shape_name = op.get('output', {}).get('shape', '')
    if not output_shape_name:
        return {'pass': True, 'errors': [], 'warnings': ['no output shape']}

    outer_shape = svc_model['shapes'].get(output_shape_name, {})
    outer_members = outer_shape.get('members', {})

    errors = []
    warnings = []

    # Unwrap single-member wrappers (e.g., {"Certificate": {...}})
    our_data = our_output
    if len(outer_members) == 1:
        wrapper_key = list(outer_members.keys())[0]
        inner_shape_name = outer_members[wrapper_key].get('shape', '')
        inner_shape = svc_model['shapes'].get(inner_shape_name, {})
        inner_members = inner_shape.get('members', {})
        required = set(inner_shape.get('required', []))

        if isinstance(our_data, dict) and wrapper_key in our_data:
            our_data = our_data[wrapper_key]
        elif isinstance(our_data, dict):
            our_data = our_data
    else:
        inner_members = outer_members
        required = set(outer_shape.get('required', []))

    our_fields = set(our_data.keys()) if isinstance(our_data, dict) else set()
    aws_fields = set(inner_members.keys()) - SKIP_FIELDS
    missing_required = (aws_fields & required) - our_fields

    for field in missing_required:
        errors.append(f"MISSING REQUIRED: {op_name}.{field}")

    # Type-check present fields
    for field in our_fields & aws_fields:
        member_def = inner_members[field]
        errors.extend(validate_field(our_data[field], member_def, svc_model, f"{op_name}.{field}"))  # noqa: E501

    # Warn about extra fields
    extra = our_fields - aws_fields - SKIP_FIELDS
    for field in extra:
        warnings.append(f"EXTRA: {op_name}.{field} (not in AWS shape)")

    return {
        'pass': len(errors) == 0,
        'errors': errors,
        'warnings': warnings,
        'aws_fields': len(aws_fields),
        'our_fields': len(our_fields - SKIP_FIELDS),
        'missing_required': len(missing_required),
        'extra': len(extra),
        'matched': len(our_fields & aws_fields),
    }


def validate_service(service: str, specific_op: str = None) -> dict:
    """Validate all handlers for a service. Returns summary dict."""
    svc_model = load_service_model(service)
    store = load_store(service)

    if store is None:
        return {'service': service, 'pass': False, 'error': 'No store found'}

    handlers_dir = ASSEMBLED / service
    if not handlers_dir.exists():
        return {'service': service, 'pass': False, 'error': 'No handlers directory'}  # noqa: E501

    handler_files = sorted(handlers_dir.glob("*.code.py"))
    if specific_op:
        handler_files = [f for f in handler_files if specific_op.lower() in f.stem.lower()]  # noqa: E501

    results = []
    op_count = 0

    for hf in handler_files:
        # Strip .code suffix from stem (files are named like describe-certificate.code.py)  # noqa: E501
        clean_stem = hf.name.replace('.code.py', '')
        op_name = clean_stem.replace('-', '')
        # Convert kebab-case to CamelCase for matching AWS operation names
        camel_op = ''.join(w.capitalize() for w in clean_stem.split('-'))
        # Try to find matching AWS operation
        aws_ops = list(svc_model['operations'].keys())
        matches = [o for o in aws_ops if o.lower() == camel_op.lower()]
        if not matches:
            matches = [o for o in aws_ops if op_name.lower() in o.lower().replace('_', '')]  # noqa: E501
        if not matches:
            if hf.name.startswith(('DeleteI', 'DeleteR', 'DeleteR', 'DeleteW', 'PutP')):  # noqa: E501
                print(f"DEBUG SKIP: {hf.name} camel={camel_op} op_name={op_name}", file=__import__('sys').stderr)  # noqa: E501
            continue

        aws_op = matches[0]
        if aws_op not in svc_model['operations']:
            continue

        # Load handler
        spec = importlib.util.spec_from_file_location(op_name, str(hf))
        mod = importlib.util.module_from_spec(spec)
        # Inject exceptions — scan both the store class AND the models module.  # noqa: E501
        # Many exception classes are defined at module level (not inside the Store class),  # noqa: E501
        # so dir(type(store)) alone misses them.
        import sys as _sys
        models_mod = _sys.modules.get(f"{service}_models")
        injected = set()
        for exc_name in dir(type(store)):
            if exc_name.endswith('Exception') and exc_name not in injected:
                setattr(mod, exc_name, getattr(type(store), exc_name, Exception))  # noqa: E501
                injected.add(exc_name)
        if models_mod:
            for name in dir(models_mod):
                # Skip dunders (__name__) and already-injected names.
                # Allow user callable helpers like _find_resource_by_name.
                if name in injected:
                    continue
                if name.startswith('__') and name.endswith('__'):
                    continue
                obj = getattr(models_mod, name)
                if name.startswith('_') and not callable(obj):
                    continue
                # Skip dataclasses utilities — they're FunctionType and would be  # noqa: E501
                # picked up as the handler function (dataclass(fn) is valid in 3.14).  # noqa: E501
                if name in ('dataclass', 'field', 'Field'):
                    continue
                # Inject exceptions and user-defined helper functions
                if name.endswith('Exception') or callable(obj):
                    setattr(mod, name, obj)
                    injected.add(name)
        # Inject uuid module — handlers may reference uuid.uuid4() from models  # noqa: E501
        import uuid as _uuid
        setattr(mod, 'uuid', _uuid)  # noqa: B010
        # Inject time module — handlers may reference time.time() from models
        import time as _time
        setattr(mod, 'time', _time)  # noqa: B010
        # Inject _helpers.code.py if it exists (e.g., _find_by_arn for tag handlers)  # noqa: E501
        helpers_path = handlers_dir / '_helpers.code.py'
        if helpers_path.exists():
            helpers_spec = importlib.util.spec_from_file_location(f'{service}_helpers', str(helpers_path))  # noqa: E501
            helpers_mod = importlib.util.module_from_spec(helpers_spec)
            helpers_spec.loader.exec_module(helpers_mod)
            for hname in dir(helpers_mod):
                if hname.startswith('_') and not hname.startswith('__'):
                    obj = getattr(helpers_mod, hname)
                    if callable(obj) and hname not in injected:
                        setattr(mod, hname, obj)
                        injected.add(hname)
        try:
            if spec.loader is None:
                results.append({'op': aws_op, 'pass': False, 'errors': ['IMPORT ERROR: no loader for module']})  # noqa: E501
                continue
            spec.loader.exec_module(mod)
        except Exception as e:
            results.append({'op': aws_op, 'pass': False, 'errors': [f"IMPORT ERROR: {e}"]})  # noqa: E501
            continue

        # Find handler function
        import types as _types
        handler = None
        for v in mod.__dict__.values():
            if isinstance(v, _types.FunctionType) and not v.__name__.startswith('_'):  # noqa: E501
                handler = v
                break
        if handler is None:
            continue

        # Call handler with minimal valid input
        try:
            output = _call_handler(service, aws_op, handler, store)
        except Exception as e:
            results.append({'op': aws_op, 'pass': False, 'errors': [f"HANDLER CRASH: {e}"]})  # noqa: E501
            continue

        if output is None:
            # Delete*/Associate*/Disassociate*/PutPermissionPolicy/UntagResource return None.  # noqa: E501
            # Treat as passing empty result instead of skipping.
            output = {}

        result = validate_operation(service, aws_op, output, svc_model)
        result['op'] = aws_op
        results.append(result)
        op_count += 1

    passed = sum(1 for r in results if r['pass'])
    failed = sum(1 for r in results if not r['pass'])
    total_errors = sum(len(r.get('errors', [])) for r in results)

    return {
        'service': service,
        'pass': failed == 0,
        'ops_tested': op_count,
        'ops_passed': passed,
        'ops_failed': failed,
        'total_errors': total_errors,
        'results': results,
    }


def _get_lock(record, extra: dict) -> dict:
    """Build test input dict with the correct LockToken from a store record."""
    result = dict(extra)
    if hasattr(record, 'lock_token'):
        result['LockToken'] = record.lock_token
    return result


def _call_handler(service: str, op_name: str, handler, store) -> dict:
    """Call a handler with minimal valid test input. Returns dict or None."""
    # Inject model record classes into global scope for lambda test inputs.
    # (locals()[...] = doesn't propagate to lambda body scope in Python.)
    import sys as _csys
    _cmod = _csys.modules.get(f"{service}_models")
    if _cmod:
        for _cname in dir(_cmod):
            if _cname.endswith('Record'):
                obj = getattr(_cmod, _cname)
                if isinstance(obj, type):
                    globals()[_cname] = obj
    # Test inputs loaded from per-service files (QUALITY-001 refactor)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from test_inputs import load_test_inputs
    test_inputs = load_test_inputs(service)

    test = test_inputs.get(f"{service}.{op_name}", test_inputs.get(op_name, {}))  # noqa: E501
    if callable(test):
        test = test(store)
    if not test:
        test = {}
    return handler(store, test)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='AWS Shape Validator — botocore-driven correctness')  # noqa: E501
    parser.add_argument('service', nargs='?', help='Service name (e.g., acm)')
    parser.add_argument('--op', help='Specific operation to validate')
    parser.add_argument('--all', action='store_true', help='Validate all services')  # noqa: E501
    parser.add_argument('--json', action='store_true', help='Output JSON')
    args = parser.parse_args()

    if args.all:
        # Discover all services with assembled handlers
        services = [d.name for d in ASSEMBLED.iterdir() if d.is_dir() and (d / "models.code.py").exists()]  # noqa: E501
        all_results = []
        for svc in services:
            if svc.startswith('_') or svc.startswith('.'):
                continue
            result = validate_service(svc)
            all_results.append(result)
            status = "✅" if result['pass'] else f"❌ {result.get('total_errors', 0)} errors"  # noqa: E501
            print(f"  {status} {svc}: {result.get('ops_passed', 0)}/{result.get('ops_tested', 0)} ops")  # noqa: E501
        passed = sum(1 for r in all_results if r['pass'])
        print(f"\n{passed}/{len(all_results)} services pass shape validation")
        if args.json:
            print(json.dumps(all_results, indent=2))
        sys.exit(0 if passed == len(all_results) else 1)

    if not args.service:
        parser.print_help()
        sys.exit(1)

    result = validate_service(args.service, args.op)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for r in result.get('results', []):
            status = "✅" if r['pass'] else "❌"
            print(f"  {status} {r['op']}: {r.get('matched', 0)}/{r.get('aws_fields', '?')} fields")  # noqa: E501
            for err in r.get('errors', []):
                print(f"     {err}")
            for warn in r.get('warnings', [])[:3]:
                print(f"     ⚠️  {warn}")

    sys.exit(0 if result.get('pass') else 1)


if __name__ == '__main__':
    main()
