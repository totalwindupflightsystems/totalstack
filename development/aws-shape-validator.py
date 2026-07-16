#!/usr/bin/env python3
"""
AWS Shape Validator — botocore-driven correctness gate.
Compares TotalStack handler output against AWS service-2.json shapes.
Every response field is checked: required, optional, types, enums.

Usage:
  python3 aws-shape-validator.py <service>          # validate all handlers
  python3 aws-shape-validator.py <service> --op DescribeCertificate  # single op
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
    spec = importlib.util.spec_from_file_location(f"{service}_models", str(models_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Register in sys.modules so the handler-loading loop can find exceptions
    import sys as _sys
    _sys.modules[f"{service}_models"] = mod
    # Find the Store class (convention: <Service>Store)
    for name, obj in mod.__dict__.items():
        if name.endswith('Store') and isinstance(obj, type):
            return obj()
    return None


def get_shape_members(svc_model: dict, shape_name: str) -> dict:
    """Get all member fields of a shape, recursively unwrapping."""
    shape = svc_model['shapes'].get(shape_name, {})
    if 'members' in shape:
        return dict(shape['members'])
    return {}


def validate_field(value, member_def: dict, svc_model: dict, path: str) -> list:
    """Validate a single field value against its shape definition. Returns error list."""
    errors = []
    shape_name = member_def.get('shape', '')
    shape = svc_model['shapes'].get(shape_name, {})

    if value is None:
        return errors  # optional field, no value

    shape_type = shape.get('type', '')

    if shape_type == 'string':
        if not isinstance(value, str):
            errors.append(f"{path}: expected string, got {type(value).__name__}")
    elif shape_type == 'integer' or shape_type == 'long':
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"{path}: expected integer, got {type(value).__name__}")
    elif shape_type == 'boolean':
        if not isinstance(value, bool):
            errors.append(f"{path}: expected boolean, got {type(value).__name__}")
    elif shape_type == 'timestamp':
        if not isinstance(value, (int, float, str)):
            errors.append(f"{path}: expected timestamp, got {type(value).__name__}")
    elif shape_type == 'list':
        if not isinstance(value, list):
            errors.append(f"{path}: expected list, got {type(value).__name__}")
        elif 'member' in shape:
            member_def = shape['member']
            for i, item in enumerate(value):
                errors.extend(validate_field(item, member_def, svc_model, f"{path}[{i}]"))
    elif shape_type == 'structure':
        if not isinstance(value, dict):
            errors.append(f"{path}: expected dict/structure, got {type(value).__name__}")
    elif shape_type == 'map':
        if not isinstance(value, dict):
            errors.append(f"{path}: expected dict/map, got {type(value).__name__}")

    # Check enum values
    if 'enum' in shape and value not in shape['enum']:
        errors.append(f"{path}: '{value}' not in enum {shape['enum'][:5]}...")

    return errors


def validate_operation(service: str, op_name: str, our_output: dict, svc_model: dict) -> dict:
    """Validate one operation's output against AWS shape. Returns {pass: bool, errors: [], warnings: []}."""
    if op_name not in svc_model['operations']:
        return {'pass': True, 'errors': [], 'warnings': [f"op {op_name} not in service model"]}

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
        errors.extend(validate_field(our_data[field], member_def, svc_model, f"{op_name}.{field}"))

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
        return {'service': service, 'pass': False, 'error': 'No handlers directory'}

    handler_files = sorted(handlers_dir.glob("*.code.py"))
    if specific_op:
        handler_files = [f for f in handler_files if specific_op.lower() in f.stem.lower()]

    results = []
    op_count = 0

    for hf in handler_files:
        # Strip .code suffix from stem (files are named like describe-certificate.code.py)
        clean_stem = hf.name.replace('.code.py', '')
        op_name = clean_stem.replace('-', '')
        # Convert kebab-case to CamelCase for matching AWS operation names
        camel_op = ''.join(w.capitalize() for w in clean_stem.split('-'))
        # Try to find matching AWS operation
        aws_ops = list(svc_model['operations'].keys())
        matches = [o for o in aws_ops if o.lower() == camel_op.lower()]
        if not matches:
            matches = [o for o in aws_ops if op_name.lower() in o.lower().replace('_', '')]
        if not matches:
            continue

        aws_op = matches[0]
        if aws_op not in svc_model['operations']:
            continue

        # Load handler
        spec = importlib.util.spec_from_file_location(op_name, str(hf))
        mod = importlib.util.module_from_spec(spec)
        # Inject exceptions — scan both the store class AND the models module.
        # Many exception classes are defined at module level (not inside the Store class),
        # so dir(type(store)) alone misses them.
        import sys as _sys
        models_mod = _sys.modules.get(f"{service}_models")
        injected = set()
        for exc_name in dir(type(store)):
            if exc_name.endswith('Exception') and exc_name not in injected:
                setattr(mod, exc_name, getattr(type(store), exc_name, Exception))
                injected.add(exc_name)
        if models_mod:
            for exc_name in dir(models_mod):
                if exc_name.endswith('Exception') and exc_name not in injected:
                    setattr(mod, exc_name, getattr(models_mod, exc_name, Exception))
                    injected.add(exc_name)
        try:
            if spec.loader is None:
                results.append({'op': aws_op, 'pass': False, 'errors': ['IMPORT ERROR: no loader for module']})
                continue
            spec.loader.exec_module(mod)
        except Exception as e:
            results.append({'op': aws_op, 'pass': False, 'errors': [f"IMPORT ERROR: {e}"]})
            continue

        # Find handler function
        import types as _types
        handler = None
        for v in mod.__dict__.values():
            if isinstance(v, _types.FunctionType) and not v.__name__.startswith('_'):
                handler = v
                break
        if handler is None:
            continue

        # Call handler with minimal valid input
        try:
            output = _call_handler(service, aws_op, handler, store)
        except Exception as e:
            results.append({'op': aws_op, 'pass': False, 'errors': [f"HANDLER CRASH: {e}"]})
            continue

        if output is None:
            continue

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


