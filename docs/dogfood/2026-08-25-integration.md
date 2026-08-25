# TotalStack Dogfood — 2026-08-25 Integration Report

**Verdict: 🟡 PROMISING-BUT-ROUGH** · **Run type:** real use — event-driven serverless app
**Tester:** coding-hermes dogfood cron · **Emulator:** `make start` in-memory, `0.3.11.dev8359`

## Promise (null hypothesis)

> "With TotalStack, you can run your AWS applications or Lambdas entirely on
> your local machine" (README) — i.e. a realistic **multi-service event-driven
> app** (IAM → DynamoDB → Lambda → S3 event notification → object upload → item
> written) should work end-to-end against `make start`.

## Reality in one paragraph

**The promise holds — with two sharp edges.** The full S3→Lambda→DynamoDB
pipeline works: upload → event → Lambda execution (130ms) → DDB item in
**1.1 seconds**. SNS→SQS fanout works. IAM role creation works. Lambda logs
come back through the `logs` API with real START/END/REPORT lines. But: (1) a
handler written the *naive documented way* — boto3 pointed at
`http://localhost:4566`, as every README snippet teaches — **fails inside the
Lambda container** with a confusing `EndpointConnectionError`, because inside
the container the emulator is at the docker bridge gateway, reachable via the
injected `AWS_ENDPOINT_URL` env var; and (2) an upload fired immediately after
`update_function_code` had its invocation **cancelled** (`CancelledError` in
the lambda assignment layer, visible only in the boot log).

## The working integration (what to do)

### 1. Boot (same as before — ~15s, no Docker)

```bash
cd /home/kara/totalstack && make start
curl -s localhost:4566/_localstack/health   # services "available"
```

### 2. Sanitize the host env for awslocal (TS-GAP-015 fix VERIFIED)

With `AWS_ENDPOINT_URL`/`AWS_PROFILE` set, the venv wrapper now warns and
forces localhost (no more real-cloud leak):

```
$ .venv/bin/awslocal sqs list-queues --region us-east-1
totalstack: warning: AWS_ENDPOINT_URL is set (https://hel1.your-objectstorage.com) — unsetting it ...
totalstack: warning: requests will be sent to http://localhost:4566 (the TotalStack emulator edge)
```

boto3: always pass `endpoint_url='http://localhost:4566'` explicitly (or unset
the ambient vars). Dummy creds + `us-east-1` work.

### 3. THE canonical event-driven app (S3 → Lambda → DynamoDB) — verified working

```python
import boto3, json, time

def c(svc): return boto3.client(svc, endpoint_url="http://localhost:4566",
                                region_name="us-east-1",
                                aws_access_key_id="test", aws_secret_access_key="test")

iam = c("iam")
role = iam.create_role(RoleName="app-role", AssumeRolePolicyDocument=json.dumps({
    "Version": "2012-10-17", "Statement": [{"Effect": "Allow",
    "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}))["Role"]["Arn"]

ddb = c("dynamodb")
ddb.create_table(TableName="events", KeySchema=[{"AttributeName": "pk", "KeyType": "HASH"}],
    AttributeDefinitions=[{"AttributeName": "pk", "AttributeType": "S"}], BillingMode="PAY_PER_REQUEST")

lam = c("lambda")
lam.create_function(FunctionName="s3-to-ddb", Runtime="python3.12", Role=role,
    Handler="handler.handler", Code={"ZipFile": open("function.zip", "rb").read()}, Timeout=30)
# poll get_function until State == "Active" (1-3s) before any invoke/event

s3 = c("s3")
s3.create_bucket(Bucket="input")
s3.put_bucket_notification_configuration(Bucket="input", NotificationConfiguration={
    "LambdaFunctionConfigurations": [{"LambdaFunctionArn": "<fn arn>", "Events": ["s3:ObjectCreated:*"]}]})

s3.put_object(Bucket="input", Key="k.json", Body=b'{"a":1}')
# poll DynamoDB get_item → item appears in ~1.1s
```

**The handler — THIS IS THE TRAP.** Inside the Lambda container,
`localhost:4566` does not resolve. The runtime injects
`AWS_ENDPOINT_URL=http://172.17.0.1:4566` (the docker bridge gateway), so:

