"""Integration tests for DynamoDB Streams."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'dynamodbstreams')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

DynamoDBStreamsStore = models_mod.DynamoDBStreamsStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
ExpiredIteratorException = models_mod.ExpiredIteratorException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ExpiredIteratorException = ExpiredIteratorException
    mod.InternalServerError = models_mod.InternalServerError
    mod.LimitExceededException = models_mod.LimitExceededException
    mod.TrimmedDataAccessException = models_mod.TrimmedDataAccessException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestDynamoDBStreams:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = DynamoDBStreamsStore()
        return self._store

    def test_list_streams_empty(self):
        handler = _load_handler('ListStreams')
        resp = handler(self.store, {})
        assert resp["Streams"] == []

    def test_list_streams_with_results(self):
        self.store._add_stream("arn:aws:dynamodb:us-east-1:123456789012:table/mytable/stream/2025-01-01", "mytable")
        self.store._add_stream("arn:aws:dynamodb:us-east-1:123456789012:table/other/stream/2025-01-02", "other")
        handler = _load_handler('ListStreams')
        resp = handler(self.store, {})
        assert len(resp["Streams"]) == 2

    def test_list_streams_filter_by_table(self):
        self.store._add_stream("arn:aws:dynamodb:us-east-1:123456789012:table/mytable/stream/2025-01-01", "mytable")
        self.store._add_stream("arn:aws:dynamodb:us-east-1:123456789012:table/other/stream/2025-01-02", "other")
        handler = _load_handler('ListStreams')
        resp = handler(self.store, {"TableName": "mytable"})
        assert len(resp["Streams"]) == 1
        assert resp["Streams"][0]["TableName"] == "mytable"

    def test_describe_stream_happy(self):
        stream = self.store._add_stream("arn:aws:dynamodb:us-east-1:123456789012:table/mytable/stream/2025-01-01", "mytable")
        handler = _load_handler('DescribeStream')
        resp = handler(self.store, {"StreamArn": stream.streamArn})
        assert resp["StreamDescription"]["TableName"] == "mytable"
        assert len(resp["StreamDescription"]["Shards"]) == 1

    def test_describe_stream_nonexistent(self):
        handler = _load_handler('DescribeStream')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"StreamArn": "nonexistent"})

    def test_get_shard_iterator_happy(self):
        stream = self.store._add_stream("arn:aws:dynamodb:us-east-1:123456789012:table/mytable/stream/2025-01-01", "mytable")
        handler = _load_handler('GetShardIterator')
        resp = handler(self.store, {
            "StreamArn": stream.streamArn,
            "ShardId": stream.shards[0].ShardId,
            "ShardIteratorType": "TRIM_HORIZON",
        })
        assert "ShardIterator" in resp

    def test_get_shard_iterator_nonexistent_stream(self):
        handler = _load_handler('GetShardIterator')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                "StreamArn": "nonexistent",
                "ShardId": "shard-123",
                "ShardIteratorType": "TRIM_HORIZON",
            })

    def test_get_records_empty(self):
        stream = self.store._add_stream("arn:aws:dynamodb:us-east-1:123456789012:table/mytable/stream/2025-01-01", "mytable")
        iter_handler = _load_handler('GetShardIterator')
        it_resp = iter_handler(self.store, {
            "StreamArn": stream.streamArn,
            "ShardId": stream.shards[0].ShardId,
            "ShardIteratorType": "TRIM_HORIZON",
        })
        handler = _load_handler('GetRecords')
        resp = handler(self.store, {"ShardIterator": it_resp["ShardIterator"]})
        assert resp["Records"] == []

    def test_get_records_expired_iterator(self):
        handler = _load_handler('GetRecords')
        with pytest.raises(ExpiredIteratorException):
            handler(self.store, {"ShardIterator": "expired-iterator"})