def _ensure_create(store, method_name, name, scope, *args, **kwargs):
    """Create a resource if it doesn't already exist (idempotent)."""
    # Check if resource exists by listing
    list_methods = {
        'create_web_acl': 'web_acls',
        'create_ip_set': 'ip_sets',
        'create_regex_pattern_set': 'regex_pattern_sets',
        'create_rule_group': 'rule_groups',
    }
    store_attr = list_methods.get(method_name)
    if store_attr:
        for record in getattr(store, store_attr).values():
            if record.name == name:
                return  # already exists
    method = getattr(store, method_name)
    method(name=name, scope=scope, *args, **kwargs)


def _call_handler(service: str, op_name: str, handler, store) -> dict:
    """Call a handler with minimal valid test input. Returns dict or None."""
    # Minimal test inputs per service/operation — extend as needed
    test_inputs = {
        # ── acm ────────────────────────────────────────────────────────────
        'RequestCertificate': {'DomainName': 'shape-test.example.com'},
        'DescribeCertificate': lambda store: {'CertificateArn': store.request_certificate(DomainName='test.com')['CertificateArn']},
        'ListCertificates': {},
        'DeleteCertificate': lambda store: {'CertificateArn': store.request_certificate(DomainName='del-test.com')['CertificateArn']},
        'GetCertificate': lambda store: {'CertificateArn': store.import_certificate(Certificate="test", PrivateKey="test")['CertificateArn']},
        'ImportCertificate': {'Certificate': 'test-cert', 'PrivateKey': 'test-key'},
        'GetAccountConfiguration': {},
        'PutAccountConfiguration': {'ExpiryEvents': {'DaysBeforeExpiry': 30}},
        'AddTagsToCertificate': lambda store: {'CertificateArn': store.request_certificate(DomainName='tag-test.com')['CertificateArn'], 'Tags': [{'Key': 'test', 'Value': 'val'}]},
        'ListTagsForCertificate': lambda store: {'CertificateArn': store.request_certificate(DomainName='lt-test.com')['CertificateArn']},
        'RemoveTagsFromCertificate': lambda store: {'CertificateArn': store.request_certificate(DomainName='rt-test.com')['CertificateArn'], 'Tags': [{'Key': 'test', 'Value': 'val'}]},
        'RenewCertificate': lambda store: {'CertificateArn': store.import_certificate(Certificate="test", PrivateKey="test")['CertificateArn']},
        'RevokeCertificate': lambda store: {'CertificateArn': store.import_certificate(Certificate="test", PrivateKey="test")['CertificateArn'], 'RevocationReason': 'UNSPECIFIED'},
        'UpdateCertificateOptions': lambda store: {'CertificateArn': store.import_certificate(Certificate="test", PrivateKey="test")['CertificateArn'], 'Options': {'CertificateTransparencyLoggingPreference': 'ENABLED'}},
        # ── wafv2 — create ─────────────────────────────────────────────────
        'CreateWebACL': {'Name': 'test-webacl', 'Scope': 'REGIONAL',
                         'DefaultAction': {'Block': {}},
                         'VisibilityConfig': {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}},
        'CreateRuleGroup': {'Name': 'test-rulegroup', 'Scope': 'REGIONAL',
                            'VisibilityConfig': {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'},
                            'Capacity': 100},
        'CreateIPSet': {'Name': 'test-ipset', 'Scope': 'REGIONAL',
                        'IPAddressVersion': 'IPV4', 'Addresses': ['10.0.0.0/16']},
        'CreateRegexPatternSet': {'Name': 'test-regexset', 'Scope': 'REGIONAL',
                                  'RegularExpressionList': [{'RegexString': '^test.*'}]},
        # ── wafv2 — list ───────────────────────────────────────────────────
        'ListWebACLs': {'Scope': 'REGIONAL'},
        'ListRuleGroups': {'Scope': 'REGIONAL'},
        'ListIPSets': {'Scope': 'REGIONAL'},
        'ListRegexPatternSets': {'Scope': 'REGIONAL'},
        'ListLoggingConfigurations': {'Scope': 'REGIONAL'},
        'ListTagsForResource': {'ResourceARN': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123'},
        'ListResourcesForWebACL': {'WebACLArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123'},
        # ── wafv2 — get (name-based lookup — no Id needed, resource created by Create*) ──
        'GetWebACL': {'Scope': 'REGIONAL', 'Name': 'test-webacl'},
        'GetRuleGroup': {'Scope': 'REGIONAL', 'Name': 'test-rulegroup'},
        'GetIPSet': {'Scope': 'REGIONAL', 'Name': 'test-ipset'},
        'GetRegexPatternSet': {'Scope': 'REGIONAL', 'Name': 'test-regexset'},
        'GetLoggingConfiguration': lambda store: {'ResourceArn': list(store.logging_configs.keys())[0]} if store.logging_configs else {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123'},
        'GetPermissionPolicy': lambda store: {'ResourceArn': list(store.permission_policies.keys())[0]} if store.permission_policies else {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123'},
        'GetWebACLForResource': lambda store: {'ResourceArn': list(store.webacl_associations.keys())[0]} if store.webacl_associations else {'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-alb/abc123'},
        # ── wafv2 — update (need correct lock_token from store) ────────────
        'UpdateWebACL': lambda store: _get_lock(store.get_web_acl(None, 'test-webacl', 'REGIONAL'), {'Name': 'test-webacl', 'Scope': 'REGIONAL', 'DefaultAction': {'Block': {}}, 'VisibilityConfig': {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}}),
        'UpdateRuleGroup': lambda store: _get_lock(store.get_rule_group(None, 'test-rulegroup', 'REGIONAL'), {'Name': 'test-rulegroup', 'Scope': 'REGIONAL', 'VisibilityConfig': {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}}),
        'UpdateIPSet': lambda store: _get_lock(store.get_ip_set(None, 'test-ipset', 'REGIONAL'), {'Name': 'test-ipset', 'Scope': 'REGIONAL', 'Addresses': ['10.0.0.0/16']}),
        'UpdateRegexPatternSet': lambda store: _get_lock(store.get_regex_pattern_set(None, 'test-regexset', 'REGIONAL'), {'Name': 'test-regexset', 'Scope': 'REGIONAL', 'RegularExpressionList': [{'RegexString': '^test.*'}]}),
        # ── wafv2 — delete (need correct lock_token from store) ────────────
        'DeleteWebACL': lambda store: _get_lock(store.get_web_acl(None, 'test-webacl', 'REGIONAL'), {'Name': 'test-webacl', 'Scope': 'REGIONAL'}),
        'DeleteRuleGroup': lambda store: _get_lock(store.get_rule_group(None, 'test-rulegroup', 'REGIONAL'), {'Name': 'test-rulegroup', 'Scope': 'REGIONAL'}),
        'DeleteIPSet': lambda store: _get_lock(store.get_ip_set(None, 'test-ipset', 'REGIONAL'), {'Name': 'test-ipset', 'Scope': 'REGIONAL'}),
        'DeleteRegexPatternSet': lambda store: _get_lock(store.get_regex_pattern_set(None, 'test-regexset', 'REGIONAL'), {'Name': 'test-regexset', 'Scope': 'REGIONAL'}),
        'DeleteLoggingConfiguration': lambda store: {'ResourceArn': list(store.logging_configs.keys())[0]} if store.logging_configs else {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123'},
        'DeletePermissionPolicy': lambda store: {'ResourceArn': list(store.permission_policies.keys())[0]} if store.permission_policies else {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123'},
        # ── wafv2 — misc (need prior resource creation) ────────────────────
        'AssociateWebACL': lambda store: _ensure_create(store, 'create_web_acl', 'test-webacl', 'REGIONAL', {'Block': {}}, {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}) or {'WebACLArn': store.list_web_acls('REGIONAL')['WebACLs'][0]['ARN'], 'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-alb/abc123'},
        'DisassociateWebACL': lambda store: {'ResourceArn': list(store.webacl_associations.keys())[0]} if store.webacl_associations else {'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/test-alb/abc123'},
        'TagResource': lambda store: {'ResourceARN': store.list_web_acls('REGIONAL')['WebACLs'][0]['ARN'], 'Tags': [{'Key': 'test', 'Value': 'val'}]} if store.list_web_acls('REGIONAL')['WebACLs'] else {'ResourceARN': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123', 'Tags': [{'Key': 'test', 'Value': 'val'}]},
        'UntagResource': lambda store: {'ResourceARN': store.list_web_acls('REGIONAL')['WebACLs'][0]['ARN'], 'TagKeys': ['test']} if store.list_web_acls('REGIONAL')['WebACLs'] else {'ResourceARN': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123', 'TagKeys': ['test']},
        'ListTagsForResource': lambda store: {'ResourceARN': store.list_web_acls('REGIONAL')['WebACLs'][0]['ARN']} if store.list_web_acls('REGIONAL')['WebACLs'] else {'ResourceARN': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123'},
        'PutLoggingConfiguration': {'LoggingConfiguration': {
            'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123',
            'LogDestinationConfigs': ['arn:aws:firehose:us-east-1:123456789012:deliverystream/test']}},
        'PutPermissionPolicy': {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123',
                                'Policy': '{"Version":"2012-10-17","Statement":[]}'},
    }

    test = test_inputs.get(op_name, {})
    if callable(test):
        test = test(store)
    return handler(store, test)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='AWS Shape Validator — botocore-driven correctness')
    parser.add_argument('service', nargs='?', help='Service name (e.g., acm)')
    parser.add_argument('--op', help='Specific operation to validate')
    parser.add_argument('--all', action='store_true', help='Validate all services')
    parser.add_argument('--json', action='store_true', help='Output JSON')
    args = parser.parse_args()

    if args.all:
        # Discover all services with assembled handlers
        services = [d.name for d in ASSEMBLED.iterdir() if d.is_dir() and (d / "models.code.py").exists()]
        all_results = []
        for svc in services:
            if svc.startswith('_') or svc.startswith('.'):
                continue
            result = validate_service(svc)
            all_results.append(result)
            status = "✅" if result['pass'] else f"❌ {result.get('total_errors', 0)} errors"
            print(f"  {status} {svc}: {result.get('ops_passed', 0)}/{result.get('ops_tested', 0)} ops")
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
            print(f"  {status} {r['op']}: {r.get('matched', 0)}/{r.get('aws_fields', '?')} fields")
            for err in r.get('errors', []):
                print(f"     {err}")
            for warn in r.get('warnings', [])[:3]:
                print(f"     ⚠️  {warn}")

    sys.exit(0 if result.get('pass') else 1)


if __name__ == '__main__':
    main()