```python
# ✅ RIGHT — use the injected endpoint (or omit endpoint_url entirely):
import os, boto3
ddb = boto3.resource("dynamodb", endpoint_url=os.environ["AWS_ENDPOINT_URL"], region_name="us-east-1")
# or simply: boto3.resource("dynamodb", region_name="us-east-1")  # env injection handles it

# ❌ WRONG — this fails with EndpointConnectionError inside the container:
ddb = boto3.resource("dynamodb", endpoint_url="http://localhost:4566", region_name="us-east-1")
```

Symptom of the wrong way: `lambda.invoke` returns HTTP 200 whose payload is
`{"errorMessage": "Could not connect to the endpoint URL: \"http://localhost:4566/\"", "errorType": "EndpointConnectionError", ...}`.
(Board: TS-GAP-043.)

### 4. SNS → SQS fanout (verified, ~2s)

```python
topic = c("sns").create_topic(Name="t")["TopicArn"]
q = c("sqs").create_queue(QueueName="q")["QueueUrl"]
qarn = c("sqs").get_queue_attributes(QueueUrl=q, AttributeNames=["QueueArn"])["Attributes"]["QueueArn"]
c("sns").subscribe(TopicArn=topic, Protocol="sqs", Endpoint=qarn)
c("sns").publish(TopicArn=topic, Message="hi")
# sqs.receive_message → Notification envelope with MessageId/TopicArn
```

### 5. Lambda logs (verified)

```python
c("logs").describe_log_streams(logGroupName="/aws/lambda/<fn>", orderBy="LastEventTime", descending=True)
c("logs").get_log_events(logGroupName="/aws/lambda/<fn>", logStreamName=<stream>)
# → START / EVENT: {...} / END / REPORT ... Duration: 130.89 ms
```

## Errors hit in real use (and the real story)

| # | What happened | Root cause | Resolution |
|---|---------------|-----------|------------|
| 1 | Handler `EndpointConnectionError: http://localhost:4566/` | localhost doesn't exist inside the Lambda container; injected endpoint is `AWS_ENDPOINT_URL` (gateway IP) | Use `os.environ["AWS_ENDPOINT_URL"]` or omit endpoint_url (TS-GAP-043) |
| 2 | Upload after `update_function_code` → item never written; boot log shows `ERROR ... Failed invocation <<class 'concurrent.futures._base.CancelledError'>>` in `l.s.l.i.assignment` (~40s after upload) | Invocation-assignment race with code update | Retry / re-upload after function settles; filed TS-GAP-044 |
| 3 | First-ever S3-event delivery took ~26s to reach the function | Cold path (container spawn + assignment) | Subsequent deliveries are fast (1.1s) |
| 4 | `s3.head_object` on missing bucket → bare `404 Not Found` (was `Key "key" does not exist` on 08-11) | Upstream-core S3 provider; NoSuchBucket mapping blocked (TS-GAP-017) | Read the bucket name from your own command |
| 5 | `create_bucket` twice → HTTP 200, silent success (AWS raises `BucketAlreadyOwnedByYou`) | S3 provider/Moto semantics | Filed TS-GAP-045 |

## Time-to-first-success & friction count

- **T2FS (quickstart path): ~20s** — boot 15s + first `awslocal` command (wrapper safe now).
- **T2FS (event-driven app, naive handler): ~6 min** — two failed attempts + log
  diagnosis; the localhost trap cost ~5 min. With the right pattern: ~1 min.
- **Friction count: 5** (2 P1 — endpoint trap, CancelledError flake; 2 P2 parity
  errors; 1 minor cold-start). The P0 env-leak from the 08-11 run is **fixed** —
  zero friction this run.

## Would I use it again?

Yes — and this run proves the flagship claim: a real event-driven app runs
locally end-to-end in ~1s. The remaining P1s are (a) a docs gap that costs
first-timers ~5 minutes and (b) a flake on the update-then-upload path that
event-driven dev workflows hit constantly. Both are fixable; neither blocks
the core value.

## What a new user needs that isn't documented

1. The in-Lambda endpoint rule (TS-GAP-043) — the single highest-value doc fix.
2. "After updating Lambda code, wait for Active and expect the first event may
   be dropped/cancelled" (TS-GAP-044).
3. Duplicate `create_bucket` silently succeeds (TS-GAP-045).
