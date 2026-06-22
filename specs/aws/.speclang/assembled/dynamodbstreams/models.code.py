"""DynamoDB Streams store — Stream, Shard, ShardIterator."""
import uuid
import time as _time


class ResourceNotFoundException(Exception):
    pass

class InternalServerError(Exception):
    pass

class LimitExceededException(Exception):
    pass

class ExpiredIteratorException(Exception):
    pass

class TrimmedDataAccessException(Exception):
    pass


class StreamRecord:
    def __init__(self, streamArn, tableName):
        self.streamArn = streamArn
        self.streamLabel = f"2025-{uuid.uuid4().hex[:8]}"
        self.tableName = tableName
        self.streamStatus = "ENABLED"
        self.shards = []
        self.created_time = _time.time()

    def to_dict(self):
        return {
            "StreamArn": self.streamArn,
            "StreamLabel": self.streamLabel,
            "TableName": self.tableName,
            "StreamStatus": self.streamStatus,
            "Shards": [s.to_dict() for s in self.shards],
        }


class ShardRecord:
    def __init__(self, shardId, parentShardId=None):
        self.ShardId = shardId
        self.ParentShardId = parentShardId or ""
        self.SequenceNumberRange = {
            "StartingSequenceNumber": "100000000000000000001",
            "EndingSequenceNumber": None,
        }
        self.records = []

    def to_dict(self):
        return {
            "ShardId": self.ShardId,
            "ParentShardId": self.ParentShardId,
            "SequenceNumberRange": self.SequenceNumberRange,
        }


class DynamoDBStreamsStore:
    def __init__(self):
        self._streams: dict[str, StreamRecord] = {}
        self._iterators: dict[str, dict] = {}

    def list_streams(self, TableName=None, Limit=None, ExclusiveStartStreamArn=None):
        streams = list(self._streams.values())
        if TableName:
            streams = [s for s in streams if s.tableName == TableName]
        return {"Streams": [s.to_dict() for s in streams]}

    def describe_stream(self, StreamArn, Limit=None, ExclusiveStartShardId=None):
        s = self._streams.get(StreamArn)
        if not s:
            raise ResourceNotFoundException(f"Stream '{StreamArn}' not found")
        return {"StreamDescription": s.to_dict()}

    def get_shard_iterator(self, StreamArn, ShardId, ShardIteratorType,
                           SequenceNumber=None):
        s = self._streams.get(StreamArn)
        if not s:
            raise ResourceNotFoundException(f"Stream '{StreamArn}' not found")
        shard = None
        for sh in s.shards:
            if sh.ShardId == ShardId:
                shard = sh
                break
        if not shard:
            raise ResourceNotFoundException(f"Shard '{ShardId}' not found")
        iterator_id = f"iterator-{uuid.uuid4().hex[:12]}"
        self._iterators[iterator_id] = {
            "streamArn": StreamArn,
            "shardId": ShardId,
            "type": ShardIteratorType,
        }
        return {"ShardIterator": iterator_id}

    def get_records(self, ShardIterator, Limit=None):
        it = self._iterators.get(ShardIterator)
        if not it:
            raise ExpiredIteratorException("ShardIterator has expired")
        return {"Records": [], "NextShardIterator": None}

    def _add_stream(self, streamArn, tableName):
        record = StreamRecord(streamArn, tableName)
        shard = ShardRecord(f"shardId-{uuid.uuid4().hex[:12]}")
        record.shards.append(shard)
        self._streams[streamArn] = record
        return record
