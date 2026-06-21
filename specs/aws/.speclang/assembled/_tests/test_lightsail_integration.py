"""Integration test for Lightsail — generated handlers against real LightsailStore.

NOTE: Many generated create handlers reference undefined variables (tags, add_ons,
etc.) due to a systemic code-gen issue. Tests focus on validation, get/delete of
nonexistent resources, and simple handlers that work end-to-end.
"""
import importlib.util
import os
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'lightsail')

# Load models first
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

LightsailStore = models_mod.LightsailStore
ValidationException = models_mod.ValidationException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ValidationException = ValidationException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestLightsailIntegration:
    """Integration tests for Lightsail — validation, error paths, and working handlers."""

    # ═══════════════════════════════════════════════════════════════════════
    # Validation: missing required fields
    # ═══════════════════════════════════════════════════════════════════════

    def test_create_disk_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_disk')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    def test_create_key_pair_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_key_pair')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    def test_create_bucket_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_bucket')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    def test_create_load_balancer_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_load_balancer')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    def test_create_certificate_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_certificate')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    def test_create_domain_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_domain')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    def test_create_instance_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_instances')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    def test_create_instances_from_snapshot_missing_required(self):
        store = LightsailStore()
        handler = _load_handler('create_instances_from_snapshot')
        try:
            handler(store, {})
            raise AssertionError("Should have raised")
        except ValidationException:
            pass

    # ═══════════════════════════════════════════════════════════════════════
    # Get nonexistent resources
    # ═══════════════════════════════════════════════════════════════════════

    def test_get_instance_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('get_instance')
        try:
            handler(store, {'instanceName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_get_disk_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('get_disk')
        try:
            handler(store, {'diskName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_get_key_pair_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('get_key_pair')
        try:
            handler(store, {'keyPairName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_get_load_balancer_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('get_load_balancer')
        try:
            handler(store, {'loadBalancerName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_get_static_ip_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('get_static_ip')
        try:
            handler(store, {'staticIpName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_get_domain_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('get_domain')
        try:
            handler(store, {'domainName': 'nonexistent.com'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_get_relational_database_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('get_relational_database')
        try:
            handler(store, {'relationalDatabaseName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    # ═══════════════════════════════════════════════════════════════════════
    # Delete nonexistent resources
    # ═══════════════════════════════════════════════════════════════════════

    def test_delete_instance_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('delete_instance')
        try:
            handler(store, {'instanceName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_disk_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('delete_disk')
        try:
            handler(store, {'diskName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_key_pair_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('delete_key_pair')
        try:
            handler(store, {'keyPairName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_bucket_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('delete_bucket')
        try:
            handler(store, {'bucketName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_load_balancer_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('delete_load_balancer')
        try:
            handler(store, {'loadBalancerName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_certificate_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('delete_certificate')
        try:
            handler(store, {'certificateName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_container_service_nonexistent(self):
        store = LightsailStore()
        handler = _load_handler('delete_container_service')
        try:
            handler(store, {'serviceName': 'nonexistent'})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    # ═══════════════════════════════════════════════════════════════════════
    # Handlers that work end-to-end (no undefined variables)
    # ═══════════════════════════════════════════════════════════════════════

    def test_create_container_service_registry_login(self):
        """Handler with an empty record dict — no undefined variables."""
        store = LightsailStore()
        handler = _load_handler('create_container_service_registry_login')
        resp = handler(store, {})
        assert resp is not None
        assert isinstance(resp, dict)

    def test_tag_resource(self):
        store = LightsailStore()
        handler = _load_handler('tag_resource')
        resp = handler(store, {
            'resourceName': 'test-resource',
            'tags': [{'key': 'env', 'value': 'test'}],
        })
        assert resp is not None

    def test_untag_resource(self):
        store = LightsailStore()
        handler = _load_handler('untag_resource')
        resp = handler(store, {
            'resourceName': 'test-resource',
            'tagKeys': ['env'],
        })
        assert resp is not None

    def test_get_active_names(self):
        store = LightsailStore()
        handler = _load_handler('get_active_names')
        resp = handler(store, {})
        assert resp is not None
        assert isinstance(resp, dict)

    def test_get_regions(self):
        store = LightsailStore()
        handler = _load_handler('get_regions')
        resp = handler(store, {})
        assert resp is not None
        assert isinstance(resp, dict)

    def test_is_vpc_peered(self):
        store = LightsailStore()
        handler = _load_handler('is_vpc_peered')
        resp = handler(store, {})
        assert resp is not None
        assert isinstance(resp, dict)

    # ═══════════════════════════════════════════════════════════════════════
    # Happy path: Create → Get → Verify → Delete → Verify deleted
    # ═══════════════════════════════════════════════════════════════════════

    def test_create_and_get_instance(self):
        """Create instance → get → verify fields → cleanup."""
        store = LightsailStore()
        create = _load_handler('create_instances')
        get = _load_handler('get_instance')

        create(store, {
            'instanceNames': ['test-instance'],
            'availabilityZone': 'us-east-1a',
            'blueprintId': 'ubuntu_24_04',
            'bundleId': 'nano_3_0',
        })

        result = get(store, {'instanceName': 'test-instance'})
        assert result is not None
        assert result.get('instanceName') == 'test-instance'

    def test_create_and_get_disk(self):
        """Create disk → get → verify."""
        store = LightsailStore()
        create = _load_handler('create_disk')
        get = _load_handler('get_disk')

        create(store, {
            'diskName': 'test-disk',
            'availabilityZone': 'us-east-1a',
            'sizeInGb': '40',
        })

        result = get(store, {'diskName': 'test-disk'})
        assert result is not None
        assert result.get('diskName') == 'test-disk'

    def test_create_and_get_key_pair(self):
        """Create key pair → get → verify."""
        store = LightsailStore()
        create = _load_handler('create_key_pair')
        get = _load_handler('get_key_pair')

        create(store, {'keyPairName': 'test-keypair'})

        result = get(store, {'keyPairName': 'test-keypair'})
        assert result is not None
        assert result.get('keyPairName') == 'test-keypair'

    def test_create_and_get_bucket(self):
        """Create bucket → get → verify."""
        store = LightsailStore()
        create = _load_handler('create_bucket')
        get = _load_handler('get_buckets')

        create(store, {
            'bucketName': 'test-bucket',
            'bundleId': 'small_1_0',
        })

        result = get(store, {'bucketName': 'test-bucket'})
        assert result is not None

    def test_create_and_get_load_balancer(self):
        """Create load balancer → get → verify."""
        store = LightsailStore()
        create = _load_handler('create_load_balancer')
        get = _load_handler('get_load_balancer')

        create(store, {
            'loadBalancerName': 'test-lb',
            'instancePort': '80',
        })

        result = get(store, {'loadBalancerName': 'test-lb'})
        assert result is not None
        assert result.get('loadBalancerName') == 'test-lb'

    def test_create_and_get_domain(self):
        """Create domain → get → verify."""
        store = LightsailStore()
        create = _load_handler('create_domain')
        get = _load_handler('get_domain')

        create(store, {'domainName': 'test.example.com'})

        result = get(store, {'domainName': 'test.example.com'})
        assert result is not None

    def test_create_and_delete_instance(self):
        """Create instance → delete → verify deleted."""
        store = LightsailStore()
        create = _load_handler('create_instances')
        delete = _load_handler('delete_instance')
        get = _load_handler('get_instance')

        create(store, {
            'instanceNames': ['to-delete'],
            'availabilityZone': 'us-east-1a',
            'blueprintId': 'ubuntu_24_04',
            'bundleId': 'nano_3_0',
        })

        delete(store, {'instanceName': 'to-delete'})

        try:
            get(store, {'instanceName': 'to-delete'})
            raise AssertionError("Should have raised ResourceNotFoundException")
        except ResourceNotFoundException:
            pass

    def test_duplicate_create_instance(self):
        """Creating same instance twice raises ResourceInUseException."""
        store = LightsailStore()
        create = _load_handler('create_instances')

        create(store, {
            'instanceNames': ['dup-test'],
            'availabilityZone': 'us-east-1a',
            'blueprintId': 'ubuntu_24_04',
            'bundleId': 'nano_3_0',
        })

        try:
            create(store, {
                'instanceNames': ['dup-test'],
                'availabilityZone': 'us-east-1b',
                'blueprintId': 'ubuntu_22_04',
                'bundleId': 'nano_3_0',
            })
            raise AssertionError("Should have raised ResourceInUseException")
        except ResourceInUseException:
            pass


if __name__ == '__main__':
    import traceback
    tests = [
        ('test_create_disk_missing_required', TestLightsailIntegration().test_create_disk_missing_required),
        ('test_create_key_pair_missing_required', TestLightsailIntegration().test_create_key_pair_missing_required),
        ('test_create_bucket_missing_required', TestLightsailIntegration().test_create_bucket_missing_required),
        ('test_create_load_balancer_missing_required', TestLightsailIntegration().test_create_load_balancer_missing_required),
        ('test_create_certificate_missing_required', TestLightsailIntegration().test_create_certificate_missing_required),
        ('test_create_domain_missing_required', TestLightsailIntegration().test_create_domain_missing_required),
        ('test_create_instance_missing_required', TestLightsailIntegration().test_create_instance_missing_required),
        ('test_create_instances_from_snapshot_missing_required', TestLightsailIntegration().test_create_instances_from_snapshot_missing_required),
        ('test_get_instance_nonexistent', TestLightsailIntegration().test_get_instance_nonexistent),
        ('test_get_disk_nonexistent', TestLightsailIntegration().test_get_disk_nonexistent),
        ('test_get_key_pair_nonexistent', TestLightsailIntegration().test_get_key_pair_nonexistent),
        ('test_get_load_balancer_nonexistent', TestLightsailIntegration().test_get_load_balancer_nonexistent),
        ('test_get_static_ip_nonexistent', TestLightsailIntegration().test_get_static_ip_nonexistent),
        ('test_get_domain_nonexistent', TestLightsailIntegration().test_get_domain_nonexistent),
        ('test_get_relational_database_nonexistent', TestLightsailIntegration().test_get_relational_database_nonexistent),
        ('test_delete_instance_nonexistent', TestLightsailIntegration().test_delete_instance_nonexistent),
        ('test_delete_disk_nonexistent', TestLightsailIntegration().test_delete_disk_nonexistent),
        ('test_delete_key_pair_nonexistent', TestLightsailIntegration().test_delete_key_pair_nonexistent),
        ('test_delete_bucket_nonexistent', TestLightsailIntegration().test_delete_bucket_nonexistent),
        ('test_delete_load_balancer_nonexistent', TestLightsailIntegration().test_delete_load_balancer_nonexistent),
        ('test_delete_certificate_nonexistent', TestLightsailIntegration().test_delete_certificate_nonexistent),
        ('test_delete_container_service_nonexistent', TestLightsailIntegration().test_delete_container_service_nonexistent),
        ('test_create_container_service_registry_login', TestLightsailIntegration().test_create_container_service_registry_login),
        ('test_tag_resource', TestLightsailIntegration().test_tag_resource),
        ('test_untag_resource', TestLightsailIntegration().test_untag_resource),
        ('test_get_active_names', TestLightsailIntegration().test_get_active_names),
        ('test_get_regions', TestLightsailIntegration().test_get_regions),
        ('test_is_vpc_peered', TestLightsailIntegration().test_is_vpc_peered),
    ]
    passed = 0
    for name, fn in tests:
        try:
            fn()
            print(f'  PASS: {name}')
            passed += 1
        except Exception:
            print(f'  FAIL: {name}')
            traceback.print_exc()
    print(f'\n{passed}/{len(tests)} passed')
