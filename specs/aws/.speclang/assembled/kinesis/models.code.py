"""Kinesis Data Streams Store."""

class ResourceNotFoundException(Exception):
    pass
class ResourceInUseException(Exception):
    pass
class InvalidArgumentException(Exception):
    pass
class LimitExceededException(Exception):
    pass

class KinesisStore:
    def __init__(self):
        self._streams: dict[str, dict] = {}
        self._shards: dict[str, list] = {}
        self._records: dict[str, list] = {}
        self._tags: dict[str, list] = {}

    def create_stream(self, name: str, shard_count: int = 1, **kwargs) -> dict:
        if name in self._streams:
            raise ResourceInUseException(f"Stream {name} already exists")
        stream = {
            'StreamName': name,
            'StreamARN': f'arn:aws:kinesis:us-east-1:123456789012:stream/{name}',
            'StreamStatus': 'ACTIVE',
            'ShardCount': shard_count,
            'RetentionPeriodHours': kwargs.get('RetentionPeriodHours', 24),
            'StreamCreationTimestamp': 1625000000.0,
        }
        self._streams[name] = stream
        self._shards[name] = [{'ShardId': f'shardId-{i:012d}', 'StartingHashKey': str(i)} for i in range(shard_count)]
        self._records[name] = []
        return {}

    def describe_stream(self, name: str, limit: int = 10, shard_id: str = None) -> dict:
        if name not in self._streams:
            raise ResourceNotFoundException(f"Stream {name} not found")
        shards = self._shards.get(name, [])
        if shard_id:
            shards = [s for s in shards if s['ShardId'] == shard_id]
        return {
            'StreamDescription': {
                **self._streams[name],
                'Shards': shards[:limit],
                'HasMoreShards': len(shards) > limit,
                'EnhancedMonitoring': [{'ShardLevelMetrics': []}],
            }
        }

    def list_streams(self, limit: int = 10, exclusive_start_name: str = None) -> dict:
        names = sorted(self._streams.keys())
        if exclusive_start_name and exclusive_start_name in names:
            idx = names.index(exclusive_start_name) + 1
            names = names[idx:]
        return {'StreamNames': names[:limit], 'HasMoreStreams': len(names) > limit}

    def delete_stream(self, name: str, enforce_consumer_deletion: bool = False) -> dict:
        if name not in self._streams:
            raise ResourceNotFoundException(f"Stream {name} not found")
        del self._streams[name]
        self._shards.pop(name, None)
        self._records.pop(name, None)
        return {}

    def put_record(self, stream_name: str, data: str, partition_key: str, **kwargs) -> dict:
        if stream_name not in self._streams:
            raise ResourceNotFoundException(f"Stream {stream_name} not found")
        seq = str(len(self._records.get(stream_name, [])) + 1)
        shard = self._shards[stream_name][0] if self._shards.get(stream_name) else {'ShardId': 'shardId-0'}
        record = {'Data': data, 'PartitionKey': partition_key, 'SequenceNumber': seq}
        self._records.setdefault(stream_name, []).append(record)
        return {'ShardId': shard['ShardId'], 'SequenceNumber': seq}

    def put_records(self, stream_name: str, records: list) -> dict:
        if stream_name not in self._streams:
            raise ResourceNotFoundException(f"Stream {stream_name} not found")
        results = []
        for r in records:
            seq = str(len(self._records.get(stream_name, [])) + 1)
            self._records.setdefault(stream_name, []).append({'Data': r['Data'], 'PartitionKey': r['PartitionKey'], 'SequenceNumber': seq})
            results.append({'SequenceNumber': seq, 'ShardId': 'shardId-0'})
        return {'Records': [{'SequenceNumber': r['SequenceNumber'], 'ShardId': r['ShardId']} for r in results], 'FailedRecordCount': 0}

    def get_shard_iterator(self, stream_name: str, shard_id: str, iterator_type: str, **kwargs) -> dict:
        if stream_name not in self._streams:
            raise ResourceNotFoundException(f"Stream {stream_name} not found")
        return {'ShardIterator': f'iterator-{shard_id}-{iterator_type}'}

    def get_records(self, shard_iterator: str, limit: int = 10) -> dict:
        return {'Records': [], 'NextShardIterator': shard_iterator, 'MillisBehindLatest': 0}

    def tag_stream(self, stream_name: str, tags: dict) -> dict:
        items = [{'Key': k, 'Value': v} for k, v in tags.items()]
        self._tags.setdefault(stream_name, []).extend(items)
        return {}

    def list_tags(self, stream_name: str) -> dict:
        tags = self._tags.get(stream_name, [])
        return {'Tags': tags, 'HasMoreTags': False}

    def remove_tags(self, stream_name: str, tag_keys: list) -> dict:
        if stream_name in self._tags:
            self._tags[stream_name] = [t for t in self._tags[stream_name] if t['Key'] not in tag_keys]
        return {}
