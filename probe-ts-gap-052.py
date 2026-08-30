#!/usr/bin/env python3
"""TS-GAP-052 live probe — TotalStack variants (s3tables, dynamodbstreams, transcribe).

Boot: PROVIDER_OVERRIDE_S3TABLES=totalstack PROVIDER_OVERRIDE_DYNAMODBSTREAMS=totalstack
      PROVIDER_OVERRIDE_TRANSCRIBE=totalstack make start  (runtime 4.14.1.dev697, :4566)
Each op records HTTP status + error shape. Expectation: no HTTP 500, no '_w' AttributeError.
"""
import json
import sys
import uuid

import boto3
from botocore.exceptions import ClientError

ENDPOINT = "http://localhost:4566"
REGION = "us-east-1"
results = []


def trim(obj):
    s = json.dumps(obj, default=str, indent=2)
    return s[:1200] + ("..." if len(s) > 1200 else "")


def call(label, fn):
    try:
        resp = fn()
        status = resp["ResponseMetadata"]["HTTPStatusCode"]
        results.append({"op": label, "status": status, "ok": status < 400,
                        "response": trim(resp)})
        print(f"  OK   {label}: HTTP {status}")
    except ClientError as e:
        status = e.response["ResponseMetadata"]["HTTPStatusCode"]
        code = e.response["Error"]["Code"]
        results.append({"op": label, "status": status, "ok": status < 500,
                        "error_code": code,
                        "error_message": trim(e.response["Error"]["Message"])})
        print(f"  ERR  {label}: HTTP {status} {code} ({e.response['Error']['Message'][:90]})")
    except Exception as e:
        results.append({"op": label, "status": "EXC", "ok": False,
                        "error": f"{type(e).__name__}: {e}"})
        print(f"  EXC  {label}: {type(e).__name__}: {e}")


uid = uuid.uuid4().hex[:8]
bucket_arn = None


def make_bucket():
    global bucket_arn
    resp = s3t.create_table_bucket(name=bucket_name)
    bucket_arn = resp["arn"]
    return resp


print(f"== s3tables (PROVIDER_OVERRIDE_S3TABLES=totalstack) ==  uid={uid}")
s3t = boto3.client("s3tables", endpoint_url=ENDPOINT, region_name=REGION,
                   aws_access_key_id="test", aws_secret_access_key="test")

bucket_name = f"probe-bucket-{uid}"
call("s3tables.ListTableBuckets", lambda: s3t.list_table_buckets())
call("s3tables.CreateTableBucket", make_bucket)
if bucket_arn:
    call("s3tables.GetTableBucket", lambda: s3t.get_table_bucket(
        tableBucketARN=bucket_arn))
    call("s3tables.TagResource", lambda: s3t.tag_resource(
        resourceArn=bucket_arn, tags={"environment": "test", "team": "qa"}))
    call("s3tables.ListTagsForResource", lambda: s3t.list_tags_for_resource(
        resourceArn=bucket_arn))
    call("s3tables.UntagResource", lambda: s3t.untag_resource(
        resourceArn=bucket_arn, tagKeys=["team"]))
    call("s3tables.ListTagsForResource-after-untag",
         lambda: s3t.list_tags_for_resource(resourceArn=bucket_arn))
    call("s3tables.DeleteTableBucket", lambda: s3t.delete_table_bucket(
        tableBucketARN=bucket_arn))

print("\n== dynamodbstreams (PROVIDER_OVERRIDE_DYNAMODBSTREAMS=totalstack) ==")
ddbs = boto3.client("dynamodbstreams", endpoint_url=ENDPOINT, region_name=REGION,
                    aws_access_key_id="test", aws_secret_access_key="test")
call("dynamodbstreams.ListStreams", lambda: ddbs.list_streams())
call("dynamodbstreams.ListStreams-TableName-filter",
     lambda: ddbs.list_streams(TableName=f"probe-{uid}"))

print("\n== transcribe (PROVIDER_OVERRIDE_TRANSCRIBE=totalstack) ==")
tr = boto3.client("transcribe", endpoint_url=ENDPOINT, region_name=REGION,
                  aws_access_key_id="test", aws_secret_access_key="test")
call("transcribe.ListVocabularies", lambda: tr.list_vocabularies())
call("transcribe.GetTranscriptionJob-missing",
     lambda: tr.get_transcription_job(TranscriptionJobName=f"probe-{uid}"))
call("transcribe.ListTranscriptionJobs", lambda: tr.list_transcription_jobs())

print("\n== SUMMARY ==")
fails = [r for r in results if not r["ok"]]
print(f"{len(results) - len(fails)}/{len(results)} ops OK (no 500 / no '_w' AttributeError)")
print(json.dumps(results, indent=2, default=str))
sys.exit(1 if fails else 0)
