#!/usr/bin/env python3
import os
d = '/home/kara/totalstack/specs/aws/.speclang/assembled/kinesis'
os.makedirs(d, exist_ok=True)
for name, code in {
    'createstream': 'def handler(store, r: dict) -> dict:\n    return store.create_stream(r["StreamName"], r.get("ShardCount", 1))',
    'describestream': 'def handler(store, r: dict) -> dict:\n    return store.describe_stream(r["StreamName"], r.get("Limit", 10), r.get("ExclusiveStartShardId"))',
    'liststreams': 'def handler(store, r: dict) -> dict:\n    return store.list_streams(r.get("Limit", 10), r.get("ExclusiveStartStreamName"))',
    'deletestream': 'def handler(store, r: dict) -> dict:\n    return store.delete_stream(r["StreamName"], r.get("EnforceConsumerDeletion", False))',
    'putrecord': 'def handler(store, r: dict) -> dict:\n    return store.put_record(r["StreamName"], r["Data"], r["PartitionKey"])',
    'putrecords': 'def handler(store, r: dict) -> dict:\n    return store.put_records(r["StreamName"], r["Records"])',
    'getsharditerator': 'def handler(store, r: dict) -> dict:\n    return store.get_shard_iterator(r["StreamName"], r["ShardId"], r["ShardIteratorType"])',
    'getrecords': 'def handler(store, r: dict) -> dict:\n    return store.get_records(r["ShardIterator"], r.get("Limit", 10))',
    'tagstream': 'def handler(store, r: dict) -> dict:\n    return store.tag_stream(r["StreamName"], r["Tags"])',
    'listtagsforstream': 'def handler(store, r: dict) -> dict:\n    return store.list_tags(r["StreamName"])',
    'removetagsfromstream': 'def handler(store, r: dict) -> dict:\n    return store.remove_tags(r["StreamName"], r["TagKeys"])',
}.items():
    with open(f'{d}/{name}.code.py', 'w') as f: f.write(code)
print('11 handlers')
