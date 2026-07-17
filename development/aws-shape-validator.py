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
    # Register in sys.modules so handler-loading can find exception classes
    import sys as _sys_load
    _sys_load.modules[f"{service}_models"] = mod
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
            if hf.name.startswith(('DeleteI', 'DeleteR', 'DeleteR', 'DeleteW', 'PutP')):
                print(f"DEBUG SKIP: {hf.name} camel={camel_op} op_name={op_name}", file=__import__('sys').stderr)
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
                # Inject exceptions and user-defined helper functions
                if name.endswith('Exception') or callable(obj):
                    setattr(mod, name, obj)
                    injected.add(name)
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
            # Delete*/Associate*/Disassociate*/PutPermissionPolicy/UntagResource return None.
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
        # ── wafv2 — get (lambdas create fresh resources, then look up) ──────
        'GetWebACL': lambda store: (
            store.create_web_acl(name='s-get-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            {'Name': 's-get-webacl', 'Scope': 'REGIONAL'})[1],
        'GetRuleGroup': lambda store: (
            store.create_rule_group(name='s-get-rulegroup', scope='REGIONAL',
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'},
                capacity=100),
            {'Name': 's-get-rulegroup', 'Scope': 'REGIONAL'})[1],
        'GetIPSet': lambda store: (
            store.create_ip_set(name='s-get-ipset', scope='REGIONAL',
                ip_address_version='IPV4', addresses=['10.0.0.0/16']),
            {'Name': 's-get-ipset', 'Scope': 'REGIONAL'})[1],
        'GetRegexPatternSet': lambda store: (
            store.create_regex_pattern_set(name='s-get-regexset', scope='REGIONAL',
                regular_expression_list=[{'RegexString': '^test.*'}]),
            {'Name': 's-get-regexset', 'Scope': 'REGIONAL'})[1],
        'GetLoggingConfiguration': lambda store: (
            store.put_logging_configuration({'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-get-log/abc', 'LogDestinationConfigs': ['arn:aws:firehose:us-east-1:123456789012:deliverystream/test']}),
            {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-get-log/abc'})[1],
        'GetPermissionPolicy': lambda store: (
            store.put_permission_policy('arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-get-pol/abc', '{"Version":"2012-10-17","Statement":[]}'),
            {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-get-pol/abc'})[1],
        'GetWebACLForResource': lambda store: (
            store.create_web_acl(name='s-gwfr-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            store.associate_web_acl(
                web_acl_arn=store.list_web_acls('REGIONAL')['WebACLs'][-1]['ARN'],
                resource_arn='arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/s-gwfr/abc'),
            {'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/s-gwfr/abc'})[2],
        # ── wafv2 — delete (lambdas create fresh resources, then delete) ────
        'DeleteWebACL': lambda store: (
            store.create_web_acl(name='s-del-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            _get_lock(store.get_web_acl(None, 's-del-webacl', 'REGIONAL'),
                {'Name': 's-del-webacl', 'Scope': 'REGIONAL'}))[1],
        'DeleteRuleGroup': lambda store: (
            store.create_rule_group(name='s-del-rulegroup', scope='REGIONAL',
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'},
                capacity=100),
            _get_lock(store.get_rule_group(None, 's-del-rulegroup', 'REGIONAL'),
                {'Name': 's-del-rulegroup', 'Scope': 'REGIONAL'}))[1],
        'DeleteIPSet': lambda store: (
            store.create_ip_set(name='s-del-ipset', scope='REGIONAL',
                ip_address_version='IPV4', addresses=['10.0.0.0/16']),
            _get_lock(store.get_ip_set(None, 's-del-ipset', 'REGIONAL'),
                {'Name': 's-del-ipset', 'Scope': 'REGIONAL'}))[1],
        'DeleteRegexPatternSet': lambda store: (
            store.create_regex_pattern_set(name='s-del-regexset', scope='REGIONAL',
                regular_expression_list=[{'RegexString': '^test.*'}]),
            _get_lock(store.get_regex_pattern_set(None, 's-del-regexset', 'REGIONAL'),
                {'Name': 's-del-regexset', 'Scope': 'REGIONAL'}))[1],
        'DeleteLoggingConfiguration': lambda store: (
            store.put_logging_configuration({'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-del-log/abc', 'LogDestinationConfigs': ['arn:aws:firehose:us-east-1:123456789012:deliverystream/test']}),
            {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-del-log/abc'})[1],
        'DeletePermissionPolicy': lambda store: (
            store.put_permission_policy('arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-del-pol/abc', '{"Version":"2012-10-17","Statement":[]}'),
            {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/s-del-pol/abc'})[1],
        # ── wafv2 — update (lambdas create fresh resources, then update) ────
        'UpdateWebACL': lambda store: (
            store.create_web_acl(name='s-upd-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            _get_lock(store.get_web_acl(None, 's-upd-webacl', 'REGIONAL'),
                {'Name': 's-upd-webacl', 'Scope': 'REGIONAL',
                 'DefaultAction': {'Block': {}},
                 'VisibilityConfig': {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}}))[1],
        'UpdateRuleGroup': lambda store: (
            store.create_rule_group(name='s-upd-rulegroup', scope='REGIONAL',
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'},
                capacity=100),
            _get_lock(store.get_rule_group(None, 's-upd-rulegroup', 'REGIONAL'),
                {'Name': 's-upd-rulegroup', 'Scope': 'REGIONAL',
                 'VisibilityConfig': {'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}}))[1],
        'UpdateIPSet': lambda store: (
            store.create_ip_set(name='s-upd-ipset', scope='REGIONAL',
                ip_address_version='IPV4', addresses=['10.0.0.0/16']),
            _get_lock(store.get_ip_set(None, 's-upd-ipset', 'REGIONAL'),
                {'Name': 's-upd-ipset', 'Scope': 'REGIONAL',
                 'Addresses': ['10.0.0.0/16']}))[1],
        'UpdateRegexPatternSet': lambda store: (
            store.create_regex_pattern_set(name='s-upd-regexset', scope='REGIONAL',
                regular_expression_list=[{'RegexString': '^test.*'}]),
            _get_lock(store.get_regex_pattern_set(None, 's-upd-regexset', 'REGIONAL'),
                {'Name': 's-upd-regexset', 'Scope': 'REGIONAL',
                 'RegularExpressionList': [{'RegexString': '^test.*'}]}))[1],
        # ── wafv2 — misc (self-contained lambdas) ────────────────────────────
        'AssociateWebACL': lambda store: (
            store.create_web_acl(name='s-assoc-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            {'WebACLArn': store.list_web_acls('REGIONAL')['WebACLs'][-1]['ARN'],
             'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/s-assoc/abc'})[1],
        'DisassociateWebACL': lambda store: (
            store.create_web_acl(name='s-disassoc-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            store.associate_web_acl(
                web_acl_arn=store.list_web_acls('REGIONAL')['WebACLs'][-1]['ARN'],
                resource_arn='arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/s-disassoc/abc'),
            {'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/s-disassoc/abc'})[2],
        'PutLoggingConfiguration': {'LoggingConfiguration': {
            'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test/abc123',
            'LogDestinationConfigs': ['arn:aws:firehose:us-east-1:123456789012:deliverystream/test']}},
        'PutPermissionPolicy': {'ResourceArn': 'arn:aws:wafv2:us-east-1:123456789012:regional/webacl/test-policy/abc',
                                'Policy': '{"Version":"2012-10-17","Statement":[]}'},
        # ── comprehend — create ────────────────────────────────────────────
        'CreateDataset': {'DatasetArn': 'arn:aws:comprehend:us-east-1:123456789012:dataset/test-ds', 'DatasetName': 'test-ds'},
        'CreateDocumentClassifier': {'DocumentClassifierArn': 'arn:aws:comprehend:us-east-1:123456789012:document-classifier/test-clf', 'DocumentClassifierName': 'test-clf'},
        'CreateEndpoint': {'EndpointArn': 'arn:aws:comprehend:us-east-1:123456789012:endpoint/test-ep', 'EndpointName': 'test-ep'},
        'CreateEntityRecognizer': {'EntityRecognizerArn': 'arn:aws:comprehend:us-east-1:123456789012:entity-recognizer/test-er', 'EntityRecognizerName': 'test-er'},
        'CreateFlywheel': {'FlywheelArn': 'arn:aws:comprehend:us-east-1:123456789012:flywheel/test-fw', 'FlywheelName': 'test-fw'},
        # ── comprehend — list ──────────────────────────────────────────────
        'ListDatasets': {},
        'ListDocumentClassifiers': {},
        'ListEndpoints': {},
        'ListEntityRecognizers': {},
        'ListFlywheels': {},
        # ── comprehend — delete (lambdas create prerequisite, then delete) ─
        'DeleteDataset': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:dataset/s-del-ds', 's-del-ds', 'dataset'), {'DatasetArn': 'arn:aws:comprehend:us-east-1:123456789012:dataset/s-del-ds'})[1],
        'DeleteDocumentClassifier': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:document-classifier/s-del-clf', 's-del-clf', 'document-classifier'), {'DocumentClassifierArn': 'arn:aws:comprehend:us-east-1:123456789012:document-classifier/s-del-clf'})[1],
        'DeleteEndpoint': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:endpoint/s-del-ep', 's-del-ep', 'endpoint'), {'EndpointArn': 'arn:aws:comprehend:us-east-1:123456789012:endpoint/s-del-ep'})[1],
        'DeleteEntityRecognizer': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:entity-recognizer/s-del-er', 's-del-er', 'entity-recognizer'), {'EntityRecognizerArn': 'arn:aws:comprehend:us-east-1:123456789012:entity-recognizer/s-del-er'})[1],
        'DeleteFlywheel': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:flywheel/s-del-fw', 's-del-fw', 'flywheel'), {'FlywheelArn': 'arn:aws:comprehend:us-east-1:123456789012:flywheel/s-del-fw'})[1],
        # ── comprehend — describe (lambdas create prerequisite, then describe) ─
        'DescribeDataset': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:dataset/s-desc-ds', 's-desc-ds', 'dataset'), {'DatasetArn': 'arn:aws:comprehend:us-east-1:123456789012:dataset/s-desc-ds'})[1],
        'DescribeDocumentClassifier': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:document-classifier/s-desc-clf', 's-desc-clf', 'document-classifier'), {'DocumentClassifierArn': 'arn:aws:comprehend:us-east-1:123456789012:document-classifier/s-desc-clf'})[1],
        'DescribeEndpoint': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:endpoint/s-desc-ep', 's-desc-ep', 'endpoint'), {'EndpointArn': 'arn:aws:comprehend:us-east-1:123456789012:endpoint/s-desc-ep'})[1],
        'DescribeEntityRecognizer': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:entity-recognizer/s-desc-er', 's-desc-er', 'entity-recognizer'), {'EntityRecognizerArn': 'arn:aws:comprehend:us-east-1:123456789012:entity-recognizer/s-desc-er'})[1],
        'DescribeFlywheel': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:flywheel/s-desc-fw', 's-desc-fw', 'flywheel'), {'FlywheelArn': 'arn:aws:comprehend:us-east-1:123456789012:flywheel/s-desc-fw'})[1],
        # ── comprehend — detect (synchronous text analysis) ────────────────
        'DetectDominantLanguage': {'Text': 'This is a test sentence for language detection.'},
        'DetectEntities': {'Text': 'Amazon is headquartered in Seattle. Jeff Bezos founded it.', 'LanguageCode': 'en'},
        'DetectKeyPhrases': {'Text': 'This is a test sentence for key phrase detection.', 'LanguageCode': 'en'},
        'DetectPiiEntities': {'Text': 'John Doe lives at 123 Main St. His email is john@example.com.', 'LanguageCode': 'en'},
        'DetectSentiment': {'Text': 'I love this product, it works great!', 'LanguageCode': 'en'},
        'DetectSyntax': {'Text': 'The quick brown fox jumps over the lazy dog.', 'LanguageCode': 'en'},
        'DetectTargetedSentiment': {'Text': 'I love Amazon and Microsoft but I hate their customer service.', 'LanguageCode': 'en'},
        'DetectToxicContent': {'TextSegments': [{'Text': 'This is a perfectly fine test sentence.'}]},
        # ── comprehend — classify / contains (need endpoint for classify) ──
        'ClassifyDocument': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:endpoint/s-cls-ep', 's-cls-ep', 'endpoint'), {'Text': 'This is a test document for classification.', 'EndpointArn': 'arn:aws:comprehend:us-east-1:123456789012:endpoint/s-cls-ep'})[1],
        'ContainsPiiEntities': {'Text': 'John Doe lives at 123 Main St. His email is john@example.com.', 'LanguageCode': 'en'},
        # ── comprehend — tag / untag (service-prefixed to avoid overrides) ──
        'comprehend.TagResource': {'ResourceArn': 'arn:aws:comprehend:us-east-1:123456789012:dataset/test', 'Tags': [{'Key': 'env', 'Value': 'test'}]},
        'comprehend.UntagResource': {'ResourceArn': 'arn:aws:comprehend:us-east-1:123456789012:dataset/test', 'TagKeys': ['env']},
        'comprehend.ListTagsForResource': {'ResourceArn': 'arn:aws:comprehend:us-east-1:123456789012:dataset/test'},
        # ── comprehend — update (lambdas create prerequisite, then update) ─
        'UpdateEndpoint': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:endpoint/s-upd-ep', 's-upd-ep', 'endpoint'), {'EndpointArn': 'arn:aws:comprehend:us-east-1:123456789012:endpoint/s-upd-ep', 'DesiredInferenceUnits': 1})[1],
        'UpdateFlywheel': lambda store: (store.create_entity('arn:aws:comprehend:us-east-1:123456789012:flywheel/s-upd-fw', 's-upd-fw', 'flywheel'), {'FlywheelArn': 'arn:aws:comprehend:us-east-1:123456789012:flywheel/s-upd-fw', 'DataAccessRoleArn': 'arn:aws:iam::123456789012:role/test-data-role'})[1],
        # ── eks ────────────────────────────────────────────────────────────
        'CreateCluster': {'name': 'test-cluster', 'roleArn': 'arn:aws:iam::123456789012:role/test-role'},
        'DescribeCluster': {'name': 'test-cluster'},
        'DeleteCluster': {'name': 'test-cluster'},
        'ListClusters': {},
        'ListAddons': {'clusterName': 'test-cluster'},
        'DescribeAddon': {'clusterName': 'test-cluster', 'addonName': 'test-addon'},
        'CreateAddon': {'clusterName': 'test-cluster', 'addonName': 'test-addon'},
        'DeleteAddon': {'clusterName': 'test-cluster', 'addonName': 'test-addon'},
        'UpdateAddon': {'clusterName': 'test-cluster', 'addonName': 'test-addon', 'addonVersion': 'v1.0.0'},
        'ListUpdates': {'name': 'test-cluster'},
        'DescribeUpdate': {'name': 'test-cluster', 'updateId': 'test-update'},
        'ListNodegroups': {'clusterName': 'test-cluster'},
        'DescribeNodegroup': {'clusterName': 'test-cluster', 'nodegroupName': 'test-nodegroup'},
        'CreateNodegroup': {'clusterName': 'test-cluster', 'nodegroupName': 'test-nodegroup'},
        'DeleteNodegroup': {'clusterName': 'test-cluster', 'nodegroupName': 'test-nodegroup'},
        'UpdateNodegroupConfig': {'clusterName': 'test-cluster', 'nodegroupName': 'test-nodegroup'},
        'UpdateNodegroupVersion': {'clusterName': 'test-cluster', 'nodegroupName': 'test-nodegroup'},
        'ListFargateProfiles': {'clusterName': 'test-cluster'},
        'DescribeFargateProfile': {'clusterName': 'test-cluster', 'fargateProfileName': 'test-fargate'},
        'CreateFargateProfile': {'clusterName': 'test-cluster', 'fargateProfileName': 'test-fargate', 'podExecutionRoleArn': 'arn:aws:iam::123456789012:role/test-pod-role'},
        'DeleteFargateProfile': {'clusterName': 'test-cluster', 'fargateProfileName': 'test-fargate'},
        'ListAccessEntries': {'clusterName': 'test-cluster'},
        'DescribeAccessEntry': {'clusterName': 'test-cluster', 'principalArn': 'arn:aws:iam::123456789012:role/test-principal'},
        'CreateAccessEntry': {'clusterName': 'test-cluster', 'principalArn': 'arn:aws:iam::123456789012:role/test-principal'},
        'DeleteAccessEntry': {'clusterName': 'test-cluster', 'principalArn': 'arn:aws:iam::123456789012:role/test-principal'},
        'UpdateAccessEntry': {'clusterName': 'test-cluster', 'principalArn': 'arn:aws:iam::123456789012:role/test-principal'},
        'AssociateAccessPolicy': {'clusterName': 'test-cluster', 'principalArn': 'arn:aws:iam::123456789012:role/test-principal', 'policyArn': 'arn:aws:eks::aws:cluster-access-policy/test-policy'},
        'DisassociateAccessPolicy': {'clusterName': 'test-cluster', 'principalArn': 'arn:aws:iam::123456789012:role/test-principal', 'policyArn': 'arn:aws:eks::aws:cluster-access-policy/test-policy'},
        'ListAssociatedAccessPolicies': {'clusterName': 'test-cluster', 'principalArn': 'arn:aws:iam::123456789012:role/test-principal'},
        'TagResource': {'resourceArn': 'arn:aws:eks:us-east-1:123456789012:cluster/test-cluster', 'tags': {'test': 'val'}},
        'UntagResource': {'resourceArn': 'arn:aws:eks:us-east-1:123456789012:cluster/test-cluster', 'tagKeys': ['test']},
        'ListTagsForResource': {'resourceArn': 'arn:aws:eks:us-east-1:123456789012:cluster/test-cluster'},
        'UpdateClusterConfig': {'name': 'test-cluster'},
        'UpdateClusterVersion': {'name': 'test-cluster', 'version': '1.30'},
        # ── athena — create ───────────────────────────────────────────────
        'StartQueryExecution': {'QueryString': 'SELECT 1'},
        'CreateWorkGroup': {'Name': 'test-workgroup'},
        'CreateDataCatalog': {'Name': 'test-catalog', 'Type': 'GLUE'},
        'CreateNamedQuery': {'Name': 'test-named-query', 'Database': 'test-db', 'QueryString': 'SELECT 1'},
        'CreatePreparedStatement': {'StatementName': 'test-stmt', 'WorkGroup': 'test-workgroup', 'QueryStatement': 'SELECT 2'},
        # ── athena — list ──────────────────────────────────────────────────
        'ListWorkGroups': {},
        'ListDataCatalogs': {},
        'ListDatabases': {},
        'ListNamedQueries': {},
        'ListPreparedStatements': {'WorkGroup': 'test-workgroup'},
        'ListQueryExecutions': {},
        'ListTableMetadata': {'CatalogName': 'AwsDataCatalog', 'DatabaseName': 'test-db'},
        'ListTagsForResource': {'ResourceARN': 'arn:aws:athena:us-east-1:000000000000:workgroup/test-workgroup'},
        # ── athena — get (need prior resource creation) ────────────────────
        'GetWorkGroup': lambda store: store.create_work_group(Name='test-workgroup') or {'WorkGroup': 'test-workgroup'},
        'GetQueryExecution': lambda store: {'QueryExecutionId': store.start_query_execution(QueryString='SELECT 1')['QueryExecutionId']},
        'GetNamedQuery': lambda store: {'NamedQueryId': store.create_named_query(Name='test-nq', Database='test-db', QueryString='SELECT 1')['NamedQueryId']},
        'GetPreparedStatement': lambda store: (store.create_work_group(Name='test-workgroup'), store.create_prepared_statement(StatementName='test-stmt', WorkGroup='test-workgroup', QueryStatement='SELECT 2'))[1] or {'StatementName': 'test-stmt', 'WorkGroup': 'test-workgroup'},
        'GetDataCatalog': lambda store: store.create_data_catalog(Name='test-catalog', Type='GLUE') or {'Name': 'test-catalog'},
        'GetDatabase': lambda store: {'CatalogName': 'AwsDataCatalog', 'DatabaseName': 'test-db'},
        'GetQueryResults': lambda store: {'QueryExecutionId': store.start_query_execution(QueryString='SELECT 1')['QueryExecutionId']},
        'GetTableMetadata': lambda store: {'CatalogName': 'AwsDataCatalog', 'DatabaseName': 'test-db', 'TableName': 'test-table'},
        # ── athena — delete (need prior resource creation) ─────────────────
        'DeleteWorkGroup': lambda store: store.create_work_group(Name='test-workgroup') or {'WorkGroup': 'test-workgroup'},
        'DeleteDataCatalog': lambda store: store.create_data_catalog(Name='test-catalog', Type='GLUE') or {'Name': 'test-catalog'},
        'DeleteNamedQuery': lambda store: {'NamedQueryId': store.create_named_query(Name='test-nq', Database='test-db', QueryString='SELECT 1')['NamedQueryId']},
        'DeletePreparedStatement': lambda store: (store.create_work_group(Name='test-workgroup'), store.create_prepared_statement(StatementName='test-stmt', WorkGroup='test-workgroup', QueryStatement='SELECT 2'))[1] or {'StatementName': 'test-stmt', 'WorkGroup': 'test-workgroup'},
        # ── athena — update (need prior resource creation) ─────────────────
        'UpdateWorkGroup': lambda store: store.create_work_group(Name='test-workgroup') or {'WorkGroup': 'test-workgroup', 'Description': 'updated'},
        'UpdateDataCatalog': lambda store: store.create_data_catalog(Name='test-catalog', Type='GLUE') or {'Name': 'test-catalog', 'Type': 'GLUE'},
        'UpdateNamedQuery': lambda store: {'NamedQueryId': store.create_named_query(Name='test-nq', Database='test-db', QueryString='SELECT 1')['NamedQueryId'], 'Name': 'updated-query'},
        'UpdatePreparedStatement': lambda store: (store.create_work_group(Name='test-workgroup'), store.create_prepared_statement(StatementName='test-stmt', WorkGroup='test-workgroup', QueryStatement='SELECT 2'))[1] or {'StatementName': 'test-stmt', 'WorkGroup': 'test-workgroup', 'QueryStatement': 'SELECT 99'},
        # ── athena — misc ──────────────────────────────────────────────────
        'StopQueryExecution': lambda store: {'QueryExecutionId': store.start_query_execution(QueryString='SELECT 1')['QueryExecutionId']},
        'TagResource': {'ResourceARN': 'arn:aws:athena:us-east-1:000000000000:workgroup/test-workgroup', 'Tags': [{'Key': 'env', 'Value': 'test'}]},
        'UntagResource': {'ResourceARN': 'arn:aws:athena:us-east-1:000000000000:workgroup/test-workgroup', 'TagKeys': ['env']},
        'BatchGetNamedQuery': {'NamedQueryIds': []},
        'BatchGetQueryExecution': {'QueryExecutionIds': []},
        # ── wafv2 service-prefixed (override shared keys from eks/athena) ──
        'wafv2.TagResource': lambda store: (
            store.create_web_acl(name='s-tag-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            {'ResourceARN': store.list_web_acls('REGIONAL')['WebACLs'][-1]['ARN'],
             'Tags': [{'Key': 'test', 'Value': 'val'}]})[1],
        'wafv2.UntagResource': lambda store: (
            store.create_web_acl(name='s-untag-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            {'ResourceARN': store.list_web_acls('REGIONAL')['WebACLs'][-1]['ARN'],
             'TagKeys': ['test']})[1],
        'wafv2.ListTagsForResource': lambda store: (
            store.create_web_acl(name='s-ltf-webacl', scope='REGIONAL',
                default_action={'Block': {}},
                visibility_config={'SampledRequestsEnabled': True, 'CloudWatchMetricsEnabled': True, 'MetricName': 'test'}),
            {'ResourceARN': store.list_web_acls('REGIONAL')['WebACLs'][-1]['ARN']})[1],
        # ── quicksight — create ────────────────────────────────────────────
        'CreateAnalysis': {'AwsAccountId': '123456789012', 'AnalysisId': 'test-analysis', 'Name': 'Test Analysis'},
        'CreateDashboard': {'AwsAccountId': '123456789012', 'DashboardId': 'test-dashboard', 'Name': 'Test Dashboard'},
        'CreateDataSet': {'AwsAccountId': '123456789012', 'DataSetId': 'test-dataset', 'Name': 'Test Dataset',
                          'PhysicalTableMap': {}, 'ImportMode': 'DIRECT_QUERY'},
        'CreateDataSource': {'AwsAccountId': '123456789012', 'DataSourceId': 'test-ds', 'Name': 'Test DS', 'Type': 'S3'},
        # ── quicksight — list ──────────────────────────────────────────────
        'ListAnalyses': {'AwsAccountId': '123456789012'},
        'ListDashboards': {'AwsAccountId': '123456789012'},
        'ListDataSets': {'AwsAccountId': '123456789012'},
        'ListDataSources': {'AwsAccountId': '123456789012'},
        # ── quicksight — describe (lambdas: create first, then describe) ───
        'DescribeAnalysis': lambda store: (
            store.create_analysis('123456789012', 's-desc-analysis', Name='Test'),
            {'AwsAccountId': '123456789012', 'AnalysisId': 's-desc-analysis'})[1],
        'DescribeDashboard': lambda store: (
            store.create_dashboard('123456789012', 's-desc-dashboard', Name='Test'),
            {'AwsAccountId': '123456789012', 'DashboardId': 's-desc-dashboard'})[1],
        'DescribeDataSet': lambda store: (
            store.create_dataset('123456789012', 's-desc-dataset', Name='Test',
                                 PhysicalTableMap={}, ImportMode='DIRECT_QUERY'),
            {'AwsAccountId': '123456789012', 'DataSetId': 's-desc-dataset'})[1],
        'DescribeDataSource': lambda store: (
            store.create_datasource('123456789012', 's-desc-ds', Name='Test', Type='S3'),
            {'AwsAccountId': '123456789012', 'DataSourceId': 's-desc-ds'})[1],
        # ── quicksight — delete (lambdas: create first, then delete) ───────
        'DeleteAnalysis': lambda store: (
            store.create_analysis('123456789012', 's-del-analysis', Name='Test'),
            {'AwsAccountId': '123456789012', 'AnalysisId': 's-del-analysis'})[1],
        'DeleteDashboard': lambda store: (
            store.create_dashboard('123456789012', 's-del-dashboard', Name='Test'),
            {'AwsAccountId': '123456789012', 'DashboardId': 's-del-dashboard'})[1],
        'DeleteDataSet': lambda store: (
            store.create_dataset('123456789012', 's-del-dataset', Name='Test',
                                 PhysicalTableMap={}, ImportMode='DIRECT_QUERY'),
            {'AwsAccountId': '123456789012', 'DataSetId': 's-del-dataset'})[1],
        'DeleteDataSource': lambda store: (
            store.create_datasource('123456789012', 's-del-ds', Name='Test', Type='S3'),
            {'AwsAccountId': '123456789012', 'DataSourceId': 's-del-ds'})[1],
        # ── quicksight — update (lambdas: create first, then update) ───────
        'UpdateAnalysis': lambda store: (
            store.create_analysis('123456789012', 's-upd-analysis', Name='Test'),
            {'AwsAccountId': '123456789012', 'AnalysisId': 's-upd-analysis', 'Name': 'Updated Analysis'})[1],
        'UpdateDashboard': lambda store: (
            store.create_dashboard('123456789012', 's-upd-dashboard', Name='Test'),
            {'AwsAccountId': '123456789012', 'DashboardId': 's-upd-dashboard', 'Name': 'Updated Dashboard'})[1],
        'UpdateDataSet': lambda store: (
            store.create_dataset('123456789012', 's-upd-dataset', Name='Test',
                                 PhysicalTableMap={}, ImportMode='DIRECT_QUERY'),
            {'AwsAccountId': '123456789012', 'DataSetId': 's-upd-dataset', 'Name': 'Updated Dataset',
             'PhysicalTableMap': {}, 'ImportMode': 'DIRECT_QUERY'})[1],
        'UpdateDataSource': lambda store: (
            store.create_datasource('123456789012', 's-upd-ds', Name='Test', Type='S3'),
            {'AwsAccountId': '123456789012', 'DataSourceId': 's-upd-ds', 'Name': 'Updated DS'})[1],
        # ── quicksight — tag/untag (lambdas: create resource first, then ARN) ─
        'quicksight.TagResource': lambda store: (
            store.create_analysis('123456789012', 's-tag-analysis', Name='Test'),
            {'ResourceArn': store.analyses('123456789012')[-1].Arn,
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[1],
        'quicksight.UntagResource': lambda store: (
            store.create_analysis('123456789012', 's-untag-analysis', Name='Test'),
            {'ResourceArn': store.analyses('123456789012')[-1].Arn,
             'TagKeys': ['env']})[1],
        'quicksight.ListTagsForResource': lambda store: (
            store.create_analysis('123456789012', 's-ltfr-analysis', Name='Test'),
            {'ResourceArn': store.analyses('123456789012')[-1].Arn})[1],
        # ── neptune — create ───────────────────────────────────────────────
        'CreateDBCluster': {'DBClusterIdentifier': 'neptune-test-cluster', 'Engine': 'neptune'},
        'CreateDBClusterParameterGroup': {'DBClusterParameterGroupName': 'neptune-test-cpg',
                                          'DBParameterGroupFamily': 'neptune1', 'Description': 'test'},
        'CreateDBClusterSnapshot': lambda store: (
            store.create_cluster('s-snap-cluster', 'neptune'),
            {'DBClusterSnapshotIdentifier': 's-test-snapshot',
             'DBClusterIdentifier': 's-snap-cluster'})[1],
        'CreateDBInstance': {'DBInstanceIdentifier': 'neptune-test-instance',
                             'DBInstanceClass': 'db.r5.large', 'Engine': 'neptune',
                             'DBClusterIdentifier': 'neptune-test-cluster'},
        'CreateDBParameterGroup': {'DBParameterGroupName': 'neptune-test-pg',
                                   'DBParameterGroupFamily': 'neptune1', 'Description': 'test'},
        'CreateDBSubnetGroup': {'DBSubnetGroupName': 'neptune-test-sg',
                                'DBSubnetGroupDescription': 'test subnet group',
                                'SubnetIds': ['subnet-a', 'subnet-b']},
        # ── neptune — list ──────────────────────────────────────────────────
        'DescribeDBClusters': {},
        'DescribeDBInstances': {},
        'DescribeDBClusterParameterGroups': {},
        'DescribeDBClusterSnapshots': {},
        'DescribeDBEngineVersions': {},
        'DescribeDBParameterGroups': {},
        'DescribeDBSubnetGroups': {},
        # ── neptune — describe (lambdas: create prerequisite, then describe) ─
        'DescribeDBClusterParameters': lambda store: (
            store.create_cluster_param_group('s-desc-cpgp', 'neptune1', 'test'),
            {'DBClusterParameterGroupName': 's-desc-cpgp'})[1],
        'DescribeDBParameters': lambda store: (
            store.create_param_group('s-desc-pgp', 'neptune1', 'test'),
            {'DBParameterGroupName': 's-desc-pgp'})[1],
        # ── neptune — delete (lambdas: create first, then delete) ───────────
        'DeleteDBCluster': lambda store: (
            store.create_cluster('s-del-cluster', 'neptune', status='available'),
            {'DBClusterIdentifier': 's-del-cluster', 'SkipFinalSnapshot': True})[1],
        'DeleteDBClusterParameterGroup': lambda store: (
            store.create_cluster_param_group('s-del-cpg', 'neptune1', 'test'),
            {'DBClusterParameterGroupName': 's-del-cpg'})[1],
        'DeleteDBClusterSnapshot': lambda store: (
            store.create_cluster('s-del-snap-cluster', 'neptune', status='available'),
            store.create_snapshot('s-del-snapshot', 's-del-snap-cluster'),
            {'DBClusterSnapshotIdentifier': 's-del-snapshot'})[2],
        'DeleteDBInstance': lambda store: (
            store.create_cluster('s-del-inst-cluster', 'neptune', status='available'),
            store.create_instance('s-del-instance', 'db.r5.large', 'neptune', 's-del-inst-cluster', status='available'),
            {'DBInstanceIdentifier': 's-del-instance', 'SkipFinalSnapshot': True})[2],
        'DeleteDBParameterGroup': lambda store: (
            store.create_param_group('s-del-pg', 'neptune1', 'test'),
            {'DBParameterGroupName': 's-del-pg'})[1],
        'DeleteDBSubnetGroup': lambda store: (
            store.create_subnet_group('s-del-sg', 'test', ['subnet-a']),
            {'DBSubnetGroupName': 's-del-sg'})[1],
        # ── neptune — modify (lambdas: create first, then modify) ───────────
        'ModifyDBCluster': lambda store: (
            store.create_cluster('s-mod-cluster', 'neptune', status='available'),
            {'DBClusterIdentifier': 's-mod-cluster', 'Port': 8182})[1],
        'ModifyDBClusterParameterGroup': lambda store: (
            store.create_cluster_param_group('s-mod-cpg', 'neptune1', 'test'),
            {'DBClusterParameterGroupName': 's-mod-cpg'})[1],
        'ModifyDBInstance': lambda store: (
            store.create_cluster('s-mod-inst-cluster', 'neptune', status='available'),
            store.create_instance('s-mod-instance', 'db.r5.large', 'neptune', 's-mod-inst-cluster'),
            {'DBInstanceIdentifier': 's-mod-instance', 'DBInstanceClass': 'db.r5.large'})[2],
        'ModifyDBParameterGroup': lambda store: (
            store.create_param_group('s-mod-pg', 'neptune1', 'test'),
            {'DBParameterGroupName': 's-mod-pg'})[1],
        # ── neptune — reboot ─────────────────────────────────────────────────
        'RebootDBInstance': lambda store: (
            store.create_cluster('s-reboot-cluster', 'neptune', status='available'),
            store.create_instance('s-reboot-instance', 'db.r5.large', 'neptune', 's-reboot-cluster'),
            {'DBInstanceIdentifier': 's-reboot-instance'})[2],
        # ── neptune — tag / untag (service-prefixed; lambdas create resource first) ─
        'neptune.AddTagsToResource': lambda store: (
            store.create_cluster('s-tag-cluster', 'neptune', status='available'),
            {'ResourceName': 's-tag-cluster',
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[1],
        'neptune.RemoveTagsFromResource': lambda store: (
            store.create_cluster('s-untag-cluster', 'neptune', status='available'),
            {'ResourceName': 's-untag-cluster',
             'TagKeys': ['env']})[1],
        'neptune.ListTagsForResource': lambda store: (
            store.create_cluster('s-ltf-cluster', 'neptune', status='available'),
            {'ResourceName': 's-ltf-cluster'})[1],
        # ── lexv2-models — create ────────────────────────────────────────────
        'CreateBot': {'botName': 'test-bot', 'roleArn': 'arn:aws:iam::123456789012:role/test',
                      'dataPrivacy': {'childDirected': False}, 'idleSessionTTLInSeconds': 300},
        'CreateBotAlias': lambda store: (
            store.create_bot(botName='balias-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            {'botAliasName': 'test-alias', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT'})[2],
        'CreateIntent': lambda store: (
            store.create_bot(botName='intent-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            {'intentName': 'TestIntent', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US',
             'sampleUtterances': [{'utterance': 'hello'}]})[2],
        'CreateSlotType': lambda store: (
            store.create_bot(botName='slot-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            {'slotTypeName': 'TestSlotType', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US'})[2],
        # ── lexv2-models — list ──────────────────────────────────────────────
        'ListBots': {},
        'ListBotAliases': lambda store: (
            store.create_bot(botName='lba-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_bot_alias(botAliasName='lba-alias', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT'),
            {'botId': store.list_bots()[0]['botId']})[3],
        'ListIntents': lambda store: (
            store.create_bot(botName='li-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_intent(intentName='li-intent', botId=store.list_bots()[0]['botId'],
                                botVersion='DRAFT', localeId='en_US',
                                sampleUtterances=[{'utterance': 'hello'}]),
            {'botId': store.list_bots()[0]['botId'], 'botVersion': 'DRAFT',
             'localeId': 'en_US'})[3],
        'ListSlotTypes': lambda store: (
            store.create_bot(botName='ls-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_slot_type(slotTypeName='ls-slot', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT', localeId='en_US'),
            {'botId': store.list_bots()[0]['botId'], 'botVersion': 'DRAFT',
             'localeId': 'en_US'})[3],
        # ── lexv2-models — describe (lambdas: create prerequisite, then describe) ─
        'DescribeBot': lambda store: (
            store.create_bot(botName='desc-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            {'botId': store.list_bots()[0]['botId']})[2],
        'DescribeBotAlias': lambda store: (
            store.create_bot(botName='dba-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_bot_alias(botAliasName='dba-alias', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT'),
            {'botId': store.list_bots()[0]['botId'],
             'botAliasName': 'dba-alias'})[3],
        'DescribeIntent': lambda store: (
            store.create_bot(botName='di-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_intent(intentName='di-intent', botId=store.list_bots()[0]['botId'],
                                botVersion='DRAFT', localeId='en_US',
                                sampleUtterances=[{'utterance': 'hello'}]),
            {'intentName': 'di-intent', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US'})[3],
        'DescribeSlotType': lambda store: (
            store.create_bot(botName='ds-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_slot_type(slotTypeName='ds-slot', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT', localeId='en_US'),
            {'slotTypeName': 'ds-slot', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US'})[3],
        # ── lexv2-models — delete (lambdas: create first, then delete) ────────
        'DeleteBot': lambda store: (
            store.create_bot(botName='del-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            {'botId': store.list_bots()[0]['botId']})[2],
        'DeleteBotAlias': lambda store: (
            store.create_bot(botName='delba-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_bot_alias(botAliasName='delba-alias', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT'),
            {'botId': store.list_bots()[0]['botId'],
             'botAliasName': 'delba-alias'})[3],
        'DeleteIntent': lambda store: (
            store.create_bot(botName='deli-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_intent(intentName='deli-intent', botId=store.list_bots()[0]['botId'],
                                botVersion='DRAFT', localeId='en_US',
                                sampleUtterances=[{'utterance': 'hello'}]),
            {'intentName': 'deli-intent', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US'})[3],
        'DeleteSlotType': lambda store: (
            store.create_bot(botName='dels-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_slot_type(slotTypeName='dels-slot', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT', localeId='en_US'),
            {'slotTypeName': 'dels-slot', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US'})[3],
        # ── lexv2-models — update (lambdas: create first, then update) ────────
        'UpdateBot': lambda store: (
            store.create_bot(botName='upd-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            {'botId': store.list_bots()[0]['botId'], 'botName': 'upd-bot',
             'roleArn': 'arn:aws:iam::123456789012:role/test',
             'dataPrivacy': {'childDirected': False},
             'idleSessionTTLInSeconds': 600})[2],
        'UpdateBotAlias': lambda store: (
            store.create_bot(botName='uba-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_bot_alias(botAliasName='uba-alias', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT'),
            {'botAliasName': 'uba-alias', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT'})[3],
        'UpdateIntent': lambda store: (
            store.create_bot(botName='ui-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_intent(intentName='ui-intent', botId=store.list_bots()[0]['botId'],
                                botVersion='DRAFT', localeId='en_US',
                                sampleUtterances=[{'utterance': 'hello'}]),
            {'intentName': 'ui-intent', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US',
             'sampleUtterances': [{'utterance': 'hi there'}]})[3],
        'UpdateSlotType': lambda store: (
            store.create_bot(botName='us-bot', roleArn='arn:aws:iam::123456789012:role/test',
                             dataPrivacy={'childDirected': False}, idleSessionTTLInSeconds=300),
            store.list_bots(),
            store.create_slot_type(slotTypeName='us-slot', botId=store.list_bots()[0]['botId'],
                                   botVersion='DRAFT', localeId='en_US'),
            {'slotTypeName': 'us-slot', 'botId': store.list_bots()[0]['botId'],
             'botVersion': 'DRAFT', 'localeId': 'en_US'})[3],
        # ── opensearchserverless — policy list ──────────────────────────────
        'ListAccessPolicies': {'type': 'data'},
        'ListLifecyclePolicies': {'type': 'retention'},
        'ListSecurityPolicies': {'type': 'encryption'},
        # ── opensearchserverless — get/delete/update policies (lambdas) ──────
        'GetAccessPolicy': lambda store: (
            store.create_access_policy(type='data', name='s-get-ap',
                                       policy='{"Rules":[{"ResourceType":"collection"}]}'),
            {'type': 'data', 'name': 's-get-ap'})[1],
        'GetSecurityPolicy': lambda store: (
            store.create_security_policy(type='encryption', name='s-get-sp',
                                         policy='{"Rules":[{"ResourceType":"collection"}]}'),
            {'type': 'encryption', 'name': 's-get-sp'})[1],
        'DeleteAccessPolicy': lambda store: (
            store.create_access_policy(type='data', name='s-del-ap',
                                       policy='{"Rules":[{"ResourceType":"collection"}]}'),
            {'type': 'data', 'name': 's-del-ap'})[1],
        'DeleteLifecyclePolicy': lambda store: (
            store.create_lifecycle_policy(type='retention', name='s-del-lp',
                                          policy='{"Rules":[{"ResourceType":"index"}]}'),
            {'type': 'retention', 'name': 's-del-lp'})[1],
        'DeleteSecurityPolicy': lambda store: (
            store.create_security_policy(type='encryption', name='s-del-sp',
                                         policy='{"Rules":[{"ResourceType":"collection"}]}'),
            {'type': 'encryption', 'name': 's-del-sp'})[1],
        'UpdateAccessPolicy': lambda store: (
            store.create_access_policy(type='data', name='s-upd-ap',
                                       policy='{"Rules":[{"ResourceType":"collection"}]}'),
            {'type': 'data', 'name': 's-upd-ap', 'policyVersion': '1',
             'policy': '{"Rules":[{"ResourceType":"collection"}],"Description":"updated"}'})[1],
        'UpdateLifecyclePolicy': lambda store: (
            store.create_lifecycle_policy(type='retention', name='s-upd-lp',
                                          policy='{"Rules":[{"ResourceType":"index"}]}'),
            {'type': 'retention', 'name': 's-upd-lp', 'policyVersion': '1',
             'policy': '{"Rules":[{"ResourceType":"index"}],"Description":"updated"}'})[1],
        'UpdateSecurityPolicy': lambda store: (
            store.create_security_policy(type='encryption', name='s-upd-sp',
                                         policy='{"Rules":[{"ResourceType":"collection"}]}'),
            {'type': 'encryption', 'name': 's-upd-sp', 'policyVersion': '1',
             'policy': '{"Rules":[{"ResourceType":"collection"}],"Description":"updated"}'})[1],
        # ── opensearchserverless — collection delete/update (lambdas) ────────
        'DeleteCollection': lambda store: (
            store.create_collection(name='s-del-col', id='s-del-col', type='SEARCH'),
            {'id': 's-del-col'})[1],
        'UpdateCollection': lambda store: (
            store.create_collection(name='s-upd-col', id='s-upd-col', type='SEARCH'),
            {'id': 's-upd-col', 'description': 'updated description'})[1],
        # ── opensearchserverless — tags (lambdas: create collection for ARN) ──
        'TagResource': lambda store: (
            store.create_collection(name='s-tag-col', id='s-tag-col', type='SEARCH'),
            {'resourceArn': 'arn:aws:aoss:us-east-1:000000000000:collection/s-tag-col',
             'tags': [{'key': 'env', 'value': 'test'}]})[1],
        'UntagResource': lambda store: (
            store.create_collection(name='s-untag-col', id='s-untag-col', type='SEARCH'),
            {'resourceArn': 'arn:aws:aoss:us-east-1:000000000000:collection/s-untag-col',
             'tagKeys': ['env']})[1],
        'ListTagsForResource': lambda store: (
            store.create_collection(name='s-ltf-col', id='s-ltf-col', type='SEARCH'),
            {'resourceArn': 'arn:aws:aoss:us-east-1:000000000000:collection/s-ltf-col'})[1],
    }

    test = test_inputs.get(f"{service}.{op_name}", test_inputs.get(op_name, {}))
    if callable(test):
        test = test(store)
    if not test:
        test = {}
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
