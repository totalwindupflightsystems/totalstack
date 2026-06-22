"""Integration tests for AWS Backup."""
import os
import importlib.util
import types
import pytest
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'backup')

models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

BackupStore = models_mod.BackupStore
AlreadyExistsException = models_mod.AlreadyExistsException
ResourceNotFoundException = models_mod.ResourceNotFoundException
InvalidParameterValueException = models_mod.InvalidParameterValueException

EXC = {k: v for k, v in models_mod.__dict__.items() if isinstance(v, type) and issubclass(v, Exception) and v is not Exception}
REC = {k: v for k, v in models_mod.__dict__.items() if isinstance(v, type) and 'Record' in k}
SKIP_NAMES = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load(op):
    path = os.path.join(SERVICE_DIR, op + '.code.py')
    spec = importlib.util.spec_from_file_location(op, path)
    mod = importlib.util.module_from_spec(spec)
    for n, c in EXC.items():
        setattr(mod, n, c)
    for n, c in REC.items():
        setattr(mod, n, c)
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in SKIP_NAMES):
            handler = v
            break
    assert handler is not None, f"No handler in {op}"
    return handler


class TestBackupPlan:
    @pytest.fixture
    def store(self):
        return BackupStore()

    def test_create_plan(self, store):
        resp = _load('CreateBackupPlan')(store, {"BackupPlanName": "daily-plan"})
        assert "BackupPlanId" in resp

    def test_create_plan_duplicate(self, store):
        h = _load('CreateBackupPlan')
        h(store, {"BackupPlanName": "dup-plan"})
        with pytest.raises(AlreadyExistsException):
            h(store, {"BackupPlanName": "dup-plan"})

    def test_get_plan(self, store):
        h = _load('CreateBackupPlan')
        resp = h(store, {"BackupPlanName": "get-plan"})
        result = _load('GetBackupPlan')(store, {"BackupPlanId": resp["BackupPlanId"]})
        assert result["BackupPlanName"] == "get-plan"

    def test_get_plan_nonexistent(self, store):
        with pytest.raises(ResourceNotFoundException):
            _load('GetBackupPlan')(store, {"BackupPlanId": "nonexistent"})

    def test_delete_plan(self, store):
        h = _load('CreateBackupPlan')
        resp = h(store, {"BackupPlanName": "del-plan"})
        _load('DeleteBackupPlan')(store, {"BackupPlanId": resp["BackupPlanId"]})
        with pytest.raises(ResourceNotFoundException):
            _load('GetBackupPlan')(store, {"BackupPlanId": resp["BackupPlanId"]})

    def test_list_plans(self, store):
        h = _load('CreateBackupPlan')
        h(store, {"BackupPlanName": "p1"})
        h(store, {"BackupPlanName": "p2"})
        result = _load('ListBackupPlans')(store, {})
        assert len(result["BackupPlansList"]) == 2


class TestBackupVault:
    @pytest.fixture
    def store(self):
        return BackupStore()

    def test_create_vault(self, store):
        resp = _load('CreateBackupVault')(store, {"BackupVaultName": "my-vault"})
        assert resp["BackupVaultName"] == "my-vault"

    def test_describe_vault(self, store):
        _load('CreateBackupVault')(store, {"BackupVaultName": "desc-vault"})
        result = _load('DescribeBackupVault')(store, {"BackupVaultName": "desc-vault"})
        assert result["BackupVaultName"] == "desc-vault"

    def test_delete_vault(self, store):
        _load('CreateBackupVault')(store, {"BackupVaultName": "del-vault"})
        _load('DeleteBackupVault')(store, {"BackupVaultName": "del-vault"})
        with pytest.raises(ResourceNotFoundException):
            _load('DescribeBackupVault')(store, {"BackupVaultName": "del-vault"})

    def test_list_vaults(self, store):
        _load('CreateBackupVault')(store, {"BackupVaultName": "v1"})
        _load('CreateBackupVault')(store, {"BackupVaultName": "v2"})
        result = _load('ListBackupVaults')(store, {})
        assert len(result["BackupVaultList"]) == 2


class TestBackupSelection:
    @pytest.fixture
    def store_with_plan(self):
        store = BackupStore()
        resp = _load('CreateBackupPlan')(store, {"BackupPlanName": "sel-plan"})
        store._pid = resp["BackupPlanId"]
        return store

    def test_create_selection(self, store_with_plan):
        s = store_with_plan
        resp = _load('CreateBackupSelection')(s, {
            "BackupPlanId": s._pid, "SelectionName": "ec2-sel",
            "IamRoleArn": "arn:aws:iam::123:role/backup",
            "Resources": ["arn:aws:ec2:*:*:instance/*"],
        })
        assert "SelectionId" in resp

    def test_get_selection(self, store_with_plan):
        s = store_with_plan
        resp = _load('CreateBackupSelection')(s, {
            "BackupPlanId": s._pid, "SelectionName": "get-sel",
            "IamRoleArn": "arn:aws:iam::123:role/backup",
        })
        result = _load('GetBackupSelection')(s, {
            "BackupPlanId": s._pid, "SelectionId": resp["SelectionId"],
        })
        assert result["SelectionName"] == "get-sel"

    def test_delete_selection(self, store_with_plan):
        s = store_with_plan
        resp = _load('CreateBackupSelection')(s, {
            "BackupPlanId": s._pid, "SelectionName": "del-sel",
            "IamRoleArn": "arn:aws:iam::123:role/backup",
        })
        _load('DeleteBackupSelection')(s, {
            "BackupPlanId": s._pid, "SelectionId": resp["SelectionId"],
        })
        with pytest.raises(ResourceNotFoundException):
            _load('GetBackupSelection')(s, {
                "BackupPlanId": s._pid, "SelectionId": resp["SelectionId"],
            })


class TestBackupJob:
    @pytest.fixture
    def store_with_vault(self):
        store = BackupStore()
        _load('CreateBackupVault')(store, {"BackupVaultName": "job-vault"})
        store._vname = "job-vault"
        return store

    def test_start_job(self, store_with_vault):
        s = store_with_vault
        resp = _load('StartBackupJob')(s, {
            "BackupVaultName": s._vname,
            "ResourceArn": "arn:aws:ec2:us-east-1:123:instance/i-abc",
            "IamRoleArn": "arn:aws:iam::123:role/backup",
        })
        assert "BackupJobId" in resp

    def test_describe_job(self, store_with_vault):
        s = store_with_vault
        resp = _load('StartBackupJob')(s, {
            "BackupVaultName": s._vname,
            "ResourceArn": "arn:aws:ec2:us-east-1:123:instance/i-def",
            "IamRoleArn": "arn:aws:iam::123:role/backup",
        })
        result = _load('DescribeBackupJob')(s, {"BackupJobId": resp["BackupJobId"]})
        assert result["State"] == "CREATED"

    def test_stop_job(self, store_with_vault):
        s = store_with_vault
        resp = _load('StartBackupJob')(s, {
            "BackupVaultName": s._vname,
            "ResourceArn": "arn:aws:ec2:us-east-1:123:instance/i-ghi",
            "IamRoleArn": "arn:aws:iam::123:role/backup",
        })
        _load('StopBackupJob')(s, {"BackupJobId": resp["BackupJobId"]})
        result = _load('DescribeBackupJob')(s, {"BackupJobId": resp["BackupJobId"]})
        assert result["State"] == "STOPPED"
