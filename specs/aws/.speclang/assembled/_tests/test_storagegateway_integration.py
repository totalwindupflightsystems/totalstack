"""Integration test for Storage Gateway — real store."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'storagegateway')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

StorageGatewayStore = models_mod.StorageGatewayStore
InvalidRequestException = models_mod.InvalidRequestException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
GatewayRecord = models_mod.GatewayRecord
FileShareRecord = models_mod.FileShareRecord
VolumeRecord = models_mod.VolumeRecord
TapeRecord = models_mod.TapeRecord


def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidRequestException = InvalidRequestException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    mod.GatewayRecord = GatewayRecord
    mod.FileShareRecord = FileShareRecord
    mod.VolumeRecord = VolumeRecord
    mod.TapeRecord = TapeRecord
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    return None


class TestGateway:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = StorageGatewayStore()
        return self._store

    def test_activate_gateway_happy(self):
        handler = _load_handler('ActivateGateway')
        resp = handler(self.store, {"ActivationKey": "KEY-123"})
        assert "GatewayARN" in resp

    def test_activate_gateway_missing_required(self):
        handler = _load_handler('ActivateGateway')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_describe_gateway_happy(self):
        create = _load_handler('ActivateGateway')
        arn = create(self.store, {"ActivationKey": "KEY-DESC"})["GatewayARN"]
        handler = _load_handler('DescribeGatewayInformation')
        desc = handler(self.store, {"GatewayARN": arn})
        assert desc["GatewayARN"] == arn

    def test_describe_gateway_nonexistent(self):
        handler = _load_handler('DescribeGatewayInformation')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"GatewayARN": "arn:nonexistent"})

    def test_list_gateways(self):
        handler = _load_handler('ListGateways')
        resp = handler(self.store, {})
        assert "Gateways" in resp

    def test_delete_gateway_happy(self):
        create = _load_handler('ActivateGateway')
        arn = create(self.store, {"ActivationKey": "KEY-DEL"})["GatewayARN"]
        handler = _load_handler('DeleteGateway')
        resp = handler(self.store, {"GatewayARN": arn})
        assert resp["GatewayARN"] == arn
        dh = _load_handler('DescribeGatewayInformation')
        with pytest.raises(ResourceNotFoundException):
            dh(self.store, {"GatewayARN": arn})

    def test_delete_gateway_nonexistent(self):
        handler = _load_handler('DeleteGateway')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"GatewayARN": "arn:nonexistent"})


class TestFileShare:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = StorageGatewayStore()
        return self._store

    def _create_gateway(self):
        create = _load_handler('ActivateGateway')
        return create(self.store, {"ActivationKey": "KEY-FS"})["GatewayARN"]

    def test_create_nfs_file_share_happy(self):
        gw = self._create_gateway()
        handler = _load_handler('CreateNFSFileShare')
        resp = handler(self.store, {
            "GatewayARN": gw,
            "Role": "arn:aws:iam::000000000000:role/sgw-role",
            "LocationARN": "arn:aws:s3:::my-nfs-bucket",
        })
        assert "FileShareARN" in resp

    def test_create_smb_file_share_happy(self):
        gw = self._create_gateway()
        handler = _load_handler('CreateSMBFileShare')
        resp = handler(self.store, {
            "GatewayARN": gw,
            "Role": "arn:aws:iam::000000000000:role/sgw-role",
            "LocationARN": "arn:aws:s3:::my-smb-bucket",
        })
        assert "FileShareARN" in resp

    def test_create_file_share_missing_required(self):
        handler = _load_handler('CreateNFSFileShare')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_list_file_shares(self):
        handler = _load_handler('ListFileShares')
        resp = handler(self.store, {})
        assert "FileShareInfoList" in resp

    def test_delete_file_share_happy(self):
        gw = self._create_gateway()
        create = _load_handler('CreateNFSFileShare')
        arn = create(self.store, {
            "GatewayARN": gw,
            "Role": "arn:aws:iam::000000000000:role/sgw-role",
            "LocationARN": "arn:aws:s3:::delete-fs-test",
        })["FileShareARN"]
        handler = _load_handler('DeleteFileShare')
        resp = handler(self.store, {"FileShareARN": arn})
        assert resp["FileShareARN"] == arn

    def test_delete_file_share_nonexistent(self):
        handler = _load_handler('DeleteFileShare')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"FileShareARN": "arn:nonexistent"})


class TestVolume:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = StorageGatewayStore()
        return self._store

    def _create_gateway(self):
        create = _load_handler('ActivateGateway')
        return create(self.store, {"ActivationKey": "KEY-VOL"})["GatewayARN"]

    def test_create_cached_iscsi_volume_happy(self):
        gw = self._create_gateway()
        handler = _load_handler('CreateCachediSCSIVolume')
        resp = handler(self.store, {
            "GatewayARN": gw,
            "VolumeSizeInBytes": 107374182400,
            "TargetName": "iqn.test.com:target1",
        })
        assert "VolumeARN" in resp

    def test_create_volume_duplicate_target(self):
        gw = self._create_gateway()
        handler = _load_handler('CreateCachediSCSIVolume')
        handler(self.store, {
            "GatewayARN": gw,
            "VolumeSizeInBytes": 107374182400,
            "TargetName": "iqn.test.com:dup-target",
        })
        with pytest.raises(ResourceInUseException):
            handler(self.store, {
                "GatewayARN": gw,
                "VolumeSizeInBytes": 107374182400,
                "TargetName": "iqn.test.com:dup-target",
            })

    def test_list_volumes(self):
        handler = _load_handler('ListVolumes')
        resp = handler(self.store, {})
        assert "VolumeInfos" in resp

    def test_delete_volume_happy(self):
        gw = self._create_gateway()
        create = _load_handler('CreateCachediSCSIVolume')
        arn = create(self.store, {
            "GatewayARN": gw,
            "VolumeSizeInBytes": 107374182400,
            "TargetName": "iqn.test.com:del-target",
        })["VolumeARN"]
        handler = _load_handler('DeleteVolume')
        resp = handler(self.store, {"VolumeARN": arn})
        assert resp["VolumeARN"] == arn

    def test_delete_volume_nonexistent(self):
        handler = _load_handler('DeleteVolume')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"VolumeARN": "arn:nonexistent"})


class TestTape:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = StorageGatewayStore()
        return self._store

    def _create_gateway(self):
        create = _load_handler('ActivateGateway')
        return create(self.store, {"ActivationKey": "KEY-TAPE"})["GatewayARN"]

    def test_create_tapes_happy(self):
        gw = self._create_gateway()
        handler = _load_handler('CreateTapes')
        resp = handler(self.store, {
            "GatewayARN": gw,
            "TapeSizeInBytes": 107374182400,
            "ClientToken": "token-123",
            "NumTapesToCreate": 3,
        })
        assert "TapeARNs" in resp
        assert len(resp["TapeARNs"]) == 3

    def test_list_tapes(self):
        handler = _load_handler('ListTapes')
        resp = handler(self.store, {})
        assert "TapeInfos" in resp

    def test_delete_tape_happy(self):
        gw = self._create_gateway()
        create = _load_handler('CreateTapes')
        arns = create(self.store, {
            "GatewayARN": gw,
            "TapeSizeInBytes": 107374182400,
            "ClientToken": "token-del",
            "NumTapesToCreate": 1,
        })["TapeARNs"]
        handler = _load_handler('DeleteTape')
        resp = handler(self.store, {"GatewayARN": gw, "TapeARN": arns[0]})
        assert resp["TapeARN"] == arns[0]

    def test_delete_tape_nonexistent(self):
        gw = self._create_gateway()
        handler = _load_handler('DeleteTape')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"GatewayARN": gw, "TapeARN": "arn:nonexistent"})


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = StorageGatewayStore()
        return self._store

    def _create_gateway(self):
        create = _load_handler('ActivateGateway')
        return create(self.store, {"ActivationKey": "KEY-TAGS"})["GatewayARN"]

    def test_add_tags_happy(self):
        arn = self._create_gateway()
        handler = _load_handler('AddTagsToResource')
        resp = handler(self.store, {
            "ResourceARN": arn,
            "Tags": [{"Key": "env", "Value": "prod"}],
        })
        assert resp["ResourceARN"] == arn

    def test_list_tags_happy(self):
        arn = self._create_gateway()
        add = _load_handler('AddTagsToResource')
        add(self.store, {
            "ResourceARN": arn,
            "Tags": [{"Key": "team", "Value": "storage"}],
        })
        handler = _load_handler('ListTagsForResource')
        resp = handler(self.store, {"ResourceARN": arn})
        assert "Tags" in resp
        assert any(t["Key"] == "team" for t in resp["Tags"])

    def test_list_tags_nonexistent(self):
        handler = _load_handler('ListTagsForResource')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"ResourceARN": "arn:nonexistent"})

    def test_remove_tags_happy(self):
        arn = self._create_gateway()
        add = _load_handler('AddTagsToResource')
        add(self.store, {
            "ResourceARN": arn,
            "Tags": [{"Key": "temp", "Value": "delete-me"}],
        })
        handler = _load_handler('RemoveTagsFromResource')
        resp = handler(self.store, {
            "ResourceARN": arn,
            "TagKeys": ["temp"],
        })
        assert resp["ResourceARN"] == arn

    def test_remove_tags_nonexistent(self):
        handler = _load_handler('RemoveTagsFromResource')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                "ResourceARN": "arn:nonexistent",
                "TagKeys": ["x"],
            })
