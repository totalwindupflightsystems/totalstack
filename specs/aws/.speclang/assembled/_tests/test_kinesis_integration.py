"""Integration tests for Kinesis Data Streams."""
import os
import importlib.util
import types
import pytest
A = os.path.dirname(__file__)
S = os.path.join(A, '..', 'kinesis')
ms = importlib.util.spec_from_file_location('m', os.path.join(S, 'models.code.py'))
mm = importlib.util.module_from_spec(ms); ms.loader.exec_module(mm)
KS = mm.KinesisStore; RNF = mm.ResourceNotFoundException; RIU = mm.ResourceInUseException
def L(n):
    p = os.path.join(S, n + '.code.py')
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ != '<lambda>': return v

class TestKinesis:
    @pytest.fixture
    def store(self): return KS()
    def test_create(self, store):
        L('createstream')(store, {'StreamName': 's1', 'ShardCount': 2})
        r = L('describestream')(store, {'StreamName': 's1'})
        assert r['StreamDescription']['StreamName'] == 's1'
        assert len(r['StreamDescription']['Shards']) == 2
    def test_duplicate(self, store):
        L('createstream')(store, {'StreamName': 's1'})
        with pytest.raises(RIU): L('createstream')(store, {'StreamName': 's1'})
    def test_list(self, store):
        L('createstream')(store, {'StreamName': 's1'})
        L('createstream')(store, {'StreamName': 's2'})
        r = L('liststreams')(store, {})
        assert len(r['StreamNames']) >= 2
    def test_put_record(self, store):
        L('createstream')(store, {'StreamName': 's1'})
        r = L('putrecord')(store, {'StreamName': 's1', 'Data': 'hello', 'PartitionKey': 'pk1'})
        assert 'SequenceNumber' in r
    def test_put_records(self, store):
        L('createstream')(store, {'StreamName': 's1'})
        r = L('putrecords')(store, {'StreamName': 's1', 'Records': [{'Data': 'r1', 'PartitionKey': 'pk1'}, {'Data': 'r2', 'PartitionKey': 'pk1'}]})
        assert r['FailedRecordCount'] == 0
    def test_shard_iterator(self, store):
        L('createstream')(store, {'StreamName': 's1'})
        r = L('getsharditerator')(store, {'StreamName': 's1', 'ShardId': 'shardId-000000000000', 'ShardIteratorType': 'TRIM_HORIZON'})
        assert 'ShardIterator' in r
    def test_tags(self, store):
        L('createstream')(store, {'StreamName': 's1'})
        L('tagstream')(store, {'StreamName': 's1', 'Tags': {'env': 'prod'}})
        r = L('listtagsforstream')(store, {'StreamName': 's1'})
        assert r['Tags'][0]['Key'] == 'env'
        L('removetagsfromstream')(store, {'StreamName': 's1', 'TagKeys': ['env']})
        r = L('listtagsforstream')(store, {'StreamName': 's1'})
        assert len(r['Tags']) == 0
    def test_delete(self, store):
        L('createstream')(store, {'StreamName': 's1'})
        L('deletestream')(store, {'StreamName': 's1'})
        with pytest.raises(RNF): L('describestream')(store, {'StreamName': 's1'})

