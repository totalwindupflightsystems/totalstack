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
                # Skip dataclasses utilities — they're FunctionType and would be
                # picked up as the handler function (dataclass(fn) is valid in 3.14).
                if name in ('dataclass', 'field', 'Field'):
                    continue
                # Inject exceptions and user-defined helper functions
                if name.endswith('Exception') or callable(obj):
                    setattr(mod, name, obj)
                    injected.add(name)
        # Inject uuid module — handlers may reference uuid.uuid4() from models
        import uuid as _uuid
        setattr(mod, 'uuid', _uuid)
        # Inject time module — handlers may reference time.time() from models
        import time as _time
        setattr(mod, 'time', _time)
        # Inject _helpers.code.py if it exists (e.g., _find_by_arn for tag handlers)
        helpers_path = handlers_dir / '_helpers.code.py'
        if helpers_path.exists():
            helpers_spec = importlib.util.spec_from_file_location(f'{service}_helpers', str(helpers_path))
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
        # ── appmesh — create ──────────────────────────────────────────────────
        'CreateMesh': {'meshName': 'test-mesh', 'spec': {}},
        'CreateVirtualNode': lambda store: (
            store.create_mesh('s-vn-mesh'),
            {'meshName': 's-vn-mesh', 'virtualNodeName': 'test-vn',
             'spec': {'listeners': []}})[1],
        'CreateVirtualService': lambda store: (
            store.create_mesh('s-vs-mesh'),
            {'meshName': 's-vs-mesh', 'virtualServiceName': 'test-vs',
             'spec': {}})[1],
        'CreateVirtualRouter': lambda store: (
            store.create_mesh('s-vr-mesh'),
            {'meshName': 's-vr-mesh', 'virtualRouterName': 'test-vr',
             'spec': {}})[1],
        'CreateRoute': lambda store: (
            store.create_mesh('s-r-mesh'),
            store.create_virtual_router('s-r-mesh', 'test-vr', spec={}),
            {'meshName': 's-r-mesh', 'virtualRouterName': 'test-vr',
             'routeName': 'test-route', 'spec': {}})[2],
        # ── appmesh — list ────────────────────────────────────────────────────
        'ListMeshes': {},
        'ListVirtualNodes': {'meshName': 'test-mesh'},
        'ListVirtualServices': {'meshName': 'test-mesh'},
        'ListVirtualRouters': {'meshName': 'test-mesh'},
        'ListRoutes': {'meshName': 'test-mesh', 'virtualRouterName': 'test-vr'},
        # ── appmesh — describe (lambdas: create prerequisite, then describe) ──
        'DescribeMesh': lambda store: (
            store.create_mesh('s-desc-mesh'),
            {'meshName': 's-desc-mesh'})[1],
        'DescribeVirtualNode': lambda store: (
            store.create_mesh('s-desc-vn-mesh'),
            store.create_virtual_node('s-desc-vn-mesh', 's-desc-vn', spec={'listeners': []}),
            {'meshName': 's-desc-vn-mesh', 'virtualNodeName': 's-desc-vn'})[2],
        'DescribeVirtualService': lambda store: (
            store.create_mesh('s-desc-vs-mesh'),
            store.create_virtual_service('s-desc-vs-mesh', 's-desc-vs', spec={}),
            {'meshName': 's-desc-vs-mesh', 'virtualServiceName': 's-desc-vs'})[2],
        'DescribeVirtualRouter': lambda store: (
            store.create_mesh('s-desc-vr-mesh'),
            store.create_virtual_router('s-desc-vr-mesh', 's-desc-vr', spec={}),
            {'meshName': 's-desc-vr-mesh', 'virtualRouterName': 's-desc-vr'})[2],
        'DescribeRoute': lambda store: (
            store.create_mesh('s-desc-rt-mesh'),
            store.create_virtual_router('s-desc-rt-mesh', 's-desc-rt-vr', spec={}),
            store.create_route('s-desc-rt-mesh', 's-desc-rt-vr', 's-desc-rt', spec={}),
            {'meshName': 's-desc-rt-mesh', 'virtualRouterName': 's-desc-rt-vr',
             'routeName': 's-desc-rt'})[3],
        # ── appmesh — delete (lambdas: create prerequisite, then delete) ───────
        'DeleteMesh': lambda store: (
            store.create_mesh('s-del-mesh'),
            {'meshName': 's-del-mesh'})[1],
        'DeleteVirtualNode': lambda store: (
            store.create_mesh('s-del-vn-mesh'),
            store.create_virtual_node('s-del-vn-mesh', 's-del-vn', spec={'listeners': []}),
            {'meshName': 's-del-vn-mesh', 'virtualNodeName': 's-del-vn'})[2],
        'DeleteVirtualService': lambda store: (
            store.create_mesh('s-del-vs-mesh'),
            store.create_virtual_service('s-del-vs-mesh', 's-del-vs', spec={}),
            {'meshName': 's-del-vs-mesh', 'virtualServiceName': 's-del-vs'})[2],
        'DeleteVirtualRouter': lambda store: (
            store.create_mesh('s-del-vr-mesh'),
            store.create_virtual_router('s-del-vr-mesh', 's-del-vr', spec={}),
            {'meshName': 's-del-vr-mesh', 'virtualRouterName': 's-del-vr'})[2],
        'DeleteRoute': lambda store: (
            store.create_mesh('s-del-rt-mesh'),
            store.create_virtual_router('s-del-rt-mesh', 's-del-rt-vr', spec={}),
            store.create_route('s-del-rt-mesh', 's-del-rt-vr', 's-del-rt', spec={}),
            {'meshName': 's-del-rt-mesh', 'virtualRouterName': 's-del-rt-vr',
             'routeName': 's-del-rt'})[3],
        # ── appmesh — update (lambdas: create prerequisite, then update) ───────
        'UpdateMesh': lambda store: (
            store.create_mesh('s-upd-mesh'),
            {'meshName': 's-upd-mesh', 'spec': {}})[1],
        'UpdateVirtualNode': lambda store: (
            store.create_mesh('s-upd-vn-mesh'),
            store.create_virtual_node('s-upd-vn-mesh', 's-upd-vn', spec={'listeners': []}),
            {'meshName': 's-upd-vn-mesh', 'virtualNodeName': 's-upd-vn',
             'spec': {'listeners': []}})[2],
        'UpdateVirtualService': lambda store: (
            store.create_mesh('s-upd-vs-mesh'),
            store.create_virtual_service('s-upd-vs-mesh', 's-upd-vs', spec={}),
            {'meshName': 's-upd-vs-mesh', 'virtualServiceName': 's-upd-vs',
             'spec': {}})[2],
        'UpdateVirtualRouter': lambda store: (
            store.create_mesh('s-upd-vr-mesh'),
            store.create_virtual_router('s-upd-vr-mesh', 's-upd-vr', spec={}),
            {'meshName': 's-upd-vr-mesh', 'virtualRouterName': 's-upd-vr',
             'spec': {}})[2],
        'UpdateRoute': lambda store: (
            store.create_mesh('s-upd-rt-mesh'),
            store.create_virtual_router('s-upd-rt-mesh', 's-upd-rt-vr', spec={}),
            store.create_route('s-upd-rt-mesh', 's-upd-rt-vr', 's-upd-rt', spec={}),
            {'meshName': 's-upd-rt-mesh', 'virtualRouterName': 's-upd-rt-vr',
             'routeName': 's-upd-rt', 'spec': {}})[3],
        # ── appmesh — tag/untag (service-prefixed keys) ────────────────────────
        'appmesh.TagResource': lambda store: (
            store.create_mesh('s-tag-mesh'),
            {'resourceArn': store.meshes('s-tag-mesh').arn,
             'tags': [{'key': 'env', 'value': 'test'}]})[1],
        'appmesh.UntagResource': lambda store: (
            store.create_mesh('s-untag-mesh'),
            store.tag_resource(store.meshes('s-untag-mesh').arn, [{'key': 'env', 'value': 'test'}]),
            {'resourceArn': store.meshes('s-untag-mesh').arn,
             'tagKeys': ['env']})[2],
        'appmesh.ListTagsForResource': lambda store: (
            store.create_mesh('s-ltfr-mesh'),
            {'resourceArn': store.meshes('s-ltfr-mesh').arn})[1],
        # ── amplify — create ────────────────────────────────────────────────
        'CreateApp': {'name': 'test-amplify-app'},
        'CreateBranch': lambda store: (
            store.create_app('a-cr-br'),
            {'appId': store.apps().appId if hasattr(store.apps(), 'appId') else list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'branchName': 'test-branch'})[1],
        'CreateBackendEnvironment': lambda store: (
            store.create_app('a-cr-be'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'environmentName': 'test-env'})[1],
        'CreateDomainAssociation': lambda store: (
            store.create_app('a-cr-da'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'domainName': 'example.com',
             'subDomainSettings': [{'prefix': 'www', 'branchName': 'main'}]})[1],
        'CreateWebhook': lambda store: (
            store.create_app('a-cr-wh'),
            store.create_branch(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'wh-branch'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'branchName': 'wh-branch'})[2],
        # ── amplify — list ────────────────────────────────────────────────
        'ListApps': {},
        'ListBranches': lambda store: (
            store.create_app('a-lb'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None})[1],
        'ListBackendEnvironments': lambda store: (
            store.create_app('a-lbe'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None})[1],
        'ListDomainAssociations': lambda store: (
            store.create_app('a-lda'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None})[1],
        'ListWebhooks': lambda store: (
            store.create_app('a-lw'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None})[1],
        # ── amplify — get (lambdas: create prerequisite, then get) ───────
        'GetApp': lambda store: (
            store.create_app('a-get'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None})[1],
        'GetBranch': lambda store: (
            store.create_app('a-getbr'),
            store.create_branch(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'get-branch'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'branchName': 'get-branch'})[2],
        'GetBackendEnvironment': lambda store: (
            store.create_app('a-getbe'),
            store.create_backend_environment(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'get-be'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'environmentName': 'get-be'})[2],
        'GetDomainAssociation': lambda store: (
            store.create_app('a-getda'),
            store.create_domain_association(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'get.da.com', [{'prefix': 'www', 'branchName': 'main'}]),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'domainName': 'get.da.com'})[2],
        'GetWebhook': lambda store: (
            store.create_app('a-getwh'),
            store.create_branch(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'getwh-br'),
            store.create_webhook(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'getwh-br'),
            {'webhookId': store.webhooks()[0].webhookId if isinstance(store.webhooks(), list) and store.webhooks() else None})[3],
        # ── amplify — delete (lambdas: create prerequisite, then delete) ──
        'DeleteApp': lambda store: (
            store.create_app('a-del'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None})[1],
        'DeleteBranch': lambda store: (
            store.create_app('a-delbr'),
            store.create_branch(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'del-branch'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'branchName': 'del-branch'})[2],
        'DeleteBackendEnvironment': lambda store: (
            store.create_app('a-delbe'),
            store.create_backend_environment(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'del-be'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'environmentName': 'del-be'})[2],
        'DeleteDomainAssociation': lambda store: (
            store.create_app('a-delda'),
            store.create_domain_association(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'del.da.com', [{'prefix': 'www', 'branchName': 'main'}]),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'domainName': 'del.da.com'})[2],
        'DeleteWebhook': lambda store: (
            store.create_app('a-delwh'),
            store.create_branch(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'delwh-br'),
            store.create_webhook(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'delwh-br'),
            {'webhookId': store.webhooks()[0].webhookId if isinstance(store.webhooks(), list) and store.webhooks() else None})[3],
        # ── amplify — update (lambdas: create prerequisite, then update) ──
        'UpdateApp': lambda store: (
            store.create_app('a-upd'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'name': 'updated-app'})[1],
        'UpdateBranch': lambda store: (
            store.create_app('a-updbr'),
            store.create_branch(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'upd-branch'),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'branchName': 'upd-branch'})[2],
        'UpdateDomainAssociation': lambda store: (
            store.create_app('a-updda'),
            store.create_domain_association(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'upd.da.com', [{'prefix': 'www', 'branchName': 'main'}]),
            {'appId': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'domainName': 'upd.da.com',
             'subDomainSettings': [{'prefix': 'api', 'branchName': 'main'}]})[2],
        'UpdateWebhook': lambda store: (
            store.create_app('a-updwh'),
            store.create_branch(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'updwh-br'),
            store.create_webhook(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', 'updwh-br'),
            {'webhookId': store.webhooks()[0].webhookId if isinstance(store.webhooks(), list) and store.webhooks() else None})[3],
        # ── amplify — tag/untag (service-prefixed keys) ──────────────────
        'amplify.TagResource': lambda store: (
            store.create_app('a-tag'),
            {'resourceArn': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'tags': {'env': 'test'}})[1],
        'amplify.UntagResource': lambda store: (
            store.create_app('a-untag'),
            store.tag_resource(list(store.apps())[0].appId if isinstance(store.apps(), list) else '', {'env': 'test'}),
            {'resourceArn': list(store.apps())[0].appId if isinstance(store.apps(), list) else None,
             'tagKeys': ['env']})[2],
        'amplify.ListTagsForResource': lambda store: (
            store.create_app('a-ltfr'),
            {'resourceArn': list(store.apps())[0].appId if isinstance(store.apps(), list) else None})[1],
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
        # ── frauddetector — create ───────────────────────────────────────────
        'CreateModel': {'modelId': 's-cm-model', 'modelType': 'ONLINE_FRAUD_INSIGHTS',
                        'eventTypeName': 's-cm-et'},
        'CreateRule': lambda store: (
            store.create_detector('s-cr-detector', eventTypeName='s-cr-et'),
            {'ruleId': 's-cr-rule', 'detectorId': 's-cr-detector',
             'expression': 'true', 'language': 'DETECTORPL',
             'outcomes': ['high_risk']})[1],
        'CreateVariable': {'name': 's-cv-var', 'dataType': 'FLOAT', 'dataSource': 'EXTERNAL_MODEL_SCORE',
                           'defaultValue': '0.0'},
        # ── frauddetector — put (create via put) ─────────────────────────────
        'PutDetector': {'detectorId': 's-pd-detector', 'eventTypeName': 's-pd-et'},
        'PutEventType': {'name': 's-pe-et',
                         'eventVariables': ['var1'], 'entityTypes': ['customer'],
                         'labels': ['fraud', 'legit']},
        # ── frauddetector — describe/delete/update (lambdas) ──────────────────
        'DescribeDetector': lambda store: (
            store.create_detector('s-desc-detector', eventTypeName='s-desc-et'),
            {'detectorId': 's-desc-detector'})[1],
        'DeleteDetector': lambda store: (
            store.create_detector('s-dd-detector', eventTypeName='s-dd-et'),
            {'detectorId': 's-dd-detector'})[1],
        'DeleteEventType': lambda store: (
            store.create_eventtype('s-det-et', eventVariables=['v1'],
                                   entityTypes=['customer']),
            {'name': 's-det-et'})[1],
        'DeleteModel': lambda store: (
            store.create_model('s-dm-model', 'ONLINE_FRAUD_INSIGHTS',
                               eventTypeName='s-dm-et'),
            {'modelId': 's-dm-model', 'modelType': 'ONLINE_FRAUD_INSIGHTS'})[1],
        'DeleteRule': lambda store: (
            store.create_detector('s-dr-detector', eventTypeName='s-dr-et'),
            store.create_rule('s-dr-rule', 's-dr-detector',
                              expression='true', language='DETECTORPL',
                              outcomes=['high_risk']),
            {'rule': 's-dr-detector/s-dr-rule'})[2],
        'DeleteVariable': lambda store: (
            store.create_variable('s-dv-var', dataType='FLOAT',
                                  dataSource='EXTERNAL_MODEL_SCORE',
                                  defaultValue='0.0'),
            {'name': 's-dv-var'})[1],
        'UpdateModel': lambda store: (
            store.create_model('s-um-model', 'ONLINE_FRAUD_INSIGHTS',
                               eventTypeName='s-um-et'),
            {'modelId': 's-um-model', 'modelType': 'ONLINE_FRAUD_INSIGHTS',
             'description': 'updated'})[1],
        'UpdateVariable': lambda store: (
            store.create_variable('s-uv-var', dataType='FLOAT',
                                  dataSource='EXTERNAL_MODEL_SCORE',
                                  defaultValue='0.0'),
            {'name': 's-uv-var', 'dataType': 'FLOAT',
             'dataSource': 'EXTERNAL_MODEL_SCORE',
             'defaultValue': '0.5'})[1],
        # ── frauddetector — tags (lambdas: create detector for ARN) ───────────
        'frauddetector.TagResource': lambda store: (
            store.create_detector('s-fd-tag', eventTypeName='s-fd-tag-et'),
            {'resourceARN': 'arn:aws:frauddetector:us-east-1:123456789012:detector/s-fd-tag',
             'tags': [{'key': 'env', 'value': 'test'}]})[1],
        'frauddetector.UntagResource': lambda store: (
            store.create_detector('s-fd-untag', eventTypeName='s-fd-untag-et'),
            {'resourceARN': 'arn:aws:frauddetector:us-east-1:123456789012:detector/s-fd-untag',
             'tagKeys': ['env']})[1],
        'frauddetector.ListTagsForResource': lambda store: (
            store.create_detector('s-fd-ltf', eventTypeName='s-fd-ltf-et'),
            {'resourceARN': 'arn:aws:frauddetector:us-east-1:123456789012:detector/s-fd-ltf'})[1],
        # ── shield — create ────────────────────────────────────────────────
        'CreateProtection': {'Name': 's-test-protection',
                             'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/s-test/abc'},
        'CreateProtectionGroup': {'ProtectionGroupId': 's-test-pg',
                                  'Aggregation': 'SUM', 'Pattern': 'ARBITRARY'},
        'CreateSubscription': {},
        # ── shield — static (no prerequisites) ─────────────────────────────
        'DescribeDRTAccess': {},
        'DescribeEmergencyContactSettings': {},
        'GetSubscriptionState': {},
        'ListProtectionGroups': {},
        'ListProtections': {},
        'AssociateDRTRole': {'RoleArn': 'arn:aws:iam::123456789012:role/DRTAccess'},
        'DisassociateDRTRole': {},
        'AssociateProactiveEngagementDetails': {'EmergencyContactList': [{'EmailAddress': 'test@example.com'}]},
        'UpdateEmergencyContactSettings': {'EmergencyContactList': [{'EmailAddress': 'updated@example.com'}]},
        'EnableApplicationLayerAutomaticResponse': {'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/s-test-app/abc',
                                                      'Action': 'COUNT'},
        # ── shield — describe (lambdas: create prerequisite, then describe) ─
        'DescribeProtection': lambda store: (
            store.create_protection(name='s-desc-prot', resource_arn='arn:aws:shield::123456789012:resource/s-desc-prot'),
            {'ResourceArn': 'arn:aws:shield::123456789012:resource/s-desc-prot'})[1],
        'DescribeProtectionGroup': lambda store: (
            store.create_protection_group('s-desc-pg', aggregation='SUM', pattern='ARBITRARY'),
            {'ProtectionGroupId': 's-desc-pg'})[1],
        'DescribeSubscription': lambda store: (
            (store.create_subscription() if store.subscription is None else None),
            {})[1],
        # ── shield — delete (lambdas: create first, then delete) ───────────
        'DeleteProtection': lambda store: (
            store.create_protection(name='s-del-prot', resource_arn='arn:aws:shield::123456789012:resource/s-del-prot'),
            {'ProtectionId': [p.id for p in store.protections.values()
                              if p.resource_arn == 'arn:aws:shield::123456789012:resource/s-del-prot'][0]})[1],
        'DeleteProtectionGroup': lambda store: (
            store.create_protection_group('s-del-pg', aggregation='SUM', pattern='ARBITRARY'),
            {'ProtectionGroupId': 's-del-pg'})[1],
        'DeleteSubscription': lambda store: (
            (store.create_subscription() if store.subscription is None else None),
            {})[1],
        # ── shield — update (lambdas: create first, then update) ───────────
        'UpdateProtectionGroup': lambda store: (
            store.create_protection_group('s-upd-pg', aggregation='SUM', pattern='ARBITRARY'),
            {'ProtectionGroupId': 's-upd-pg', 'Aggregation': 'SUM', 'Pattern': 'ARBITRARY'})[1],
        'UpdateSubscription': lambda store: (
            (store.create_subscription() if store.subscription is None else None),
            {'AutoRenew': 'ENABLED'})[1],
        # ── shield — DRT log bucket (lambdas: role required first) ─────────
        'AssociateDRTLogBucket': lambda store: (
            store.associate_drt_role('arn:aws:iam::123456789012:role/DRTAccess'),
            {'LogBucket': 's-test-log-bucket-123'})[1],
        'DisassociateDRTLogBucket': lambda store: (
            store.associate_drt_role('arn:aws:iam::123456789012:role/DRTAccess'),
            store.associate_drt_log_bucket('s-disassoc-bucket'),
            {'LogBucket': 's-disassoc-bucket'})[2],
        # ── shield — health check (lambdas: protection first) ──────────────
        'AssociateHealthCheck': lambda store: (
            store.create_protection(name='s-hc-prot', resource_arn='arn:aws:shield::123456789012:resource/s-hc-prot'),
            {'ProtectionId': [p.id for p in store.protections.values()
                              if p.resource_arn == 'arn:aws:shield::123456789012:resource/s-hc-prot'][0],
             'HealthCheckArn': 'arn:aws:route53:::healthcheck/s-test-hc'})[1],
        'DisassociateHealthCheck': lambda store: (
            store.create_protection(name='s-dhc-prot', resource_arn='arn:aws:shield::123456789012:resource/s-dhc-prot'),
            store.associate_health_check(
                [p.id for p in store.protections.values()
                 if p.resource_arn == 'arn:aws:shield::123456789012:resource/s-dhc-prot'][0],
                'arn:aws:route53:::healthcheck/s-dhc'),
            {'ProtectionId': [p.id for p in store.protections.values()
                              if p.resource_arn == 'arn:aws:shield::123456789012:resource/s-dhc-prot'][0],
             'HealthCheckArn': 'arn:aws:route53:::healthcheck/s-dhc'})[2],
        # ── shield — proactive engagement (lambdas: subscription first) ────
        'EnableProactiveEngagement': lambda store: (
            (store.create_subscription() if store.subscription is None else None),
            {})[1],
        'DisableProactiveEngagement': lambda store: (
            (store.create_subscription() if store.subscription is None else None),
            {})[1],
        # ── shield — app layer (lambdas: enable first for disable/update) ──
        'DisableApplicationLayerAutomaticResponse': lambda store: (
            store.enable_application_layer_automatic_response(
                'arn:aws:shield::123456789012:resource/s-disable-app', 'COUNT'),
            {'ResourceArn': 'arn:aws:shield::123456789012:resource/s-disable-app'})[1],
        'UpdateApplicationLayerAutomaticResponse': lambda store: (
            store.enable_application_layer_automatic_response(
                'arn:aws:shield::123456789012:resource/s-update-app', 'COUNT'),
            {'ResourceArn': 'arn:aws:shield::123456789012:resource/s-update-app',
             'Action': 'BLOCK'})[1],
        # ── shield — list resources (lambda: create group with members) ────
        'ListResourcesInProtectionGroup': lambda store: (
            store.create_protection_group('s-listr-pg', aggregation='SUM', pattern='ARBITRARY',
                                           members=['arn:aws:shield::123456789012:resource/member1']),
            {'ProtectionGroupId': 's-listr-pg'})[1],
        # ── shield — tags (service-prefixed keys) ───────────────────────────
        'shield.TagResource': lambda store: (
            store.create_protection(name='s-tag-prot', resource_arn='arn:aws:shield::123456789012:resource/s-tag-prot'),
            {'ResourceARN': 'arn:aws:shield::123456789012:resource/s-tag-prot',
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[1],
        'shield.UntagResource': lambda store: (
            store.create_protection(name='s-untag-prot', resource_arn='arn:aws:shield::123456789012:resource/s-untag-prot'),
            store.tag_resource('arn:aws:shield::123456789012:resource/s-untag-prot', [{'Key': 'env', 'Value': 'test'}]),
            {'ResourceARN': 'arn:aws:shield::123456789012:resource/s-untag-prot',
             'TagKeys': ['env']})[2],
        'shield.ListTagsForResource': lambda store: (
            store.create_protection(name='s-ltf-prot', resource_arn='arn:aws:shield::123456789012:resource/s-ltf-prot'),
            store.tag_resource('arn:aws:shield::123456789012:resource/s-ltf-prot', [{'Key': 'env', 'Value': 'test'}]),
            {'ResourceARN': 'arn:aws:shield::123456789012:resource/s-ltf-prot'})[2],
        # ── rekognition — create ──────────────────────────────────────────
        'CreateCollection': {'CollectionId': 'test-collection'},
        # ── rekognition — list ────────────────────────────────────────────
        'ListCollections': {},
        'ListFaces': lambda store: (
            store.collections.__setitem__('s-list-faces-col', {'CollectionId': 's-list-faces-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-list-faces-col', set()),
            {'CollectionId': 's-list-faces-col'})[2],
        # ── rekognition — describe/delete (lambdas: create collection first)
        'DescribeCollection': lambda store: (
            store.collections.__setitem__('s-desc-col', {'CollectionId': 's-desc-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-desc-col', set()),
            {'CollectionId': 's-desc-col'})[2],
        'DeleteCollection': lambda store: (
            store.collections.__setitem__('s-del-col', {'CollectionId': 's-del-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-del-col', set()),
            {'CollectionId': 's-del-col'})[2],
        # ── rekognition — face ops (need collection first) ────────────────
        'IndexFaces': lambda store: (
            store.collections.__setitem__('s-idx-col', {'CollectionId': 's-idx-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-idx-col', set()),
            {'CollectionId': 's-idx-col', 'Image': {'Bytes': 'dGVzdA=='}})[2],
        'SearchFaces': lambda store: (
            store.collections.__setitem__('s-search-col', {'CollectionId': 's-search-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-search-col', set()),
            {'CollectionId': 's-search-col', 'FaceId': 'test-face-id'})[2],
        'SearchFacesByImage': lambda store: (
            store.collections.__setitem__('s-sfbi-col', {'CollectionId': 's-sfbi-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-sfbi-col', set()),
            {'CollectionId': 's-sfbi-col', 'Image': {'Bytes': 'dGVzdA=='}})[2],
        'DeleteFaces': lambda store: (
            store.collections.__setitem__('s-delf-col', {'CollectionId': 's-delf-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-delf-col', set()),
            store.faces.__setitem__('test-face-1', {}),
            store.collection_faces['s-delf-col'].add('test-face-1'),
            {'CollectionId': 's-delf-col', 'FaceIds': ['test-face-1']})[4],
        # ── rekognition — detection (stateless, just Image) ───────────────
        'DetectFaces': {'Image': {'Bytes': 'dGVzdA=='}},
        'DetectLabels': {'Image': {'Bytes': 'dGVzdA=='}},
        'DetectModerationLabels': {'Image': {'Bytes': 'dGVzdA=='}},
        'DetectProtectiveEquipment': {'Image': {'Bytes': 'dGVzdA=='}},
        'DetectText': {'Image': {'Bytes': 'dGVzdA=='}},
        'CompareFaces': {'SourceImage': {'Bytes': 'dGVzdA=='}, 'TargetImage': {'Bytes': 'dGVzdA=='}},
        'RecognizeCelebrities': {'Image': {'Bytes': 'dGVzdA=='}},
        # ── rekognition — async video ─────────────────────────────────────
        'StartCelebrityRecognition': {'Video': {'S3Object': {'Bucket': 'test-bucket', 'Name': 'test.mp4'}}},
        'StartContentModeration': {'Video': {'S3Object': {'Bucket': 'test-bucket', 'Name': 'test.mp4'}}},
        'StartFaceDetection': {'Video': {'S3Object': {'Bucket': 'test-bucket', 'Name': 'test.mp4'}}},
        'StartLabelDetection': {'Video': {'S3Object': {'Bucket': 'test-bucket', 'Name': 'test.mp4'}}},
        'StartTextDetection': {'Video': {'S3Object': {'Bucket': 'test-bucket', 'Name': 'test.mp4'}}},
        # ── rekognition — get async results (lambda: create job first) ────
        'GetCelebrityRecognition': lambda store: (
            store.video_jobs.__setitem__('s-gcr-job', {'JobId': 's-gcr-job', 'Status': 'SUCCEEDED', 'API': 'StartCelebrityRecognition', 'Video': {}, 'CreatedTimestamp': 0.0, 'Results': []}),
            {'JobId': 's-gcr-job'})[1],
        'GetContentModeration': lambda store: (
            store.video_jobs.__setitem__('s-gcm-job', {'JobId': 's-gcm-job', 'Status': 'SUCCEEDED', 'API': 'StartContentModeration', 'Video': {}, 'CreatedTimestamp': 0.0, 'Results': []}),
            {'JobId': 's-gcm-job'})[1],
        'GetFaceDetection': lambda store: (
            store.video_jobs.__setitem__('s-gfd-job', {'JobId': 's-gfd-job', 'Status': 'SUCCEEDED', 'API': 'StartFaceDetection', 'Video': {}, 'CreatedTimestamp': 0.0, 'Results': []}),
            {'JobId': 's-gfd-job'})[1],
        'GetLabelDetection': lambda store: (
            store.video_jobs.__setitem__('s-gld-job', {'JobId': 's-gld-job', 'Status': 'SUCCEEDED', 'API': 'StartLabelDetection', 'Video': {}, 'CreatedTimestamp': 0.0, 'Results': []}),
            {'JobId': 's-gld-job'})[1],
        'GetTextDetection': lambda store: (
            store.video_jobs.__setitem__('s-gtd-job', {'JobId': 's-gtd-job', 'Status': 'SUCCEEDED', 'API': 'StartTextDetection', 'Video': {}, 'CreatedTimestamp': 0.0, 'Results': []}),
            {'JobId': 's-gtd-job'})[1],
        # ── rekognition — celebrity ───────────────────────────────────────
        'GetCelebrityInfo': {'Id': 'celebrity-1'},
        # ── rekognition — tag/untag (service-prefixed keys) ───────────────
        'rekognition.TagResource': lambda store: (
            store.collections.__setitem__('s-tag-col', {'CollectionId': 's-tag-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-tag-col', set()),
            {'ResourceArn': 'arn:aws:rekognition:us-east-1:123456789012:collection/s-tag-col',
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[2],
        'rekognition.UntagResource': lambda store: (
            store.collections.__setitem__('s-untag-col', {'CollectionId': 's-untag-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-untag-col', set()),
            store.tags.__setitem__('arn:aws:rekognition:us-east-1:123456789012:collection/s-untag-col', {'env': 'test'}),
            {'ResourceArn': 'arn:aws:rekognition:us-east-1:123456789012:collection/s-untag-col',
             'TagKeys': ['env']})[3],
        'rekognition.ListTagsForResource': lambda store: (
            store.collections.__setitem__('s-ltfr-col', {'CollectionId': 's-ltfr-col', 'FaceCount': 0, 'CreatedTimestamp': 0.0}),
            store.collection_faces.__setitem__('s-ltfr-col', set()),
            {'ResourceArn': 'arn:aws:rekognition:us-east-1:123456789012:collection/s-ltfr-col'})[2],
        # ── sso-admin — create ─────────────────────────────────────────────
        'CreateInstance': {'name': 's-create-inst'},
        'CreateAccountAssignment': lambda store: (
            ia := store.create_instance(name='s-caa-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'targetId': '111111111111', 'targetType': 'AWS_ACCOUNT',
             'permissionSetArn': psa, 'principalType': 'USER', 'principalId': 'test-user-id'})[3],
        'CreatePermissionSet': lambda store: (
            ia := store.create_instance(name='s-cps-inst')['instanceArn'],
            {'name': 'test-ps', 'instanceArn': ia})[1],
        'CreateApplication': lambda store: (
            ia := store.create_instance(name='s-cap-inst')['instanceArn'],
            {'instanceArn': ia, 'applicationProviderArn': 'arn:aws:sso::aws:applicationProvider/custom',
             'name': 'test-app'})[1],
        # ── sso-admin — list ───────────────────────────────────────────────
        'ListInstances': {},
        'ListPermissionSets': lambda store: (
            ia := store.create_instance(name='s-lps-inst')['instanceArn'],
            {'instanceArn': ia})[1],
        'ListAccountAssignments': lambda store: (
            ia := store.create_instance(name='s-laa-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'accountId': '111111111111', 'permissionSetArn': psa})[3],
        'ListAccountAssignmentsForPrincipal': lambda store: (
            ia := store.create_instance(name='s-lafp-inst')['instanceArn'],
            {'instanceArn': ia, 'principalId': 'test-principal', 'principalType': 'USER'})[1],
        'ListApplications': lambda store: (
            ia := store.create_instance(name='s-lapp-inst')['instanceArn'],
            {'instanceArn': ia})[1],
        'ListManagedPoliciesInPermissionSet': lambda store: (
            ia := store.create_instance(name='s-lmpip-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa})[3],
        # ── sso-admin — describe (lambdas: create prerequisites) ───────────
        'DescribeInstance': lambda store: (
            ia := store.create_instance(name='s-di-inst')['instanceArn'],
            {'instanceArn': ia})[1],
        'DescribePermissionSet': lambda store: (
            ia := store.create_instance(name='s-dps-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa})[3],
        'DescribeAccountAssignmentCreationStatus': lambda store: (
            ia := store.create_instance(name='s-daacs-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            result := store.create_account_assignment(ia, '111111111111', 'AWS_ACCOUNT', psa, 'USER', 'test-user-id'),
            req_id := result['accountAssignmentCreationStatus']['requestId'],
            {'instanceArn': ia, 'accountAssignmentCreationRequestId': req_id})[5],
        'DescribeAccountAssignmentDeletionStatus': lambda store: (
            ia := store.create_instance(name='s-daads-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            result := store.create_account_assignment(ia, '111111111111', 'AWS_ACCOUNT', psa, 'USER', 'test-user-id'),
            req_id := result['accountAssignmentCreationStatus']['requestId'],
            {'instanceArn': ia, 'accountAssignmentDeletionRequestId': req_id})[5],
        'DescribeApplication': lambda store: (
            ia := store.create_instance(name='s-da-inst')['instanceArn'],
            app := store.create_application(ia, 'arn:aws:sso::aws:applicationProvider/custom', 'test-app'),
            app_arn := app['applicationArn'],
            {'applicationArn': app_arn})[3],
        # ── sso-admin — delete (lambdas: create prerequisites) ─────────────
        'DeleteInstance': lambda store: (
            ia := store.create_instance(name='s-deli-inst')['instanceArn'],
            {'instanceArn': ia})[1],
        'DeletePermissionSet': lambda store: (
            ia := store.create_instance(name='s-delps-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa})[3],
        'DeleteAccountAssignment': lambda store: (
            ia := store.create_instance(name='s-daa-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            store.create_account_assignment(ia, '111111111111', 'AWS_ACCOUNT', psa, 'USER', 'test-user-id'),
            {'instanceArn': ia, 'targetId': '111111111111', 'targetType': 'AWS_ACCOUNT',
             'permissionSetArn': psa, 'principalType': 'USER', 'principalId': 'test-user-id'})[4],
        'DeleteApplication': lambda store: (
            ia := store.create_instance(name='s-delapp-inst')['instanceArn'],
            app := store.create_application(ia, 'arn:aws:sso::aws:applicationProvider/custom', 'test-app'),
            app_arn := app['applicationArn'],
            {'applicationArn': app_arn})[3],
        'DeleteInlinePolicyFromPermissionSet': lambda store: (
            ia := store.create_instance(name='s-dipfp-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa})[3],
        # ── sso-admin — update ─────────────────────────────────────────────
        'UpdateInstance': lambda store: (
            ia := store.create_instance(name='s-ui-inst')['instanceArn'],
            {'instanceArn': ia, 'name': 'updated-name'})[1],
        'UpdatePermissionSet': lambda store: (
            ia := store.create_instance(name='s-ups-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa, 'description': 'updated desc'})[3],
        'UpdateApplication': lambda store: (
            ia := store.create_instance(name='s-ua-inst')['instanceArn'],
            app := store.create_application(ia, 'arn:aws:sso::aws:applicationProvider/custom', 'test-app'),
            app_arn := app['applicationArn'],
            {'applicationArn': app_arn, 'name': 'updated-app'})[3],
        # ── sso-admin — policy ─────────────────────────────────────────────
        'PutInlinePolicyToPermissionSet': lambda store: (
            ia := store.create_instance(name='s-piptp-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa,
             'inlinePolicy': '{"Version":"2012-10-17","Statement":[]}'})[3],
        'GetInlinePolicyForPermissionSet': lambda store: (
            ia := store.create_instance(name='s-gipfp-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa})[3],
        # ── sso-admin — managed policy ─────────────────────────────────────
        'AttachManagedPolicyToPermissionSet': lambda store: (
            ia := store.create_instance(name='s-amptp-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            {'instanceArn': ia, 'permissionSetArn': psa,
             'managedPolicyArn': 'arn:aws:iam::aws:policy/ReadOnlyAccess'})[3],
        'DetachManagedPolicyFromPermissionSet': lambda store: (
            ia := store.create_instance(name='s-dmpfp-inst')['instanceArn'],
            ps := store.create_permission_set('test-ps', ia),
            psa := ps['permissionSetArn'],
            store.attach_managed_policy_to_permission_set(ia, psa, 'arn:aws:iam::aws:policy/ReadOnlyAccess'),
            {'instanceArn': ia, 'permissionSetArn': psa,
             'managedPolicyArn': 'arn:aws:iam::aws:policy/ReadOnlyAccess'})[4],
        # ── sso-admin — tag/untag (service-prefixed keys) ──────────────────
        'sso-admin.TagResource': lambda store: (
            ia := store.create_instance(name='s-tagr-inst')['instanceArn'],
            {'resourceArn': ia, 'tags': [{'Key': 'env', 'Value': 'test'}]})[1],
        'sso-admin.UntagResource': lambda store: (
            ia := store.create_instance(name='s-untagr-inst')['instanceArn'],
            {'resourceArn': ia, 'tagKeys': ['env']})[1],
        'sso-admin.ListTagsForResource': lambda store: (
            ia := store.create_instance(name='s-ltfr-inst')['instanceArn'],
            {'resourceArn': ia})[1],
        # ── amplify — create ───────────────────────────────────────────────
        'CreateApp': {'name': 'test-app'},
        'CreateBranch': lambda store: (
            app := store.create_app('s-cb-app'),
            {'appId': app.appId, 'branchName': 'test-branch'})[1],
        'CreateBackendEnvironment': lambda store: (
            app := store.create_app('s-cbe-app'),
            {'appId': app.appId, 'environmentName': 'test-env'})[1],
        'CreateDomainAssociation': lambda store: (
            app := store.create_app('s-cda-app'),
            {'appId': app.appId, 'domainName': 'test.example.com',
             'subDomainSettings': [{'prefix': 'www', 'branchName': 'main'}]})[1],
        'CreateWebhook': lambda store: (
            app := store.create_app('s-cw-app'),
            {'appId': app.appId, 'branchName': 'main'})[1],
        # ── amplify — list ─────────────────────────────────────────────────
        'ListApps': {},
        'ListBranches': {'appId': 'nonexistent'},
        'ListBackendEnvironments': {'appId': 'nonexistent'},
        'ListDomainAssociations': {'appId': 'nonexistent'},
        'ListWebhooks': {'appId': 'nonexistent'},
        # ── amplify — describe (lambdas: create prerequisite, then describe) ─
        'GetApp': lambda store: (
            app := store.create_app('s-ga-app'),
            {'appId': app.appId})[1],
        'GetBranch': lambda store: (
            app := store.create_app('s-gb-app'),
            store.create_branch(app.appId, 'test-br'),
            {'appId': app.appId, 'branchName': 'test-br'})[2],
        'GetBackendEnvironment': lambda store: (
            app := store.create_app('s-gbe-app'),
            store.create_backend_environment(app.appId, 'test-env'),
            {'appId': app.appId, 'environmentName': 'test-env'})[2],
        'GetDomainAssociation': lambda store: (
            app := store.create_app('s-gda-app'),
            store.create_domain_association(app.appId, 'test.da.example.com', [{'prefix': 'www', 'branchName': 'main'}]),
            {'appId': app.appId, 'domainName': 'test.da.example.com'})[2],
        'GetWebhook': lambda store: (
            app := store.create_app('s-gw-app'),
            wh := store.create_webhook(app.appId, 'main'),
            {'webhookId': wh.webhookId})[2],
        # ── amplify — delete (lambdas: create prerequisite, then delete) ────
        'DeleteApp': lambda store: (
            app := store.create_app('s-da-app'),
            {'appId': app.appId})[1],
        'DeleteBranch': lambda store: (
            app := store.create_app('s-db-app'),
            store.create_branch(app.appId, 's-db-br'),
            {'appId': app.appId, 'branchName': 's-db-br'})[2],
        'DeleteBackendEnvironment': lambda store: (
            app := store.create_app('s-dbe-app'),
            store.create_backend_environment(app.appId, 's-dbe-env'),
            {'appId': app.appId, 'environmentName': 's-dbe-env'})[2],
        'DeleteDomainAssociation': lambda store: (
            app := store.create_app('s-dda-app'),
            store.create_domain_association(app.appId, 's-dda.example.com', [{'prefix': 'www', 'branchName': 'main'}]),
            {'appId': app.appId, 'domainName': 's-dda.example.com'})[2],
        'DeleteWebhook': lambda store: (
            app := store.create_app('s-dw-app'),
            wh := store.create_webhook(app.appId, 'main'),
            {'webhookId': wh.webhookId})[2],
        # ── amplify — update (lambdas: create prerequisite, then update) ────
        'UpdateApp': lambda store: (
            app := store.create_app('s-ua-app'),
            {'appId': app.appId, 'name': 'updated-app'})[1],
        'UpdateBranch': lambda store: (
            app := store.create_app('s-ub-app'),
            store.create_branch(app.appId, 's-ub-br'),
            {'appId': app.appId, 'branchName': 's-ub-br', 'stage': 'DEVELOPMENT'})[2],
        'UpdateDomainAssociation': lambda store: (
            app := store.create_app('s-uda-app'),
            store.create_domain_association(app.appId, 's-uda.example.com', [{'prefix': 'www', 'branchName': 'main'}]),
            {'appId': app.appId, 'domainName': 's-uda.example.com',
             'subDomainSettings': [{'prefix': 'www', 'branchName': 'staging'}]})[2],
        'UpdateWebhook': lambda store: (
            app := store.create_app('s-uw-app'),
            wh := store.create_webhook(app.appId, 'main'),
            {'webhookId': wh.webhookId, 'branchName': 'develop'})[2],
        # ── amplify — tag/untag (service-prefixed keys) ─────────────────────
        'amplify.TagResource': lambda store: (
            app := store.create_app('s-tr-app'),
            {'resourceArn': app.appId,
             'tags': [{'key': 'env', 'value': 'test'}]})[1],
        'amplify.UntagResource': lambda store: (
            app := store.create_app('s-utr-app'),
            {'resourceArn': app.appId,
             'tagKeys': ['env']})[1],
        'amplify.ListTagsForResource': lambda store: (
            app := store.create_app('s-ltfr-app'),
            {'resourceArn': app.appId})[1],
        # ── organizations — create ───────────────────────────────────────────
        'CreateOrganization': {'FeatureSet': 'ALL'},
        'CreateAccount': {'Email': 'test-acc@test.com', 'AccountName': 'TestAccount'},
        'CreateOrganizationalUnit': lambda store: (
            store.create_organization(),
            {'ParentId': store.roots[0], 'Name': 'TestOU'})[1],
        'CreatePolicy': lambda store: (
            store.create_organization(),
            {'Name': 'TestPolicy', 'Description': 'Test description',
             'Type': 'SERVICE_CONTROL_POLICY',
             'Content': '{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}'})[1],
        # ── organizations — list/describe ──────────────────────────────────────
        'DescribeOrganization': lambda store: (
            store.create_organization(),
            {})[1],
        'ListAccounts': lambda store: (
            store.create_organization(),
            {})[1],
        'ListRoots': lambda store: (
            store.create_organization(),
            {})[1],
        'ListAccountsForParent': lambda store: (
            store.create_organization(),
            {'ParentId': store.roots[0]})[1],
        'ListOrganizationalUnitsForParent': lambda store: (
            store.create_organization(),
            {'ParentId': store.roots[0]})[1],
        'ListPolicies': lambda store: (
            store.create_organization(),
            {'Filter': 'SERVICE_CONTROL_POLICY'})[1],
        'ListPoliciesForTarget': lambda store: (
            org := store.create_organization(),
            p := store.create_policy(
                content='{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}',
                description='Test', name='LPFT-Policy', type='SERVICE_CONTROL_POLICY'),
            store.attach_policy(p.id, store.roots[0]),
            {'TargetId': store.roots[0], 'Filter': 'SERVICE_CONTROL_POLICY'})[3],
        'DescribeAccount': lambda store: (
            org := store.create_organization(),
            acc := store.create_account(email='desc-acc@test.com', name='DescAccount'),
            {'AccountId': acc['CreateAccountStatus']['AccountId']})[2],
        'DescribeOrganizationalUnit': lambda store: (
            org := store.create_organization(),
            ou := store.create_organizational_unit(store.roots[0], 'DescOU'),
            {'OrganizationalUnitId': ou.id})[2],
        'DescribePolicy': lambda store: (
            org := store.create_organization(),
            p := store.create_policy(
                content='{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}',
                description='Test', name='DescPolicy', type='SERVICE_CONTROL_POLICY'),
            {'PolicyId': p.id})[2],
        # ── organizations — delete (lambdas: create prerequisite, then delete) ─
        'DeleteOrganization': lambda store: (
            store.create_organization(),
            {})[1],
        'DeleteOrganizationalUnit': lambda store: (
            org := store.create_organization(),
            ou := store.create_organizational_unit(store.roots[0], 'DelOU'),
            {'OrganizationalUnitId': ou.id})[2],
        'DeletePolicy': lambda store: (
            org := store.create_organization(),
            p := store.create_policy(
                content='{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}',
                description='Test', name='DelPolicy', type='SERVICE_CONTROL_POLICY'),
            {'PolicyId': p.id})[2],
        'CloseAccount': lambda store: (
            org := store.create_organization(),
            acc := store.create_account(email='close-acc@test.com', name='CloseAccount'),
            {'AccountId': acc['CreateAccountStatus']['AccountId']})[2],
        'RemoveAccountFromOrganization': lambda store: (
            org := store.create_organization(),
            acc := store.create_account(email='remove-acc@test.com', name='RemoveAccount'),
            {'AccountId': acc['CreateAccountStatus']['AccountId']})[2],
        # ── organizations — update ────────────────────────────────────────────
        'UpdateOrganizationalUnit': lambda store: (
            org := store.create_organization(),
            ou := store.create_organizational_unit(store.roots[0], 'UpdOU'),
            {'OrganizationalUnitId': ou.id, 'Name': 'UpdatedOU'})[2],
        'UpdatePolicy': lambda store: (
            org := store.create_organization(),
            p := store.create_policy(
                content='{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}',
                description='Test', name='UpdPolicy', type='SERVICE_CONTROL_POLICY'),
            {'PolicyId': p.id, 'Name': 'UpdatedPolicy'})[2],
        # ── organizations — misc ──────────────────────────────────────────────
        'EnableAllFeatures': lambda store: (
            store.create_organization(),
            {})[1],
        'MoveAccount': lambda store: (
            org := store.create_organization(),
            acc := store.create_account(email='move-acc@test.com', name='MoveAccount'),
            dest_ou := store.create_organizational_unit(store.roots[0], 'DestOU'),
            {'AccountId': acc['CreateAccountStatus']['AccountId'],
             'SourceParentId': store.roots[0],
             'DestinationParentId': dest_ou.id})[3],
        'AttachPolicy': lambda store: (
            org := store.create_organization(),
            p := store.create_policy(
                content='{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}',
                description='Test', name='AttPolicy', type='SERVICE_CONTROL_POLICY'),
            {'PolicyId': p.id, 'TargetId': store.roots[0]})[2],
        'DetachPolicy': lambda store: (
            org := store.create_organization(),
            p := store.create_policy(
                content='{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}',
                description='Test', name='DetPolicy', type='SERVICE_CONTROL_POLICY'),
            store.attach_policy(p.id, store.roots[0]),
            {'PolicyId': p.id, 'TargetId': store.roots[0]})[3],
        # ── elasticache — create ───────────────────────────────────────────
        'CreateCacheCluster': {'CacheClusterId': 'test-cluster'},
        'CreateCacheParameterGroup': {'CacheParameterGroupName': 'test-pg',
                                      'CacheParameterGroupFamily': 'redis7.0',
                                      'Description': 'test parameter group'},
        'CreateCacheSubnetGroup': {'CacheSubnetGroupName': 'test-sg',
                                   'CacheSubnetGroupDescription': 'test subnet group',
                                   'SubnetIds': ['subnet-12345678']},
        'CreateReplicationGroup': {'ReplicationGroupId': 'test-rg',
                                   'ReplicationGroupDescription': 'test replication group'},
        'CreateSnapshot': {'SnapshotName': 'test-snapshot'},
        'CreateUser': {'UserId': 'test-user', 'UserName': 'testuser',
                       'Engine': 'redis', 'AccessString': 'on ~* +@all'},
        'CreateUserGroup': {'UserGroupId': 'test-ug', 'Engine': 'redis'},
        # ── elasticache — list ─────────────────────────────────────────────
        'DescribeCacheClusters': {},
        'DescribeCacheEngineVersions': {},
        'DescribeCacheParameterGroups': {},
        'DescribeCacheSubnetGroups': {},
        'DescribeEvents': {},
        'DescribeReplicationGroups': {},
        'DescribeSnapshots': {},
        'DescribeUserGroups': {},
        'DescribeUsers': {},
        # ── elasticache — delete (lambdas: create prerequisite, then delete) ─
        'DeleteCacheCluster': lambda store: (
            store.cache_clusters.setdefault('el-del-cc', {'CacheClusterId': 'el-del-cc', 'Status': 'available'}),
            {'CacheClusterId': 'el-del-cc'})[1],
        'DeleteCacheParameterGroup': lambda store: (
            store.parameter_groups.setdefault('el-del-pg',
                {'CacheParameterGroupName': 'el-del-pg', 'CacheParameterGroupFamily': 'redis7.0',
                 'Description': 'test'}),
            {'CacheParameterGroupName': 'el-del-pg'})[1],
        'DeleteCacheSubnetGroup': lambda store: (
            store.subnet_groups.setdefault('el-del-sg',
                {'CacheSubnetGroupName': 'el-del-sg', 'CacheSubnetGroupDescription': 'test',
                 'SubnetIds': ['subnet-12345678'], 'VpcId': 'vpc-12345'}),
            {'CacheSubnetGroupName': 'el-del-sg'})[1],
        'DeleteReplicationGroup': lambda store: (
            store.replication_groups.setdefault('el-del-rg',
                {'ReplicationGroupId': 'el-del-rg', 'ReplicationGroupDescription': 'test',
                 'Status': 'available'}),
            {'ReplicationGroupId': 'el-del-rg'})[1],
        'DeleteSnapshot': lambda store: (
            store.snapshots.setdefault('el-del-snap', {'SnapshotName': 'el-del-snap', 'Status': 'available'}),
            {'SnapshotName': 'el-del-snap'})[1],
        'DeleteUser': lambda store: (
            store.users.setdefault('el-del-user', {'UserId': 'el-del-user', 'UserName': 'deluser',
                'Engine': 'redis', 'AccessString': 'on', 'Status': 'available'}),
            {'UserId': 'el-del-user'})[1],
        'DeleteUserGroup': lambda store: (
            store.user_groups.setdefault('el-del-ug', {'UserGroupId': 'el-del-ug', 'Engine': 'redis',
                'Status': 'available'}),
            {'UserGroupId': 'el-del-ug'})[1],
        # ── elasticache — modify (lambdas: create prerequisite, then modify) ─
        'ModifyCacheCluster': lambda store: (
            store.cache_clusters.setdefault('el-mod-cc', {'CacheClusterId': 'el-mod-cc', 'Status': 'available'}),
            {'CacheClusterId': 'el-mod-cc'})[1],
        'ModifyCacheParameterGroup': lambda store: (
            store.parameter_groups.setdefault('el-mod-pg',
                {'CacheParameterGroupName': 'el-mod-pg', 'CacheParameterGroupFamily': 'redis7.0',
                 'Description': 'test'}),
            {'CacheParameterGroupName': 'el-mod-pg',
             'ParameterNameValues': [{'ParameterName': 'timeout', 'ParameterValue': '300'}]})[1],
        'ModifyCacheSubnetGroup': lambda store: (
            store.subnet_groups.setdefault('el-mod-sg',
                {'CacheSubnetGroupName': 'el-mod-sg', 'CacheSubnetGroupDescription': 'test',
                 'SubnetIds': ['subnet-12345678'], 'VpcId': 'vpc-12345'}),
            {'CacheSubnetGroupName': 'el-mod-sg', 'SubnetIds': ['subnet-87654321']})[1],
        'ModifyReplicationGroup': lambda store: (
            store.replication_groups.setdefault('el-mod-rg',
                {'ReplicationGroupId': 'el-mod-rg', 'ReplicationGroupDescription': 'test',
                 'Status': 'available'}),
            {'ReplicationGroupId': 'el-mod-rg'})[1],
        'ModifyUser': lambda store: (
            store.users.setdefault('el-mod-user', {'UserId': 'el-mod-user', 'UserName': 'moduser',
                'Engine': 'redis', 'AccessString': 'on', 'Status': 'available'}),
            {'UserId': 'el-mod-user'})[1],
        'ModifyUserGroup': lambda store: (
            store.user_groups.setdefault('el-mod-ug', {'UserGroupId': 'el-mod-ug', 'Engine': 'redis',
                'Status': 'available'}),
            {'UserGroupId': 'el-mod-ug'})[1],
        # ── elasticache — misc ──────────────────────────────────────────────
        'CopySnapshot': lambda store: (
            store.snapshots.setdefault('el-copy-src', {'SnapshotName': 'el-copy-src', 'Status': 'available'}),
            {'SourceSnapshotName': 'el-copy-src', 'TargetSnapshotName': 'el-copy-dst'})[1],
        'RebootCacheCluster': lambda store: (
            store.cache_clusters.setdefault('el-reb-cc', {'CacheClusterId': 'el-reb-cc', 'Status': 'available',
                'NumCacheNodes': 2}),
            {'CacheClusterId': 'el-reb-cc', 'CacheNodeIdsToReboot': ['0001']})[1],
        # ── elasticache — tag/untag (service-prefixed keys) ─────────────────
        'elasticache.AddTagsToResource': lambda store: (
            store.tags.setdefault('el-tag-arn', []),
            {'ResourceName': 'el-tag-arn',
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[1],
        'elasticache.RemoveTagsFromResource': lambda store: (
            store.tags.setdefault('el-untag-arn', [{'Key': 'env', 'Value': 'test'}]),
            {'ResourceName': 'el-untag-arn',
             'TagKeys': ['env']})[1],
        'elasticache.ListTagsForResource': lambda store: (
            store.tags.setdefault('el-ltfr-arn', []),
            {'ResourceName': 'el-ltfr-arn'})[1],
        # ── servicecatalog — create ──────────────────────────────────────────
        'CreatePortfolio': {'DisplayName': 'TestPortfolio', 'ProviderName': 'TestProvider'},
        'CreateProduct': {'Name': 'TestProduct', 'Owner': 'TestOwner', 'ProductType': 'CLOUD_FORMATION_TEMPLATE'},
        'CreateTagOption': {'Key': 'env', 'Value': 'test'},
        'CreateConstraint': lambda store: (
            pf := store.create_portfolio('sc-cs-pf', 'sc-cs-prov'),
            pd := store.create_product('sc-cs-pd', 'sc-cs-owner', 'CLOUD_FORMATION_TEMPLATE'),
            {'PortfolioId': pf['Id'], 'ProductId': pd['Id'],
             'Type': 'TEMPLATE', 'Parameters': '{}'})[2],
        'CreateProvisioningArtifact': lambda store: (
            pd := store.create_product('sc-cpa-pd', 'sc-cpa-owner', 'CLOUD_FORMATION_TEMPLATE'),
            {'ProductId': pd['Id'], 'Parameters': {'Name': 'v1', 'Info': {'LoadTemplateFromURL': 'https://example.com/template'}}})[1],
        'AssociateProductWithPortfolio': lambda store: (
            pf := store.create_portfolio('sc-as-pf', 'sc-as-prov'),
            pd := store.create_product('sc-as-pd', 'sc-as-owner', 'CLOUD_FORMATION_TEMPLATE'),
            {'PortfolioId': pf['Id'], 'ProductId': pd['Id']})[2],
        'ProvisionProduct': lambda store: (
            pd := store.create_product('sc-prov-pd', 'sc-prov-owner', 'CLOUD_FORMATION_TEMPLATE'),
            pa := store.create_provisioning_artifact(pd['Id'], 'v1'),
            {'ProductId': pd['Id'], 'ProvisionedProductName': 'TestPP',
             'ProvisioningArtifactId': pa['Id']})[2],
        # ── servicecatalog — list/describe ────────────────────────────────────
        'ListPortfolios': {},
        'SearchProducts': {},
        'SearchProductsAsAdmin': {},
        'ListTagOptions': {},
        'ListProvisioningArtifacts': lambda store: (
            pd := store.create_product('sc-lpa-pd', 'sc-lpa-owner', 'CLOUD_FORMATION_TEMPLATE'),
            store.create_provisioning_artifact(pd['Id'], 'v1'),
            {'ProductId': pd['Id']})[2],
        'DescribePortfolio': lambda store: (
            pf := store.create_portfolio('sc-dp-pf', 'sc-dp-prov'),
            {'Id': pf['Id']})[1],
        'DescribeProduct': lambda store: (
            pd := store.create_product('sc-dpd-pd', 'sc-dpd-owner', 'CLOUD_FORMATION_TEMPLATE'),
            {'Id': pd['Id']})[1],
        'DescribeConstraint': lambda store: (
            pf := store.create_portfolio('sc-dc-pf', 'sc-dc-prov'),
            pd := store.create_product('sc-dc-pd', 'sc-dc-owner', 'CLOUD_FORMATION_TEMPLATE'),
            ct := store.create_constraint(pf['Id'], pd['Id'], 'TEMPLATE', '{}'),
            {'Id': ct['ConstraintId']})[3],
        'DescribeProvisioningArtifact': lambda store: (
            pd := store.create_product('sc-dpa-pd', 'sc-dpa-owner', 'CLOUD_FORMATION_TEMPLATE'),
            pa := store.create_provisioning_artifact(pd['Id'], 'v1'),
            {'ProductId': pd['Id'], 'ProvisioningArtifactId': pa['Id']})[2],
        'DescribeProvisionedProduct': lambda store: (
            pd := store.create_product('sc-dpp-pd', 'sc-dpp-owner', 'CLOUD_FORMATION_TEMPLATE'),
            pa := store.create_provisioning_artifact(pd['Id'], 'v1'),
            pp := store.provision_product(pd['Id'], 'TestPP', pa['Id']),
            {'Id': pp['Id']})[3],
        # ── servicecatalog — delete (lambdas: create prerequisite, then delete) ─
        'DeletePortfolio': lambda store: (
            pf := store.create_portfolio('sc-del-pf', 'sc-del-prov'),
            {'Id': pf['Id']})[1],
        'DeleteProduct': lambda store: (
            pd := store.create_product('sc-del-pd', 'sc-del-owner', 'CLOUD_FORMATION_TEMPLATE'),
            {'Id': pd['Id']})[1],
        'DeleteConstraint': lambda store: (
            pf := store.create_portfolio('sc-del-ct-pf', 'sc-del-ct-prov'),
            pd := store.create_product('sc-del-ct-pd', 'sc-del-ct-owner', 'CLOUD_FORMATION_TEMPLATE'),
            ct := store.create_constraint(pf['Id'], pd['Id'], 'TEMPLATE', '{}'),
            {'Id': ct['ConstraintId']})[3],
        'DeleteProvisioningArtifact': lambda store: (
            pd := store.create_product('sc-del-pa-pd', 'sc-del-pa-owner', 'CLOUD_FORMATION_TEMPLATE'),
            pa := store.create_provisioning_artifact(pd['Id'], 'v1'),
            {'ProductId': pd['Id'], 'ProvisioningArtifactId': pa['Id']})[2],
        'DisassociateProductFromPortfolio': lambda store: (
            pf := store.create_portfolio('sc-dis-pf', 'sc-dis-prov'),
            pd := store.create_product('sc-dis-pd', 'sc-dis-owner', 'CLOUD_FORMATION_TEMPLATE'),
            store.associate_product_with_portfolio(pf['Id'], pd['Id']),
            {'PortfolioId': pf['Id'], 'ProductId': pd['Id']})[3],
        'TerminateProvisionedProduct': lambda store: (
            pd := store.create_product('sc-term-pd', 'sc-term-owner', 'CLOUD_FORMATION_TEMPLATE'),
            pa := store.create_provisioning_artifact(pd['Id'], 'v1'),
            pp := store.provision_product(pd['Id'], 'TestPP', pa['Id']),
            {'ProvisionedProductId': pp['Id']})[3],
        # ── servicecatalog — update (lambdas: create prerequisite, then update) ─
        'UpdatePortfolio': lambda store: (
            pf := store.create_portfolio('sc-upd-pf', 'sc-upd-prov'),
            {'Id': pf['Id'], 'DisplayName': 'UpdatedPortfolio', 'ProviderName': 'UpdatedProvider'})[1],
        'UpdateProduct': lambda store: (
            pd := store.create_product('sc-upd-pd', 'sc-upd-owner', 'CLOUD_FORMATION_TEMPLATE'),
            {'Id': pd['Id'], 'Name': 'UpdatedProduct', 'Owner': 'UpdatedOwner'})[1],
        'UpdateProvisionedProduct': lambda store: (
            pd := store.create_product('sc-upp-pd', 'sc-upp-owner', 'CLOUD_FORMATION_TEMPLATE'),
            pa := store.create_provisioning_artifact(pd['Id'], 'v1'),
            pp := store.provision_product(pd['Id'], 'TestPP', pa['Id']),
            {'ProvisionedProductId': pp['Id']})[3],
        # ── fsx — create ─────────────────────────────────────────────────────
        'CreateFileCache': {'FileCacheType': 'LUSTRE', 'FileCacheTypeVersion': '2.12',
                            'StorageCapacity': 1200, 'SubnetIds': ['subnet-abc123']},
        'CreateFileSystem': {'FileSystemType': 'WINDOWS', 'SubnetIds': ['subnet-abc123']},
        'CreateVolume': {'VolumeType': 'ONTAP', 'Name': 'fsx-test-vol'},
        'CreateBackup': {},
        'CopyBackup': lambda store: (
            bk := store.create_backup(),
            {'SourceBackupId': bk.BackupId})[1],
        'CreateFileSystemFromBackup': lambda store: (
            bk := store.create_backup(),
            {'BackupId': bk.BackupId, 'SubnetIds': ['subnet-abc123']})[1],
        'CreateSnapshot': lambda store: (
            vol := store.create_volume('ONTAP', 'fsx-test-vol'),
            {'Name': 'fsx-test-snap', 'VolumeId': vol.VolumeId})[1],
        'CreateStorageVirtualMachine': lambda store: (
            fs := store.create_file_system('WINDOWS', ['subnet-abc123']),
            {'FileSystemId': fs.FileSystemId, 'Name': 'fsx-test-svm'})[1],
        'CreateVolumeFromBackup': lambda store: (
            vol := store.create_volume('ONTAP', 'test-vol-bk'),
            bk := store.create_backup(VolumeId=vol.VolumeId),
            {'BackupId': bk.BackupId, 'Name': 'restored-vol', 'VolumeType': 'ONTAP'})[2],
        # ── fsx — list/describe ──────────────────────────────────────────────
        'DescribeFileCaches': {},
        'DescribeFileSystems': {},
        'DescribeVolumes': {},
        'DescribeBackups': {},
        'DescribeSnapshots': {},
        'DescribeStorageVirtualMachines': {},
        # ── fsx — delete (lambdas: create prerequisite, then delete) ──────────
        'DeleteFileCache': lambda store: (
            fc := store.create_file_cache('LUSTRE', '2.12', 1200, ['subnet-abc123']),
            {'FileCacheId': fc.FileCacheId})[1],
        'DeleteFileSystem': lambda store: (
            fs := store.create_file_system('WINDOWS', ['subnet-abc123']),
            {'FileSystemId': fs.FileSystemId})[1],
        'DeleteVolume': lambda store: (
            vol := store.create_volume('ONTAP', 'fsx-del-vol'),
            {'VolumeId': vol.VolumeId})[1],
        'DeleteBackup': lambda store: (
            bk := store.create_backup(),
            {'BackupId': bk.BackupId})[1],
        'DeleteSnapshot': lambda store: (
            vol := store.create_volume('ONTAP', 'fsx-snap-vol'),
            snap := store.create_snapshot(Name='fsx-test-snap', VolumeId=vol.VolumeId),
            {'SnapshotId': snap.SnapshotId})[2],
        'DeleteStorageVirtualMachine': lambda store: (
            fs := store.create_file_system('ONTAP', ['subnet-abc123'], StorageCapacity=1200),
            svm := store.create_storage_virtual_machine(FileSystemId=fs.FileSystemId,
                                                        Name='fsx-del-svm'),
            {'StorageVirtualMachineId': svm.StorageVirtualMachineId})[2],
        # ── fsx — update (lambdas: create prerequisite, then update) ──────────
        'UpdateFileCache': lambda store: (
            fc := store.create_file_cache('LUSTRE', '2.12', 1200, ['subnet-abc123']),
            {'FileCacheId': fc.FileCacheId, 'ClientRequestToken': 'tok'})[1],
        'UpdateFileSystem': lambda store: (
            fs := store.create_file_system('WINDOWS', ['subnet-abc123']),
            {'FileSystemId': fs.FileSystemId})[1],
        'UpdateVolume': lambda store: (
            vol := store.create_volume('ONTAP', 'fsx-upd-vol'),
            {'VolumeId': vol.VolumeId, 'Name': 'fsx-updated-vol'})[1],
        'UpdateSnapshot': lambda store: (
            vol := store.create_volume('ONTAP', 'fsx-upd-vol'),
            snap := store.create_snapshot(Name='fsx-upd-snap-old', VolumeId=vol.VolumeId),
            {'SnapshotId': snap.SnapshotId, 'Name': 'fsx-updated-snap'})[2],
        'UpdateStorageVirtualMachine': lambda store: (
            fs := store.create_file_system('ONTAP', ['subnet-abc123'], StorageCapacity=1200),
            svm := store.create_storage_virtual_machine(FileSystemId=fs.FileSystemId,
                                                        Name='fsx-upd-svm'),
            {'StorageVirtualMachineId': svm.StorageVirtualMachineId,
             'ActiveDirectoryConfiguration': {'SelfManagedActiveDirectoryConfiguration': {
                 'DomainName': 'corp.example.com',
                 'OrganizationalUnitDistinguishedName': 'OU=FileSystems,DC=corp,DC=example,DC=com',
                 'FileSystemAdministratorsGroup': 'FSxAdmins',
                 'UserName': 'Admin',
                 'Password': 'Passw0rd!',
                 'DnsIps': ['10.0.1.4', '10.0.2.5']}}})[2],
        # ── fsx — tag/untag (service-prefixed keys) ───────────────────────────
        'fsx.ListTagsForResource': lambda store: (
            fs := store.create_file_system('WINDOWS', ['subnet-abc123']),
            {'ResourceARN': f'arn:aws:fsx:us-east-1:000000000000:file-system/{fs.FileSystemId}'})[1],
        'fsx.TagResource': lambda store: (
            fs := store.create_file_system('WINDOWS', ['subnet-abc123']),
            {'ResourceARN': f'arn:aws:fsx:us-east-1:000000000000:file-system/{fs.FileSystemId}',
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[1],
        'fsx.UntagResource': lambda store: (
            fs := store.create_file_system('WINDOWS', ['subnet-abc123']),
            {'ResourceARN': f'arn:aws:fsx:us-east-1:000000000000:file-system/{fs.FileSystemId}',
             'TagKeys': ['env']})[1],
        # ── memorydb — create ─────────────────────────────────────────────────
        'CreateCluster': {'ClusterName': 'test-cluster', 'NodeType': 'db.r6gd.xlarge',
                           'ACLName': 'open-access'},
        'CreateACL': {'ACLName': 'test-acl'},
        'CreateUser': {'UserName': 'test-user',
                        'AuthenticationMode': {'Type': 'password', 'Passwords': ['Test1234!']}},
        'CreateParameterGroup': {'ParameterGroupName': 'test-pg', 'Family': 'memorydb_redis7'},
        'CreateSubnetGroup': {'SubnetGroupName': 'test-sg', 'SubnetIds': ['subnet-abc123']},
        'CreateSnapshot': lambda store: (
            store.create_cluster(ClusterName='mem-snap-cluster', NodeType='db.r6gd.xlarge',
                                 ACLName='open-access'),
            {'SnapshotName': 'test-snap', 'ClusterName': 'mem-snap-cluster'})[1],
        # ── memorydb — list/describe ──────────────────────────────────────────
        'DescribeClusters': {},
        'DescribeACLs': {},
        'DescribeUsers': {},
        'DescribeParameterGroups': {},
        'DescribeSubnetGroups': {},
        'DescribeSnapshots': {},
        # ── memorydb — delete (lambdas: create prerequisite, then delete) ──────
        'DeleteCluster': lambda store: (
            store.create_cluster(ClusterName='mem-del-cluster', NodeType='db.r6gd.xlarge',
                                 ACLName='open-access'),
            {'ClusterName': 'mem-del-cluster'})[1],
        'DeleteACL': lambda store: (
            store.create_acl(ACLName='mem-del-acl'),
            {'ACLName': 'mem-del-acl'})[1],
        'DeleteUser': lambda store: (
            store.create_user(UserName='mem-del-user',
                              AuthenticationMode={'Type': 'password', 'Passwords': ['Test1234!']}),
            {'UserName': 'mem-del-user'})[1],
        'DeleteParameterGroup': lambda store: (
            store.create_parameter_group(ParameterGroupName='mem-del-pg', Family='memorydb_redis7'),
            {'ParameterGroupName': 'mem-del-pg'})[1],
        'DeleteSubnetGroup': lambda store: (
            store.create_subnet_group(SubnetGroupName='mem-del-sg', SubnetIds=['subnet-abc123']),
            {'SubnetGroupName': 'mem-del-sg'})[1],
        'DeleteSnapshot': lambda store: (
            store.create_cluster(ClusterName='mem-ds-cluster', NodeType='db.r6gd.xlarge',
                                 ACLName='open-access'),
            store.create_snapshot(SnapshotName='mem-del-snap', ClusterName='mem-ds-cluster'),
            {'SnapshotName': 'mem-del-snap'})[2],
        # ── memorydb — update (lambdas: create prerequisite, then update) ──────
        'UpdateCluster': lambda store: (
            store.create_cluster(ClusterName='mem-upd-cluster', NodeType='db.r6gd.xlarge',
                                 ACLName='open-access'),
            {'ClusterName': 'mem-upd-cluster', 'Description': 'Updated cluster'})[1],
        'UpdateACL': lambda store: (
            store.create_acl(ACLName='mem-upd-acl'),
            {'ACLName': 'mem-upd-acl', 'UserNames': ['test-user']})[1],
        'UpdateUser': lambda store: (
            store.create_user(UserName='mem-upd-user',
                              AuthenticationMode={'Type': 'password', 'Passwords': ['Test1234!']}),
            {'UserName': 'mem-upd-user', 'AccessString': 'off ~*'})[1],
        'UpdateParameterGroup': lambda store: (
            store.create_parameter_group(ParameterGroupName='mem-upd-pg', Family='memorydb_redis7'),
            {'ParameterGroupName': 'mem-upd-pg', 'Description': 'Updated PG'})[1],
        'UpdateSubnetGroup': lambda store: (
            store.create_subnet_group(SubnetGroupName='mem-upd-sg', SubnetIds=['subnet-abc123']),
            {'SubnetGroupName': 'mem-upd-sg', 'Description': 'Updated SG'})[1],
        # ── memorydb — misc ───────────────────────────────────────────────────
        'ResetParameterGroup': lambda store: (
            store.create_parameter_group(ParameterGroupName='mem-rst-pg', Family='memorydb_redis7'),
            {'ParameterGroupName': 'mem-rst-pg'})[1],
        'ListTags': lambda store: (
            store.create_cluster(ClusterName='mem-lt-cluster', NodeType='db.r6gd.xlarge',
                                 ACLName='open-access'),
            cl := store.describe_clusters('mem-lt-cluster'),
            {'ResourceArn': cl['Clusters'][0]['ARN']})[2],
        'memorydb.TagResource': lambda store: (
            store.create_cluster(ClusterName='mem-tr-cluster', NodeType='db.r6gd.xlarge',
                                 ACLName='open-access'),
            cl := store.describe_clusters('mem-tr-cluster'),
            {'ResourceArn': cl['Clusters'][0]['ARN'],
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[2],
        'memorydb.UntagResource': lambda store: (
            store.create_cluster(ClusterName='mem-utr-cluster', NodeType='db.r6gd.xlarge',
                                 ACLName='open-access'),
            cl := store.describe_clusters('mem-utr-cluster'),
            {'ResourceArn': cl['Clusters'][0]['ARN'],
             'TagKeys': ['env']})[2],
        # ── redshift — create ──────────────────────────────────────────────────
        'CreateCluster': {'ClusterIdentifier': 'test-cluster', 'NodeType': 'dc2.large',
                           'MasterUsername': 'admin'},
        'CreateClusterParameterGroup': {'ParameterGroupName': 'test-pg',
                                         'ParameterGroupFamily': 'redshift-1.0',
                                         'Description': 'Test parameter group'},
        'CreateClusterSnapshot': lambda store: (
            store.create_cluster(ClusterIdentifier='red-snap-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            {'SnapshotIdentifier': 'test-snap',
             'ClusterIdentifier': 'red-snap-cluster'})[1],
        'CreateClusterSubnetGroup': {'ClusterSubnetGroupName': 'test-sg',
                                      'Description': 'Test subnet group',
                                      'SubnetIds': ['subnet-abc123']},
        'CreateEventSubscription': {'SubscriptionName': 'test-sub',
                                     'SnsTopicArn': 'arn:aws:sns:us-east-1:000000000000:test'},
        # ── redshift — list/describe ───────────────────────────────────────────
        'DescribeClusters': {},
        'DescribeClusterParameterGroups': {},
        'DescribeClusterSnapshots': {},
        'DescribeClusterSubnetGroups': {},
        'DescribeEventSubscriptions': {},
        # ── redshift — delete (lambdas: create prerequisite, then delete) ──────
        'DeleteCluster': lambda store: (
            store.create_cluster(ClusterIdentifier='red-del-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            {'ClusterIdentifier': 'red-del-cluster',
             'SkipFinalClusterSnapshot': True})[1],
        'DeleteClusterParameterGroup': lambda store: (
            store.create_cluster_parameter_group(ParameterGroupName='red-del-pg',
                                                  ParameterGroupFamily='redshift-1.0',
                                                  Description='Delete me'),
            {'ParameterGroupName': 'red-del-pg'})[1],
        'DeleteClusterSnapshot': lambda store: (
            store.create_cluster(ClusterIdentifier='red-ds-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            store.create_cluster_snapshot(SnapshotIdentifier='red-del-snap',
                                          ClusterIdentifier='red-ds-cluster'),
            {'SnapshotIdentifier': 'red-del-snap'})[2],
        'DeleteClusterSubnetGroup': lambda store: (
            store.create_cluster_subnet_group(ClusterSubnetGroupName='red-del-sg',
                                               Description='Delete me',
                                               SubnetIds=['subnet-abc123']),
            {'ClusterSubnetGroupName': 'red-del-sg'})[1],
        'DeleteEventSubscription': lambda store: (
            store.create_event_subscription(SubscriptionName='red-del-sub',
                                             SnsTopicArn='arn:aws:sns:us-east-1:000000000000:test'),
            {'SubscriptionName': 'red-del-sub'})[1],
        # ── redshift — modify (lambdas: create prerequisite, then modify) ──────
        'ModifyCluster': lambda store: (
            store.create_cluster(ClusterIdentifier='red-mod-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            {'ClusterIdentifier': 'red-mod-cluster',
             'MasterUserPassword': 'NewPass123!'})[1],
        'ModifyClusterParameterGroup': lambda store: (
            store.create_cluster_parameter_group(ParameterGroupName='red-mod-pg',
                                                  ParameterGroupFamily='redshift-1.0',
                                                  Description='Modify me'),
            {'ParameterGroupName': 'red-mod-pg',
             'Parameters': [{'ParameterName': 'max_connections', 'ParameterValue': '100'}]})[1],
        'ModifyClusterSubnetGroup': lambda store: (
            store.create_cluster_subnet_group(ClusterSubnetGroupName='red-mod-sg',
                                               Description='Modify me',
                                               SubnetIds=['subnet-abc123']),
            {'ClusterSubnetGroupName': 'red-mod-sg',
             'SubnetIds': ['subnet-xyz789']})[1],
        'ModifyEventSubscription': lambda store: (
            store.create_event_subscription(SubscriptionName='red-mod-sub',
                                             SnsTopicArn='arn:aws:sns:us-east-1:000000000000:test'),
            {'SubscriptionName': 'red-mod-sub',
             'Enabled': False})[1],
        # ── redshift — cluster operations (lambdas: create prerequisite) ───────
        'PauseCluster': lambda store: (
            store.create_cluster(ClusterIdentifier='red-pause-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            {'ClusterIdentifier': 'red-pause-cluster'})[1],
        'ResumeCluster': lambda store: (
            store.create_cluster(ClusterIdentifier='red-resume-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            {'ClusterIdentifier': 'red-resume-cluster'})[1],
        'RebootCluster': lambda store: (
            store.create_cluster(ClusterIdentifier='red-reboot-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            {'ClusterIdentifier': 'red-reboot-cluster'})[1],
        'ResizeCluster': lambda store: (
            store.create_cluster(ClusterIdentifier='red-resize-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            {'ClusterIdentifier': 'red-resize-cluster', 'NodeType': 'dc2.8xlarge',
             'NumberOfNodes': 4})[1],
        # ── redshift — snapshot copy + parameter reset ────────────────────────
        'CopyClusterSnapshot': lambda store: (
            store.create_cluster(ClusterIdentifier='red-copy-cluster', NodeType='dc2.large',
                                 MasterUsername='admin'),
            store.create_cluster_snapshot(SnapshotIdentifier='red-src-snap',
                                          ClusterIdentifier='red-copy-cluster'),
            {'SourceSnapshotIdentifier': 'red-src-snap',
             'TargetSnapshotIdentifier': 'red-tgt-snap'})[2],
        'ResetClusterParameterGroup': lambda store: (
            store.create_cluster_parameter_group(ParameterGroupName='red-rst-pg',
                                                  ParameterGroupFamily='redshift-1.0',
                                                  Description='Reset me'),
            {'ParameterGroupName': 'red-rst-pg',
             'ResetAllParameters': True})[1],
        # ── network-firewall — create (policy first, then firewall + rule-group) ─
        'CreateFirewallPolicy': {
            'FirewallPolicyName': 'nfw-test-policy',
            'FirewallPolicy': {'StatelessDefaultActions': ['aws:forward_to_sfe'],
                               'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']},
        },
        'CreateFirewall': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-fw-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            {'FirewallName': 'nfw-test-fw',
             'FirewallPolicyArn': store.policies()[-1].FirewallPolicyArn})[1],
        'CreateRuleGroup': {
            'RuleGroupName': 'nfw-test-rg',
            'Type': 'STATELESS',
            'Capacity': 100,
            'RuleGroup': {'RulesSource': {}},
        },
        # ── network-firewall — list ─────────────────────────────────────────
        'ListFirewalls': {},
        'ListFirewallPolicies': {},
        'ListRuleGroups': {},
        # ── network-firewall — describe (lambdas: create prerequisite) ──────
        'DescribeFirewall': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-desc-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-desc-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn})[2],
        'DescribeFirewallPolicy': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-desc-pol',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            {'FirewallPolicyArn': store.policies()[-1].FirewallPolicyArn})[1],
        'DescribeFirewallMetadata': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-meta-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-meta-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn})[2],
        'DescribeRuleGroup': lambda store: (
            store.create_rule_group(RuleGroupName='nfw-desc-rg', Type='STATELESS',
                Capacity=100, RuleGroup={'RulesSource': {}}),
            {'RuleGroupArn': store.rule_groups()[-1].RuleGroupArn})[1],
        # ── network-firewall — delete (lambdas: create prerequisite) ────────
        'DeleteFirewall': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-del-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-del-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn})[2],
        'DeleteFirewallPolicy': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-del-pol',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            {'FirewallPolicyArn': store.policies()[-1].FirewallPolicyArn})[1],
        'DeleteRuleGroup': lambda store: (
            store.create_rule_group(RuleGroupName='nfw-del-rg', Type='STATELESS',
                Capacity=100, RuleGroup={'RulesSource': {}}),
            {'RuleGroupArn': store.rule_groups()[-1].RuleGroupArn})[1],
        # ── network-firewall — tag/untag (service-prefixed keys) ────────────
        'network-firewall.TagResource': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-tag-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-tag-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'ResourceArn': store.firewalls()[-1].FirewallArn,
             'Tags': [{'Key': 'env', 'Value': 'test'}]})[2],
        'network-firewall.UntagResource': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-untag-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-untag-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            store.tag_resource(ResourceArn=store.firewalls()[-1].FirewallArn,
                Tags=[{'Key': 'env', 'Value': 'test'}]),
            {'ResourceArn': store.firewalls()[-1].FirewallArn,
             'TagKeys': ['env']})[3],
        'network-firewall.ListTagsForResource': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-ltr-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-ltr-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            store.tag_resource(ResourceArn=store.firewalls()[-1].FirewallArn,
                Tags=[{'Key': 'env', 'Value': 'test'}]),
            {'ResourceArn': store.firewalls()[-1].FirewallArn})[3],
        # ── network-firewall — update (lambdas: create prerequisite) ────────
        'AssociateFirewallPolicy': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-asc-pol1',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall_policy(FirewallPolicyName='nfw-asc-pol2',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-asc-fw',
                FirewallPolicyArn=store.policies()[-2].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn,
             'FirewallPolicyArn': store.policies()[-1].FirewallPolicyArn})[3],
        'UpdateFirewallDeleteProtection': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-udp-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-udp-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn,
             'DeleteProtection': True})[2],
        'UpdateFirewallDescription': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-udesc-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-udesc-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn,
             'Description': 'Updated description'})[2],
        'UpdateFirewallPolicyChangeProtection': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-upcp-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-upcp-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn,
             'FirewallPolicyChangeProtection': True})[2],
        'UpdateSubnetChangeProtection': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-usc-policy',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            store.create_firewall(FirewallName='nfw-usc-fw',
                FirewallPolicyArn=store.policies()[-1].FirewallPolicyArn),
            {'FirewallArn': store.firewalls()[-1].FirewallArn,
             'SubnetChangeProtection': True})[2],
        'UpdateFirewallPolicy': lambda store: (
            store.create_firewall_policy(FirewallPolicyName='nfw-up-pol',
                FirewallPolicy={'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe']}),
            {'UpdateToken': 'update-token',
             'FirewallPolicyArn': store.policies()[-1].FirewallPolicyArn,
             'FirewallPolicy': {'StatelessDefaultActions': ['aws:forward_to_sfe'],
                                'StatelessFragmentDefaultActions': ['aws:forward_to_sfe'],
                                'StatefulDefaultActions': ['aws:drop_strict']}})[1],
        'UpdateRuleGroup': lambda store: (
            store.create_rule_group(RuleGroupName='nfw-urg-rg', Type='STATELESS',
                Capacity=100, RuleGroup={'RulesSource': {}}),
            {'UpdateToken': 'update-token',
             'RuleGroupArn': store.rule_groups()[-1].RuleGroupArn,
             'RuleGroup': {'RulesSource': {'StatelessRulesAndCustomActions': {'StatelessRules': []}}}})[1],
        # ── ram — create ──────────────────────────────────────────────────────
        'CreateResourceShare': {'name': 'test-ram-share'},
        'CreatePermission': {'name': 'test-ram-perm', 'resourceType': 'ec2:Instance',
                              'policyTemplate': '{"Effect":"Allow"}'},
        'CreatePermissionVersion': lambda store: (
            store.create_permission(name='ram-cpv-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            {'permissionArn': store.permissions()[0].permissionArn,
             'policyTemplate': '{"Effect":"AllowV2"}'})[1],
        # ── ram — list/describe (simple) ─────────────────────────────────────
        'ListPermissions': {},
        'ListResourceTypes': {},
        'ListResources': {},
        'ListPrincipals': {},
        'GetResourceShares': {},
        'GetResourceShareInvitations': {},
        'GetResourceShareAssociations': {'associationType': 'PRINCIPAL'},
        'EnableSharingWithAwsOrganization': {},
        # ── ram — get (lambdas: create prerequisite, then get) ──────────────
        'GetPermission': lambda store: (
            store.create_permission(name='ram-get-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            {'permissionArn': store.permissions()[0].permissionArn})[1],
        'ListPermissionVersions': lambda store: (
            store.create_permission(name='ram-lpv-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            {'permissionArn': store.permissions()[0].permissionArn})[1],
        'ListResourceSharePermissions': lambda store: (
            store.create_resource_share(name='ram-lrsp-share'),
            {'resourceShareArn': store.resource_shares()[0].resourceShareArn})[1],
        # ── ram — delete (lambdas: create prerequisite, then delete) ────────
        'DeleteResourceShare': lambda store: (
            store.create_resource_share(name='ram-del-share'),
            {'resourceShareArn': store.resource_shares()[0].resourceShareArn})[1],
        'DeletePermission': lambda store: (
            store.create_permission(name='ram-del-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            {'permissionArn': store.permissions()[0].permissionArn})[1],
        'DeletePermissionVersion': lambda store: (
            store.create_permission(name='ram-dpv-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            store.create_permission_version(store.permissions()[0].permissionArn,
                                            '{"Effect":"AllowV2"}'),
            {'permissionArn': store.permissions()[0].permissionArn,
             'permissionVersion': 2})[2],
        # ── ram — update (lambdas: create prerequisite, then update) ────────
        'UpdateResourceShare': lambda store: (
            store.create_resource_share(name='ram-upd-share'),
            {'resourceShareArn': store.resource_shares()[0].resourceShareArn,
             'name': 'ram-updated-share'})[1],
        'SetDefaultPermissionVersion': lambda store: (
            store.create_permission(name='ram-sdpv-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            store.create_permission_version(store.permissions()[0].permissionArn,
                                            '{"Effect":"AllowV2"}'),
            {'permissionArn': store.permissions()[0].permissionArn,
             'permissionVersion': 2})[2],
        # ── ram — associate/disassociate (lambdas: create both, then operate) ─
        'AssociateResourceSharePermission': lambda store: (
            store.create_resource_share(name='ram-asp-share'),
            store.create_permission(name='ram-asp-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            {'resourceShareArn': store.resource_shares()[0].resourceShareArn,
             'permissionArn': store.permissions()[0].permissionArn})[2],
        'AssociateResourceShare': lambda store: (
            store.create_resource_share(name='ram-as-share'),
            {'resourceShareArn': store.resource_shares()[0].resourceShareArn,
             'resourceArns': ['arn:aws:ec2:us-east-1:000000000000:instance/i-test'],
             'principals': ['000000000000']})[1],
        'DisassociateResourceSharePermission': lambda store: (
            store.create_resource_share(name='ram-dsp-share'),
            store.create_permission(name='ram-dsp-perm', resourceType='ec2:Instance',
                                    policyTemplate='{"Effect":"Allow"}'),
            store.associate_resource_share_permission(
                store.resource_shares()[0].resourceShareArn,
                store.permissions()[0].permissionArn),
            {'resourceShareArn': store.resource_shares()[0].resourceShareArn,
             'permissionArn': store.permissions()[0].permissionArn})[3],
        'DisassociateResourceShare': lambda store: (
            store.create_resource_share(name='ram-ds-share'),
            store.associate_resource_share(store.resource_shares()[0].resourceShareArn,
                                           resourceArns=['arn:aws:ec2:us-east-1:000000000000:instance/i-test']),
            {'resourceShareArn': store.resource_shares()[0].resourceShareArn,
             'resourceArns': ['arn:aws:ec2:us-east-1:000000000000:instance/i-test']})[2],
        # ── ram — tag/untag (service-prefixed keys, lambdas: create, then tag) ─
        'ram.TagResource': lambda store: (
            store.create_resource_share(name='ram-tag-share'),
            {'resourceShareArn': store.resource_shares()[-1].resourceShareArn,
             'tags': [{'key': 'env', 'value': 'test'}]})[1],
        'ram.UntagResource': lambda store: (
            store.create_resource_share(name='ram-untag-share'),
            store.tag_resource(resourceShareArn=store.resource_shares()[-1].resourceShareArn,
                               tags=[{'key': 'env', 'value': 'test'}]),
            {'resourceShareArn': store.resource_shares()[-1].resourceShareArn,
             'tagKeys': ['env']})[2],
        # ── ram — invitation (lambdas: create share + invitation, then operate) ─
        'AcceptResourceShareInvitation': lambda store: (
            store.create_resource_share(name='ram-acc-share'),
            store.create_invitation(store.resource_shares()[-1].resourceShareArn),
            {'resourceShareInvitationArn': store.invitations()[-1].resourceShareInvitationArn})[2],
        'RejectResourceShareInvitation': lambda store: (
            store.create_resource_share(name='ram-rej-share'),
            store.create_invitation(store.resource_shares()[-1].resourceShareArn),
            {'resourceShareInvitationArn': store.invitations()[-1].resourceShareInvitationArn})[2],
        # ── appsync — create ──────────────────────────────────────────────────
        'CreateGraphqlApi': {'name': 'as-test-api', 'authenticationType': 'API_KEY'},
        # ── appsync — list (simple: no prerequisite api needed) ────────────────
        'ListGraphqlApis': {},
        'ListApiKeys': {'apiId': 'as-test-api'},
        'ListDataSources': {'apiId': 'as-test-api'},
        'ListResolvers': {'apiId': 'as-test-api', 'typeName': 'Query'},
        # ── appsync — create (dependent ops: need api created first) ──────────
        'CreateApiKey': lambda store: (
            api := store.create_graphql_api('as-cak-api', 'API_KEY')['graphqlApi'],
            {'apiId': api['apiId']})[1],
        'CreateDataSource': lambda store: (
            api := store.create_graphql_api('as-cds-api', 'API_KEY')['graphqlApi'],
            {'apiId': api['apiId'], 'name': 'as-cds-ds', 'type': 'AWS_LAMBDA'})[1],
        'CreateResolver': lambda store: (
            api := store.create_graphql_api('as-crsv-api', 'API_KEY')['graphqlApi'],
            {'apiId': api['apiId'], 'typeName': 'Query', 'fieldName': 'getItem'})[1],
        # ── appsync — get/describe (lambdas: create prerequisite, then get) ──
        'GetGraphqlApi': lambda store: (
            api := store.create_graphql_api('as-get-api', 'API_KEY')['graphqlApi'],
            {'apiId': api['apiId']})[1],
        'GetDataSource': lambda store: (
            api := store.create_graphql_api('as-gds-api', 'API_KEY')['graphqlApi'],
            ds := store.create_data_source(api['apiId'], 'as-gds-ds', 'AWS_LAMBDA')['dataSource'],
            {'apiId': api['apiId'], 'name': ds['name']})[2],
        'GetResolver': lambda store: (
            api := store.create_graphql_api('as-grsv-api', 'API_KEY')['graphqlApi'],
            rsv := store.create_resolver(api['apiId'], 'Query', 'getItem')['resolver'],
            {'apiId': api['apiId'], 'typeName': rsv['typeName'], 'fieldName': rsv['fieldName']})[2],
        # ── appsync — delete (lambdas: create prerequisite, then delete) ──────
        'DeleteGraphqlApi': lambda store: (
            api := store.create_graphql_api('as-del-api', 'API_KEY')['graphqlApi'],
            {'apiId': api['apiId']})[1],
        'DeleteDataSource': lambda store: (
            api := store.create_graphql_api('as-dds-api', 'API_KEY')['graphqlApi'],
            ds := store.create_data_source(api['apiId'], 'as-dds-ds', 'AWS_LAMBDA')['dataSource'],
            {'apiId': api['apiId'], 'name': ds['name']})[2],
        'DeleteResolver': lambda store: (
            api := store.create_graphql_api('as-drsv-api', 'API_KEY')['graphqlApi'],
            rsv := store.create_resolver(api['apiId'], 'Query', 'getItem')['resolver'],
            {'apiId': api['apiId'], 'typeName': rsv['typeName'], 'fieldName': rsv['fieldName']})[2],
        'DeleteApiKey': lambda store: (
            api := store.create_graphql_api('as-dak-api', 'API_KEY')['graphqlApi'],
            key := store.create_api_key(api['apiId'])['apiKey'],
            {'apiId': api['apiId'], 'id': key['id']})[2],
        # ── appsync — update (lambdas: create prerequisite, then update) ──────
        'UpdateGraphqlApi': lambda store: (
            api := store.create_graphql_api('as-upd-api', 'API_KEY')['graphqlApi'],
            {'apiId': api['apiId'], 'name': 'as-updated-api', 'authenticationType': 'AWS_IAM'})[1],
        'UpdateDataSource': lambda store: (
            api := store.create_graphql_api('as-uds-api', 'API_KEY')['graphqlApi'],
            ds := store.create_data_source(api['apiId'], 'as-uds-ds', 'AWS_LAMBDA')['dataSource'],
            {'apiId': api['apiId'], 'name': ds['name'], 'type': 'AMAZON_DYNAMODB'})[2],
        'UpdateResolver': lambda store: (
            api := store.create_graphql_api('as-ursv-api', 'API_KEY')['graphqlApi'],
            rsv := store.create_resolver(api['apiId'], 'Query', 'getItem')['resolver'],
            {'apiId': api['apiId'], 'typeName': rsv['typeName'], 'fieldName': rsv['fieldName']})[2],
        'UpdateApiKey': lambda store: (
            api := store.create_graphql_api('as-uak-api', 'API_KEY')['graphqlApi'],
            key := store.create_api_key(api['apiId'])['apiKey'],
            {'apiId': api['apiId'], 'id': key['id']})[2],
        # ── appsync — tag/untag (service-prefixed keys) ───────────────────────
        'appsync.TagResource': lambda store: (
            api := store.create_graphql_api('as-tag-api', 'API_KEY')['graphqlApi'],
            {'resourceArn': api['arn'], 'tags': [{'key': 'env', 'value': 'test'}]})[1],
        'appsync.UntagResource': lambda store: (
            api := store.create_graphql_api('as-untag-api', 'API_KEY')['graphqlApi'],
            store.tag_resource(api['arn'], [{'key': 'env', 'value': 'test'}]),
            {'resourceArn': api['arn'], 'tagKeys': ['env']})[2],
        'appsync.ListTagsForResource': lambda store: (
            api := store.create_graphql_api('as-ltr-api', 'API_KEY')['graphqlApi'],
            store.tag_resource(api['arn'], [{'key': 'env', 'value': 'test'}]),
            {'resourceArn': api['arn']})[2],
        # ── textract — synchronous analysis (plain dicts) ──────────────────────
        'AnalyzeDocument': {'Document': {'Bytes': 'dGVzdA=='}, 'FeatureTypes': ['TABLES']},
        'AnalyzeExpense': {'Document': {'Bytes': 'dGVzdA=='}},
        'AnalyzeID': {'DocumentPages': [{'Document': {'Bytes': 'dGVzdA=='}}]},
        'DetectDocumentText': {'Document': {'Bytes': 'dGVzdA=='}},
        # ── textract — adapter CRUD ────────────────────────────────────────────
        'CreateAdapter': {'AdapterName': 'tx-adapter', 'FeatureTypes': ['TABLES']},
        'ListAdapters': {},
        'GetAdapter': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-get-adapter', adapter_name='get-me', feature_types=['TABLES'])),
            {'AdapterId': 'tx-get-adapter'})[1],
        'UpdateAdapter': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-upd-adapter', adapter_name='update-me', feature_types=['TABLES'])),
            {'AdapterId': 'tx-upd-adapter', 'AdapterName': 'tx-updated', 'AutoUpdate': 'ENABLED'})[1],
        'DeleteAdapter': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-del-adapter', adapter_name='delete-me', feature_types=['TABLES'])),
            {'AdapterId': 'tx-del-adapter'})[1],
        'CreateAdapterVersion': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-ver-adapter', adapter_name='version-me', feature_types=['TABLES'])),
            {'AdapterId': 'tx-ver-adapter'})[1],
        'ListAdapterVersions': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-lv-adapter', adapter_name='list-versions', feature_types=['TABLES'])),
            {'AdapterId': 'tx-lv-adapter'})[1],
        'GetAdapterVersion': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-gv-adapter', adapter_name='get-version', feature_types=['TABLES'])),
            store.get_adapter('tx-gv-adapter').versions.__setitem__('1', AdapterVersionRecord(adapter_version='1', creation_time=0, status='ACTIVE')),
            {'AdapterId': 'tx-gv-adapter', 'AdapterVersion': '1'})[2],
        'DeleteAdapterVersion': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-dv-adapter', adapter_name='del-version', feature_types=['TABLES'])),
            store.get_adapter('tx-dv-adapter').versions.__setitem__('1', AdapterVersionRecord(adapter_version='1', creation_time=0)),
            {'AdapterId': 'tx-dv-adapter', 'AdapterVersion': '1'})[2],
        # ── textract — async job operations ────────────────────────────────────
        'StartDocumentAnalysis': {'DocumentLocation': {'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}}, 'FeatureTypes': ['TABLES']},
        'StartDocumentTextDetection': {'DocumentLocation': {'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}}},
        'StartExpenseAnalysis': {'DocumentLocation': {'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}}},
        'StartLendingAnalysis': {'DocumentLocation': {'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}}},
        'GetDocumentAnalysis': lambda store: (
            job := store.put_job(JobRecord(job_id='tx-da-job', api='StartDocumentAnalysis', document_location={'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}}, feature_types=['TABLES'])),
            {'JobId': 'tx-da-job'})[1],
        'GetDocumentTextDetection': lambda store: (
            job := store.put_job(JobRecord(job_id='tx-dtd-job', api='StartDocumentTextDetection', document_location={'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}})),
            {'JobId': 'tx-dtd-job'})[1],
        'GetExpenseAnalysis': lambda store: (
            job := store.put_job(JobRecord(job_id='tx-ea-job', api='StartExpenseAnalysis', document_location={'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}})),
            {'JobId': 'tx-ea-job'})[1],
        'GetLendingAnalysis': lambda store: (
            job := store.put_job(JobRecord(job_id='tx-la-job', api='StartLendingAnalysis', document_location={'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}})),
            {'JobId': 'tx-la-job'})[1],
        'GetLendingAnalysisSummary': lambda store: (
            job := store.put_job(JobRecord(job_id='tx-las-job', api='StartLendingAnalysis', document_location={'S3Object': {'Bucket': 'tx-bucket', 'Name': 'doc.pdf'}})),
            {'JobId': 'tx-las-job'})[1],
        # ── textract — tags (service-prefixed keys) ────────────────────────────
        'textract.TagResource': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-tag-adapter', adapter_name='tag-me', feature_types=['TABLES'])),
            {'ResourceARN': 'arn:aws:textract:us-east-1:000000000000:adapter/tx-tag-adapter', 'Tags': {'env': 'test'}})[1],
        'textract.UntagResource': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-untag-adapter', adapter_name='untag-me', feature_types=['TABLES'])),
            store.tag_resource('arn:aws:textract:us-east-1:000000000000:adapter/tx-untag-adapter', {'env': 'test'}),
            {'ResourceARN': 'arn:aws:textract:us-east-1:000000000000:adapter/tx-untag-adapter', 'TagKeys': ['env']})[2],
        'textract.ListTagsForResource': lambda store: (
            store.put_adapter(AdapterRecord(adapter_id='tx-ltr-adapter', adapter_name='ltr-me', feature_types=['TABLES'])),
            store.tag_resource('arn:aws:textract:us-east-1:000000000000:adapter/tx-ltr-adapter', {'env': 'test'}),
            {'ResourceARN': 'arn:aws:textract:us-east-1:000000000000:adapter/tx-ltr-adapter'})[2],
        # ── s3tables — create bucket ──────────────────────────────────────────
        'CreateTableBucket': {'name': 's3t-shape-test'},
        # ── s3tables — list ───────────────────────────────────────────────────
        'ListTableBuckets': {},
        'ListNamespaces': lambda store: (
            bucket := store.create_table_bucket(name='s3t-lns-bucket'),
            {'tableBucketARN': bucket['tableBucketARN']})[1],
        'ListTables': lambda store: (
            bucket := store.create_table_bucket(name='s3t-ltb-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default'})[2],
        # ── s3tables — get (lambdas: create bucket first) ──────────────────────
        'GetTableBucket': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtb-bucket'),
            {'tableBucketARN': bucket['tableBucketARN']})[1],
        'GetNamespace': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gn-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default'})[2],
        'GetTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gt-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            store.create_table(bucket['tableBucketARN'], 'default', 'test-table', format='ICEBERG'),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default', 'name': 'test-table'})[3],
        'GetTableBucketEncryption': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtbe-bucket'),
            {'tableBucketARN': bucket['tableBucketARN']})[1],
        'GetTableEncryption': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gte-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            store.create_table(bucket['tableBucketARN'], 'default', 'test-table', format='ICEBERG'),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default', 'name': 'test-table'})[3],
        'GetTableMaintenanceConfiguration': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtmc-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            store.create_table(bucket['tableBucketARN'], 'default', 'test-table', format='ICEBERG'),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default', 'name': 'test-table'})[3],
        'GetTableBucketMaintenanceConfiguration': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtbmc-bucket'),
            {'tableBucketARN': bucket['tableBucketARN']})[1],
        # ── s3tables — create namespace/table (lambdas: bucket prerequisite) ───
        'CreateNamespace': lambda store: (
            bucket := store.create_table_bucket(name='s3t-cn-bucket'),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': ['default']})[1],
        'CreateTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-ct-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default', 'name': 'test-table', 'format': 'ICEBERG'})[2],
        # ── s3tables — delete (lambdas: create prerequisite, then delete) ──────
        'DeleteTableBucket': lambda store: (
            bucket := store.create_table_bucket(name='s3t-dtb-bucket'),
            {'tableBucketARN': bucket['tableBucketARN']})[1],
        'DeleteNamespace': lambda store: (
            bucket := store.create_table_bucket(name='s3t-dn-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default'})[2],
        'DeleteTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-dt-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            store.create_table(bucket['tableBucketARN'], 'default', 'del-table', format='ICEBERG'),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default', 'name': 'del-table'})[3],
        # ── s3tables — rename ──────────────────────────────────────────────────
        'RenameTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-rt-bucket'),
            store.create_namespace(bucket['tableBucketARN'], ['default']),
            store.create_table(bucket['tableBucketARN'], 'default', 'old-table', format='ICEBERG'),
            {'tableBucketARN': bucket['tableBucketARN'], 'namespace': 'default', 'name': 'old-table', 'newNamespaceName': 'default', 'newName': 'new-table'})[3],
        # ── s3tables — tags (service-prefixed keys) ───────────────────────────
        's3tables.TagResource': lambda store: (
            bucket := store.create_table_bucket(name='s3t-tr-bucket'),
            {'resourceArn': bucket['tableBucketARN'], 'tags': {'env': 'test'}})[1],
        's3tables.UntagResource': lambda store: (
            bucket := store.create_table_bucket(name='s3t-utr-bucket'),
            store.tag_resource(bucket['tableBucketARN'], {'env': 'test'}),
            {'resourceArn': bucket['tableBucketARN'], 'tagKeys': ['env']})[2],
        's3tables.ListTagsForResource': lambda store: (
            bucket := store.create_table_bucket(name='s3t-ltr-bucket'),
            store.tag_resource(bucket['tableBucketARN'], {'env': 'test'}),
            {'resourceArn': bucket['tableBucketARN']})[2],
        # ── emr — cluster prerequisites (run_job_flow returns ClusterRecord object) ─
        'RunJobFlow': {'Name': 'emr-shape-test'},
        'ListClusters': {},
        'DescribeCluster': lambda store: (
            cluster := store.run_job_flow(Name='emr-desc'),
            {'ClusterId': cluster.Id})[1],
        'TerminateJobFlows': lambda store: (
            cluster := store.run_job_flow(Name='emr-term'),
            {'JobFlowIds': [cluster.Id]})[1],
        'ListInstanceFleets': lambda store: (
            cluster := store.run_job_flow(Name='emr-lif'),
            {'ClusterId': cluster.Id})[1],
        'ListInstanceGroups': lambda store: (
            cluster := store.run_job_flow(Name='emr-lig'),
            {'ClusterId': cluster.Id})[1],
        'ListSteps': lambda store: (
            cluster := store.run_job_flow(Name='emr-ls'),
            {'ClusterId': cluster.Id})[1],
        'AddInstanceFleet': lambda store: (
            cluster := store.run_job_flow(Name='emr-aif'),
            {'ClusterId': cluster.Id, 'InstanceFleet': {'Name': 'core', 'InstanceFleetType': 'CORE', 'TargetOnDemandCapacity': 1, 'InstanceTypeConfigs': [{'InstanceType': 'm5.xlarge'}]}})[1],
        'AddInstanceGroups': lambda store: (
            cluster := store.run_job_flow(Name='emr-aig'),
            {'JobFlowId': cluster.Id, 'InstanceGroups': [{'Name': 'master', 'InstanceRole': 'MASTER', 'InstanceType': 'm5.xlarge', 'InstanceCount': 1}]})[1],
        'AddJobFlowSteps': lambda store: (
            cluster := store.run_job_flow(Name='emr-ajfs'),
            {'JobFlowId': cluster.Id, 'Steps': [{'Name': 'test-step', 'ActionOnFailure': 'CONTINUE', 'HadoopJarStep': {'Jar': 'command-runner.jar', 'Args': ['echo', 'test']}}]})[1],
        'CancelSteps': lambda store: (
            cluster := store.run_job_flow(Name='emr-cancel'),
            step := store.add_job_flow_steps(cluster.Id, [{'Name': 'cancel-step', 'ActionOnFailure': 'CONTINUE', 'HadoopJarStep': {'Jar': 'command-runner.jar', 'Args': ['echo', 'test']}}]),
            {'ClusterId': cluster.Id, 'StepIds': [step[0].Id]})[2],
        'DescribeStep': lambda store: (
            cluster := store.run_job_flow(Name='emr-dstep'),
            steps := store.add_job_flow_steps(cluster.Id, [{'Name': 'desc-step', 'ActionOnFailure': 'CONTINUE', 'HadoopJarStep': {'Jar': 'command-runner.jar', 'Args': ['echo', 'test']}}]),
            {'ClusterId': cluster.Id, 'StepId': steps[0].Id})[2],
        'ModifyInstanceFleet': lambda store: (
            cluster := store.run_job_flow(Name='emr-mif'),
            fleet := store.add_instance_fleet(cluster.Id, {'Name': 'core', 'InstanceFleetType': 'CORE', 'TargetOnDemandCapacity': 1, 'InstanceTypeConfigs': [{'InstanceType': 'm5.xlarge'}]}),
            {'ClusterId': cluster.Id, 'InstanceFleet': {'InstanceFleetId': fleet.Id, 'TargetOnDemandCapacity': 2}})[2],
        'ModifyInstanceGroups': lambda store: (
            cluster := store.run_job_flow(Name='emr-mig'),
            groups := store.add_instance_groups(cluster.Id, [{'Name': 'master', 'InstanceRole': 'MASTER', 'InstanceType': 'm5.xlarge', 'InstanceCount': 1}]),
            {'ClusterId': cluster.Id, 'InstanceGroups': [{'InstanceGroupId': groups[0].Id, 'InstanceCount': 2}]})[2],
        # ── emr — security configurations ──────────────────────────────────────
        'CreateSecurityConfiguration': {'Name': 'emr-sec-config', 'SecurityConfiguration': '{"EncryptionConfiguration": {}}'},
        'ListSecurityConfigurations': {},
        'DescribeSecurityConfiguration': lambda store: (
            store.create_security_configuration(Name='emr-dsc', SecurityConfiguration='{}'),
            {'Name': 'emr-dsc'})[1],
        'DeleteSecurityConfiguration': lambda store: (
            store.create_security_configuration(Name='emr-del-sc', SecurityConfiguration='{}'),
            {'Name': 'emr-del-sc'})[1],
        # ── emr — studios ───────────────────────────────────────────────────────
        'CreateStudio': {'Name': 'emr-studio'},
        'ListStudios': {},
        'DescribeStudio': lambda store: (
            studio := store.create_studio(Name='emr-ds'),
            {'StudioId': studio.StudioId})[1],
        'UpdateStudio': lambda store: (
            studio := store.create_studio(Name='emr-us'),
            {'StudioId': studio.StudioId, 'Description': 'Updated'})[1],
        'DeleteStudio': lambda store: (
            studio := store.create_studio(Name='emr-del-s'),
            {'StudioId': studio.StudioId})[1],
        # ── emr — tags ─────────────────────────────────────────────────────────
        'emr.TagResource': lambda store: (
            cluster := store.run_job_flow(Name='emr-tag'),
            {'ResourceId': cluster.Id, 'Tags': [{'Key': 'env', 'Value': 'test'}]})[1],
        'emr.UntagResource': lambda store: (
            cluster := store.run_job_flow(Name='emr-untag'),
            store.add_tags(cluster.Id, [{'Key': 'env', 'Value': 'test'}]),
            {'ResourceId': cluster.Id, 'TagKeys': ['env']})[2],
        'emr.ListTagsForResource': lambda store: (
            cluster := store.run_job_flow(Name='emr-ltr'),
            store.add_tags(cluster.Id, [{'Key': 'env', 'Value': 'test'}]),
            {'ResourceId': cluster.Id})[2],
        # ── sesv2 — contact lists ───────────────────────────────────────────
        'CreateContactList': {'ContactListName': 'sesv2-shape-cl'},
        'ListContactLists': {},
        'GetContactList': lambda store: (
            store.create_contact_list(ContactListName='sesv2-gcl'),
            {'ContactListName': 'sesv2-gcl'})[1],
        'DeleteContactList': lambda store: (
            store.create_contact_list(ContactListName='sesv2-dcl'),
            {'ContactListName': 'sesv2-dcl'})[1],
        # ── sesv2 — contacts ─────────────────────────────────────────────────
        'CreateContact': lambda store: (
            store.create_contact_list(ContactListName='sesv2-contacts'),
            {'ContactListName': 'sesv2-contacts', 'EmailAddress': 'test@example.com'})[1],
        'ListContacts': lambda store: (
            store.create_contact_list(ContactListName='sesv2-lc'),
            {'ContactListName': 'sesv2-lc'})[1],
        'GetContact': lambda store: (
            store.create_contact_list(ContactListName='sesv2-gc'),
            store.create_contact(ContactListName='sesv2-gc', EmailAddress='get@example.com'),
            {'ContactListName': 'sesv2-gc', 'EmailAddress': 'get@example.com'})[2],
        'UpdateContact': lambda store: (
            store.create_contact_list(ContactListName='sesv2-uc'),
            store.create_contact(ContactListName='sesv2-uc', EmailAddress='upd@example.com'),
            {'ContactListName': 'sesv2-uc', 'EmailAddress': 'upd@example.com', 'UnsubscribeAll': True})[2],
        'DeleteContact': lambda store: (
            store.create_contact_list(ContactListName='sesv2-dc'),
            store.create_contact(ContactListName='sesv2-dc', EmailAddress='del@example.com'),
            {'ContactListName': 'sesv2-dc', 'EmailAddress': 'del@example.com'})[2],
        # ── sesv2 — email identities ─────────────────────────────────────────
        'CreateEmailIdentity': {'EmailIdentity': 'test@sesv2-shape.example.com'},
        'ListEmailIdentities': {},
        'GetEmailIdentity': lambda store: (
            store.create_email_identity(EmailIdentity='get@sesv2-shape.example.com'),
            {'EmailIdentity': 'get@sesv2-shape.example.com'})[1],
        'DeleteEmailIdentity': lambda store: (
            store.create_email_identity(EmailIdentity='del@sesv2-shape.example.com'),
            {'EmailIdentity': 'del@sesv2-shape.example.com'})[1],
        # ── sesv2 — email templates ──────────────────────────────────────────
        'CreateEmailTemplate': {
            'TemplateName': 'sesv2-shape-template',
            'TemplateContent': {'Subject': 'Test', 'Text': 'Hello', 'Html': '<p>Hello</p>'},
        },
        'ListEmailTemplates': {},
        'GetEmailTemplate': lambda store: (
            store.create_email_template(TemplateName='sesv2-get', TemplateContent={'Subject': 'T', 'Text': 'B', 'Html': 'B'}),
            {'TemplateName': 'sesv2-get'})[1],
        'UpdateEmailTemplate': lambda store: (
            store.create_email_template(TemplateName='sesv2-upd', TemplateContent={'Subject': 'Old', 'Text': 'Old', 'Html': 'Old'}),
            {'TemplateName': 'sesv2-upd', 'TemplateContent': {'Subject': 'New', 'Text': 'New', 'Html': 'New'}})[1],
        'DeleteEmailTemplate': lambda store: (
            store.create_email_template(TemplateName='sesv2-del', TemplateContent={'Subject': 'D', 'Text': 'D', 'Html': 'D'}),
            {'TemplateName': 'sesv2-del'})[1],
        # ── sesv2 — configuration sets ──────────────────────────────────────
        'CreateConfigurationSet': {'ConfigurationSetName': 'sesv2-shape-cs'},
        'ListConfigurationSets': {},
        'GetConfigurationSet': lambda store: (
            store.create_configuration_set(ConfigurationSetName='sesv2-gcs'),
            {'ConfigurationSetName': 'sesv2-gcs'})[1],
        'DeleteConfigurationSet': lambda store: (
            store.create_configuration_set(ConfigurationSetName='sesv2-dcs'),
            {'ConfigurationSetName': 'sesv2-dcs'})[1],
        # ── sesv2 — send ─────────────────────────────────────────────────────
        'SendEmail': {
            'FromEmailAddress': 'sender@example.com',
            'Destination': {'ToAddresses': ['recipient@example.com']},
            'Content': {'Simple': {'Subject': {'Data': 'Test'}, 'Body': {'Text': {'Data': 'Hello'}}}},
        },
        # ── mq — broker ──────────────────────────────────────────────────────
        'CreateBroker': {'BrokerName': 'mq-shape-test', 'EngineType': 'ACTIVEMQ'},
        'ListBrokers': {},
        'DescribeBroker': lambda store: (
            broker := store.create_broker(BrokerName='mq-desc', EngineType='ACTIVEMQ'),
            {'BrokerId': broker['BrokerId']})[1],
        'DeleteBroker': lambda store: (
            broker := store.create_broker(BrokerName='mq-del', EngineType='ACTIVEMQ'),
            {'BrokerId': broker['BrokerId']})[1],
        'UpdateBroker': lambda store: (
            broker := store.create_broker(BrokerName='mq-upd', EngineType='ACTIVEMQ'),
            {'BrokerId': broker['BrokerId'], 'AutoMinorVersionUpgrade': False})[1],
        'RebootBroker': lambda store: (
            broker := store.create_broker(BrokerName='mq-reboot', EngineType='ACTIVEMQ'),
            {'BrokerId': broker['BrokerId']})[1],
        # ── mq — configuration ───────────────────────────────────────────────
        'CreateConfiguration': {'Name': 'mq-shape-config', 'EngineType': 'ACTIVEMQ', 'EngineVersion': '5.17.6'},
        'ListConfigurations': {},
        'DescribeConfiguration': lambda store: (
            cfg := store.create_configuration(Name='mq-desc-cfg', EngineType='ACTIVEMQ', EngineVersion='5.17.6'),
            {'ConfigurationId': cfg['Id']})[1],
        'DeleteConfiguration': lambda store: (
            cfg := store.create_configuration(Name='mq-del-cfg', EngineType='ACTIVEMQ', EngineVersion='5.17.6'),
            {'ConfigurationId': cfg['Id']})[1],
        'UpdateConfiguration': lambda store: (
            cfg := store.create_configuration(Name='mq-upd-cfg', EngineType='ACTIVEMQ', EngineVersion='5.17.6'),
            {'ConfigurationId': cfg['Id'], 'Data': 'updated', 'Description': 'Updated'})[1],
        'DescribeConfigurationRevision': lambda store: (
            cfg := store.create_configuration(Name='mq-rev-cfg', EngineType='ACTIVEMQ', EngineVersion='5.17.6'),
            {'ConfigurationId': cfg['Id'], 'ConfigurationRevision': 1})[1],
        # ── mq — user ─────────────────────────────────────────────────────────
        'CreateUser': lambda store: (
            broker := store.create_broker(BrokerName='mq-user-broker', EngineType='ACTIVEMQ'),
            {'BrokerId': broker['BrokerId'], 'Username': 'test-user'})[1],
        'ListUsers': lambda store: (
            broker := store.create_broker(BrokerName='mq-lu-broker', EngineType='ACTIVEMQ'),
            {'BrokerId': broker['BrokerId']})[1],
        'DescribeUser': lambda store: (
            broker := store.create_broker(BrokerName='mq-du-broker', EngineType='ACTIVEMQ'),
            store.create_user(broker['BrokerId'], 'desc-user'),
            {'BrokerId': broker['BrokerId'], 'Username': 'desc-user'})[2],
        'DeleteUser': lambda store: (
            broker := store.create_broker(BrokerName='mq-delusr-broker', EngineType='ACTIVEMQ'),
            store.create_user(broker['BrokerId'], 'del-user'),
            {'BrokerId': broker['BrokerId'], 'Username': 'del-user'})[2],
        'UpdateUser': lambda store: (
            broker := store.create_broker(BrokerName='mq-updusr-broker', EngineType='ACTIVEMQ'),
            store.create_user(broker['BrokerId'], 'upd-user'),
            {'BrokerId': broker['BrokerId'], 'Username': 'upd-user', 'Groups': ['admin']})[2],
        # ── mq — tags (service-prefixed keys) ─────────────────────────────────
        'mq.CreateTags': lambda store: (
            broker := store.create_broker(BrokerName='mq-tag-broker', EngineType='ACTIVEMQ'),
            {'ResourceArn': broker['BrokerArn'], 'Tags': {'env': 'test'}})[1],
        'mq.DeleteTags': lambda store: (
            broker := store.create_broker(BrokerName='mq-dtag-broker', EngineType='ACTIVEMQ'),
            store.create_tags(broker['BrokerArn'], {'env': 'test'}),
            {'ResourceArn': broker['BrokerArn'], 'TagKeys': ['env']})[2],
        'mq.ListTags': lambda store: (
            broker := store.create_broker(BrokerName='mq-ltag-broker', EngineType='ACTIVEMQ'),
            store.create_tags(broker['BrokerArn'], {'env': 'test'}),
            {'ResourceArn': broker['BrokerArn']})[2],
        # ── kafka — cluster ──────────────────────────────────────────────────
        'CreateCluster': {'ClusterName': 'kafka-shape-test', 'NumberOfBrokerNodes': 1},
        'CreateClusterV2': {'ClusterName': 'kafka-shape-v2', 'NumberOfBrokerNodes': 1},
        'DescribeCluster': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-desc', NumberOfBrokerNodes=1),
            {'ClusterArn': cluster['ClusterArn']})[1],
        'DescribeClusterV2': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-descv2', NumberOfBrokerNodes=1),
            {'ClusterArn': cluster['ClusterArn']})[1],
        'ListClusters': {},
        'ListClustersV2': {},
        'DeleteCluster': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-del', NumberOfBrokerNodes=1),
            {'ClusterArn': cluster['ClusterArn']})[1],
        'GetBootstrapBrokers': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-bb', NumberOfBrokerNodes=1),
            {'ClusterArn': cluster['ClusterArn']})[1],
        # ── kafka — topic ────────────────────────────────────────────────────
        'CreateTopic': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-topic', NumberOfBrokerNodes=1),
            {'ClusterArn': cluster['ClusterArn'], 'TopicName': 'shape-test-topic'})[1],
        'DescribeTopic': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-dtop', NumberOfBrokerNodes=1),
            store.create_topic(cluster['ClusterArn'], TopicName='desc-topic'),
            {'ClusterArn': cluster['ClusterArn'], 'TopicName': 'desc-topic'})[2],
        'ListTopics': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-ltop', NumberOfBrokerNodes=1),
            {'ClusterArn': cluster['ClusterArn']})[1],
        'DeleteTopic': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-deltop', NumberOfBrokerNodes=1),
            store.create_topic(cluster['ClusterArn'], TopicName='del-topic'),
            {'ClusterArn': cluster['ClusterArn'], 'TopicName': 'del-topic'})[2],
        'UpdateTopic': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-updtop', NumberOfBrokerNodes=1),
            store.create_topic(cluster['ClusterArn'], TopicName='upd-topic'),
            {'ClusterArn': cluster['ClusterArn'], 'TopicName': 'upd-topic', 'NumPartitions': 3})[2],
        # ── kafka — configuration ────────────────────────────────────────────
        'CreateConfiguration': {'Name': 'kafka-shape-config', 'ServerProperties': 'test.prop=1'},
        'DescribeConfiguration': lambda store: (
            cfg := store.create_configuration(Name='kafka-desc-cfg', ServerProperties='sp'),
            {'Arn': cfg['Arn']})[1],
        'ListConfigurations': {},
        'DeleteConfiguration': lambda store: (
            cfg := store.create_configuration(Name='kafka-del-cfg', ServerProperties='sp'),
            {'Arn': cfg['Arn']})[1],
        'UpdateConfiguration': lambda store: (
            cfg := store.create_configuration(Name='kafka-upd-cfg', ServerProperties='sp'),
            {'Arn': cfg['Arn'], 'ServerProperties': 'updated.prop=2', 'Description': 'Updated config'})[1],
        # ── kafka — tags (service-prefixed keys) ─────────────────────────────
        'kafka.TagResource': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-tag', NumberOfBrokerNodes=1, Tags={'env': 'test'}),
            {'ResourceArn': cluster['ClusterArn'], 'Tags': {'env': 'test'}})[1],
        'kafka.UntagResource': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-utag', NumberOfBrokerNodes=1, Tags={'env': 'test'}),
            {'ResourceArn': cluster['ClusterArn'], 'TagKeys': ['env']})[1],
        'kafka.ListTagsForResource': lambda store: (
            cluster := store.create_cluster(ClusterName='kafka-ltag', NumberOfBrokerNodes=1, Tags={'env': 'test'}),
            {'ResourceArn': cluster['ClusterArn']})[1],
        # ── codepipeline ─────────────────────────────────────────────────────
        'CreatePipeline': {
            'pipeline': {
                'name': 'cp-create-test',
                'roleArn': 'arn:aws:iam::000000000000:role/test-role',
                'stages': [{'name': 'Source', 'actions': [{'name': 'Src', 'actionTypeId': {'category': 'Source', 'owner': 'AWS', 'provider': 'S3', 'version': '1'}, 'outputArtifacts': [{'name': 'Out'}]}]}],
            },
        },
        'GetPipeline': lambda store: (
            pipeline := store.create_pipeline(name='cp-get', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            {'name': pipeline.get('name', 'cp-get')}
        )[1],
        'UpdatePipeline': lambda store: (
            pipeline := store.create_pipeline(name='cp-upd', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            {'pipeline': {'name': pipeline.get('name', 'cp-upd'), 'roleArn': 'arn:aws:iam::000000000000:role/r', 'stages': [{'name': 'Source', 'actions': []}]}}
        )[1],
        'DeletePipeline': lambda store: (
            pipeline := store.create_pipeline(name='cp-del', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            {'name': pipeline.get('name', 'cp-del')}
        )[1],
        'ListPipelines': {},
        'StartPipelineExecution': lambda store: (
            pipeline := store.create_pipeline(name='cp-start', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            {'name': pipeline.get('name', 'cp-start')}
        )[1],
        'StopPipelineExecution': lambda store: (
            pipeline := store.create_pipeline(name='cp-stop', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            exec_result := store.start_pipeline_execution(name=pipeline.get('name', 'cp-stop')),
            {'pipelineName': pipeline.get('name', 'cp-stop'), 'pipelineExecutionId': exec_result.get('pipelineExecutionId', 'test-exec-id')}
        )[2],
        'GetPipelineExecution': lambda store: (
            pipeline := store.create_pipeline(name='cp-gpex', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            exec_result := store.start_pipeline_execution(name=pipeline.get('name', 'cp-gpex')),
            {'pipelineName': pipeline.get('name', 'cp-gpex'), 'pipelineExecutionId': exec_result.get('pipelineExecutionId', 'test-exec-id')}
        )[2],
        'ListPipelineExecutions': lambda store: (
            pipeline := store.create_pipeline(name='cp-lpex', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            {'pipelineName': pipeline.get('name', 'cp-lpex')}
        )[1],
        'GetPipelineState': lambda store: (
            pipeline := store.create_pipeline(name='cp-gps', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}]),
            {'name': pipeline.get('name', 'cp-gps')}
        )[1],
        'CreateCustomActionType': {
            'category': 'Test',
            'provider': 'cp-test-provider',
            'version': '1',
        },
        'DeleteCustomActionType': lambda store: (
            store.create_custom_action_type(category='Test', provider='cp-del-provider', version='1'),
            {'category': 'Test', 'provider': 'cp-del-provider', 'version': '1'}
        )[1],
        'GetActionType': {
            'category': 'Test',
            'owner': 'Custom',
            'provider': 'cp-test-provider',
            'version': '1',
        },
        'UpdateActionType': lambda store: (
            store.create_custom_action_type(category='Test', provider='cp-upd-provider', version='1'),
            {'actionType': {'id': {'category': 'Test', 'owner': 'Custom', 'provider': 'cp-upd-provider', 'version': '1'}}}
        )[1],
        'ListActionTypes': {},
        'EnableStageTransition': lambda store: (
            pipeline := store.create_pipeline(name='cp-enst', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'Source', 'actions': []}]),
            {'pipelineName': pipeline.get('name', 'cp-enst'), 'stageName': 'Source', 'transitionType': 'Inbound'}
        )[1],
        'DisableStageTransition': lambda store: (
            pipeline := store.create_pipeline(name='cp-dist', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'Source', 'actions': []}]),
            {'pipelineName': pipeline.get('name', 'cp-dist'), 'stageName': 'Source', 'transitionType': 'Inbound', 'reason': 'testing'}
        )[1],
        'codepipeline.TagResource': lambda store: (
            pipeline := store.create_pipeline(name='cp-tag', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}], tags={'env': 'test'}),
            arn := f"arn:aws:codepipeline:us-east-1:000000000000:pipeline/{pipeline.get('name', 'cp-tag')}",
            {'ResourceArn': arn, 'Tags': {'Key': 'env', 'Value': 'test'}}
        )[2],
        'codepipeline.UntagResource': lambda store: (
            pipeline := store.create_pipeline(name='cp-utag', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}], tags={'env': 'test'}),
            arn := f"arn:aws:codepipeline:us-east-1:000000000000:pipeline/{pipeline.get('name', 'cp-utag')}",
            {'ResourceArn': arn, 'TagKeys': ['env']}
        )[2],
        'codepipeline.ListTagsForResource': lambda store: (
            pipeline := store.create_pipeline(name='cp-ltag', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}], tags={'env': 'test'}),
            arn := f"arn:aws:codepipeline:us-east-1:000000000000:pipeline/{pipeline.get('name', 'cp-ltag')}",
            {'ResourceArn': arn}
        )[2],
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
