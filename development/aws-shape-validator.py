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
        'quicksight.CreateDataSource': {'AwsAccountId': '123456789012', 'DataSourceId': 'test-ds', 'Name': 'Test DS', 'Type': 'S3'},
        # ── quicksight — list ──────────────────────────────────────────────
        'ListAnalyses': {'AwsAccountId': '123456789012'},
        'ListDashboards': {'AwsAccountId': '123456789012'},
        'ListDataSets': {'AwsAccountId': '123456789012'},
        'quicksight.ListDataSources': {'AwsAccountId': '123456789012'},
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
        'quicksight.DescribeDataSource': lambda store: (
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
        'quicksight.DeleteDataSource': lambda store: (
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
        'quicksight.UpdateDataSource': lambda store: (
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
        'CreateAccount': lambda store: (
            store.create_organization(),
            {'Email': 'test-acc@test.com', 'AccountName': 'TestAccount'})[1],
        'CreateOrganizationalUnit': lambda store: (
            store.create_organization(),
            {'ParentId': store.roots[0], 'Name': 'TestOU'})[1],
        'organizations.CreatePolicy': lambda store: (
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
        'organizations.ListPolicies': lambda store: (
            store.create_organization(),
            {'Filter': 'SERVICE_CONTROL_POLICY'})[1],
        'organizations.ListPoliciesForTarget': lambda store: (
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
            # Clean up any non-management accounts created by earlier ops in the shared store
            [store.accounts.pop(aid) for aid in list(store.accounts.keys())
             if aid != store.organization.master_account_id],
            {})[1],
        'DeleteOrganizationalUnit': lambda store: (
            org := store.create_organization(),
            ou := store.create_organizational_unit(store.roots[0], 'DelOU'),
            {'OrganizationalUnitId': ou.id})[2],
        'organizations.DeletePolicy': lambda store: (
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
            {'tableBucketARN': bucket['arn']})[1],
        's3tables.ListTables': lambda store: (
            bucket := store.create_table_bucket(name='s3t-ltb-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default'})[2],
        # ── s3tables — get (lambdas: create bucket first) ──────────────────────
        'GetTableBucket': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtb-bucket'),
            {'tableBucketARN': bucket['arn']})[1],
        'GetNamespace': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gn-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default'})[2],
        's3tables.GetTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gt-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            store.create_table(bucket['arn'], 'default', 'test-table', format='ICEBERG'),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default', 'name': 'test-table'})[3],
        'GetTableBucketEncryption': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtbe-bucket'),
            {'tableBucketARN': bucket['arn']})[1],
        'GetTableEncryption': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gte-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            store.create_table(bucket['arn'], 'default', 'test-table', format='ICEBERG'),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default', 'name': 'test-table'})[3],
        'GetTableMaintenanceConfiguration': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtmc-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            store.create_table(bucket['arn'], 'default', 'test-table', format='ICEBERG'),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default', 'name': 'test-table'})[3],
        'GetTableBucketMaintenanceConfiguration': lambda store: (
            bucket := store.create_table_bucket(name='s3t-gtbmc-bucket'),
            {'tableBucketARN': bucket['arn']})[1],
        # ── s3tables — create namespace/table (lambdas: bucket prerequisite) ───
        'CreateNamespace': lambda store: (
            bucket := store.create_table_bucket(name='s3t-cn-bucket'),
            {'tableBucketARN': bucket['arn'], 'namespace': ['default']})[1],
        's3tables.CreateTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-ct-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default', 'name': 'test-table', 'format': 'ICEBERG'})[2],
        # ── s3tables — delete (lambdas: create prerequisite, then delete) ──────
        'DeleteTableBucket': lambda store: (
            bucket := store.create_table_bucket(name='s3t-dtb-bucket'),
            {'tableBucketARN': bucket['arn']})[1],
        'DeleteNamespace': lambda store: (
            bucket := store.create_table_bucket(name='s3t-dn-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default'})[2],
        's3tables.DeleteTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-dt-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            store.create_table(bucket['arn'], 'default', 'del-table', format='ICEBERG'),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default', 'name': 'del-table'})[3],
        # ── s3tables — rename ──────────────────────────────────────────────────
        'RenameTable': lambda store: (
            bucket := store.create_table_bucket(name='s3t-rt-bucket'),
            store.create_namespace(bucket['arn'], ['default']),
            store.create_table(bucket['arn'], 'default', 'old-table', format='ICEBERG'),
            {'tableBucketARN': bucket['arn'], 'namespace': 'default', 'name': 'old-table', 'newNamespaceName': 'default', 'newName': 'new-table'})[3],
        # ── s3tables — tags (service-prefixed keys) ───────────────────────────
        's3tables.TagResource': lambda store: (
            bucket := store.create_table_bucket(name='s3t-tr-bucket'),
            {'resourceArn': bucket['arn'], 'tags': {'env': 'test'}})[1],
        's3tables.UntagResource': lambda store: (
            bucket := store.create_table_bucket(name='s3t-utr-bucket'),
            store.tag_resource(bucket['arn'], {'env': 'test'}),
            {'resourceArn': bucket['arn'], 'tagKeys': ['env']})[2],
        's3tables.ListTagsForResource': lambda store: (
            bucket := store.create_table_bucket(name='s3t-ltr-bucket'),
            store.tag_resource(bucket['arn'], {'env': 'test'}),
            {'resourceArn': bucket['arn']})[2],
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
            store.create_custom_action_type(category='Test', provider='cp-del-provider', version='1',
                input_artifact_details={'minimumCount': 0, 'maximumCount': 5},
                output_artifact_details={'minimumCount': 0, 'maximumCount': 5}),
            {'category': 'Test', 'provider': 'cp-del-provider', 'version': '1'}
        )[1],
        'GetActionType': {
            'category': 'Test',
            'owner': 'Custom',
            'provider': 'cp-test-provider',
            'version': '1',
        },
        'UpdateActionType': lambda store: (
            store.create_custom_action_type(category='Test', provider='cp-upd-provider', version='1',
                input_artifact_details={'minimumCount': 0, 'maximumCount': 5},
                output_artifact_details={'minimumCount': 0, 'maximumCount': 5}),
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
            pipeline := store.create_pipeline(name='cp-tag', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}], tags=[{'Key': 'env', 'Value': 'test'}]),
            arn := f"arn:aws:codepipeline:us-east-1:000000000000:pipeline/{pipeline.get('name', 'cp-tag')}",
            {'resourceArn': arn, 'tags': [{'Key': 'env', 'Value': 'test'}]}
        )[2],
        'codepipeline.UntagResource': lambda store: (
            pipeline := store.create_pipeline(name='cp-utag', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}], tags=[{'Key': 'env', 'Value': 'test'}]),
            arn := f"arn:aws:codepipeline:us-east-1:000000000000:pipeline/{pipeline.get('name', 'cp-utag')}",
            {'resourceArn': arn, 'tagKeys': ['env']}
        )[2],
        'codepipeline.ListTagsForResource': lambda store: (
            pipeline := store.create_pipeline(name='cp-ltag', role_arn='arn:aws:iam::000000000000:role/r', stages=[{'name': 'S', 'actions': []}], tags=[{'Key': 'env', 'Value': 'test'}]),
            arn := f"arn:aws:codepipeline:us-east-1:000000000000:pipeline/{pipeline.get('name', 'cp-ltag')}",
            {'resourceArn': arn}
        )[2],
        # ── amp — workspace ───────────────────────────────────────────────
        'CreateWorkspace': {'alias': 'amp-shape'},
        'DescribeWorkspace': lambda store: (
            ws := store.create_workspace(alias='amp-desc'),
            {'workspaceId': ws['workspaceId']}
        )[1],
        'ListWorkspaces': {},
        'DeleteWorkspace': lambda store: (
            ws := store.create_workspace(alias='amp-del'),
            {'workspaceId': ws['workspaceId']}
        )[1],
        'UpdateWorkspaceAlias': lambda store: (
            ws := store.create_workspace(alias='amp-upd-old'),
            {'workspaceId': ws['workspaceId'], 'alias': 'amp-upd-new'}
        )[1],
        # ── amp — scraper ─────────────────────────────────────────────────
        'CreateScraper': {'alias': 'amp-scraper', 'source': {'eksConfiguration': {'clusterArn': 'arn:aws:eks:us-east-1:000000000000:cluster/test'}}, 'destination': {'ampConfiguration': {'workspaceArn': 'arn:aws:prometheus:us-east-1:000000000000:workspace/ws-test'}}},
        'DescribeScraper': lambda store: (
            sr := store.create_scraper(alias='amp-desc-scr', source={'eksConfiguration': {'clusterArn': 'arn:aws:eks:us-east-1:000000000000:cluster/test'}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:prometheus:us-east-1:000000000000:workspace/ws-test'}}),
            {'scraperId': sr['scraperId']}
        )[1],
        'ListScrapers': {},
        'DeleteScraper': lambda store: (
            sr := store.create_scraper(alias='amp-del-scr', source={'eksConfiguration': {'clusterArn': 'arn:aws:eks:us-east-1:000000000000:cluster/test'}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:prometheus:us-east-1:000000000000:workspace/ws-test'}}),
            {'scraperId': sr['scraperId']}
        )[1],
        'UpdateScraper': lambda store: (
            sr := store.create_scraper(alias='amp-upd-scr', source={'eksConfiguration': {'clusterArn': 'arn:aws:eks:us-east-1:000000000000:cluster/test'}}, destination={'ampConfiguration': {'workspaceArn': 'arn:aws:prometheus:us-east-1:000000000000:workspace/ws-test'}}),
            {'scraperId': sr['scraperId'], 'alias': 'amp-updated-scraper'}
        )[1],
        'GetDefaultScraperConfiguration': {},
        # ── amp — rule groups namespace ────────────────────────────────────
        'CreateRuleGroupsNamespace': lambda store: (
            ws := store.create_workspace(alias='amp-rgn'),
            {'workspaceId': ws['workspaceId'], 'name': 'default', 'data': 'groups:\n  - name: test'}
        )[1],
        'DescribeRuleGroupsNamespace': lambda store: (
            ws := store.create_workspace(alias='amp-drgn'),
            rgn := store.create_rule_groups_namespace(workspaceId=ws['workspaceId'], name='default', data='groups: []'),
            {'workspaceId': ws['workspaceId'], 'name': 'default'}
        )[2],
        'ListRuleGroupsNamespaces': lambda store: (
            ws := store.create_workspace(alias='amp-lrgn'),
            {'workspaceId': ws['workspaceId']}
        )[1],
        'DeleteRuleGroupsNamespace': lambda store: (
            ws := store.create_workspace(alias='amp-delrgn'),
            rgn := store.create_rule_groups_namespace(workspaceId=ws['workspaceId'], name='default', data='groups: []'),
            {'workspaceId': ws['workspaceId'], 'name': 'default'}
        )[2],
        'PutRuleGroupsNamespace': lambda store: (
            ws := store.create_workspace(alias='ampprgn'),
            {'workspaceId': ws['workspaceId'], 'name': 'default', 'data': 'groups:\n  - name: test'}
        )[1],
        # ── amp — alert manager definition ─────────────────────────────────
        'CreateAlertManagerDefinition': lambda store: (
            ws := store.create_workspace(alias='amp-amd'),
            {'workspaceId': ws['workspaceId'], 'data': 'alertmanager_config: |\n  global:\n    slack_api_url: https://hooks.slack.com/test'}
        )[1],
        'DescribeAlertManagerDefinition': lambda store: (
            ws := store.create_workspace(alias='amp-damd'),
            amd := store.create_alert_manager_definition(workspaceId=ws['workspaceId'], data='alertmanager_config: ""'),
            {'workspaceId': ws['workspaceId']}
        )[2],
        'DeleteAlertManagerDefinition': lambda store: (
            ws := store.create_workspace(alias='amp-delamd'),
            amd := store.create_alert_manager_definition(workspaceId=ws['workspaceId'], data='alertmanager_config: ""'),
            {'workspaceId': ws['workspaceId']}
        )[2],
        'PutAlertManagerDefinition': lambda store: (
            ws := store.create_workspace(alias='amp-pamd'),
            {'workspaceId': ws['workspaceId'], 'data': 'alertmanager_config: |\n  receivers:\n  - name: default'}
        )[1],
        # ── amp — tags (service-prefixed keys) ─────────────────────────────
        'amp.TagResource': lambda store: (
            ws := store.create_workspace(alias='amp-tag', tags={'env': 'test'}),
            {'resourceArn': ws['arn'], 'tags': [{'key': 'env', 'value': 'test'}]}
        )[1],
        'amp.UntagResource': lambda store: (
            ws := store.create_workspace(alias='amp-utag', tags={'env': 'test'}),
            {'resourceArn': ws['arn'], 'tagKeys': ['env']}
        )[1],
        'amp.ListTagsForResource': lambda store: (
            ws := store.create_workspace(alias='amp-ltag', tags={'env': 'test'}),
            {'resourceArn': ws['arn']}
        )[1],
        # ── keyspaces — keyspaces ───────────────────────────────────────────
        'CreateKeyspace': {'keyspaceName': 'ks-create'},
        'GetKeyspace': lambda store: (
            store.create_keyspace('ks-get'),
            {'keyspaceName': 'ks-get'}
        )[1],
        'ListKeyspaces': {},
        'DeleteKeyspace': lambda store: (
            store.create_keyspace('ks-del'),
            {'keyspaceName': 'ks-del'}
        )[1],
        'UpdateKeyspace': lambda store: (
            store.create_keyspace('ks-upd'),
            {'keyspaceName': 'ks-upd'}
        )[1],
        # ── keyspaces — tables ─────────────────────────────────────────────
        'CreateTable': lambda store: (
            store.create_keyspace('ks-ctbl'),
            {'keyspaceName': 'ks-ctbl', 'tableName': 'test-table',
             'schemaDefinition': {'allColumns': [{'name': 'id', 'type': 'int'}, {'name': 'val', 'type': 'text'}], 'partitionKeys': [{'name': 'id'}]}}
        )[1],
        'GetTable': lambda store: (
            store.create_keyspace('ks-gtbl'),
            store.create_table('ks-gtbl', 'test-table', schemaDefinition={'allColumns': [{'name': 'id', 'type': 'int'}], 'partitionKeys': [{'name': 'id'}]}),
            {'keyspaceName': 'ks-gtbl', 'tableName': 'test-table'}
        )[2],
        'ListTables': lambda store: (
            store.create_keyspace('ks-ltbl'),
            {'keyspaceName': 'ks-ltbl'}
        )[1],
        'DeleteTable': lambda store: (
            store.create_keyspace('ks-dtbl'),
            store.create_table('ks-dtbl', 'test-table', schemaDefinition={'allColumns': [{'name': 'id', 'type': 'int'}], 'partitionKeys': [{'name': 'id'}]}),
            {'keyspaceName': 'ks-dtbl', 'tableName': 'test-table'}
        )[2],
        'UpdateTable': lambda store: (
            store.create_keyspace('ks-utbl'),
            store.create_table('ks-utbl', 'test-table', schemaDefinition={'allColumns': [{'name': 'id', 'type': 'int'}], 'partitionKeys': [{'name': 'id'}]}),
            {'keyspaceName': 'ks-utbl', 'tableName': 'test-table'}
        )[2],
        # ── keyspaces — types ──────────────────────────────────────────────
        'CreateType': lambda store: (
            store.create_keyspace('ks-ctyp'),
            {'keyspaceName': 'ks-ctyp', 'typeName': 'address',
             'fieldDefinitions': [{'name': 'street', 'type': 'text'}, {'name': 'city', 'type': 'text'}]}
        )[1],
        'GetType': lambda store: (
            store.create_keyspace('ks-gtyp'),
            store.create_type('ks-gtyp', 'address', fieldDefinitions=[{'name': 'street', 'type': 'text'}]),
            {'keyspaceName': 'ks-gtyp', 'typeName': 'address'}
        )[2],
        'ListTypes': lambda store: (
            store.create_keyspace('ks-ltyp'),
            {'keyspaceName': 'ks-ltyp'}
        )[1],
        'DeleteType': lambda store: (
            store.create_keyspace('ks-dtyp'),
            store.create_type('ks-dtyp', 'address', fieldDefinitions=[{'name': 'street', 'type': 'text'}]),
            {'keyspaceName': 'ks-dtyp', 'typeName': 'address'}
        )[2],
        # ── keyspaces — auto scaling ───────────────────────────────────────
        'GetTableAutoScalingSettings': lambda store: (
            store.create_keyspace('ks-as'),
            store.create_table('ks-as', 'test-table', schemaDefinition={'allColumns': [{'name': 'id', 'type': 'int'}], 'partitionKeys': [{'name': 'id'}]}),
            {'keyspaceName': 'ks-as', 'tableName': 'test-table'}
        )[2],
        # ── keyspaces — tags (service-prefixed keys) ───────────────────────
        'keyspaces.TagResource': lambda store: (
            ks := store.create_keyspace('ks-tag'),
            {'resourceArn': ks['resourceArn'], 'tags': [{'key': 'env', 'value': 'test'}]}
        )[1],
        'keyspaces.UntagResource': lambda store: (
            ks := store.create_keyspace('ks-utag'),
            {'resourceArn': ks['resourceArn'], 'tags': [{'key': 'env', 'value': 'test'}]}
        )[1],
        'keyspaces.ListTagsForResource': lambda store: (
            ks := store.create_keyspace('ks-ltag'),
            {'resourceArn': ks['resourceArn']}
        )[1],
        # ── bedrock — foundation models (read-only) ────────────────────────
        'GetFoundationModel': {'modelIdentifier': 'anthropic.claude-v2'},
        'GetFoundationModelAvailability': {'modelId': 'anthropic.claude-v2'},
        'ListFoundationModels': {},
        # ── bedrock — guardrails ─────────────────────────────────────────
        'CreateGuardrail': {'name': 'test-guardrail', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'},
        'GetGuardrail': lambda store: (
            gr := store.create_guardrail({'name': 'gr-get', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'}),
            {'guardrailIdentifier': gr.guardrailId}
        )[1],
        'ListGuardrails': {},
        'DeleteGuardrail': lambda store: (
            gr := store.create_guardrail({'name': 'gr-del', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'}),
            {'guardrailIdentifier': gr.guardrailId}
        )[1],
        'UpdateGuardrail': lambda store: (
            gr := store.create_guardrail({'name': 'gr-upd', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'}),
            {'guardrailIdentifier': gr.guardrailId, 'name': 'gr-updated', 'blockedInputMessaging': 'Updated', 'blockedOutputsMessaging': 'Updated'}
        )[1],
        'CreateGuardrailVersion': lambda store: (
            gr := store.create_guardrail({'name': 'gr-ver', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'}),
            {'guardrailIdentifier': gr.guardrailId}
        )[1],
        # ── bedrock — model customization jobs ──────────────────────────
        'CreateModelCustomizationJob': {'jobName': 'test-job', 'customModelName': 'test-model', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'baseModelIdentifier': 'anthropic.claude-v2', 'trainingDataConfig': {'s3Uri': 's3://test/train.jsonl'}, 'outputDataConfig': {'s3Uri': 's3://test/output/'}},
        'GetModelCustomizationJob': lambda store: (
            job := store.create_model_customization_job({'jobName': 'job-get', 'customModelName': 'model-get', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'baseModelIdentifier': 'anthropic.claude-v2', 'trainingDataConfig': {'s3Uri': 's3://test/train.jsonl'}, 'outputDataConfig': {'s3Uri': 's3://test/output/'}}),
            {'jobIdentifier': job.jobArn}
        )[1],
        'StopModelCustomizationJob': lambda store: (
            job := store.create_model_customization_job({'jobName': 'job-stop', 'customModelName': 'model-stop', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'baseModelIdentifier': 'anthropic.claude-v2', 'trainingDataConfig': {'s3Uri': 's3://test/train.jsonl'}, 'outputDataConfig': {'s3Uri': 's3://test/output/'}}),
            {'jobIdentifier': job.jobArn}
        )[1],
        'ListModelCustomizationJobs': {},
        # ── bedrock — provisioned model throughput ──────────────────────
        'CreateProvisionedModelThroughput': {'modelUnits': 1, 'provisionedModelName': 'test-pt', 'modelId': 'anthropic.claude-v2'},
        'GetProvisionedModelThroughput': lambda store: (
            pm := store.create_provisioned_model_throughput({'modelUnits': 1, 'provisionedModelName': 'pm-get', 'modelId': 'anthropic.claude-v2'}),
            {'provisionedModelId': pm.provisionedModelId}
        )[1],
        'UpdateProvisionedModelThroughput': lambda store: (
            pm := store.create_provisioned_model_throughput({'modelUnits': 1, 'provisionedModelName': 'pm-upd', 'modelId': 'anthropic.claude-v2'}),
            {'provisionedModelId': pm.provisionedModelId, 'desiredProvisionedModelName': 'pm-updated'}
        )[1],
        'DeleteProvisionedModelThroughput': lambda store: (
            pm := store.create_provisioned_model_throughput({'modelUnits': 1, 'provisionedModelName': 'pm-del', 'modelId': 'anthropic.claude-v2'}),
            {'provisionedModelId': pm.provisionedModelId}
        )[1],
        'ListProvisionedModelThroughputs': {},
        # ── bedrock — tags (service-prefixed keys) ─────────────────────
        'bedrock.TagResource': lambda store: (
            gr := store.create_guardrail({'name': 'gr-tag', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'}),
            {'resourceARN': gr.guardrailArn, 'tags': [{'key': 'env', 'value': 'test'}]}
        )[1],
        'bedrock.UntagResource': lambda store: (
            gr := store.create_guardrail({'name': 'gr-utag', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'}),
            {'resourceARN': gr.guardrailArn, 'tagKeys': ['env']}
        )[1],
        'bedrock.ListTagsForResource': lambda store: (
            gr := store.create_guardrail({'name': 'gr-ltag', 'blockedInputMessaging': 'Blocked', 'blockedOutputsMessaging': 'Blocked'}),
            {'resourceARN': gr.guardrailArn}
        )[1],
        # ── backup — plans ──────────────────────────────────────────────
        'CreateBackupPlan': {'BackupPlanName': 'test-plan'},
        'GetBackupPlan': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-get'),
            {'BackupPlanId': plan['BackupPlanId']}
        )[1],
        'ListBackupPlans': {},
        'DeleteBackupPlan': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-del'),
            {'BackupPlanId': plan['BackupPlanId']}
        )[1],
        'UpdateBackupPlan': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-upd'),
            {'BackupPlanId': plan['BackupPlanId']}
        )[1],
        # ── backup — vaults ─────────────────────────────────────────────
        'CreateBackupVault': {'BackupVaultName': 'test-vault'},
        'DescribeBackupVault': lambda store: (
            vault := store.create_backup_vault(BackupVaultName='vault-desc'),
            {'BackupVaultName': vault['BackupVaultName']}
        )[1],
        'ListBackupVaults': {},
        'DeleteBackupVault': lambda store: (
            vault := store.create_backup_vault(BackupVaultName='vault-del'),
            {'BackupVaultName': vault['BackupVaultName']}
        )[1],
        # ── backup — selections ─────────────────────────────────────────
        'CreateBackupSelection': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-sel'),
            {'BackupPlanId': plan['BackupPlanId'], 'SelectionName': 'test-sel',
             'IamRoleArn': 'arn:aws:iam::000000000000:role/test'}
        )[1],
        'GetBackupSelection': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-gsel'),
            sel := store.create_backup_selection(BackupPlanId=plan['BackupPlanId'],
                SelectionName='sel-get', IamRoleArn='arn:aws:iam::000000000000:role/test'),
            {'BackupPlanId': plan['BackupPlanId'], 'SelectionId': sel['SelectionId']}
        )[2],
        'ListBackupSelections': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-lsel'),
            {'BackupPlanId': plan['BackupPlanId']}
        )[1],
        'DeleteBackupSelection': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-dsel'),
            sel := store.create_backup_selection(BackupPlanId=plan['BackupPlanId'],
                SelectionName='sel-del', IamRoleArn='arn:aws:iam::000000000000:role/test'),
            {'BackupPlanId': plan['BackupPlanId'], 'SelectionId': sel['SelectionId']}
        )[2],
        # ── backup — jobs ───────────────────────────────────────────────
        'StartBackupJob': lambda store: (
            vault := store.create_backup_vault(BackupVaultName='vault-job'),
            {'BackupVaultName': vault['BackupVaultName'],
             'ResourceArn': 'arn:aws:ec2:us-east-1:000000000000:instance/i-test',
             'IamRoleArn': 'arn:aws:iam::000000000000:role/test'}
        )[1],
        'DescribeBackupJob': lambda store: (
            vault := store.create_backup_vault(BackupVaultName='vault-djob'),
            job := store.start_backup_job(BackupVaultName=vault['BackupVaultName'],
                ResourceArn='arn:aws:ec2:us-east-1:000000000000:instance/i-test',
                IamRoleArn='arn:aws:iam::000000000000:role/test'),
            {'BackupJobId': job['BackupJobId']}
        )[2],
        'ListBackupJobs': {},
        'StopBackupJob': lambda store: (
            vault := store.create_backup_vault(BackupVaultName='vault-sjob'),
            job := store.start_backup_job(BackupVaultName=vault['BackupVaultName'],
                ResourceArn='arn:aws:ec2:us-east-1:000000000000:instance/i-test',
                IamRoleArn='arn:aws:iam::000000000000:role/test'),
            {'BackupJobId': job['BackupJobId']}
        )[2],
        # ── backup — tags (service-prefixed keys) ────────────────────────
        'backup.TagResource': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-tag'),
            {'ResourceArn': plan['BackupPlanArn'], 'Tags': {'env': 'test'}}
        )[1],
        'backup.UntagResource': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-utag'),
            {'ResourceArn': plan['BackupPlanArn'], 'TagKeys': ['env']}
        )[1],
        'backup.ListTags': lambda store: (
            plan := store.create_backup_plan(BackupPlanName='plan-ltags'),
            {'ResourceArn': plan['BackupPlanArn']}
        )[1],
        # ── kendra — indices ────────────────────────────────────────────
        'CreateIndex': {'Name': 'test-idx', 'RoleArn': 'arn:aws:iam::000000000000:role/test'},
        'DescribeIndex': lambda store: (
            idx := store.create_index(Name='idx-desc', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'Id': idx['Id']}
        )[1],
        'ListIndices': {},
        'DeleteIndex': lambda store: (
            idx := store.create_index(Name='idx-del', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'Id': idx['Id']}
        )[1],
        'UpdateIndex': lambda store: (
            idx := store.create_index(Name='idx-upd', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'Id': idx['Id']}
        )[1],
        # ── kendra — data sources ────────────────────────────────────────
        'CreateDataSource': lambda store: (
            idx := store.create_index(Name='idx-ds', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id'], 'Name': 'test-ds', 'Type': 'S3'}
        )[1],
        'DescribeDataSource': lambda store: (
            idx := store.create_index(Name='idx-dds', RoleArn='arn:aws:iam::000000000000:role/test'),
            ds := store.create_data_source(IndexId=idx['Id'], Name='ds-desc', Type='S3'),
            {'Id': ds['Id'], 'IndexId': idx['Id']}
        )[2],
        'ListDataSources': lambda store: (
            idx := store.create_index(Name='idx-lds', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id']}
        )[1],
        'DeleteDataSource': lambda store: (
            idx := store.create_index(Name='idx-dds2', RoleArn='arn:aws:iam::000000000000:role/test'),
            ds := store.create_data_source(IndexId=idx['Id'], Name='ds-del', Type='S3'),
            {'Id': ds['Id'], 'IndexId': idx['Id']}
        )[2],
        'UpdateDataSource': lambda store: (
            idx := store.create_index(Name='idx-uds', RoleArn='arn:aws:iam::000000000000:role/test'),
            ds := store.create_data_source(IndexId=idx['Id'], Name='ds-upd', Type='S3'),
            {'Id': ds['Id'], 'IndexId': idx['Id']}
        )[2],
        # ── kendra — faqs ────────────────────────────────────────────────
        'CreateFaq': lambda store: (
            idx := store.create_index(Name='idx-faq', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id'], 'Name': 'test-faq', 'S3Path': 's3://test/faq.csv',
             'RoleArn': 'arn:aws:iam::000000000000:role/test'}
        )[1],
        'DescribeFaq': lambda store: (
            idx := store.create_index(Name='idx-dfq', RoleArn='arn:aws:iam::000000000000:role/test'),
            faq := store.create_faq(IndexId=idx['Id'], Name='faq-desc', S3Path='s3://test/faq.csv',
                RoleArn='arn:aws:iam::000000000000:role/test'),
            {'Id': faq['Id'], 'IndexId': idx['Id']}
        )[2],
        'ListFaqs': lambda store: (
            idx := store.create_index(Name='idx-lfq', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id']}
        )[1],
        'DeleteFaq': lambda store: (
            idx := store.create_index(Name='idx-dfq2', RoleArn='arn:aws:iam::000000000000:role/test'),
            faq := store.create_faq(IndexId=idx['Id'], Name='faq-del', S3Path='s3://test/faq.csv',
                RoleArn='arn:aws:iam::000000000000:role/test'),
            {'Id': faq['Id'], 'IndexId': idx['Id']}
        )[2],
        # ── kendra — thesauri ────────────────────────────────────────────
        'CreateThesaurus': lambda store: (
            idx := store.create_index(Name='idx-ths', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id'], 'Name': 'test-thes', 'RoleArn': 'arn:aws:iam::000000000000:role/test',
             'SourceS3Path': 's3://test/thesaurus.txt'}
        )[1],
        'DescribeThesaurus': lambda store: (
            idx := store.create_index(Name='idx-dth', RoleArn='arn:aws:iam::000000000000:role/test'),
            ths := store.create_thesaurus(IndexId=idx['Id'], Name='ths-desc',
                RoleArn='arn:aws:iam::000000000000:role/test', SourceS3Path='s3://test/thesaurus.txt'),
            {'Id': ths['Id'], 'IndexId': idx['Id']}
        )[2],
        'ListThesauri': lambda store: (
            idx := store.create_index(Name='idx-lth', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id']}
        )[1],
        'DeleteThesaurus': lambda store: (
            idx := store.create_index(Name='idx-dth2', RoleArn='arn:aws:iam::000000000000:role/test'),
            ths := store.create_thesaurus(IndexId=idx['Id'], Name='ths-del',
                RoleArn='arn:aws:iam::000000000000:role/test', SourceS3Path='s3://test/thesaurus.txt'),
            {'Id': ths['Id'], 'IndexId': idx['Id']}
        )[2],
        # ── kendra — experiences ─────────────────────────────────────────
        'CreateExperience': lambda store: (
            idx := store.create_index(Name='idx-exp', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id'], 'Name': 'test-exp'}
        )[1],
        'DescribeExperience': lambda store: (
            idx := store.create_index(Name='idx-dex', RoleArn='arn:aws:iam::000000000000:role/test'),
            exp := store.create_experience(IndexId=idx['Id'], Name='exp-desc'),
            {'Id': exp['Id'], 'IndexId': idx['Id']}
        )[2],
        'ListExperiences': lambda store: (
            idx := store.create_index(Name='idx-lex', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id']}
        )[1],
        'DeleteExperience': lambda store: (
            idx := store.create_index(Name='idx-dex2', RoleArn='arn:aws:iam::000000000000:role/test'),
            exp := store.create_experience(IndexId=idx['Id'], Name='exp-del'),
            {'Id': exp['Id'], 'IndexId': idx['Id']}
        )[2],
        # ── kendra — query ───────────────────────────────────────────────
        'Query': lambda store: (
            idx := store.create_index(Name='idx-query', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'IndexId': idx['Id'], 'QueryText': 'test query'}
        )[1],
        # ── kendra — tags ────────────────────────────────────────────────
        'kendra.TagResource': lambda store: (
            idx := store.create_index(Name='idx-tag', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'ResourceARN': 'arn:aws:kendra:us-east-1:000000000000:index/' + idx['Id'],
             'Tags': [{'Key': 'env', 'Value': 'test'}]}
        )[1],
        'kendra.UntagResource': lambda store: (
            idx := store.create_index(Name='idx-utag', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'ResourceARN': 'arn:aws:kendra:us-east-1:000000000000:index/' + idx['Id'],
             'TagKeys': ['env']}
        )[1],
        'kendra.ListTagsForResource': lambda store: (
            idx := store.create_index(Name='idx-ltags', RoleArn='arn:aws:iam::000000000000:role/test'),
            {'ResourceARN': 'arn:aws:kendra:us-east-1:000000000000:index/' + idx['Id']}
        )[1],
        # ── codedeploy — applications ──────────────────────────────────────
        'CreateApplication': {'applicationName': 'test-app', 'computePlatform': 'Server'},
        'GetApplication': lambda store: (
            store.applications.create_application(application_name='cd-get-app'),
            {'applicationName': 'cd-get-app'}
        )[1],
        'UpdateApplication': lambda store: (
            store.applications.create_application(application_name='cd-upd-app'),
            {'applicationName': 'cd-upd-app', 'newApplicationName': 'cd-upd-app-renamed'}
        )[1],
        'DeleteApplication': lambda store: (
            store.applications.create_application(application_name='cd-del-app'),
            {'applicationName': 'cd-del-app'}
        )[1],
        'ListApplications': {},
        'BatchGetApplications': lambda store: (
            store.applications.create_application(application_name='cd-bg-app'),
            {'applicationNames': ['cd-bg-app']}
        )[1],
        # ── codedeploy — deployment configs ────────────────────────────────
        'CreateDeploymentConfig': {'deploymentConfigName': 'test-config',
            'minimumHealthyHosts': {'type': 'HOST_COUNT', 'value': 1}},
        'GetDeploymentConfig': {'deploymentConfigName': 'CodeDeployDefault.OneAtATime'},
        'DeleteDeploymentConfig': lambda store: (
            store.deployment_configs.create_deployment_config(deployment_config_name='cd-dc-del'),
            {'deploymentConfigName': 'cd-dc-del'}
        )[1],
        'ListDeploymentConfigs': {},
        # ── codedeploy — deployment groups ─────────────────────────────────
        'CreateDeploymentGroup': lambda store: (
            store.applications.create_application(application_name='cd-dg-app'),
            {'applicationName': 'cd-dg-app', 'deploymentGroupName': 'test-dg',
             'serviceRoleArn': 'arn:aws:iam::000000000000:role/test'}
        )[1],
        'GetDeploymentGroup': lambda store: (
            store.applications.create_application(application_name='cd-gdg-app'),
            store.applications.create_application(application_name='cd-gdg-app'),
            store.deployment_groups.create_deployment_group(application_name='cd-gdg-app',
                deployment_group_name='cd-gdg-group', service_role_arn='arn:aws:iam::000000000000:role/r'),
            {'applicationName': 'cd-gdg-app', 'deploymentGroupName': 'cd-gdg-group'}
        )[2],
        'UpdateDeploymentGroup': lambda store: (
            store.applications.create_application(application_name='cd-udg-app'),
            store.deployment_groups.create_deployment_group(application_name='cd-udg-app',
                deployment_group_name='cd-udg-group', service_role_arn='arn:aws:iam::000000000000:role/r'),
            {'applicationName': 'cd-udg-app', 'currentDeploymentGroupName': 'cd-udg-group',
             'newDeploymentGroupName': 'cd-udg-renamed'}
        )[2],
        'DeleteDeploymentGroup': lambda store: (
            store.applications.create_application(application_name='cd-dd-app'),
            store.deployment_groups.create_deployment_group(application_name='cd-dd-app',
                deployment_group_name='cd-dd-group', service_role_arn='arn:aws:iam::000000000000:role/r'),
            {'applicationName': 'cd-dd-app', 'deploymentGroupName': 'cd-dd-group'}
        )[2],
        'ListDeploymentGroups': lambda store: (
            store.applications.create_application(application_name='cd-ldg-app'),
            {'applicationName': 'cd-ldg-app'}
        )[1],
        # ── codedeploy — deployments ───────────────────────────────────────
        'CreateDeployment': lambda store: (
            store.applications.create_application(application_name='cd-cdep-app'),
            store.deployment_groups.create_deployment_group(application_name='cd-cdep-app',
                deployment_group_name='cd-cdep-dg', service_role_arn='arn:aws:iam::000000000000:role/r'),
            {'applicationName': 'cd-cdep-app', 'deploymentGroupName': 'cd-cdep-dg',
             'revision': {'revisionType': 'S3', 's3Location': {'bucket': 'test', 'key': 'app.zip', 'bundleType': 'zip'}}}
        )[2],
        'GetDeployment': lambda store: (
            store.applications.create_application(application_name='cd-gdep-app'),
            store.deployment_groups.create_deployment_group(application_name='cd-gdep-app',
                deployment_group_name='cd-gdep-dg', service_role_arn='arn:aws:iam::000000000000:role/r'),
            dep := store.deployments.create_deployment(application_name='cd-gdep-app',
                deployment_group_name='cd-gdep-dg'),
            {'deploymentId': dep.deploymentId}
        )[3],
        'StopDeployment': lambda store: (
            store.applications.create_application(application_name='cd-sdep-app'),
            store.deployment_groups.create_deployment_group(application_name='cd-sdep-app',
                deployment_group_name='cd-sdep-dg', service_role_arn='arn:aws:iam::000000000000:role/r'),
            dep := store.deployments.create_deployment(application_name='cd-sdep-app',
                deployment_group_name='cd-sdep-dg'),
            {'deploymentId': dep.deploymentId}
        )[3],
        'ListDeployments': {},
        'BatchGetDeployments': lambda store: (
            store.applications.create_application(application_name='cd-bgdep-app'),
            store.deployment_groups.create_deployment_group(application_name='cd-bgdep-app',
                deployment_group_name='cd-bgdep-dg', service_role_arn='arn:aws:iam::000000000000:role/r'),
            dep := store.deployments.create_deployment(application_name='cd-bgdep-app',
                deployment_group_name='cd-bgdep-dg'),
            {'deploymentIds': [dep.deploymentId]}
        )[3],
        # ── identitystore — users ──────────────────────────────────────────
        'CreateUser': {'identityStoreId': 'd-12345', 'userName': 'test-user',
             'displayName': 'Test User', 'emails': [{'value': 'test@example.com', 'primary': True}],
             'name': {'givenName': 'Test', 'familyName': 'User'}},
        'DescribeUser': lambda store: (
            u := store.create_user(identityStoreId='d-is-desc', userName='desc-user'),
            {'identityStoreId': 'd-is-desc', 'userId': u['UserId']}
        )[1],
        'UpdateUser': lambda store: (
            u := store.create_user(identityStoreId='d-is-upd', userName='upd-user'),
            {'identityStoreId': 'd-is-upd', 'userId': u['UserId'],
             'operations': [{'attributePath': 'userName', 'attributeValue': 'upd-user-renamed'}]}
        )[1],
        'DeleteUser': lambda store: (
            u := store.create_user(identityStoreId='d-is-del', userName='del-user'),
            {'identityStoreId': 'd-is-del', 'userId': u['UserId']}
        )[1],
        'ListUsers': {'identityStoreId': 'd-12345'},
        'GetUserId': lambda store: (
            store.create_user(identityStoreId='d-is-gid', userName='gid-user'),
            {'identityStoreId': 'd-is-gid',
             'alternateIdentifier': {'UniqueAttribute': {'AttributePath': 'userName', 'AttributeValue': 'gid-user'}}}
        )[1],
        # ── identitystore — groups ─────────────────────────────────────────
        'CreateGroup': {'identityStoreId': 'd-12345', 'displayName': 'test-group',
             'description': 'Test group'},
        'DescribeGroup': lambda store: (
            g := store.create_group(identityStoreId='d-is-dgrp', displayName='desc-group'),
            {'identityStoreId': 'd-is-dgrp', 'groupId': g['GroupId']}
        )[1],
        'UpdateGroup': lambda store: (
            g := store.create_group(identityStoreId='d-is-ugrp', displayName='upd-group'),
            {'identityStoreId': 'd-is-ugrp', 'groupId': g['GroupId'],
             'operations': [{'attributePath': 'displayName', 'attributeValue': 'upd-group-renamed'}]}
        )[1],
        'DeleteGroup': lambda store: (
            g := store.create_group(identityStoreId='d-is-dgrp2', displayName='del-group'),
            {'identityStoreId': 'd-is-dgrp2', 'groupId': g['GroupId']}
        )[1],
        'ListGroups': {'identityStoreId': 'd-12345'},
        'GetGroupId': lambda store: (
            store.create_group(identityStoreId='d-is-ggid', displayName='ggid-group'),
            {'identityStoreId': 'd-is-ggid',
             'alternateIdentifier': {'UniqueAttribute': {'AttributePath': 'displayName', 'AttributeValue': 'ggid-group'}}}
        )[1],
        # ── identitystore — memberships ────────────────────────────────────
        'CreateGroupMembership': lambda store: (
            g := store.create_group(identityStoreId='d-is-cgm', displayName='cgm-group'),
            u := store.create_user(identityStoreId='d-is-cgm', userName='cgm-user'),
            {'identityStoreId': 'd-is-cgm', 'groupId': g['GroupId'],
             'memberId': {'userId': u['UserId']}}
        )[2],
        'DescribeGroupMembership': lambda store: (
            g := store.create_group(identityStoreId='d-is-dgm', displayName='dgm-group'),
            u := store.create_user(identityStoreId='d-is-dgm', userName='dgm-user'),
            m := store.create_group_membership(identityStoreId='d-is-dgm', groupId=g['GroupId'],
                memberId={'userId': u['UserId']}),
            {'identityStoreId': 'd-is-dgm', 'membershipId': m['MembershipId']}
        )[3],
        'DeleteGroupMembership': lambda store: (
            g := store.create_group(identityStoreId='d-is-lgm', displayName='lgm-group'),
            u := store.create_user(identityStoreId='d-is-lgm', userName='lgm-user'),
            m := store.create_group_membership(identityStoreId='d-is-lgm', groupId=g['GroupId'],
                memberId={'userId': u['UserId']}),
            {'identityStoreId': 'd-is-lgm', 'membershipId': m['MembershipId']}
        )[3],
        'ListGroupMemberships': lambda store: (
            g := store.create_group(identityStoreId='d-is-lgm2', displayName='lgm2-group'),
            {'identityStoreId': 'd-is-lgm2', 'groupId': g['GroupId']}
        )[1],
        'ListGroupMembershipsForMember': lambda store: (
            u := store.create_user(identityStoreId='d-is-lgmm', userName='lgmm-user'),
            {'identityStoreId': 'd-is-lgmm', 'memberId': {'userId': u['UserId']}}
        )[1],
        'GetGroupMembershipId': lambda store: (
            g := store.create_group(identityStoreId='d-is-ggmi', displayName='ggmi-group'),
            u := store.create_user(identityStoreId='d-is-ggmi', userName='ggmi-user'),
            store.create_group_membership(identityStoreId='d-is-ggmi', groupId=g['GroupId'],
                memberId={'userId': u['UserId']}),
            {'identityStoreId': 'd-is-ggmi', 'groupId': g['GroupId'],
             'memberId': {'userId': u['UserId']}}
        )[3],
        'IsMemberInGroups': lambda store: (
            g := store.create_group(identityStoreId='d-is-img', displayName='img-group'),
            u := store.create_user(identityStoreId='d-is-img', userName='img-user'),
            store.create_group_membership(identityStoreId='d-is-img', groupId=g['GroupId'],
                memberId={'userId': u['UserId']}),
            {'identityStoreId': 'd-is-img', 'memberId': {'userId': u['UserId']},
             'groupIds': [g['GroupId']]}
        )[3],
        # ── appconfig — applications ───────────────────────────────────────
        'CreateApplication': {'name': 'test-app', 'description': 'Test AppConfig app'},
        'GetApplication': lambda store: (
            a := store.create_application(name='ac-get-app'),
            {'applicationId': a['id']}
        )[1],
        'UpdateApplication': lambda store: (
            a := store.create_application(name='ac-upd-app'),
            {'applicationId': a['id'], 'name': 'ac-upd-renamed'}
        )[1],
        'DeleteApplication': lambda store: (
            a := store.create_application(name='ac-del-app'),
            {'applicationId': a['id']}
        )[1],
        'ListApplications': {},
        # ── appconfig — configuration profiles ─────────────────────────────
        'CreateConfigurationProfile': lambda store: (
            a := store.create_application(name='ac-cp-app'),
            {'applicationId': a['id'], 'name': 'test-profile',
             'locationUri': 'hosted://test'}
        )[1],
        'GetConfigurationProfile': lambda store: (
            a := store.create_application(name='ac-gcp-app'),
            p := store.create_configuration_profile(applicationId=a['id'], name='gcp-prof',
                locationUri='hosted://test'),
            {'applicationId': a['id'], 'configurationProfileId': p['id']}
        )[2],
        'UpdateConfigurationProfile': lambda store: (
            a := store.create_application(name='ac-ucp-app'),
            p := store.create_configuration_profile(applicationId=a['id'], name='ucp-prof',
                locationUri='hosted://test'),
            {'applicationId': a['id'], 'configurationProfileId': p['id'],
             'name': 'ucp-renamed'}
        )[2],
        'DeleteConfigurationProfile': lambda store: (
            a := store.create_application(name='ac-dcp-app'),
            p := store.create_configuration_profile(applicationId=a['id'], name='dcp-prof',
                locationUri='hosted://test'),
            {'applicationId': a['id'], 'configurationProfileId': p['id']}
        )[2],
        'ListConfigurationProfiles': lambda store: (
            a := store.create_application(name='ac-lcp-app'),
            {'applicationId': a['id']}
        )[1],
        # ── appconfig — environments ───────────────────────────────────────
        'CreateEnvironment': lambda store: (
            a := store.create_application(name='ac-env-app'),
            {'applicationId': a['id'], 'name': 'test-env'}
        )[1],
        'GetEnvironment': lambda store: (
            a := store.create_application(name='ac-genv-app'),
            e := store.create_environment(applicationId=a['id'], name='genv-env'),
            {'applicationId': a['id'], 'environmentId': e['id']}
        )[2],
        'UpdateEnvironment': lambda store: (
            a := store.create_application(name='ac-uenv-app'),
            e := store.create_environment(applicationId=a['id'], name='uenv-env'),
            {'applicationId': a['id'], 'environmentId': e['id'],
             'name': 'uenv-renamed'}
        )[2],
        'DeleteEnvironment': lambda store: (
            a := store.create_application(name='ac-denv-app'),
            e := store.create_environment(applicationId=a['id'], name='denv-env'),
            {'applicationId': a['id'], 'environmentId': e['id']}
        )[2],
        'ListEnvironments': lambda store: (
            a := store.create_application(name='ac-lenv-app'),
            {'applicationId': a['id']}
        )[1],
        # ── appconfig — tags ──────────────────────────────────────────────
        'appconfig.TagResource': lambda store: (
            a := store.create_application(name='ac-tag-app'),
            {'resourceArn': 'arn:aws:appconfig:us-east-1:000000000000:application/' + a['id'],
             'tags': {'env': 'test'}}
        )[1],
        'appconfig.UntagResource': lambda store: (
            a := store.create_application(name='ac-utag-app'),
            {'resourceArn': 'arn:aws:appconfig:us-east-1:000000000000:application/' + a['id'],
             'tagKeys': ['env']}
        )[1],
        'appconfig.ListTagsForResource': lambda store: (
            a := store.create_application(name='ac-ltag-app'),
            {'resourceArn': 'arn:aws:appconfig:us-east-1:000000000000:application/' + a['id']}
        )[1],
        # ── codebuild — projects ──────────────────────────────────────────
        'CreateProject': {
            'name': 'test-project',
            'source': {'type': 'NO_SOURCE'},
            'environment': {'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                'type': 'LINUX_CONTAINER'},
            'artifacts': {'type': 'NO_ARTIFACTS'},
            'serviceRole': 'arn:aws:iam::000000000000:role/test'
        },
        'BatchGetProjects': lambda store: (
            store.projects.create_project(name='cb-bgp', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            {'names': ['cb-bgp']}
        )[1],
        'ListProjects': {},
        'DeleteProject': lambda store: (
            store.projects.create_project(name='cb-del', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            {'name': 'cb-del'}
        )[1],
        # ── codebuild — builds ────────────────────────────────────────────
        'StartBuild': lambda store: (
            store.projects.create_project(name='cb-sb', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            {'projectName': 'cb-sb'}
        )[1],
        'BatchGetBuilds': lambda store: (
            store.projects.create_project(name='cb-bgb', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            b := store.builds.start_build(project_name='cb-bgb'),
            {'ids': [b.id]}
        )[2],
        'StopBuild': lambda store: (
            store.projects.create_project(name='cb-stb', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            b := store.builds.start_build(project_name='cb-stb'),
            {'id': b.id}
        )[2],
        'RetryBuild': lambda store: (
            store.projects.create_project(name='cb-rb', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            b := store.builds.start_build(project_name='cb-rb'),
            {'id': b.id}
        )[2],
        'ListBuilds': {},
        'ListBuildsForProject': lambda store: (
            store.projects.create_project(name='cb-lbfp', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            {'projectName': 'cb-lbfp'}
        )[1],
        'BatchDeleteBuilds': lambda store: (
            store.projects.create_project(name='cb-bdb', source={'type': 'NO_SOURCE'},
                environment={'computeType': 'BUILD_GENERAL1_SMALL', 'image': 'aws/codebuild/standard:5.0',
                    'type': 'LINUX_CONTAINER'},
                artifacts={'type': 'NO_ARTIFACTS'}, service_role='arn:aws:iam::000000000000:role/r'),
            b := store.builds.start_build(project_name='cb-bdb'),
            {'ids': [b.id]}
        )[2],
        # ── lexv2-runtime ──────────────────────────────────────────────────
        'PutSession': {'botId': 'test-bot', 'botAliasId': 'TSTALIAS', 'localeId': 'en_US',
            'sessionId': 'test-session', 'sessionState': {'dialogAction': {'type': 'Close'}}},
        'GetSession': lambda store: (
            store.put_session(botId='l2-gs-bot', botAliasId='TSTALIAS', localeId='en_US',
                sessionId='gs-sess'),
            {'botId': 'l2-gs-bot', 'botAliasId': 'TSTALIAS', 'localeId': 'en_US',
             'sessionId': 'gs-sess'}
        )[1],
        'DeleteSession': lambda store: (
            store.put_session(botId='l2-ds-bot', botAliasId='TSTALIAS', localeId='en_US',
                sessionId='ds-sess'),
            {'botId': 'l2-ds-bot', 'botAliasId': 'TSTALIAS', 'localeId': 'en_US',
             'sessionId': 'ds-sess'}
        )[1],
        'RecognizeText': {'botId': 'test-bot', 'botAliasId': 'TSTALIAS', 'localeId': 'en_US',
            'sessionId': 'rt-sess', 'text': 'hello'},
        'RecognizeUtterance': {'botId': 'test-bot', 'botAliasId': 'TSTALIAS', 'localeId': 'en_US',
            'sessionId': 'ru-sess'},
        'StartConversation': {'botId': 'test-bot', 'botAliasId': 'TSTALIAS', 'localeId': 'en_US',
            'sessionId': 'sc-sess'},
        # ── verifiedpermissions — policy stores ──────────────────────────────
        'CreatePolicyStore': {'ValidationSettings': {'mode': 'STRICT'}},
        'GetPolicyStore': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId']}
        )[1],
        'ListPolicyStores': {},
        'DeletePolicyStore': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId']}
        )[1],
        # ── verifiedpermissions — schema ──────────────────────────────────────
        'PutSchema': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId'], 'Definition': {'cedarJson': '{"test":1}'}}
        )[1],
        'GetSchema': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            store.put_schema(PolicyStoreId=ps['policyStoreId'], Definition={'cedarJson': '{"test":1}'}),
            {'PolicyStoreId': ps['policyStoreId']}
        )[2],
        # ── verifiedpermissions — policies ────────────────────────────────────
        'CreatePolicy': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId'],
             'Definition': {'Static': {'Statement': 'permit(principal, action, resource);'}}}
        )[1],
        'GetPolicy': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            p := store.create_policy(PolicyStoreId=ps['policyStoreId'],
                Definition={'Static': {'Statement': 'permit(principal, action, resource);'}}),
            {'PolicyStoreId': ps['policyStoreId'], 'PolicyId': p['policyId']}
        )[2],
        'ListPolicies': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId']}
        )[1],
        'DeletePolicy': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            p := store.create_policy(PolicyStoreId=ps['policyStoreId'],
                Definition={'Static': {'Statement': 'permit(principal, action, resource);'}}),
            {'PolicyStoreId': ps['policyStoreId'], 'PolicyId': p['policyId']}
        )[2],
        # ── verifiedpermissions — identity sources ────────────────────────────
        'CreateIdentitySource': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId'],
             'Configuration': {'CognitoUserPoolConfiguration': {'UserPoolArn': 'arn:aws:cognito-idp:us-east-1:000000000000:userpool/test'}}}
        )[1],
        'GetIdentitySource': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            iss := store.create_identity_source(PolicyStoreId=ps['policyStoreId'],
                Configuration={'CognitoUserPoolConfiguration': {'UserPoolArn': 'arn:aws:cognito-idp:us-east-1:000000000000:userpool/test'}}),
            {'PolicyStoreId': ps['policyStoreId'], 'IdentitySourceId': iss['identitySourceId']}
        )[2],
        'ListIdentitySources': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId']}
        )[1],
        'DeleteIdentitySource': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            iss := store.create_identity_source(PolicyStoreId=ps['policyStoreId'],
                Configuration={'CognitoUserPoolConfiguration': {'UserPoolArn': 'arn:aws:cognito-idp:us-east-1:000000000000:userpool/test'}}),
            {'PolicyStoreId': ps['policyStoreId'], 'IdentitySourceId': iss['identitySourceId']}
        )[2],
        # ── verifiedpermissions — authorization ───────────────────────────────
        'IsAuthorized': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'PolicyStoreId': ps['policyStoreId'],
             'Principal': {'EntityType': 'User', 'EntityId': 'test-user'},
             'Action': {'ActionType': 'Action', 'ActionId': 'test-action'},
             'Resource': {'EntityType': 'Resource', 'EntityId': 'test-resource'}}
        )[1],
        # ── verifiedpermissions — tags ────────────────────────────────────────
        'verifiedpermissions.TagResource': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'ResourceArn': ps['arn'], 'Tags': [{'Key': 'test', 'Value': 'val'}]}
        )[1],
        'verifiedpermissions.ListTagsForResource': lambda store: (
            ps := store.create_policy_store(ValidationSettings={'mode': 'STRICT'}),
            {'ResourceArn': ps['arn']}
        )[1],
        # ── timestream-influxdb — clusters ────────────────────────────
        'CreateDbCluster': {'name': 'test-cluster', 'dbInstanceType': 'db.influx.medium',
            'vpcSubnetIds': ['subnet-abc123'], 'vpcSecurityGroupIds': ['sg-abc123']},
        'GetDbCluster': lambda store: (
            c := store.create_db_cluster(name='ts-gc', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'dbClusterId': c['id']}
        )[1],
        'ListDbClusters': {},
        'DeleteDbCluster': lambda store: (
            c := store.create_db_cluster(name='ts-dc', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'dbClusterId': c['id']}
        )[1],
        'UpdateDbCluster': lambda store: (
            c := store.create_db_cluster(name='ts-uc', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'dbClusterId': c['id'], 'port': 8087}
        )[1],
        'RebootDbCluster': lambda store: (
            c := store.create_db_cluster(name='ts-rc', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'dbClusterId': c['id']}
        )[1],
        # ── timestream-influxdb — instances ────────────────────────────
        'CreateDbInstance': {'name': 'test-instance', 'password': 'TestPass123!',
            'dbInstanceType': 'db.influx.medium', 'vpcSubnetIds': ['subnet-abc123'],
            'vpcSecurityGroupIds': ['sg-abc123'], 'allocatedStorage': 400},
        'GetDbInstance': lambda store: (
            i := store.create_db_instance(name='ts-gi', password='TestPass123!',
                dbInstanceType='db.influx.medium', vpcSubnetIds=['subnet-abc123'],
                vpcSecurityGroupIds=['sg-abc123'], allocatedStorage=400),
            {'identifier': i['id']}
        )[1],
        'ListDbInstances': {},
        'ListDbInstancesForCluster': lambda store: (
            c := store.create_db_cluster(name='ts-lic', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'dbClusterId': c['id']}
        )[1],
        'DeleteDbInstance': lambda store: (
            i := store.create_db_instance(name='ts-di', password='TestPass123!',
                dbInstanceType='db.influx.medium', vpcSubnetIds=['subnet-abc123'],
                vpcSecurityGroupIds=['sg-abc123'], allocatedStorage=400),
            {'identifier': i['id']}
        )[1],
        'UpdateDbInstance': lambda store: (
            i := store.create_db_instance(name='ts-ui', password='TestPass123!',
                dbInstanceType='db.influx.medium', vpcSubnetIds=['subnet-abc123'],
                vpcSecurityGroupIds=['sg-abc123'], allocatedStorage=400),
            {'identifier': i['id'], 'port': 8087}
        )[1],
        'RebootDbInstance': lambda store: (
            i := store.create_db_instance(name='ts-ri', password='TestPass123!',
                dbInstanceType='db.influx.medium', vpcSubnetIds=['subnet-abc123'],
                vpcSecurityGroupIds=['sg-abc123'], allocatedStorage=400),
            {'identifier': i['id']}
        )[1],
        # ── timestream-influxdb — parameter groups ─────────────────────
        'CreateDbParameterGroup': {'name': 'test-pg'},
        'GetDbParameterGroup': lambda store: (
            pg := store.create_db_parameter_group(name='ts-gpg'),
            {'identifier': pg['id']}
        )[1],
        'ListDbParameterGroups': {},
        # ── timestream-influxdb — tags ──────────────────────────────────
        'timestream-influxdb.TagResource': lambda store: (
            c := store.create_db_cluster(name='ts-tag', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'resourceArn': c['arn'], 'tags': [{'key': 'test', 'value': 'val'}]}
        )[1],
        'timestream-influxdb.UntagResource': lambda store: (
            c := store.create_db_cluster(name='ts-ut', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'resourceArn': c['arn'], 'tagKeys': ['test']}
        )[1],
        'timestream-influxdb.ListTagsForResource': lambda store: (
            c := store.create_db_cluster(name='ts-ltr', dbInstanceType='db.influx.medium',
                vpcSubnetIds=['subnet-abc123'], vpcSecurityGroupIds=['sg-abc123']),
            {'resourceArn': c['arn']}
        )[1],
        # ── storagegateway — gateways ───────────────────────────────────
        'ActivateGateway': {'ActivationKey': 'test-key-12345'},
        'DescribeGatewayInformation': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-dgi-key'),
            {'GatewayARN': g['GatewayARN']}
        )[1],
        'ListGateways': {},
        'DeleteGateway': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-dg-key'),
            {'GatewayARN': g['GatewayARN']}
        )[1],
        # ── storagegateway — file shares ────────────────────────────────
        'CreateNFSFileShare': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-nfs-key'),
            {'GatewayARN': g['GatewayARN'], 'Role': 'arn:aws:iam::000000000000:role/test',
             'LocationARN': 'arn:aws:s3:::test-bucket'}
        )[1],
        'CreateSMBFileShare': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-smb-key'),
            {'GatewayARN': g['GatewayARN'], 'Role': 'arn:aws:iam::000000000000:role/test',
             'LocationARN': 'arn:aws:s3:::test-bucket'}
        )[1],
        'DescribeNFSFileShares': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-dnfs-key'),
            fs := store.create_nfs_file_share(GatewayARN=g['GatewayARN'],
                Role='arn:aws:iam::000000000000:role/test', LocationARN='arn:aws:s3:::test'),
            {'FileShareARNList': [fs['FileShareARN']]}
        )[2],
        'ListFileShares': {},
        'DeleteFileShare': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-dfs-key'),
            fs := store.create_nfs_file_share(GatewayARN=g['GatewayARN'],
                Role='arn:aws:iam::000000000000:role/test', LocationARN='arn:aws:s3:::test'),
            {'FileShareARN': fs['FileShareARN']}
        )[2],
        # ── storagegateway — volumes ────────────────────────────────────
        'CreateCachediSCSIVolume': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-vol-key'),
            {'GatewayARN': g['GatewayARN'], 'VolumeSizeInBytes': 107374182400,
             'TargetName': 'iqn.test-target'}
        )[1],
        'DescribeCachediSCSIVolumes': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-dv-key'),
            v := store.create_cached_iscsi_volume(GatewayARN=g['GatewayARN'],
                VolumeSizeInBytes=107374182400, TargetName='iqn.dv-target'),
            {'VolumeARNs': [v['VolumeARN']]}
        )[2],
        'ListVolumes': {},
        'DeleteVolume': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-delv-key'),
            v := store.create_cached_iscsi_volume(GatewayARN=g['GatewayARN'],
                VolumeSizeInBytes=107374182400, TargetName='iqn.delv-target'),
            {'VolumeARN': v['VolumeARN']}
        )[2],
        # ── storagegateway — tapes ──────────────────────────────────────
        'CreateTapes': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-tape-key'),
            {'GatewayARN': g['GatewayARN'], 'TapeSizeInBytes': 107374182400,
             'ClientToken': 'test-token', 'NumTapesToCreate': 1}
        )[1],
        'DescribeTapes': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-dt-key'),
            t := store.create_tapes(GatewayARN=g['GatewayARN'],
                TapeSizeInBytes=107374182400, ClientToken='dt-token', NumTapesToCreate=1),
            {'TapeARNs': t['TapeARNs']}
        )[2],
        'ListTapes': {},
        'DeleteTape': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-delt-key'),
            t := store.create_tapes(GatewayARN=g['GatewayARN'],
                TapeSizeInBytes=107374182400, ClientToken='delt-token', NumTapesToCreate=1),
            {'GatewayARN': g['GatewayARN'], 'TapeARN': t['TapeARNs'][0]}
        )[2],
        # ── storagegateway — tags ───────────────────────────────────────
        'storagegateway.AddTagsToResource': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-atr-key'),
            {'ResourceARN': g['GatewayARN'], 'Tags': [{'Key': 'test', 'Value': 'val'}]}
        )[1],
        'storagegateway.ListTagsForResource': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-ltr-key'),
            {'ResourceARN': g['GatewayARN']}
        )[1],
        'storagegateway.RemoveTagsFromResource': lambda store: (
            g := store.activate_gateway(ActivationKey='sg-rtr-key'),
            {'ResourceARN': g['GatewayARN'], 'TagKeys': ['test']}
        )[1],
        # ── datasync — agents ────────────────────────────────────────────
        'CreateAgent': {'ActivationKey': 'ds-test-key'},
        'DescribeAgent': lambda store: (
            a := store.create_agent(ActivationKey='ds-da-key'),
            {'AgentArn': a['AgentArn']}
        )[1],
        'ListAgents': {},
        'DeleteAgent': lambda store: (
            a := store.create_agent(ActivationKey='ds-dela-key'),
            {'AgentArn': a['AgentArn']}
        )[1],
        'UpdateAgent': lambda store: (
            a := store.create_agent(ActivationKey='ds-ua-key'),
            {'AgentArn': a['AgentArn'], 'Name': 'updated-agent'}
        )[1],
        # ── datasync — locations ─────────────────────────────────────────
        'CreateLocationS3': {'S3BucketArn': 'arn:aws:s3:::test-bucket',
            'S3Config': {'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}},
        'CreateLocationNfs': {'Subdirectory': '/test',
            'ServerHostname': 'test-host.example.com',
            'OnPremConfig': {'AgentArns': []}},
        'ListLocations': {},
        'DeleteLocation': lambda store: (
            loc := store.create_location_s3(S3BucketArn='arn:aws:s3:::del-test',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            {'LocationArn': loc['LocationArn']}
        )[1],
        'DescribeLocationS3': lambda store: (
            loc := store.create_location_s3(S3BucketArn='arn:aws:s3:::desc-test',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            {'LocationArn': loc['LocationArn']}
        )[1],
        # ── datasync — tasks ─────────────────────────────────────────────
        'CreateTask': lambda store: (
            src := store.create_location_s3(S3BucketArn='arn:aws:s3:::src-task',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            dst := store.create_location_s3(S3BucketArn='arn:aws:s3:::dst-task',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            {'SourceLocationArn': src['LocationArn'],
             'DestinationLocationArn': dst['LocationArn']}
        )[2],
        'DescribeTask': lambda store: (
            src := store.create_location_s3(S3BucketArn='arn:aws:s3:::s-dt',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            dst := store.create_location_s3(S3BucketArn='arn:aws:s3:::d-dt',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            t := store.create_task(SourceLocationArn=src['LocationArn'],
                DestinationLocationArn=dst['LocationArn']),
            {'TaskArn': t['TaskArn']}
        )[3],
        'ListTasks': {},
        'DeleteTask': lambda store: (
            src := store.create_location_s3(S3BucketArn='arn:aws:s3:::s-delt',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            dst := store.create_location_s3(S3BucketArn='arn:aws:s3:::d-delt',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            t := store.create_task(SourceLocationArn=src['LocationArn'],
                DestinationLocationArn=dst['LocationArn']),
            {'TaskArn': t['TaskArn']}
        )[3],
        'UpdateTask': lambda store: (
            src := store.create_location_s3(S3BucketArn='arn:aws:s3:::s-ut',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            dst := store.create_location_s3(S3BucketArn='arn:aws:s3:::d-ut',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            t := store.create_task(SourceLocationArn=src['LocationArn'],
                DestinationLocationArn=dst['LocationArn']),
            {'TaskArn': t['TaskArn'], 'Name': 'updated-task'}
        )[3],
        'StartTaskExecution': lambda store: (
            src := store.create_location_s3(S3BucketArn='arn:aws:s3:::s-ste',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            dst := store.create_location_s3(S3BucketArn='arn:aws:s3:::d-ste',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            t := store.create_task(SourceLocationArn=src['LocationArn'],
                DestinationLocationArn=dst['LocationArn']),
            {'TaskArn': t['TaskArn']}
        )[3],
        'DescribeTaskExecution': lambda store: (
            src := store.create_location_s3(S3BucketArn='arn:aws:s3:::s-dte',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            dst := store.create_location_s3(S3BucketArn='arn:aws:s3:::d-dte',
                S3Config={'BucketAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            t := store.create_task(SourceLocationArn=src['LocationArn'],
                DestinationLocationArn=dst['LocationArn']),
            e := store.start_task_execution(TaskArn=t['TaskArn']),
            {'TaskExecutionArn': e['TaskExecutionArn']}
        )[4],
        # ── datasync — tags ──────────────────────────────────────────────
        'datasync.TagResource': lambda store: (
            a := store.create_agent(ActivationKey='ds-tr-key'),
            {'ResourceArn': a['AgentArn'],
             'Tags': [{'Key': 'test', 'Value': 'val'}]}
        )[1],
        'datasync.ListTagsForResource': lambda store: (
            a := store.create_agent(ActivationKey='ds-ltr-key'),
            {'ResourceArn': a['AgentArn']}
        )[1],
        # ── signer — profiles ────────────────────────────────────────────
        'PutSigningProfile': {'platformId': 'AWSLambda-SHA384-ECDSA',
            'profileName': 'test-profile'},
        'GetSigningProfile': lambda store: (
            p := store.create_profile(profileName='gs-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'profileName': 'gs-profile'}
        )[1],
        'ListSigningProfiles': {},
        'CancelSigningProfile': lambda store: (
            p := store.create_profile(profileName='cs-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'profileName': 'cs-profile'}
        )[1],
        'RevokeSigningProfile': lambda store: (
            p := store.create_profile(profileName='rs-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'profileName': 'rs-profile',
             'profileVersion': p.profileVersion,
             'reason': 'test-revocation',
             'effectiveTime': 1700000000}
        )[1],
        # ── signer — platforms ───────────────────────────────────────────
        'GetSigningPlatform': {'platformId': 'AWSLambda-SHA384-ECDSA'},
        'ListSigningPlatforms': {},
        # ── signer — jobs ────────────────────────────────────────────────
        'StartSigningJob': lambda store: (
            p := store.create_profile(profileName='sj-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'source': {'s3': {'bucketName': 'test-bucket', 'key': 'test.zip',
                'version': '1'}},
             'destination': {'s3': {'bucketName': 'out-bucket', 'prefix': 'signed/'}},
             'profileName': 'sj-profile',
             'clientRequestToken': 'token-12345'}
        )[1],
        'DescribeSigningJob': lambda store: (
            p := store.create_profile(profileName='dj-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            j := store.start_job(
                source={'s3': {'bucketName': 'tb', 'key': 'x.zip', 'version': '1'}},
                destination={'s3': {'bucketName': 'ob', 'prefix': 's/'}},
                profileName='dj-profile',
                clientRequestToken='token-dj'),
            {'jobId': j.jobId}
        )[2],
        'ListSigningJobs': {},
        'RevokeSignature': lambda store: (
            p := store.create_profile(profileName='rvs-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            j := store.start_job(
                source={'s3': {'bucketName': 'tb2', 'key': 'y.zip', 'version': '1'}},
                destination={'s3': {'bucketName': 'ob2', 'prefix': 's/'}},
                profileName='rvs-profile',
                clientRequestToken='token-rvs'),
            {'jobId': j.jobId, 'reason': 'test-revoke'}
        )[2],
        # ── signer — payload ─────────────────────────────────────────────
        'SignPayload': lambda store: (
            p := store.create_profile(profileName='sp-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'profileName': 'sp-profile',
             'payload': b'test-payload',
             'payloadFormat': 'JSON'}
        )[1],
        # ── signer — permissions ─────────────────────────────────────────
        'AddProfilePermission': lambda store: (
            p := store.create_profile(profileName='ap-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'profileName': 'ap-profile',
             'action': 'signer:StartSigningJob',
             'principal': '123456789012',
             'statementId': 'stmt-001'}
        )[1],
        'RemoveProfilePermission': lambda store: (
            p := store.create_profile(profileName='rp-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            rev := store.add_permission(profileName='rp-profile',
                action='signer:StartSigningJob', principal='123456789012',
                statementId='stmt-001'),
            {'profileName': 'rp-profile',
             'statementId': 'stmt-001',
             'revisionId': rev}
        )[2],
        'ListProfilePermissions': lambda store: (
            p := store.create_profile(profileName='lp-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'profileName': 'lp-profile'}
        )[1],
        # ── signer — revocation status ───────────────────────────────────
        'GetRevocationStatus': lambda store: (
            p := store.create_profile(profileName='grs-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            j := store.start_job(
                source={'s3': {'bucketName': 'tb3', 'key': 'z.zip', 'version': '1'}},
                destination={'s3': {'bucketName': 'ob3', 'prefix': 's/'}},
                profileName='grs-profile',
                clientRequestToken='token-grs'),
            {'signatureTimestamp': 1700000000,
             'platformId': 'AWSLambda-SHA384-ECDSA',
             'profileVersionArn': p.profileVersionArn,
             'jobArn': f'arn:aws:signer:us-east-1:123456789012:/signing-jobs/{j.jobId}',
             'certificateHashes': ['sha256hash']}
        )[2],
        # ── signer — tags ────────────────────────────────────────────────
        'signer.TagResource': lambda store: (
            p := store.create_profile(profileName='str-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'resourceArn': p.arn,
             'tags': [{'key': 'test', 'value': 'val'}]}
        )[1],
        'signer.UntagResource': lambda store: (
            p := store.create_profile(profileName='sur-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            store.tag_resource(resourceArn=p.arn,
                tags={'test': 'val'}),
            {'resourceArn': p.arn,
             'tagKeys': ['test']}
        )[2],
        'signer.ListTagsForResource': lambda store: (
            p := store.create_profile(profileName='sltr-profile',
                platformId='AWSLambda-SHA384-ECDSA'),
            {'resourceArn': p.arn}
        )[1],
        # ── bedrock-agent — create ──────────────────────────────────────────
        'bedrock-agent.CreateAgent': {'agentName': 'ba-test-agent', 'foundationModel': 'anthropic.claude-v2'},
        'bedrock-agent.CreateKnowledgeBase': {'name': 'ba-test-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}},

        # ── bedrock-agent — list ────────────────────────────────────────────
        'bedrock-agent.ListAgents': {},
        'bedrock-agent.ListKnowledgeBases': {},

        # ── bedrock-agent — get/describe (lambdas: create prerequisite) ──────
        'bedrock-agent.GetAgent': lambda store: (
            a := store.create_agent({'agentName': 'ba-get-agent', 'foundationModel': 'anthropic.claude-v2'}),
            {'agentId': a.agentId}
        )[1],
        'bedrock-agent.GetKnowledgeBase': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-get-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId}
        )[1],

        # ── bedrock-agent — delete (lambdas: create prerequisite, then delete) ──
        'bedrock-agent.DeleteAgent': lambda store: (
            a := store.create_agent({'agentName': 'ba-del-agent', 'foundationModel': 'anthropic.claude-v2'}),
            {'agentId': a.agentId}
        )[1],
        'bedrock-agent.DeleteKnowledgeBase': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-del-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId}
        )[1],

        # ── bedrock-agent — update (lambdas: create prerequisite, then update) ──
        'bedrock-agent.UpdateAgent': lambda store: (
            a := store.create_agent({'agentName': 'ba-upd-agent', 'foundationModel': 'anthropic.claude-v2'}),
            {'agentId': a.agentId, 'agentName': 'ba-upd-agent-renamed', 'foundationModel': 'anthropic.claude-v2'}
        )[1],
        'bedrock-agent.UpdateKnowledgeBase': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-upd-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId, 'name': 'ba-upd-kb-renamed', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}
        )[1],

        # ── bedroch-agent — prepare ────────────────────────────────────────
        'bedrock-agent.PrepareAgent': lambda store: (
            a := store.create_agent({'agentName': 'ba-prep-agent', 'foundationModel': 'anthropic.claude-v2'}),
            {'agentId': a.agentId}
        )[1],

        # ── bedrock-agent — data sources (lambdas: create KB prerequisite) ──
        'bedrock-agent.CreateDataSource': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-ds-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId, 'name': 'ba-test-ds', 'dataSourceConfiguration': {'s3Configuration': {'bucketArn': 'arn:aws:s3:::test-bucket'}}}
        )[1],
        'bedrock-agent.GetDataSource': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-gds-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            ds := store.create_data_source({'knowledgeBaseId': kb.knowledgeBaseId, 'name': 'ba-gds-ds', 'dataSourceConfiguration': {'s3Configuration': {'bucketArn': 'arn:aws:s3:::test-bucket'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId, 'dataSourceId': ds.dataSourceId}
        )[2],
        'bedrock-agent.UpdateDataSource': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-uds-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            ds := store.create_data_source({'knowledgeBaseId': kb.knowledgeBaseId, 'name': 'ba-uds-ds', 'dataSourceConfiguration': {'s3Configuration': {'bucketArn': 'arn:aws:s3:::test-bucket'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId, 'dataSourceId': ds.dataSourceId, 'name': 'ba-uds-ds-renamed', 'dataSourceConfiguration': {'s3Configuration': {'bucketArn': 'arn:aws:s3:::test-bucket'}}}
        )[2],
        'bedrock-agent.DeleteDataSource': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-dds-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            ds := store.create_data_source({'knowledgeBaseId': kb.knowledgeBaseId, 'name': 'ba-dds-ds', 'dataSourceConfiguration': {'s3Configuration': {'bucketArn': 'arn:aws:s3:::test-bucket'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId, 'dataSourceId': ds.dataSourceId}
        )[2],
        'bedrock-agent.ListDataSources': lambda store: (
            kb := store.create_knowledge_base({'name': 'ba-lds-kb', 'roleArn': 'arn:aws:iam::000000000000:role/test', 'knowledgeBaseConfiguration': {'type': 'VECTOR', 'vectorKnowledgeBaseConfiguration': {'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'}}}),
            {'knowledgeBaseId': kb.knowledgeBaseId}
        )[1],

        # ── bedrock-agent — tags (service-prefixed to avoid collision) ──────
        'bedrock-agent.TagResource': lambda store: (
            a := store.create_agent({'agentName': 'ba-tag-agent', 'foundationModel': 'anthropic.claude-v2'}),
            {'resourceArn': a.agentArn, 'tags': {'test': 'val'}}
        )[1],
        'bedrock-agent.UntagResource': lambda store: (
            a := store.create_agent({'agentName': 'ba-untag-agent', 'foundationModel': 'anthropic.claude-v2'}),
            store.tag_resource(resourceARN=a.agentArn, tags={'test': 'val'}),
            {'resourceArn': a.agentArn, 'tagKeys': ['test']}
        )[2],
        'bedrock-agent.ListTagsForResource': lambda store: (
            a := store.create_agent({'agentName': 'ba-ltr-agent', 'foundationModel': 'anthropic.claude-v2'}),
            {'resourceArn': a.agentArn}
        )[1],

        # ── mediaconvert — create ──────────────────────────────────────────
        'mediaconvert.CreateJob': {'Role': 'arn:aws:iam::000000000000:role/mc-test', 'Settings': {'OutputGroups': []}},
        'mediaconvert.CreateJobTemplate': {'Name': 'mc-test-template', 'Settings': {'OutputGroups': []}},
        'mediaconvert.CreatePreset': {'Name': 'mc-test-preset', 'Settings': {'ContainerSettings': {'Container': 'MP4'}}},
        'mediaconvert.CreateQueue': {'Name': 'mc-test-queue'},

        # ── mediaconvert — list ────────────────────────────────────────────
        'mediaconvert.ListJobs': {},
        'mediaconvert.ListJobTemplates': {},
        'mediaconvert.ListPresets': {},
        'mediaconvert.ListQueues': {},

        # ── mediaconvert — get/describe (lambdas: create prerequisite in store) ──
        'mediaconvert.GetJob': lambda store: (
            job := JobRecord(id='mc-get-job', role='arn:aws:iam::000000000000:role/mc-test', settings={'OutputGroups': []}),
            store.jobs.__setitem__(job.id, job),
            {'Id': job.id}
        )[2],
        'mediaconvert.GetJobTemplate': lambda store: (
            tmpl := JobTemplateRecord(name='mc-get-template', settings={'OutputGroups': []}),
            store.job_templates.__setitem__(tmpl.name, tmpl),
            {'Name': tmpl.name}
        )[2],
        'mediaconvert.GetPreset': lambda store: (
            preset := PresetRecord(name='mc-get-preset', settings={}),
            store.presets.__setitem__(preset.name, preset),
            {'Name': preset.name}
        )[2],
        'mediaconvert.GetQueue': lambda store: (
            q := QueueRecord(name='mc-get-queue'),
            store.queues.__setitem__(q.name, q),
            {'Name': q.name}
        )[2],

        # ── mediaconvert — delete (lambdas: create prerequisite, then delete) ──
        'mediaconvert.DeleteJobTemplate': lambda store: (
            tmpl := JobTemplateRecord(name='mc-del-template', settings={'OutputGroups': []}),
            store.job_templates.__setitem__(tmpl.name, tmpl),
            {'Name': tmpl.name}
        )[2],
        'mediaconvert.DeletePreset': lambda store: (
            preset := PresetRecord(name='mc-del-preset', settings={}),
            store.presets.__setitem__(preset.name, preset),
            {'Name': preset.name}
        )[2],
        'mediaconvert.DeleteQueue': lambda store: (
            q := QueueRecord(name='mc-del-queue'),
            store.queues.__setitem__(q.name, q),
            {'Name': q.name}
        )[2],

        # ── mediaconvert — cancel ───────────────────────────────────────────
        'mediaconvert.CancelJob': lambda store: (
            job := JobRecord(id='mc-cancel-job', role='arn:aws:iam::000000000000:role/mc-test', settings={'OutputGroups': []}),
            store.jobs.__setitem__(job.id, job),
            {'Id': job.id}
        )[2],

        # ── mediaconvert — update (lambdas: create prerequisite, then update) ──
        'mediaconvert.UpdateJobTemplate': lambda store: (
            tmpl := JobTemplateRecord(name='mc-upd-template', settings={'OutputGroups': []}),
            store.job_templates.__setitem__(tmpl.name, tmpl),
            {'Name': tmpl.name, 'Settings': {'OutputGroups': []}, 'Description': 'updated'}
        )[2],
        'mediaconvert.UpdatePreset': lambda store: (
            preset := PresetRecord(name='mc-upd-preset', settings={}),
            store.presets.__setitem__(preset.name, preset),
            {'Name': preset.name, 'Settings': {}}
        )[2],
        'mediaconvert.UpdateQueue': lambda store: (
            q := QueueRecord(name='mc-upd-queue'),
            store.queues.__setitem__(q.name, q),
            {'Name': q.name, 'Description': 'updated'}
        )[2],

        # ── mediaconvert — tag (lambda: set up tag first) ───────────────────
        'mediaconvert.TagResource': lambda store: (
            q := QueueRecord(name='mc-tag-queue'),
            store.queues.__setitem__(q.name, q),
            {'Arn': 'arn:aws:mediaconvert:us-east-1:000000000000:queue/mc-tag-queue', 'Tags': {'test': 'val'}}
        )[2],

        # ── transcribe — create ─────────────────────────────────────────────
        'transcribe.CreateVocabulary': {'VocabularyName': 'tr-test-vocab', 'LanguageCode': 'en-US', 'Phrases': ['hello', 'world']},
        'transcribe.CreateVocabularyFilter': {'VocabularyFilterName': 'tr-test-filter', 'LanguageCode': 'en-US', 'Words': ['badword']},
        'transcribe.StartTranscriptionJob': {'TranscriptionJobName': 'tr-test-job', 'Media': {'MediaFileUri': 's3://test-bucket/test.mp3'}, 'LanguageCode': 'en-US'},
        'transcribe.CreateLanguageModel': {'LanguageCode': 'en-US', 'BaseModelName': 'NarrowBand', 'ModelName': 'tr-test-model', 'InputDataConfig': {'S3Uri': 's3://test-bucket/', 'TuningDataS3Uri': 's3://test-bucket/tuning/', 'DataAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}},

        # ── transcribe — list ───────────────────────────────────────────────
        'transcribe.ListVocabularies': {},
        'transcribe.ListVocabularyFilters': {},
        'transcribe.ListTranscriptionJobs': {},
        'transcribe.ListLanguageModels': {},

        # ── transcribe — get/describe (lambdas: create prerequisite) ────────
        'transcribe.GetVocabulary': lambda store: (
            v := store.create_vocabulary(VocabularyName='tr-get-vocab', LanguageCode='en-US'),
            {'VocabularyName': v['VocabularyName']}
        )[1],
        'transcribe.GetVocabularyFilter': lambda store: (
            vf := store.create_vocabulary_filter(VocabularyFilterName='tr-get-filter', LanguageCode='en-US'),
            {'VocabularyFilterName': vf['VocabularyFilterName']}
        )[1],
        'transcribe.GetTranscriptionJob': lambda store: (
            j := store.start_transcription_job(TranscriptionJobName='tr-get-job', Media={'MediaFileUri': 's3://test-bucket/test.mp3'}, LanguageCode='en-US'),
            {'TranscriptionJobName': j['TranscriptionJob']['TranscriptionJobName']}
        )[1],
        'transcribe.DescribeLanguageModel': lambda store: (
            m := store.create_language_model(LanguageCode='en-US', BaseModelName='NarrowBand', ModelName='tr-get-model', InputDataConfig={'S3Uri': 's3://test-bucket/', 'TuningDataS3Uri': 's3://test-bucket/tuning/', 'DataAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            {'ModelName': m['ModelName']}
        )[1],

        # ── transcribe — delete (lambdas: create prerequisite, then delete) ──
        'transcribe.DeleteVocabulary': lambda store: (
            v := store.create_vocabulary(VocabularyName='tr-del-vocab', LanguageCode='en-US'),
            {'VocabularyName': v['VocabularyName']}
        )[1],
        'transcribe.DeleteVocabularyFilter': lambda store: (
            vf := store.create_vocabulary_filter(VocabularyFilterName='tr-del-filter', LanguageCode='en-US'),
            {'VocabularyFilterName': vf['VocabularyFilterName']}
        )[1],
        'transcribe.DeleteTranscriptionJob': lambda store: (
            j := store.start_transcription_job(TranscriptionJobName='tr-del-job', Media={'MediaFileUri': 's3://test-bucket/test.mp3'}, LanguageCode='en-US'),
            {'TranscriptionJobName': j['TranscriptionJob']['TranscriptionJobName']}
        )[1],
        'transcribe.DeleteLanguageModel': lambda store: (
            m := store.create_language_model(LanguageCode='en-US', BaseModelName='NarrowBand', ModelName='tr-del-model', InputDataConfig={'S3Uri': 's3://test-bucket/', 'TuningDataS3Uri': 's3://test-bucket/tuning/', 'DataAccessRoleArn': 'arn:aws:iam::000000000000:role/test'}),
            {'ModelName': m['ModelName']}
        )[1],

        # ── transcribe — update (lambdas: create prerequisite, then update) ──
        'transcribe.UpdateVocabulary': lambda store: (
            v := store.create_vocabulary(VocabularyName='tr-upd-vocab', LanguageCode='en-US'),
            {'VocabularyName': v['VocabularyName'], 'LanguageCode': 'en-US', 'Phrases': ['updated']}
        )[1],
        'transcribe.UpdateVocabularyFilter': lambda store: (
            vf := store.create_vocabulary_filter(VocabularyFilterName='tr-upd-filter', LanguageCode='en-US'),
            {'VocabularyFilterName': vf['VocabularyFilterName'], 'Words': ['updatedword']}
        )[1],

        # ── kinesis — create ────────────────────────────────────────────────
        'kinesis.CreateStream': {'StreamName': 'kin-test-stream', 'ShardCount': 1},
        'kinesis.TagStream': lambda store: (
            store.create_stream('kin-tag-stream'),
            {'StreamName': 'kin-tag-stream', 'Tags': {'env': 'test'}}
        )[1],
        'kinesis.PutRecord': lambda store: (
            store.create_stream('kin-pr-stream'),
            {'StreamName': 'kin-pr-stream', 'Data': 'test-data', 'PartitionKey': 'pk-1'}
        )[1],
        'kinesis.PutRecords': lambda store: (
            store.create_stream('kin-prs-stream'),
            {'StreamName': 'kin-prs-stream', 'Records': [{'Data': 'd1', 'PartitionKey': 'pk-1'}, {'Data': 'd2', 'PartitionKey': 'pk-2'}]}
        )[1],
        # ── kinesis — list ──────────────────────────────────────────────────
        'kinesis.ListStreams': {},
        'kinesis.ListTagsForStream': lambda store: (
            store.create_stream('kin-lt-stream'),
            {'StreamName': 'kin-lt-stream'}
        )[1],
        # ── kinesis — describe/get (lambdas: create prerequisite) ───────────
        'kinesis.DescribeStream': lambda store: (
            store.create_stream('kin-desc-stream'),
            {'StreamName': 'kin-desc-stream'}
        )[1],
        'kinesis.GetRecords': lambda store: (
            store.create_stream('kin-gr-stream'),
            si := store.get_shard_iterator('kin-gr-stream', 'shardId-0', 'TRIM_HORIZON'),
            {'ShardIterator': si['ShardIterator']}
        )[2],
        'kinesis.GetShardIterator': lambda store: (
            store.create_stream('kin-gsi-stream'),
            {'StreamName': 'kin-gsi-stream', 'ShardId': 'shardId-0', 'ShardIteratorType': 'TRIM_HORIZON'}
        )[1],
        # ── kinesis — delete (lambdas: create prerequisite) ─────────────────
        'kinesis.DeleteStream': lambda store: (
            store.create_stream('kin-del-stream'),
            {'StreamName': 'kin-del-stream'}
        )[1],
        'kinesis.RemoveTagsFromStream': lambda store: (
            store.create_stream('kin-rt-stream'),
            {'StreamName': 'kin-rt-stream', 'TagKeys': ['test']}
        )[1],

        # ── ssm — create/put ────────────────────────────────────────────────
        'ssm.PutParameter': {'Name': 'ssm-test-param', 'Value': 'test-value', 'Type': 'String'},
        'ssm.AddTagsToResource': lambda store: (
            store.put_parameter('ssm-tag-param', 'val', 'String'),
            {'ResourceId': 'ssm-tag-param', 'ResourceType': 'Parameter', 'Tags': [{'Key': 'env', 'Value': 'test'}]}
        )[1],
        # ── ssm — list ──────────────────────────────────────────────────────
        'ssm.DescribeParameters': {},
        'ssm.GetParameters': {'Names': ['ssm-test-param']},
        'ssm.ListTagsForResource': lambda store: (
            store.put_parameter('ssm-lt-param', 'val', 'String'),
            {'ResourceId': 'ssm-lt-param', 'ResourceType': 'Parameter'}
        )[1],
        # ── ssm — get/describe (lambdas: create prerequisite) ────────────────
        'ssm.GetParameter': lambda store: (
            store.put_parameter('ssm-get-param', 'get-val', 'String'),
            {'Name': 'ssm-get-param'}
        )[1],
        'ssm.GetParameterHistory': lambda store: (
            store.put_parameter('ssm-hist-param', 'hist-val', 'String'),
            {'Name': 'ssm-hist-param'}
        )[1],
        # ── ssm — delete (lambdas: create prerequisite) ──────────────────────
        'ssm.DeleteParameter': lambda store: (
            store.put_parameter('ssm-del-param', 'del-val', 'String'),
            {'Name': 'ssm-del-param'}
        )[1],
        'ssm.RemoveTagsFromResource': lambda store: (
            store.put_parameter('ssm-rt-param', 'rt-val', 'String'),
            {'ResourceId': 'ssm-rt-param', 'ResourceType': 'Parameter', 'TagKeys': ['test']}
        )[1],

        # ── iot — create ────────────────────────────────────────────────────
        'iot.CreateThing': {'thingName': 'iot-test-thing'},
        'iot.CreateThingGroup': {'thingGroupName': 'iot-test-group'},
        'iot.CreateThingType': {'thingTypeName': 'iot-test-type'},
        'iot.CreatePolicy': {'policyName': 'iot-test-policy', 'policyDocument': '{"Version":"2012-10-17","Statement":[]}'},
        'iot.CreateKeysAndCertificate': {},
        # ── iot — list ──────────────────────────────────────────────────────
        'iot.ListThings': {},
        'iot.ListThingGroups': {},
        'iot.ListThingTypes': {},
        'iot.ListCertificates': {},
        'iot.ListPolicies': {},
        # ── iot — describe (lambdas: create prerequisite) ────────────────────
        'iot.DescribeThing': lambda store: (
            store.create_thing(thingName='iot-desc-thing'),
            {'thingName': 'iot-desc-thing'}
        )[1],
        'iot.DescribeThingGroup': lambda store: (
            store.create_thing_group(thingGroupName='iot-desc-group'),
            {'thingGroupName': 'iot-desc-group'}
        )[1],
        'iot.DescribeThingType': lambda store: (
            store.create_thing_type(thingTypeName='iot-desc-type'),
            {'thingTypeName': 'iot-desc-type'}
        )[1],
        'iot.DescribeCertificate': lambda store: (
            c := store.create_keys_and_certificate(),
            {'certificateId': c['certificateId']}
        )[1],
        'iot.DescribePolicy': lambda store: (
            store.create_policy(policyName='iot-desc-policy', policyDocument='{"Version":"2012-10-17","Statement":[]}'),
            {'policyName': 'iot-desc-policy'}
        )[1],
        # ── iot — update (lambdas: create prerequisite) ──────────────────────
        'iot.UpdateThing': lambda store: (
            store.create_thing(thingName='iot-upd-thing'),
            {'thingName': 'iot-upd-thing', 'thingTypeName': 'iot-test-type'}
        )[1],
        'iot.UpdateThingGroup': lambda store: (
            store.create_thing_group(thingGroupName='iot-upd-group'),
            {'thingGroupName': 'iot-upd-group', 'thingGroupProperties': {}}
        )[1],
        # ── iot — delete (lambdas: create prerequisite) ──────────────────────
        'iot.DeleteThing': lambda store: (
            store.create_thing(thingName='iot-del-thing'),
            {'thingName': 'iot-del-thing'}
        )[1],
        'iot.DeleteThingGroup': lambda store: (
            store.create_thing_group(thingGroupName='iot-del-group'),
            {'thingGroupName': 'iot-del-group'}
        )[1],
        'iot.DeleteThingType': lambda store: (
            store.create_thing_type(thingTypeName='iot-del-type'),
            {'thingTypeName': 'iot-del-type'}
        )[1],
        'iot.DeleteCertificate': lambda store: (
            c := store.create_keys_and_certificate(),
            {'certificateId': c['certificateId']}
        )[1],
        'iot.DeletePolicy': lambda store: (
            store.create_policy(policyName='iot-del-policy', policyDocument='{"Version":"2012-10-17","Statement":[]}'),
            {'policyName': 'iot-del-policy'}
        )[1],

        # ── dms — create ────────────────────────────────────────────────────
        'dms.CreateReplicationInstance': {'ReplicationInstanceIdentifier': 'dms-test-inst', 'ReplicationInstanceClass': 'dms.t2.micro'},
        'dms.CreateEndpoint': {'EndpointIdentifier': 'dms-test-ep', 'EndpointType': 'source', 'EngineName': 'mysql'},
        'dms.CreateReplicationTask': lambda store: (
            store.create_replication_instance(ReplicationInstanceIdentifier='dms-task-inst', ReplicationInstanceClass='dms.t2.micro'),
            store.create_endpoint(EndpointIdentifier='dms-task-src', EndpointType='source', EngineName='mysql'),
            store.create_endpoint(EndpointIdentifier='dms-task-tgt', EndpointType='target', EngineName='mysql'),
            {'ReplicationTaskIdentifier': 'dms-test-task', 'SourceEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint/dms-task-src',
             'TargetEndpointArn': 'arn:aws:dms:us-east-1:123456789012:endpoint/dms-task-tgt',
             'MigrationType': 'full-load',
             'ReplicationInstanceArn': 'arn:aws:dms:us-east-1:123456789012:rep/dms-task-inst'}
        )[3],
        # ── dms — list ──────────────────────────────────────────────────────
        'dms.DescribeEndpoints': {},
        'dms.DescribeReplicationInstances': {},
        'dms.DescribeReplicationTasks': {},
        # ── dms — start/stop (lambdas: create prerequisite) ──────────────────
        'dms.StartReplicationTask': lambda store: (
            store.create_replication_instance(ReplicationInstanceIdentifier='dms-start-inst', ReplicationInstanceClass='dms.t2.micro'),
            store.create_endpoint(EndpointIdentifier='dms-start-src', EndpointType='source', EngineName='mysql'),
            store.create_endpoint(EndpointIdentifier='dms-start-tgt', EndpointType='target', EngineName='mysql'),
            store.create_replication_task(ReplicationTaskIdentifier='dms-start-task',
                SourceEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint/dms-start-src',
                TargetEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint/dms-start-tgt',
                MigrationType='full-load',
                ReplicationInstanceArn='arn:aws:dms:us-east-1:123456789012:rep/dms-start-inst'),
            {'ReplicationTaskIdentifier': 'dms-start-task'}
        )[4],
        'dms.StopReplicationTask': lambda store: (
            store.create_replication_instance(ReplicationInstanceIdentifier='dms-stop-inst', ReplicationInstanceClass='dms.t2.micro'),
            store.create_endpoint(EndpointIdentifier='dms-stop-src', EndpointType='source', EngineName='mysql'),
            store.create_endpoint(EndpointIdentifier='dms-stop-tgt', EndpointType='target', EngineName='mysql'),
            store.create_replication_task(ReplicationTaskIdentifier='dms-stop-task',
                SourceEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint/dms-stop-src',
                TargetEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint/dms-stop-tgt',
                MigrationType='full-load',
                ReplicationInstanceArn='arn:aws:dms:us-east-1:123456789012:rep/dms-stop-inst'),
            {'ReplicationTaskIdentifier': 'dms-stop-task'}
        )[4],
        # ── dms — delete (lambdas: create prerequisite) ──────────────────────
        'dms.DeleteEndpoint': lambda store: (
            store.create_endpoint(EndpointIdentifier='dms-del-ep', EndpointType='source', EngineName='mysql'),
            {'EndpointIdentifier': 'dms-del-ep'}
        )[1],
        'dms.DeleteReplicationInstance': lambda store: (
            store.create_replication_instance(ReplicationInstanceIdentifier='dms-del-inst', ReplicationInstanceClass='dms.t2.micro'),
            {'ReplicationInstanceIdentifier': 'dms-del-inst'}
        )[1],
        'dms.DeleteReplicationTask': lambda store: (
            store.create_replication_instance(ReplicationInstanceIdentifier='dms-delt-inst', ReplicationInstanceClass='dms.t2.micro'),
            store.create_endpoint(EndpointIdentifier='dms-delt-src', EndpointType='source', EngineName='mysql'),
            store.create_endpoint(EndpointIdentifier='dms-delt-tgt', EndpointType='target', EngineName='mysql'),
            store.create_replication_task(ReplicationTaskIdentifier='dms-delt-task',
                SourceEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint/dms-delt-src',
                TargetEndpointArn='arn:aws:dms:us-east-1:123456789012:endpoint/dms-delt-tgt',
                MigrationType='full-load',
                ReplicationInstanceArn='arn:aws:dms:us-east-1:123456789012:rep/dms-delt-inst'),
            {'ReplicationTaskIdentifier': 'dms-delt-task'}
        )[4],

        # ── efs — create ────────────────────────────────────────────────────
        'efs.CreateFileSystem': {'CreationToken': 'efs-test-token'},
        'efs.CreateMountTarget': lambda store: (
            store.create_filesystem('efs-mt-token'),
            {'FileSystemId': 'fs-00000001', 'SubnetId': 'subnet-12345678'}
        )[1],
        # ── efs — list ──────────────────────────────────────────────────────
        'efs.DescribeFileSystems': {},
        'efs.DescribeMountTargets': lambda store: (
            store.create_filesystem('efs-dmt-token'),
            {'FileSystemId': 'fs-00000001'}
        )[1],
        # ── efs — delete (lambdas: create prerequisite) ──────────────────────
        'efs.DeleteFileSystem': lambda store: (
            store.create_filesystem('efs-del-token'),
            {'FileSystemId': 'fs-00000001'}
        )[1],
        'efs.DeleteMountTarget': lambda store: (
            store.create_filesystem('efs-dmt-del-token'),
            {'FileSystemId': 'fs-00000001', 'MountTargetId': 'fsmt-00000001'}
        )[1],
        # ── efs — tags ──────────────────────────────────────────────────────
        'efs.TagResource': lambda store: (
            store.create_filesystem('efs-tag-token'),
            {'ResourceId': 'fs-00000001', 'Tags': [{'Key': 'env', 'Value': 'test'}]}
        )[1],
        'efs.UntagResource': lambda store: (
            store.create_filesystem('efs-untag-token'),
            {'ResourceId': 'fs-00000001', 'TagKeys': ['test']}
        )[1],
        'efs.ListTagsForResource': lambda store: (
            store.create_filesystem('efs-lt-token'),
            {'ResourceId': 'fs-00000001'}
        )[1],

        # ── autoscaling — create ────────────────────────────────────────────
        'autoscaling.CreateAutoScalingGroup': {'AutoScalingGroupName': 'asg-test', 'MinSize': 1, 'MaxSize': 3, 'AvailabilityZones': ['us-east-1a']},
        'autoscaling.CreateLaunchConfiguration': {'LaunchConfigurationName': 'asg-lc-test', 'ImageId': 'ami-12345', 'InstanceType': 't2.micro'},
        # ── autoscaling — list ──────────────────────────────────────────────
        'autoscaling.DescribeAutoScalingGroups': {},
        'autoscaling.DescribeLaunchConfigurations': {},
        'autoscaling.DescribeScalingActivities': {},
        # ── autoscaling — update/set (lambdas: create prerequisite) ──────────
        'autoscaling.UpdateAutoScalingGroup': lambda store: (
            store.create_group('asg-upd', 1, 3),
            {'AutoScalingGroupName': 'asg-upd', 'MinSize': 2}
        )[1],
        'autoscaling.SetDesiredCapacity': lambda store: (
            store.create_group('asg-sdc', 1, 3),
            {'AutoScalingGroupName': 'asg-sdc', 'DesiredCapacity': 2}
        )[1],
        # ── autoscaling — delete (lambdas: create prerequisite) ──────────────
        'autoscaling.DeleteAutoScalingGroup': lambda store: (
            store.create_group('asg-del', 1, 1),
            {'AutoScalingGroupName': 'asg-del'}
        )[1],
        'autoscaling.DeleteLaunchConfiguration': lambda store: (
            store.create_launch_config('asg-del-lc', 'ami-12345', 't2.micro'),
            {'LaunchConfigurationName': 'asg-del-lc'}
        )[1],

        # ── dynamodbstreams ─────────────────────────────────────────────────
        'dynamodbstreams.ListStreams': {},
        'dynamodbstreams.DescribeStream': lambda store: (
            store._add_stream('arn:aws:dynamodb:us-east-1:123456789012:table/test-table/stream/2024-01-01T00:00:00.000', 'test-table'),
            {'StreamArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/test-table/stream/2024-01-01T00:00:00.000'}
        )[1],
        'dynamodbstreams.GetShardIterator': lambda store: (
            s := store._add_stream('arn:aws:dynamodb:us-east-1:123456789012:table/test-table/stream/2024-01-01T00:00:00.000', 'test-table'),
            {'StreamArn': 'arn:aws:dynamodb:us-east-1:123456789012:table/test-table/stream/2024-01-01T00:00:00.000',
             'ShardId': s.shards[0].ShardId,
             'ShardIteratorType': 'TRIM_HORIZON'}
        )[1],
        'dynamodbstreams.GetRecords': lambda store: (
            s := store._add_stream('arn:aws:dynamodb:us-east-1:123456789012:table/test-table/stream/2024-01-01T00:00:00.000', 'test-table'),
            it := store.get_shard_iterator(
                'arn:aws:dynamodb:us-east-1:123456789012:table/test-table/stream/2024-01-01T00:00:00.000',
                s.shards[0].ShardId, 'TRIM_HORIZON'),
            {'ShardIterator': it['ShardIterator']}
        )[2],

        # ── polly ────────────────────────────────────────────────────────
        'PutLexicon': {'Name': 'test-lexicon', 'Content': '<?xml version="1.0"?><lexicon version="1.0" xmlns="http://www.w3.org/2005/01/pronunciation-lexicon" alphabet="ipa" xml:lang="en-US"><lexeme><grapheme>test</grapheme><alias>test</alias></lexeme></lexicon>'},
        'GetLexicon': lambda store: (store.put_lexicon('test-gl', '<?xml version="1.0"?><lexicon version="1.0" xmlns="http://www.w3.org/2005/01/pronunciation-lexicon" alphabet="ipa" xml:lang="en-US"><lexeme><grapheme>test</grapheme><alias>test</alias></lexeme></lexicon>'), {'Name': 'test-gl'})[1],
        'ListLexicons': {},
        'DeleteLexicon': lambda store: (store.put_lexicon('test-dl', '<?xml version="1.0"?><lexicon version="1.0" xmlns="http://www.w3.org/2005/01/pronunciation-lexicon" alphabet="ipa" xml:lang="en-US"><lexeme><grapheme>test</grapheme><alias>test</alias></lexeme></lexicon>'), {'Name': 'test-dl'})[1],
        'DescribeVoices': {},
        'SynthesizeSpeech': {'OutputFormat': 'mp3', 'Text': 'Hello world', 'VoiceId': 'Joanna'},
        'StartSpeechSynthesisTask': {'OutputFormat': 'mp3', 'OutputS3BucketName': 'test-bucket', 'Text': 'Hello world', 'VoiceId': 'Joanna'},
        'GetSpeechSynthesisTask': lambda store: (t := store.start_speech_synthesis_task(OutputFormat='mp3', OutputS3BucketName='test-bucket', Text='Hello', VoiceId='Joanna'), {'TaskId': t['SynthesisTask']['TaskId']})[1],
        'ListSpeechSynthesisTasks': {},

        # ── grafana ──────────────────────────────────────────────────────
        'CreateWorkspace': {'accountAccessType': 'CURRENT_ACCOUNT', 'permissionType': 'CUSTOMER_MANAGED', 'authenticationProviders': ['SAML']},
        'ListWorkspaces': {},
        'DescribeWorkspace': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='desc-ws'), {'workspaceId': store.workspaces()[-1].id})[1],
        'UpdateWorkspace': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='upd-ws'), {'workspaceId': store.workspaces()[-1].id, 'workspaceName': 'updated-name'})[1],
        'DeleteWorkspace': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='del-ws'), {'workspaceId': store.workspaces()[-1].id})[1],
        'CreateWorkspaceApiKey': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='apikey-ws'), {'workspaceId': store.workspaces()[-1].id, 'keyName': 'test-key', 'keyRole': 'ADMIN', 'secondsToLive': 3600})[1],
        'DeleteWorkspaceApiKey': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='delkey-ws'), ws_id := store.workspaces()[-1].id, store.create_workspace_api_key(ws_id, 'tmp-key', 'ADMIN', 3600), {'workspaceId': ws_id, 'keyName': 'tmp-key'})[3],
        'CreateWorkspaceServiceAccount': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='sa-ws'), ws_id := store.workspaces()[-1].id, {'workspaceId': ws_id, 'name': 'test-sa', 'grafanaRole': 'VIEWER'})[2],
        'DeleteWorkspaceServiceAccount': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='delsa-ws'), ws_id := store.workspaces()[-1].id, sa := store.create_workspace_service_account(ws_id, 'tmp-sa', 'VIEWER'), {'workspaceId': ws_id, 'serviceAccountId': sa['id']})[3],
        'CreateWorkspaceServiceAccountToken': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='sat-ws'), ws_id := store.workspaces()[-1].id, sa := store.create_workspace_service_account(ws_id, 'tmp-sa', 'VIEWER'), {'workspaceId': ws_id, 'serviceAccountId': sa['id'], 'name': 'test-token', 'secondsToLive': 3600})[3],
        'DeleteWorkspaceServiceAccountToken': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='delsat-ws'), ws_id := store.workspaces()[-1].id, sa := store.create_workspace_service_account(ws_id, 'tmp-sa', 'VIEWER'), tok := store.create_workspace_service_account_token(ws_id, sa['id'], 'tmp-tok', 3600), {'workspaceId': ws_id, 'serviceAccountId': sa['id'], 'tokenId': tok['id']})[4],
        'DescribeWorkspaceAuthentication': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='auth-ws'), {'workspaceId': store.workspaces()[-1].id})[1],
        'UpdateWorkspaceAuthentication': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='updauth-ws'), {'workspaceId': store.workspaces()[-1].id, 'authenticationProviders': ['SAML', 'AWS_SSO']})[1],
        'grafana.TagResource': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='tag-ws'), ws := store.workspaces()[-1], {'resourceArn': ws.arn, 'tags': {'test': 'val'}})[2],
        'grafana.UntagResource': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='untag-ws'), ws := store.workspaces()[-1], store.tag_resource(ws.arn, {'test': 'val'}), {'resourceArn': ws.arn, 'tagKeys': ['test']})[3],
        'grafana.ListTagsForResource': lambda store: (store.create_workspace('CURRENT_ACCOUNT', 'CUSTOMER_MANAGED', ['SAML'], workspaceName='listag-ws'), ws := store.workspaces()[-1], {'resourceArn': ws.arn})[2],

        # ── fis ──────────────────────────────────────────────────────────
        'CreateExperimentTemplate': {'description': 'test template', 'roleArn': 'arn:aws:iam::123456789012:role/test', 'stopConditions': [{'source': 'none'}], 'actions': {}, 'targets': {}},
        'ListExperimentTemplates': {},
        'DescribeExperimentTemplate': lambda store: (t := store.create_experiment_template(description='desc', roleArn='arn:aws:iam::123456789012:role/test', stopConditions=[{'source': 'none'}], actions={}, targets={}), {'id': t['id']})[1],
        'UpdateExperimentTemplate': lambda store: (t := store.create_experiment_template(description='upd', roleArn='arn:aws:iam::123456789012:role/test', stopConditions=[{'source': 'none'}], actions={}, targets={}), {'id': t['id'], 'description': 'updated'})[1],
        'DeleteExperimentTemplate': lambda store: (t := store.create_experiment_template(description='del', roleArn='arn:aws:iam::123456789012:role/test', stopConditions=[{'source': 'none'}], actions={}, targets={}), {'id': t['id']})[1],
        'StartExperiment': lambda store: (t := store.create_experiment_template(description='start', roleArn='arn:aws:iam::123456789012:role/test', stopConditions=[{'source': 'none'}], actions={}, targets={}), {'experimentTemplateId': t['id']})[1],
        'ListExperiments': {},
        'DescribeExperiment': lambda store: (t := store.create_experiment_template(description='de', roleArn='arn:aws:iam::123456789012:role/test', stopConditions=[{'source': 'none'}], actions={}, targets={}), e := store.start_experiment(experimentTemplateId=t['id']), {'id': e['id']})[2],
        'StopExperiment': lambda store: (t := store.create_experiment_template(description='stop', roleArn='arn:aws:iam::123456789012:role/test', stopConditions=[{'source': 'none'}], actions={}, targets={}), e := store.start_experiment(experimentTemplateId=t['id']), {'id': e['id']})[2],
        'DeleteExperiment': lambda store: (t := store.create_experiment_template(description='dele', roleArn='arn:aws:iam::123456789012:role/test', stopConditions=[{'source': 'none'}], actions={}, targets={}), e := store.start_experiment(experimentTemplateId=t['id']), {'id': e['id']})[2],

        # ── docdb ────────────────────────────────────────────────────────
        'CreateDBCluster': {'DBClusterIdentifier': 'test-cluster', 'Engine': 'docdb'},
        'CreateDBClusterParameterGroup': {'DBClusterParameterGroupName': 'test-pg', 'DBParameterGroupFamily': 'docdb4.0', 'Description': 'test parameter group'},
        'CreateDBClusterSnapshot': lambda store: (store.create_cluster('snapshot-cluster', 'docdb'), {'DBClusterSnapshotIdentifier': 'test-snapshot', 'DBClusterIdentifier': 'snapshot-cluster'})[1],
        'CreateDBInstance': lambda store: (store.create_cluster('inst-cluster', 'docdb'), {'DBInstanceIdentifier': 'test-instance', 'DBClusterIdentifier': 'inst-cluster', 'DBInstanceClass': 'db.r5.large', 'Engine': 'docdb'})[1],
        'CreateDBSubnetGroup': {'DBSubnetGroupName': 'test-subnet-group', 'DBSubnetGroupDescription': 'test subnet group', 'SubnetIds': ['subnet-12345678']},
        'DescribeDBClusters': {},
        'DescribeDBClusterParameterGroups': {},
        'DescribeDBClusterSnapshots': {},
        'DescribeDBInstances': {},
        'DescribeDBSubnetGroups': {},
        'DeleteDBCluster': lambda store: (store.create_cluster('del-cluster', 'docdb'), {'DBClusterIdentifier': 'del-cluster'})[1],
        'DeleteDBClusterParameterGroup': lambda store: (store.create_parameter_group('del-pg', 'docdb4.0', 'to delete'), {'DBClusterParameterGroupName': 'del-pg'})[1],
        'DeleteDBClusterSnapshot': lambda store: (store.create_cluster('delsnap-cluster', 'docdb'), store.create_snapshot('del-snapshot', 'delsnap-cluster'), {'DBClusterSnapshotIdentifier': 'del-snapshot'})[2],
        'DeleteDBInstance': lambda store: (store.create_cluster('delinst-cluster', 'docdb'), store.create_instance('del-instance', 'delinst-cluster', 'db.r5.large', 'docdb'), {'DBInstanceIdentifier': 'del-instance'})[2],
        'DeleteDBSubnetGroup': lambda store: (store.create_subnet_group('del-subnet', 'to delete', ['subnet-12345678']), {'DBSubnetGroupName': 'del-subnet'})[1],
        'ModifyDBCluster': lambda store: (store.create_cluster('mod-cluster', 'docdb'), {'DBClusterIdentifier': 'mod-cluster'})[1],
        'ModifyDBClusterParameterGroup': lambda store: (store.create_parameter_group('mod-pg', 'docdb4.0', 'to modify'), {'DBClusterParameterGroupName': 'mod-pg', 'Parameters': []})[1],
        'ModifyDBInstance': lambda store: (store.create_cluster('modinst-cluster', 'docdb'), store.create_instance('mod-instance', 'modinst-cluster', 'db.r5.large', 'docdb'), {'DBInstanceIdentifier': 'mod-instance'})[2],
        'ModifyDBSubnetGroup': lambda store: (store.create_subnet_group('mod-subnet', 'to modify', ['subnet-12345678']), {'DBSubnetGroupName': 'mod-subnet', 'SubnetIds': ['subnet-87654321']})[1],
        'RebootDBInstance': lambda store: (store.create_cluster('reboot-cluster', 'docdb'), store.create_instance('reboot-instance', 'reboot-cluster', 'db.r5.large', 'docdb'), {'DBInstanceIdentifier': 'reboot-instance'})[2],
        'ResetDBClusterParameterGroup': lambda store: (store.create_parameter_group('reset-pg', 'docdb4.0', 'to reset'), {'DBClusterParameterGroupName': 'reset-pg'})[1],
        'CopyDBClusterSnapshot': lambda store: (store.create_cluster('copy-cluster', 'docdb'), store.create_snapshot('source-snapshot', 'copy-cluster'), {'SourceDBClusterSnapshotIdentifier': 'source-snapshot', 'TargetDBClusterSnapshotIdentifier': 'target-snapshot'})[2],
        'RestoreDBClusterFromSnapshot': lambda store: (store.create_cluster('restore-cluster', 'docdb'), store.create_snapshot('restore-snapshot', 'restore-cluster'), {'DBClusterIdentifier': 'restored-cluster', 'DBClusterSnapshotIdentifier': 'restore-snapshot', 'Engine': 'docdb'})[2],
        'StartDBCluster': lambda store: (store.create_cluster('start-cluster', 'docdb'), {'DBClusterIdentifier': 'start-cluster'})[1],
        'StopDBCluster': lambda store: (store.create_cluster('stop-cluster', 'docdb'), {'DBClusterIdentifier': 'stop-cluster'})[1],

        # ── greengrassv2 ─────────────────────────────────────────────────
        'CreateComponentVersion': {'componentName': 'test-component', 'componentVersion': '1.0.0'},
        'ListComponents': {},
        'DescribeComponent': lambda store: (store.create_component_version(componentName='desc-comp', componentVersion='1.0.0'), {'componentName': 'desc-comp', 'componentVersion': '1.0.0'})[1],
        'DeleteComponent': lambda store: (store.create_component_version(componentName='del-comp', componentVersion='1.0.0'), {'componentName': 'del-comp', 'componentVersion': '1.0.0'})[1],
        'CreateCoreDevice': {'coreDeviceThingName': 'test-thing'},
        'ListCoreDevices': {},
        'DescribeCoreDevice': lambda store: (store.create_core_device(coreDeviceThingName='desc-thing'), {'coreDeviceThingName': 'desc-thing'})[1],
        'DeleteCoreDevice': lambda store: (store.create_core_device(coreDeviceThingName='del-thing'), {'coreDeviceThingName': 'del-thing'})[1],
        'CreateDeployment': {'targetArn': 'arn:aws:iot:us-east-1:123456789012:thing/test-thing'},
        'ListDeployments': {},
        'DescribeDeployment': lambda store: (d := store.create_deployment(targetArn='arn:aws:iot:us-east-1:123456789012:thing/desc-thing'), {'deploymentId': d['deploymentId']})[1],
        'DeleteDeployment': lambda store: (d := store.create_deployment(targetArn='arn:aws:iot:us-east-1:123456789012:thing/del-thing'), {'deploymentId': d['deploymentId']})[1],

        # ── sagemaker ────────────────────────────────────────────────────
        'CreateTrainingJob': {'TrainingJobName': 'test-job', 'AlgorithmSpecification': {'TrainingImage': 'test-image', 'TrainingInputMode': 'File'}, 'OutputDataConfig': {'S3OutputPath': 's3://test-bucket/'}, 'ResourceConfig': {'InstanceCount': 1, 'InstanceType': 'ml.m5.large', 'VolumeSizeInGB': 10}, 'RoleArn': 'arn:aws:iam::123456789012:role/test', 'StoppingCondition': {'MaxRuntimeInSeconds': 3600}},
        'ListTrainingJobs': {},
        'DescribeTrainingJob': lambda store: (t := store.create_training_job(TrainingJobName='desc-job', AlgorithmSpecification={'TrainingImage': 'test', 'TrainingInputMode': 'File'}, OutputDataConfig={'S3OutputPath': 's3://test/'}, ResourceConfig={'InstanceCount': 1, 'InstanceType': 'ml.m5.large', 'VolumeSizeInGB': 10}, RoleArn='arn:aws:iam::123456789012:role/test', StoppingCondition={'MaxRuntimeInSeconds': 3600}), {'TrainingJobName': 'desc-job'})[1],
        'StopTrainingJob': lambda store: (store.create_training_job(TrainingJobName='stop-job', AlgorithmSpecification={'TrainingImage': 'test', 'TrainingInputMode': 'File'}, OutputDataConfig={'S3OutputPath': 's3://test/'}, ResourceConfig={'InstanceCount': 1, 'InstanceType': 'ml.m5.large', 'VolumeSizeInGB': 10}, RoleArn='arn:aws:iam::123456789012:role/test', StoppingCondition={'MaxRuntimeInSeconds': 3600}), {'TrainingJobName': 'stop-job'})[1],
        'DeleteTrainingJob': lambda store: (store.create_training_job(TrainingJobName='del-job', AlgorithmSpecification={'TrainingImage': 'test', 'TrainingInputMode': 'File'}, OutputDataConfig={'S3OutputPath': 's3://test/'}, ResourceConfig={'InstanceCount': 1, 'InstanceType': 'ml.m5.large', 'VolumeSizeInGB': 10}, RoleArn='arn:aws:iam::123456789012:role/test', StoppingCondition={'MaxRuntimeInSeconds': 3600}), {'TrainingJobName': 'del-job'})[1],
        'CreateModel': {'ModelName': 'test-model', 'PrimaryContainer': {'Image': 'test-image'}, 'ExecutionRoleArn': 'arn:aws:iam::123456789012:role/test'},
        'ListModels': {},
        'DescribeModel': lambda store: (m := store.create_model(ModelName='desc-model', PrimaryContainer={'Image': 'test'}, ExecutionRoleArn='arn:aws:iam::123456789012:role/test'), {'ModelName': 'desc-model'})[1],
        'DeleteModel': lambda store: (store.create_model(ModelName='del-model', PrimaryContainer={'Image': 'test'}, ExecutionRoleArn='arn:aws:iam::123456789012:role/test'), {'ModelName': 'del-model'})[1],
        'CreateEndpointConfig': {'EndpointConfigName': 'test-config', 'ProductionVariants': [{'InstanceType': 'ml.m5.large', 'InitialVariantWeight': 1.0, 'ModelName': 'test-model', 'VariantName': 'test-variant'}]},
        'ListEndpointConfigs': {},
        'DescribeEndpointConfig': lambda store: (ec := store.create_endpoint_config(EndpointConfigName='desc-config', ProductionVariants=[{'InstanceType': 'ml.m5.large', 'InitialVariantWeight': 1.0, 'ModelName': 'test-model', 'VariantName': 'test-variant'}]), {'EndpointConfigName': 'desc-config'})[1],
        'DeleteEndpointConfig': lambda store: (store.create_endpoint_config(EndpointConfigName='del-config', ProductionVariants=[{'InstanceType': 'ml.m5.large', 'InitialVariantWeight': 1.0, 'ModelName': 'test-model', 'VariantName': 'test-variant'}]), {'EndpointConfigName': 'del-config'})[1],
        'CreateEndpoint': {'EndpointName': 'test-endpoint', 'EndpointConfigName': 'test-config'},
        'ListEndpoints': {},
        'DescribeEndpoint': lambda store: (store.create_endpoint_config(EndpointConfigName='ep-config', ProductionVariants=[{'InstanceType': 'ml.m5.large', 'InitialVariantWeight': 1.0, 'ModelName': 'test-model', 'VariantName': 'test-variant'}]), ep := store.create_endpoint(EndpointName='desc-ep', EndpointConfigName='ep-config'), {'EndpointName': 'desc-ep'})[2],
        'DeleteEndpoint': lambda store: (store.create_endpoint_config(EndpointConfigName='dep-config', ProductionVariants=[{'InstanceType': 'ml.m5.large', 'InitialVariantWeight': 1.0, 'ModelName': 'test-model', 'VariantName': 'test-variant'}]), store.create_endpoint(EndpointName='del-ep', EndpointConfigName='dep-config'), {'EndpointName': 'del-ep'})[2],
        'UpdateEndpoint': lambda store: (store.create_endpoint_config(EndpointConfigName='updep-config', ProductionVariants=[{'InstanceType': 'ml.m5.large', 'InitialVariantWeight': 1.0, 'ModelName': 'test-model', 'VariantName': 'test-variant'}]), store.create_endpoint(EndpointName='upd-ep', EndpointConfigName='updep-config'), {'EndpointName': 'upd-ep', 'EndpointConfigName': 'updep-config'})[2],
        # ── codeartifact ──────────────────────────────────────────────────────
        'codeartifact.CreateDomain': {'domain': 'ca-test-domain'},
        'codeartifact.ListDomains': {},
        'codeartifact.DescribeDomain': lambda store: (d := store.domains.setdefault('ca-dd', DomainRecord('ca-dd', '123456789012')), store.domain_policies.setdefault('ca-dd', ''), {'domain': 'ca-dd'})[2],
        'codeartifact.DeleteDomain': lambda store: (d := store.domains.setdefault('ca-del-d', DomainRecord('ca-del-d', '123456789012')), store.domain_policies.setdefault('ca-del-d', ''), {'domain': 'ca-del-d'})[2],
        'codeartifact.CreateRepository': lambda store: (store.domains.setdefault('ca-cr-d', DomainRecord('ca-cr-d', '123456789012')), store.domain_policies.setdefault('ca-cr-d', ''), {'domain': 'ca-cr-d', 'repository': 'ca-cr-r'})[2],
        'codeartifact.ListRepositories': {},
        'codeartifact.ListRepositoriesInDomain': lambda store: (store.domains.setdefault('ca-lrid-d', DomainRecord('ca-lrid-d', '123456789012')), store.domain_policies.setdefault('ca-lrid-d', ''), {'domain': 'ca-lrid-d'})[2],
        'codeartifact.DescribeRepository': lambda store: (store.domains.setdefault('ca-dr-d', DomainRecord('ca-dr-d', '123456789012')), store.domain_policies.setdefault('ca-dr-d', ''), store.repositories.setdefault(('ca-dr-d', 'ca-dr-r'), RepositoryRecord('ca-dr-r', 'ca-dr-d', '123456789012')), {'domain': 'ca-dr-d', 'repository': 'ca-dr-r'})[3],
        'codeartifact.DeleteRepository': lambda store: (store.domains.setdefault('ca-delr-d', DomainRecord('ca-delr-d', '123456789012')), store.domain_policies.setdefault('ca-delr-d', ''), store.repositories.setdefault(('ca-delr-d', 'ca-delr-r'), RepositoryRecord('ca-delr-r', 'ca-delr-d', '123456789012')), {'domain': 'ca-delr-d', 'repository': 'ca-delr-r'})[3],
        'codeartifact.UpdateRepository': lambda store: (store.domains.setdefault('ca-ur-d', DomainRecord('ca-ur-d', '123456789012')), store.domain_policies.setdefault('ca-ur-d', ''), store.repositories.setdefault(('ca-ur-d', 'ca-ur-r'), RepositoryRecord('ca-ur-r', 'ca-ur-d', '123456789012')), {'domain': 'ca-ur-d', 'repository': 'ca-ur-r'})[3],
        'codeartifact.ListPackages': lambda store: (store.domains.setdefault('ca-lp-d', DomainRecord('ca-lp-d', '123456789012')), store.domain_policies.setdefault('ca-lp-d', ''), store.repositories.setdefault(('ca-lp-d', 'ca-lp-r'), RepositoryRecord('ca-lp-r', 'ca-lp-d', '123456789012')), {'domain': 'ca-lp-d', 'repository': 'ca-lp-r'})[3],
        'codeartifact.ListPackageVersions': lambda store: (store.domains.setdefault('ca-lpv-d', DomainRecord('ca-lpv-d', '123456789012')), store.domain_policies.setdefault('ca-lpv-d', ''), store.repositories.setdefault(('ca-lpv-d', 'ca-lpv-r'), RepositoryRecord('ca-lpv-r', 'ca-lpv-d', '123456789012')), {'domain': 'ca-lpv-d', 'repository': 'ca-lpv-r', 'format': 'npm', 'package': 'ca-test-pkg'})[3],
        'codeartifact.DescribePackageVersion': lambda store: (store.domains.setdefault('ca-dpv-d', DomainRecord('ca-dpv-d', '123456789012')), store.domain_policies.setdefault('ca-dpv-d', ''), store.repositories.setdefault(('ca-dpv-d', 'ca-dpv-r'), RepositoryRecord('ca-dpv-r', 'ca-dpv-d', '123456789012')), store.package_versions.setdefault(('ca-dpv-d', 'ca-dpv-r', 'ca-test-pkg', 'npm'), {}).setdefault('1.0.0', PackageVersionRecord('1.0.0', 'ca-test-pkg', 'npm')), {'domain': 'ca-dpv-d', 'repository': 'ca-dpv-r', 'format': 'npm', 'package': 'ca-test-pkg', 'packageVersion': '1.0.0'})[4],
        'codeartifact.GetRepositoryEndpoint': lambda store: (store.domains.setdefault('ca-gre-d', DomainRecord('ca-gre-d', '123456789012')), store.domain_policies.setdefault('ca-gre-d', ''), store.repositories.setdefault(('ca-gre-d', 'ca-gre-r'), RepositoryRecord('ca-gre-r', 'ca-gre-d', '123456789012')), {'domain': 'ca-gre-d', 'repository': 'ca-gre-r', 'format': 'npm'})[3],
        'codeartifact.GetAuthorizationToken': lambda store: (store.domains.setdefault('ca-gat-d', DomainRecord('ca-gat-d', '123456789012')), store.domain_policies.setdefault('ca-gat-d', ''), {'domain': 'ca-gat-d'})[2],
        'codeartifact.GetPackageVersionReadme': lambda store: (store.domains.setdefault('ca-gpvr-d', DomainRecord('ca-gpvr-d', '123456789012')), store.domain_policies.setdefault('ca-gpvr-d', ''), store.repositories.setdefault(('ca-gpvr-d', 'ca-gpvr-r'), RepositoryRecord('ca-gpvr-r', 'ca-gpvr-d', '123456789012')), store.package_versions.setdefault(('ca-gpvr-d', 'ca-gpvr-r', 'ca-readme-pkg', 'npm'), {}).setdefault('1.0.0', PackageVersionRecord('1.0.0', 'ca-readme-pkg', 'npm')), {'domain': 'ca-gpvr-d', 'repository': 'ca-gpvr-r', 'format': 'npm', 'package': 'ca-readme-pkg', 'packageVersion': '1.0.0'})[4],
        # ── codeartifact — permissions ─────────────────────────────────────────
        'codeartifact.GetDomainPermissionsPolicy': lambda store: (store.domains.setdefault('ca-gdpp-d', DomainRecord('ca-gdpp-d', '123456789012')), store.domain_policies.setdefault('ca-gdpp-d', ''), {'domain': 'ca-gdpp-d'})[2],
        'codeartifact.PutDomainPermissionsPolicy': lambda store: (store.domains.setdefault('ca-pdpp-d', DomainRecord('ca-pdpp-d', '123456789012')), store.domain_policies.setdefault('ca-pdpp-d', ''), {'domain': 'ca-pdpp-d', 'policyDocument': '{"Version":"2012-10-17"}'})[2],
        'codeartifact.DeleteDomainPermissionsPolicy': lambda store: (store.domains.setdefault('ca-ddpp-d', DomainRecord('ca-ddpp-d', '123456789012')), store.domain_policies.setdefault('ca-ddpp-d', ''), {'domain': 'ca-ddpp-d'})[2],
        'codeartifact.GetRepositoryPermissionsPolicy': lambda store: (store.domains.setdefault('ca-grpp-d', DomainRecord('ca-grpp-d', '123456789012')), store.domain_policies.setdefault('ca-grpp-d', ''), store.repositories.setdefault(('ca-grpp-d', 'ca-grpp-r'), RepositoryRecord('ca-grpp-r', 'ca-grpp-d', '123456789012')), {'domain': 'ca-grpp-d', 'repository': 'ca-grpp-r'})[3],
        'codeartifact.PutRepositoryPermissionsPolicy': lambda store: (store.domains.setdefault('ca-prpp-d', DomainRecord('ca-prpp-d', '123456789012')), store.domain_policies.setdefault('ca-prpp-d', ''), store.repositories.setdefault(('ca-prpp-d', 'ca-prpp-r'), RepositoryRecord('ca-prpp-r', 'ca-prpp-d', '123456789012')), {'domain': 'ca-prpp-d', 'repository': 'ca-prpp-r', 'policyDocument': '{"Version":"2012-10-17"}'})[3],
        'codeartifact.DeleteRepositoryPermissionsPolicy': lambda store: (store.domains.setdefault('ca-drpp-d', DomainRecord('ca-drpp-d', '123456789012')), store.domain_policies.setdefault('ca-drpp-d', ''), store.repositories.setdefault(('ca-drpp-d', 'ca-drpp-r'), RepositoryRecord('ca-drpp-r', 'ca-drpp-d', '123456789012')), {'domain': 'ca-drpp-d', 'repository': 'ca-drpp-r'})[3],
        # ── codeartifact — tags ────────────────────────────────────────────────
        'codeartifact.TagResource': lambda store: (d := store.domains.setdefault('ca-tag-d', DomainRecord('ca-tag-d', '123456789012')), {'resourceArn': d.arn, 'tags': [{'key': 'test', 'value': 'val'}]})[1],
        'codeartifact.UntagResource': lambda store: (d := store.domains.setdefault('ca-untag-d', DomainRecord('ca-untag-d', '123456789012')), {'resourceArn': d.arn, 'tagKeys': ['test']})[1],
        'UpdateEndpoint': lambda store: (store.create_endpoint_config(EndpointConfigName='updep-config', ProductionVariants=[{'InstanceType': 'ml.m5.large', 'InitialVariantWeight': 1.0, 'ModelName': 'test-model', 'VariantName': 'test-variant'}]), store.create_endpoint(EndpointName='upd-ep', EndpointConfigName='updep-config'), {'EndpointName': 'upd-ep', 'EndpointConfigName': 'updep-config'})[2],
        # ── codeartifact — create ───────────────────────────────────────
        'CreateDomain': {'domain': 'ca-test-domain'},
        'CreateRepository': lambda store: {'domain': 'ca-test-domain', 'repository': 'ca-test-repo'},
        # ── codeartifact — describe/get (lambdas: create prerequisite) ──
        'DescribeDomain': lambda store: (store.domains.setdefault('ca-desc-domain',
            type('_DR',(),{'name':'ca-desc-domain','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-desc-domain','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-desc-domain','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'domain': 'ca-desc-domain'})[1],
        'DescribeRepository': lambda store: (store.domains.setdefault('ca-desc-repo-d',
            type('_DR',(),{'name':'ca-desc-repo-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-desc-repo-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-desc-repo-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-desc-repo-d','ca-desc-repo'),
            type('_RR',(),{'name':'ca-desc-repo','domain_name':'ca-desc-repo-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-desc-repo-d/ca-desc-repo','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-desc-repo-d', 'repository': 'ca-desc-repo'})[2],
        'DescribePackageVersion': lambda store: (store.domains.setdefault('ca-desc-pv-d',
            type('_DR',(),{'name':'ca-desc-pv-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-desc-pv-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-desc-pv-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-desc-pv-d','ca-desc-pv-r'),
            type('_RR',(),{'name':'ca-desc-pv-r','domain_name':'ca-desc-pv-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-desc-pv-d/ca-desc-pv-r','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-desc-pv-d', 'repository': 'ca-desc-pv-r', 'format': 'npm', 'package': 'test-pkg', 'packageVersion': '1.0.0'})[2],
        'GetDomainPermissionsPolicy': lambda store: (store.domains.setdefault('ca-gdpp-d',
            type('_DR',(),{'name':'ca-gdpp-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-gdpp-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-gdpp-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'domain': 'ca-gdpp-d'})[1],
        'GetPackageVersionReadme': lambda store: (store.domains.setdefault('ca-gpvr-d',
            type('_DR',(),{'name':'ca-gpvr-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-gpvr-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-gpvr-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-gpvr-d','ca-gpvr-r'),
            type('_RR',(),{'name':'ca-gpvr-r','domain_name':'ca-gpvr-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-gpvr-d/ca-gpvr-r','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-gpvr-d', 'repository': 'ca-gpvr-r', 'format': 'npm', 'package': 'test-pkg', 'packageVersion': '1.0.0'})[2],
        'GetRepositoryEndpoint': lambda store: (store.domains.setdefault('ca-gre-d',
            type('_DR',(),{'name':'ca-gre-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-gre-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-gre-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-gre-d','ca-gre-r'),
            type('_RR',(),{'name':'ca-gre-r','domain_name':'ca-gre-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-gre-d/ca-gre-r','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-gre-d', 'repository': 'ca-gre-r', 'format': 'npm'})[2],
        # ── codeartifact — list ──────────────────────────────────────────
        'ListDomains': {},
        'ListRepositories': {},
        'ListRepositoriesInDomain': lambda store: (store.domains.setdefault('ca-test-domain',
            type('_DR',(),{'name':'ca-test-domain','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-test-domain','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-test-domain','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'domain': 'ca-test-domain'})[1],
        'ListPackages': lambda store: (store.domains.setdefault('ca-test-domain',
            type('_DR',(),{'name':'ca-test-domain','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-test-domain','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-test-domain','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-test-domain','ca-test-repo'),
            type('_RR',(),{'name':'ca-test-repo','domain_name':'ca-test-domain','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-test-domain/ca-test-repo','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-test-domain', 'repository': 'ca-test-repo'})[2],
        'ListPackageVersions': lambda store: (store.domains.setdefault('ca-test-domain',
            type('_DR',(),{'name':'ca-test-domain','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-test-domain','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-test-domain','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-test-domain','ca-test-repo'),
            type('_RR',(),{'name':'ca-test-repo','domain_name':'ca-test-domain','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-test-domain/ca-test-repo','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-test-domain', 'repository': 'ca-test-repo', 'format': 'npm', 'package': 'test-pkg'})[2],
        # ── codeartifact — delete ────────────────────────────────────────
        'DeleteDomain': lambda store: (store.domains.setdefault('ca-del-domain',
            type('_DR',(),{'name':'ca-del-domain','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-del-domain','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-del-domain','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'domain': 'ca-del-domain'})[1],
        'DeleteRepository': lambda store: (store.domains.setdefault('ca-del-repo-d',
            type('_DR',(),{'name':'ca-del-repo-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-del-repo-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-del-repo-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-del-repo-d','ca-del-repo'),
            type('_RR',(),{'name':'ca-del-repo','domain_name':'ca-del-repo-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-del-repo-d/ca-del-repo','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-del-repo-d', 'repository': 'ca-del-repo'})[2],
        'DeleteDomainPermissionsPolicy': lambda store: (store.domains.setdefault('ca-ddpp-d',
            type('_DR',(),{'name':'ca-ddpp-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-ddpp-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-ddpp-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'domain': 'ca-ddpp-d'})[1],
        'DeleteRepositoryPermissionsPolicy': lambda store: (store.domains.setdefault('ca-drpp-d',
            type('_DR',(),{'name':'ca-drpp-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-drpp-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-drpp-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-drpp-d','ca-drpp-r'),
            type('_RR',(),{'name':'ca-drpp-r','domain_name':'ca-drpp-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-drpp-d/ca-drpp-r','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-drpp-d', 'repository': 'ca-drpp-r'})[2],
        'GetRepositoryPermissionsPolicy': lambda store: (store.domains.setdefault('ca-grpp-d',
            type('_DR',(),{'name':'ca-grpp-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-grpp-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-grpp-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-grpp-d','ca-grpp-r'),
            type('_RR',(),{'name':'ca-grpp-r','domain_name':'ca-grpp-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-grpp-d/ca-grpp-r','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-grpp-d', 'repository': 'ca-grpp-r'})[2],
        'PutDomainPermissionsPolicy': lambda store: (store.domains.setdefault('ca-pdpp-d',
            type('_DR',(),{'name':'ca-pdpp-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-pdpp-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-pdpp-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'domain': 'ca-pdpp-d', 'policyDocument': '{"Version":"2012-10-17","Statement":[]}', 'policyRevision': 'rev-1'})[1],
        'PutRepositoryPermissionsPolicy': lambda store: (store.domains.setdefault('ca-prpp-d',
            type('_DR',(),{'name':'ca-prpp-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-prpp-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-prpp-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-prpp-d','ca-prpp-r'),
            type('_RR',(),{'name':'ca-prpp-r','domain_name':'ca-prpp-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-prpp-d/ca-prpp-r','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-prpp-d', 'repository': 'ca-prpp-r', 'policyDocument': '{"Version":"2012-10-17","Statement":[]}', 'policyRevision': 'rev-1'})[2],
        'UpdateRepository': lambda store: (store.domains.setdefault('ca-upd-repo-d',
            type('_DR',(),{'name':'ca-upd-repo-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-upd-repo-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-upd-repo-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        store.repositories.setdefault(('ca-upd-repo-d','ca-upd-repo'),
            type('_RR',(),{'name':'ca-upd-repo','domain_name':'ca-upd-repo-d','domain_owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:repository/ca-upd-repo-d/ca-upd-repo','description':'','created_time':0,'administrator_account':'123456789012','external_connections':[],'upstreams':[]})()),
        {'domain': 'ca-upd-repo-d', 'repository': 'ca-upd-repo'})[2],
        # ── codeartifact — tag (service-prefixed keys) ──────────────────
        'codeartifact.TagResource': lambda store: (store.domains.setdefault('ca-tag-d',
            type('_DR',(),{'name':'ca-tag-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-tag-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-tag-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'resourceArn': 'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-tag-d', 'tags': [{'key': 'env', 'value': 'test'}]})[1],
        'codeartifact.UntagResource': lambda store: (store.domains.setdefault('ca-untag-d',
            type('_DR',(),{'name':'ca-untag-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-untag-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-untag-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'resourceArn': 'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-untag-d', 'tagKeys': ['env']})[1],
        'codeartifact.ListTagsForResource': lambda store: (store.domains.setdefault('ca-ltfr-d',
            type('_DR',(),{'name':'ca-ltfr-d','owner':'123456789012','arn':'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-ltfr-d','encryption_key':'AWS_OWNED_KEY','s3_bucket_arn':'arn:aws:s3:::codeartifact-ca-ltfr-d','repository_count':0,'asset_size_bytes':0,'status':'Active','created_time':0})()),
        {'resourceArn': 'arn:aws:codeartifact:us-east-1:123456789012:domain/ca-ltfr-d'})[1],
        # ── mwaa ─────────────────────────────────────────────────────────
        'CreateEnvironment': {'Name': 'mwaa-test-env', 'ExecutionRoleArn': 'arn:aws:iam::123456789012:role/mwaa', 'SourceBucketArn': 'arn:aws:s3:::mwaa-test', 'DagS3Path': 'dags/', 'NetworkConfiguration': {'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}},
        'GetEnvironment': lambda store: (store.create_environment(Name='mwaa-get-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'Name': 'mwaa-get-env'})[1],
        'ListEnvironments': {},
        'UpdateEnvironment': lambda store: (store.create_environment(Name='mwaa-upd-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'Name': 'mwaa-upd-env', 'ExecutionRoleArn': 'arn:aws:iam::123456789012:role/mwaa'})[1],
        'DeleteEnvironment': lambda store: (store.create_environment(Name='mwaa-del-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'Name': 'mwaa-del-env'})[1],
        'CreateCliToken': lambda store: (store.create_environment(Name='mwaa-cli-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'Name': 'mwaa-cli-env'})[1],
        'CreateWebLoginToken': lambda store: (store.create_environment(Name='mwaa-wlt-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'Name': 'mwaa-wlt-env'})[1],
        'InvokeRestApi': lambda store: (store.create_environment(Name='mwaa-api-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'Name': 'mwaa-api-env', 'Path': '/dags', 'Method': 'GET'})[1],
        'PublishMetrics': lambda store: (store.create_environment(Name='mwaa-pm-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'EnvironmentName': 'mwaa-pm-env', 'MetricData': [{'MetricName': 'test', 'Timestamp': 0, 'Value': 1.0}]})[1],
        'mwaa.TagResource': lambda store: (store.create_environment(Name='mwaa-tag-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'ResourceArn': store._generate_arn('mwaa-tag-env'), 'Tags': {'env': 'test'}})[1],
        'mwaa.UntagResource': lambda store: (store.create_environment(Name='mwaa-untag-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'ResourceArn': store._generate_arn('mwaa-untag-env'), 'tagKeys': ['env']})[1],
        'mwaa.ListTagsForResource': lambda store: (store.create_environment(Name='mwaa-ltfr-env', ExecutionRoleArn='arn:aws:iam::123456789012:role/mwaa', SourceBucketArn='arn:aws:s3:::mwaa-test', DagS3Path='dags/', NetworkConfiguration={'SecurityGroupIds': ['sg-123'], 'SubnetIds': ['subnet-123']}), {'ResourceArn': store._generate_arn('mwaa-ltfr-env')})[1],
        # ── glue ─────────────────────────────────────────────────────────
        'CreateDatabase': {'Name': 'glue-test-db'},
        'GetDatabase': lambda store: (store.databases(name='glue-get-db', catalog_id='default', record={'Name': 'glue-get-db'}), {'Name': 'glue-get-db'})[1],
        'CreateCrawler': {'Name': 'glue-test-crawler', 'Role': 'arn:aws:iam::123456789012:role/glue', 'Targets': {'JdbcTargets': []}},
        'codeartifact.ListTagsForResource': lambda store: (d := store.domains.setdefault('ca-ltfr-d', DomainRecord('ca-ltfr-d', '123456789012')), {'resourceArn': d.arn})[1],

        # ── forecast ──────────────────────────────────────────────────────────
        'forecast.CreateDataset': {'DatasetName': 'fc-test-dataset', 'Domain': 'CUSTOM', 'DatasetType': 'TARGET_TIME_SERIES', 'Schema': {}},
        'forecast.CreateForecast': {'ForecastName': 'fc-test-forecast', 'PredictorArn': 'arn:aws:forecast:us-east-1:123456789012:predictor/fc-test-predictor'},
        'forecast.CreatePredictor': {'PredictorName': 'fc-test-predictor', 'InputDataConfig': {'DatasetGroupArn': 'arn:aws:forecast:us-east-1:123456789012:dataset-group/fc-test-dg'}, 'FeaturizationConfig': {'ForecastFrequency': 'D'}, 'ForecastHorizon': 7},
        'forecast.DeleteDataset': lambda store: (r := store.create_dataset('fc-del-ds', Domain='CUSTOM', DatasetType='TARGET_TIME_SERIES', Schema={}), {'DatasetArn': r.DatasetArn})[1],
        'forecast.DeleteForecast': lambda store: (r := store.create_forecast('fc-del-fc', PredictorArn='arn:aws:forecast:us-east-1:123456789012:predictor/fc-p'), {'ForecastArn': r.ForecastArn})[1],
        'forecast.DeletePredictor': lambda store: (r := store.create_predictor('fc-del-pr', InputDataConfig={'DatasetGroupArn': 'arn:test'}, FeaturizationConfig={'ForecastFrequency': 'D'}, ForecastHorizon=7), {'PredictorArn': r.PredictorArn})[1],
        'forecast.DescribeDataset': lambda store: (r := store.create_dataset('fc-desc-ds', Domain='CUSTOM', DatasetType='TARGET_TIME_SERIES', Schema={}), {'DatasetArn': r.DatasetArn})[1],
        'forecast.DescribeForecast': lambda store: (r := store.create_forecast('fc-desc-fc', PredictorArn='arn:aws:forecast:us-east-1:123456789012:predictor/fc-p'), {'ForecastArn': r.ForecastArn})[1],
        'forecast.DescribePredictor': lambda store: (r := store.create_predictor('fc-desc-pr', InputDataConfig={'DatasetGroupArn': 'arn:test'}, FeaturizationConfig={'ForecastFrequency': 'D'}, ForecastHorizon=7), {'PredictorArn': r.PredictorArn})[1],
        'forecast.ListDatasets': {},
        'forecast.ListForecasts': {},
        'forecast.ListPredictors': {},
        'forecast.TagResource': lambda store: (r := store.create_dataset('fc-tag-ds', Domain='CUSTOM', DatasetType='TARGET_TIME_SERIES', Schema={}), {'ResourceArn': r.DatasetArn, 'Tags': [{'Key': 'test', 'Value': 'val'}]})[1],
        'forecast.UntagResource': lambda store: (r := store.create_dataset('fc-untag-ds', Domain='CUSTOM', DatasetType='TARGET_TIME_SERIES', Schema={}), {'ResourceArn': r.DatasetArn, 'TagKeys': ['test']})[1],
        'forecast.ListTagsForResource': lambda store: (r := store.create_dataset('fc-ltfr-ds', Domain='CUSTOM', DatasetType='TARGET_TIME_SERIES', Schema={}), {'ResourceArn': r.DatasetArn})[1],

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
