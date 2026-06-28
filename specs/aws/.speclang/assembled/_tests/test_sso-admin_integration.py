"""Integration test for SSO Admin — real SsoAdminStore."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'sso-admin')

models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

SsoAdminStore = models_mod.SsoAdminStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
ValidationException = models_mod.ValidationException
ConflictException = models_mod.ConflictException


def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ValidationException = ValidationException
    mod.ConflictException = ConflictException
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    skip_names = {'uuid', 'time', 'datetime', 'dataclass', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType) and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestInstance:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SsoAdminStore()
        return self._store

    def test_create_instance(self):
        handler = _load_handler('create-instance')
        resp = handler(self.store, {})
        assert resp["instanceArn"].startswith("arn:aws:sso:")
        assert resp["status"] == "ACTIVE"

    def test_describe_instance(self):
        create_h = _load_handler('create-instance')
        resp = create_h(self.store, {"name": "my-instance"})
        arn = resp["instanceArn"]
        handler = _load_handler('describe-instance')
        resp = handler(self.store, {"instanceArn": arn})
        assert resp["name"] == "my-instance"

    def test_describe_nonexistent(self):
        handler = _load_handler('describe-instance')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"instanceArn": "arn:nonexistent"})

    def test_update_instance(self):
        create_h = _load_handler('create-instance')
        resp = create_h(self.store, {"name": "old-name"})
        arn = resp["instanceArn"]
        handler = _load_handler('update-instance')
        handler(self.store, {"instanceArn": arn, "name": "new-name"})
        desc_h = _load_handler('describe-instance')
        resp = desc_h(self.store, {"instanceArn": arn})
        assert resp["name"] == "new-name"

    def test_delete_instance(self):
        create_h = _load_handler('create-instance')
        resp = create_h(self.store, {"name": "del-me"})
        arn = resp["instanceArn"]
        handler = _load_handler('delete-instance')
        handler(self.store, {"instanceArn": arn})
        desc_h = _load_handler('describe-instance')
        with pytest.raises(ResourceNotFoundException):
            desc_h(self.store, {"instanceArn": arn})

    def test_list_instances(self):
        create_h = _load_handler('create-instance')
        create_h(self.store, {"name": "i1"})
        create_h(self.store, {"name": "i2"})
        handler = _load_handler('list-instances')
        resp = handler(self.store, {})
        assert len(resp["instances"]) >= 2


class TestPermissionSet:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SsoAdminStore()
        return self._store

    def _create_instance(self):
        handler = _load_handler('create-instance')
        return handler(self.store, {"name": "test"})["instanceArn"]

    def test_create_permission_set(self):
        iarn = self._create_instance()
        handler = _load_handler('create-permission-set')
        resp = handler(self.store, {"name": "AdminAccess", "instanceArn": iarn})
        assert "permissionSetArn" in resp
        assert resp["name"] == "AdminAccess"

    def test_create_missing_required(self):
        handler = _load_handler('create-permission-set')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_describe_permission_set(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        resp = create_h(self.store, {"name": "ReadOnly", "instanceArn": iarn})
        ps_arn = resp["permissionSetArn"]
        handler = _load_handler('describe-permission-set')
        resp = handler(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        assert resp["name"] == "ReadOnly"

    def test_describe_nonexistent(self):
        iarn = self._create_instance()
        handler = _load_handler('describe-permission-set')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"instanceArn": iarn, "permissionSetArn": "arn:nonexistent"})

    def test_update_permission_set(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        resp = create_h(self.store, {"name": "OldPS", "instanceArn": iarn})
        ps_arn = resp["permissionSetArn"]
        handler = _load_handler('update-permission-set')
        handler(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn, "description": "Updated"})
        desc_h = _load_handler('describe-permission-set')
        resp = desc_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        assert resp["description"] == "Updated"

    def test_delete_permission_set(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        resp = create_h(self.store, {"name": "DelPS", "instanceArn": iarn})
        ps_arn = resp["permissionSetArn"]
        handler = _load_handler('delete-permission-set')
        handler(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        desc_h = _load_handler('describe-permission-set')
        with pytest.raises(ResourceNotFoundException):
            desc_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})

    def test_list_permission_sets(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        create_h(self.store, {"name": "PS1", "instanceArn": iarn})
        create_h(self.store, {"name": "PS2", "instanceArn": iarn})
        handler = _load_handler('list-permission-sets')
        resp = handler(self.store, {"instanceArn": iarn})
        assert len(resp["permissionSets"]) == 2

    def test_put_and_get_inline_policy(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        resp = create_h(self.store, {"name": "PolicyPS", "instanceArn": iarn})
        ps_arn = resp["permissionSetArn"]
        put_h = _load_handler('put-inline-policy-to-permission-set')
        put_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn, "inlinePolicy": '{"Version":"2012-10-17","Statement":[]}'})
        get_h = _load_handler('get-inline-policy-for-permission-set')
        resp = get_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        assert resp["inlinePolicy"] == '{"Version":"2012-10-17","Statement":[]}'

    def test_delete_inline_policy(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        resp = create_h(self.store, {"name": "DelPolicy", "instanceArn": iarn})
        ps_arn = resp["permissionSetArn"]
        put_h = _load_handler('put-inline-policy-to-permission-set')
        put_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn, "inlinePolicy": "test"})
        del_h = _load_handler('delete-inline-policy-from-permission-set')
        del_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        get_h = _load_handler('get-inline-policy-for-permission-set')
        resp = get_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        assert resp["inlinePolicy"] == ""

    def test_attach_and_list_managed_policies(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        resp = create_h(self.store, {"name": "ManagedPolicyPS", "instanceArn": iarn})
        ps_arn = resp["permissionSetArn"]
        attach_h = _load_handler('attach-managed-policy-to-permission-set')
        attach_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn, "managedPolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"})
        list_h = _load_handler('list-managed-policies-in-permission-set')
        resp = list_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        assert len(resp["attachedManagedPolicies"]) == 1

    def test_detach_managed_policy(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-permission-set')
        resp = create_h(self.store, {"name": "DetachPS", "instanceArn": iarn})
        ps_arn = resp["permissionSetArn"]
        attach_h = _load_handler('attach-managed-policy-to-permission-set')
        attach_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn, "managedPolicyArn": "arn:policy/test"})
        detach_h = _load_handler('detach-managed-policy-from-permission-set')
        detach_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn, "managedPolicyArn": "arn:policy/test"})
        list_h = _load_handler('list-managed-policies-in-permission-set')
        resp = list_h(self.store, {"instanceArn": iarn, "permissionSetArn": ps_arn})
        assert len(resp["attachedManagedPolicies"]) == 0


class TestAccountAssignment:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SsoAdminStore()
        return self._store

    def _create_instance_and_ps(self):
        create_i = _load_handler('create-instance')
        iarn = create_i(self.store, {"name": "test"})["instanceArn"]
        create_ps = _load_handler('create-permission-set')
        ps_arn = create_ps(self.store, {"name": "AdminAccess", "instanceArn": iarn})["permissionSetArn"]
        return iarn, ps_arn

    def test_create_account_assignment(self):
        iarn, ps_arn = self._create_instance_and_ps()
        handler = _load_handler('create-account-assignment')
        resp = handler(self.store, {
            "instanceArn": iarn, "targetId": "123456789012",
            "targetType": "AWS_ACCOUNT", "permissionSetArn": ps_arn,
            "principalType": "USER", "principalId": "user-1",
        })
        assert "accountAssignmentCreationStatus" in resp

    def test_create_missing_required(self):
        handler = _load_handler('create-account-assignment')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_delete_account_assignment(self):
        iarn, ps_arn = self._create_instance_and_ps()
        create_h = _load_handler('create-account-assignment')
        create_h(self.store, {
            "instanceArn": iarn, "targetId": "123456789012",
            "targetType": "AWS_ACCOUNT", "permissionSetArn": ps_arn,
            "principalType": "USER", "principalId": "user-1",
        })
        del_h = _load_handler('delete-account-assignment')
        resp = del_h(self.store, {
            "instanceArn": iarn, "targetId": "123456789012",
            "targetType": "AWS_ACCOUNT", "permissionSetArn": ps_arn,
            "principalType": "USER", "principalId": "user-1",
        })
        assert "accountAssignmentDeletionStatus" in resp

    def test_delete_nonexistent(self):
        iarn, ps_arn = self._create_instance_and_ps()
        del_h = _load_handler('delete-account-assignment')
        with pytest.raises(ResourceNotFoundException):
            del_h(self.store, {
                "instanceArn": iarn, "targetId": "999999999999",
                "targetType": "AWS_ACCOUNT", "permissionSetArn": ps_arn,
                "principalType": "USER", "principalId": "user-nope",
            })

    def test_list_account_assignments(self):
        iarn, ps_arn = self._create_instance_and_ps()
        create_h = _load_handler('create-account-assignment')
        create_h(self.store, {
            "instanceArn": iarn, "targetId": "123456789012",
            "targetType": "AWS_ACCOUNT", "permissionSetArn": ps_arn,
            "principalType": "USER", "principalId": "user-1",
        })
        list_h = _load_handler('list-account-assignments')
        resp = list_h(self.store, {
            "instanceArn": iarn, "accountId": "123456789012",
            "permissionSetArn": ps_arn,
        })
        assert len(resp["accountAssignments"]) == 1

    def test_list_account_assignments_for_principal(self):
        iarn, ps_arn = self._create_instance_and_ps()
        create_h = _load_handler('create-account-assignment')
        create_h(self.store, {
            "instanceArn": iarn, "targetId": "123456789012",
            "targetType": "AWS_ACCOUNT", "permissionSetArn": ps_arn,
            "principalType": "USER", "principalId": "user-99",
        })
        list_h = _load_handler('list-account-assignments-for-principal')
        resp = list_h(self.store, {
            "instanceArn": iarn, "principalId": "user-99",
            "principalType": "USER",
        })
        assert len(resp["accountAssignments"]) == 1

    def test_describe_creation_status(self):
        iarn, ps_arn = self._create_instance_and_ps()
        create_h = _load_handler('create-account-assignment')
        resp = create_h(self.store, {
            "instanceArn": iarn, "targetId": "123456789012",
            "targetType": "AWS_ACCOUNT", "permissionSetArn": ps_arn,
            "principalType": "USER", "principalId": "user-1",
        })
        req_id = resp["accountAssignmentCreationStatus"]["requestId"]
        desc_h = _load_handler('describe-account-assignment-creation-status')
        resp = desc_h(self.store, {
            "instanceArn": iarn,
            "accountAssignmentCreationRequestId": req_id,
        })
        assert resp["accountAssignmentCreationStatus"]["requestId"] == req_id


class TestApplication:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SsoAdminStore()
        return self._store

    def _create_instance(self):
        handler = _load_handler('create-instance')
        return handler(self.store, {"name": "test"})["instanceArn"]

    def test_create_application(self):
        iarn = self._create_instance()
        handler = _load_handler('create-application')
        resp = handler(self.store, {
            "instanceArn": iarn,
            "applicationProviderArn": "arn:aws:sso::aws:applicationProvider/saas",
            "name": "MyApp",
        })
        assert resp["applicationArn"].startswith("arn:aws:sso:")
        assert resp["name"] == "MyApp"

    def test_describe_application(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-application')
        resp = create_h(self.store, {
            "instanceArn": iarn,
            "applicationProviderArn": "arn:aws:sso::aws:applicationProvider/saas",
            "name": "DescribeMe",
        })
        app_arn = resp["applicationArn"]
        handler = _load_handler('describe-application')
        resp = handler(self.store, {"applicationArn": app_arn})
        assert resp["name"] == "DescribeMe"

    def test_describe_nonexistent(self):
        handler = _load_handler('describe-application')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"applicationArn": "arn:nonexistent"})

    def test_update_application(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-application')
        resp = create_h(self.store, {
            "instanceArn": iarn,
            "applicationProviderArn": "arn:provider/test",
            "name": "UpdateMe",
        })
        app_arn = resp["applicationArn"]
        handler = _load_handler('update-application')
        handler(self.store, {"applicationArn": app_arn, "name": "UpdatedApp", "description": "New desc"})
        desc_h = _load_handler('describe-application')
        resp = desc_h(self.store, {"applicationArn": app_arn})
        assert resp["name"] == "UpdatedApp"
        assert resp["description"] == "New desc"

    def test_delete_application(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-application')
        resp = create_h(self.store, {
            "instanceArn": iarn,
            "applicationProviderArn": "arn:provider/test",
            "name": "DelApp",
        })
        app_arn = resp["applicationArn"]
        handler = _load_handler('delete-application')
        handler(self.store, {"applicationArn": app_arn})
        desc_h = _load_handler('describe-application')
        with pytest.raises(ResourceNotFoundException):
            desc_h(self.store, {"applicationArn": app_arn})

    def test_list_applications(self):
        iarn = self._create_instance()
        create_h = _load_handler('create-application')
        create_h(self.store, {
            "instanceArn": iarn, "applicationProviderArn": "arn:p/p",
            "name": "App1",
        })
        create_h(self.store, {
            "instanceArn": iarn, "applicationProviderArn": "arn:p/p",
            "name": "App2",
        })
        handler = _load_handler('list-applications')
        resp = handler(self.store, {"instanceArn": iarn})
        assert len(resp["applications"]) == 2
