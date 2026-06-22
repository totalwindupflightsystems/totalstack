import os
import importlib.util
import types
import pytest
A = os.path.dirname(__file__); S = os.path.join(A, '..', 'efs')
ms = importlib.util.spec_from_file_location('m', os.path.join(S, 'models.code.py'))
mm = importlib.util.module_from_spec(ms); ms.loader.exec_module(mm)
ES = mm.EfsStore; RNF = mm.ResourceNotFoundException
def L(n):
    p = os.path.join(S, n + '.code.py')
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ != '<lambda>': return v
class TestEFS:
    @pytest.fixture
    def store(self): return ES()
    def test_create(self, store):
        L('createfilesystem')(store, {'CreationToken': 'tok1'})
        r = L('describefilesystems')(store, {})
        assert len(r['FileSystems']) == 1
    def test_mount_target(self, store):
        L('createfilesystem')(store, {'CreationToken': 'tok1'})
        r = L('describefilesystems')(store, {})
        L('createmounttarget')(store, {'FileSystemId': r['FileSystems'][0]['FileSystemId'], 'SubnetId': 'subnet-1'})
        r = L('describemounttargets')(store, {'FileSystemId': r['FileSystems'][0]['FileSystemId']})
        assert len(r['MountTargets']) == 1
    def test_tags(self, store):
        L('createfilesystem')(store, {'CreationToken': 'tok1'})
        r = L('describefilesystems')(store, {})
        fid = r['FileSystems'][0]['FileSystemId']
        L('tagresource')(store, {'ResourceId': fid, 'Tags': [{'Key': 'env', 'Value': 'prod'}]})
        r = L('listtagsforresource')(store, {'ResourceId': fid})
        assert r['Tags'][0]['Key'] == 'env'
    def test_delete(self, store):
        L('createfilesystem')(store, {'CreationToken': 'tok1'})
        r = L('describefilesystems')(store, {})
        fid = r['FileSystems'][0]['FileSystemId']
        L('deletefilesystem')(store, {'FileSystemId': fid})
        with pytest.raises(RNF): L('describefilesystems')(store, {'FileSystemId': fid})

