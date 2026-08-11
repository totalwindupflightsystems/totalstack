---
name: totalstack-usage
description: >-
  How to actually USE the TotalStack local AWS emulator (a LocalStack fork):
  boot it, talk to it with awslocal/boto3, avoid the environment-variable
  traffic leak, and know that state is ephemeral. Load this before doing
  anything with totalstack — the naive quickstart path can send requests to a
  REAL cloud endpoint.
version: 1.0.0
category: software-development
---

# TotalStack Usage — Field-Tested Guide

TotalStack is a fork of LocalStack: a local AWS emulator (S3, SQS, DynamoDB,
Lambda, CloudFormation, IAM, EC2, and more) running in-memory on
`http://localhost:4566` — no Docker required via `make start`.

Dogfood-verified 2026-08-11: S3, SQS, DynamoDB, Lambda (python3.12), and
CloudFormation all work end-to-end. See `docs/dogfood/2026-08-11-integration.md`
for the full evidence trail.

## Entry points

| What | How |
|---|---|
| Boot emulator | `make start` (repo root) — or `source .venv/bin/activate && python3 -m localstack.runtime.main` |
| Health check | `curl -s localhost:4566/_localstack/health` |
| CLI | `.venv/bin/awslocal` (installed by `make install-test`) |
| SDK | boto3 with `endpoint_url='http://localhost:4566'`, any dummy creds, `region_name='us-east-1'` |
| Docker mode | `DOCKER.md` (volume-mounted, has persistence via `./volume:/var/lib/localstack`) |

## ⚠️ RULE 1 — sanitize AWS env vars BEFORE any awslocal call (P0)

The venv `awslocal` defaults to localhost **but ambient `AWS_ENDPOINT_URL`,
`AWS_ENDPOINT_URL_<SERVICE>`, or `AWS_PROFILE` silently override that** — verified:
with `AWS_ENDPOINT_URL=https://hel1.your-objectstorage.com` set, `awslocal sqs
create-queue` hit a real Hetzner S3 endpoint (returned Hetzner error XML). This is
a real-cloud traffic leak. Always:

```bash
unset AWS_ENDPOINT_URL AWS_ENDPOINT_URL_* AWS_PROFILE AWS_DEFAULT_PROFILE AWS_DEFAULT_REGION AWS_REGION
# or verify: env | grep ^AWS  → should print nothing
```

The repo wrapper `./scripts/awslocal` warns and unsets endpoint vars, but does NOT
unset `AWS_PROFILE` — with a dangling profile it crashes with `ProfileNotFound`.
Clean env is the reliable path. (Board: TS-GAP-015.)

## ⚠️ RULE 2 — state is EPHEMERAL (P1)

`make start` is in-memory: **every resource vanishes on restart** (verified:
S3 buckets, SQS queues, DynamoDB tables, Lambda functions, CFN stacks all gone
after restart). There is no PERSISTENCE support in the fork. Plan to recreate
state, or use the Docker/volume workflow for anything you need to keep.
(Board: TS-GAP-016.)

## The right-way patterns

```bash
# Boot + verify
make start &
curl -s localhost:4566/_localstack/health | python3 -m json.tool

# S3 object roundtrip (works, incl. presigned URLs)
awslocal s3 mb s3://bucket --region us-east-1
awslocal s3 cp f.txt s3://bucket/ --region us-east-1
awslocal s3 cp s3://bucket/f.txt out.txt --region us-east-1

# Lambda: ALWAYS poll for Active before invoking
awslocal lambda create-function --function-name fn --runtime python3.12 \
  --role arn:aws:iam::000000000000:role/dev --handler handler.handler \
  --zip-file fileb://function.zip --region us-east-1
awslocal lambda get-function --function-name fn --region us-east-1   # wait for State=Active
awslocal lambda invoke --function-name fn --payload '{}' out.json --region us-east-1

# CloudFormation (works, ~30s deploy)
awslocal cloudformation deploy --stack-name st --template-file stack.yaml --region us-east-1
```

## Common pitfalls (all hit in real use)

1. **Traffic leak** — see RULE 1. Symptom: urllib3 `InsecureRequestWarning` about a
   non-local host, or error XML mentioning a real provider. Board TS-GAP-015.
2. **Lambda `ResourceConflictException: ... state: Pending`** right after create —
   normal; poll `get-function` until `State: Active` (1-3s). Do NOT treat as failure.
3. **State gone after restart** — see RULE 2. Board TS-GAP-016.
4. **S3 missing-bucket error lies** — `Key "key" does not exist` for a missing
   *bucket* (should be NoSuchBucket). Trust your own command, not the message.
   Board TS-GAP-017.
5. **Boot log noise** — `ERROR ... cannot run command as root ... dns.server -p 53`
   and `WARN cbor2 patching disabled` before `Ready.` are harmless (DNS needs root
   for port 53). Board TS-GAP-018.
6. **Plain `aws` CLI** needs configured credentials — awslocal injects test creds;
   with `aws` use `--endpoint-url http://localhost:4566` + dummy `aws configure`.
7. **`--region` flag**: pass `--region us-east-1` explicitly; without it awslocal
   falls back to ambient region config.

## Verification cheatsheet (did it work?)

- `curl -s localhost:4566/_localstack/health` → all services "available"
- S3 presigned URL fetch returns the object bytes
- `awslocal cloudformation describe-stacks` → `CREATE_COMPLETE` and outputs resolve
- Lambda invoke returns `StatusCode: 200` with the handler's JSON in the output file

## Board & process

- Board: `.coding-hermes/board/tasks.jsonl` (JSONL is canonical; board.db is a
  gitignored cache). Tasks: `TS-GAP-<NNN>`.
- Foreman ticks run idle-maintenance audits; gates: test suite (1865 tests), ACM
  parity (7/7), validator (76/76), guard (5/5).
- Dogfood trail: `docs/dogfood/` (integration report + diagnostics).
