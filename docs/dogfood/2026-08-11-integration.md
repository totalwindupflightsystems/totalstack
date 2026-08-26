# TotalStack Dogfood — 2026-08-11 Integration Report

**Verdict: 🟡 PROMISING-BUT-ROUGH** · **Run type:** real use (emulator as a user would use it)
**Tester:** coding-hermes dogfood cron · **Emulator:** `make start` in-memory mode, `0.3.11.dev8259`

## Promise (null hypothesis)

> "TotalStack is a fully functional local AWS cloud stack... `make start` boots the
> emulator in-memory (no Docker required) on `http://localhost:4566`; use `awslocal`
> (installed by `make install-test`) or boto3 to develop and test AWS applications
> locally, offline, without real AWS."

## Reality in one paragraph

The emulator itself **works impressively well**: cold boot to healthy in ~14s,
S3/SQS/DynamoDB/Lambda/CloudFormation all functioned end-to-end with correct
responses. But the **documented quickstart path (`awslocal` from the venv) silently
routes requests to whatever `AWS_ENDPOINT_URL` is set in your environment** — the
first command of this run leaked to a real Hetzner S3 endpoint (`hel1.your-objectstorage.com`)
and returned Hetzner error XML. And **all state vanishes on restart** with no
documentation warning. Both are safety/usability blockers for exactly the target
audience (AWS developers, who virtually always have AWS env vars set).

## The working integration (what to do)

### 1. Boot (no Docker, ~15s)

```bash
cd /home/kara/totalstack
make start          # or: source .venv/bin/activate && python3 -m localstack.runtime.main
curl -s localhost:4566/_localstack/health   # {"services": {...}, ...} all "available"
```

### 2. CRITICAL: sanitize the environment BEFORE using awslocal

The venv `awslocal` honors ambient AWS variables over its localhost default:

```bash
# A machine with AWS_ENDPOINT_URL / AWS_PROFILE set (typical for AWS devs)
# will silently route awslocal traffic to a REAL cloud. Fix:
unset AWS_ENDPOINT_URL AWS_ENDPOINT_URL_* AWS_PROFILE AWS_DEFAULT_PROFILE
# or use the repo wrapper (warns + unsets endpoint vars, but crashes on dangling profiles):
./scripts/awslocal sqs list-queues
```

Never run `.venv/bin/awslocal` with `AWS_ENDPOINT_URL` set — verify with
`env | grep ^AWS` first.

### 3. Real workflows that worked (all verified 2026-08-11)

```bash
export PATH="$PWD/.venv/bin:$PATH"; unset AWS_ENDPOINT_URL AWS_PROFILE AWS_DEFAULT_REGION AWS_REGION

# SQS — create/send/receive
awslocal sqs create-queue --queue-name my-queue --region us-east-1
awslocal sqs send-message --queue-url <QURL> --message-body '{"hi":"there"}' --region us-east-1
awslocal sqs receive-message --queue-url <QURL> --region us-east-1

# S3 — full object roundtrip + presigned URL (works, signature valid)
awslocal s3 mb s3://my-bucket --region us-east-1
awslocal s3 cp ./file.txt s3://my-bucket/notes/ --region us-east-1
awslocal s3 presign s3://my-bucket/notes/file.txt --region us-east-1   # curl the URL → object content

# DynamoDB
awslocal dynamodb create-table --table-name t --attribute-definitions AttributeName=pk,AttributeType=S \
  --key-schema AttributeName=pk,KeyType=HASH --billing-mode PAY_PER_REQUEST --region us-east-1
awslocal dynamodb put-item --table-name t --item '{"pk":{"S":"u1"}}' --region us-east-1
awslocal dynamodb get-item --table-name t --key '{"pk":{"S":"u1"}}' --region us-east-1

# Lambda — create → wait Active → invoke (cold start ~5s)
awslocal lambda create-function --function-name fn --runtime python3.12 \
  --role arn:aws:iam::000000000000:role/dev --handler handler.handler \
  --zip-file fileb://function.zip --region us-east-1
# NOTE: invoke immediately after create fails with ResourceConflictException
# "function is currently in the following state: Pending" — poll get-function until Active.
awslocal lambda invoke --function-name fn --payload '{"a":1}' out.json --region us-east-1

# CloudFormation — deploy a stack (works; ~30s)
awslocal cloudformation deploy --stack-name st --template-file stack.yaml --region us-east-1
```

boto3 works identically: point `endpoint_url='http://localhost:4566'` (use any
access key id/secret, e.g. `test`/`test`; region us-east-1). No auth validation.

> **Caveat (2026-08-25):** the `localhost:4566` convention above applies to
> code running OUTSIDE Lambda containers. Inside a Lambda handler the emulator
> is reached via the injected `AWS_ENDPOINT_URL` (docker bridge gateway) —
> `localhost:4566` does not resolve there, and hardcoding it fails with a
> hidden `EndpointConnectionError` (invoke returns HTTP 200). Use
> `os.environ["AWS_ENDPOINT_URL"]` or plain boto3 with no `endpoint_url`. See
> [2026-08-25-integration.md](2026-08-25-integration.md) for the full walkthrough.

### 4. Pitfalls hit (and their workarounds)

| # | Pitfall | Workaround |
|---|---------|------------|
| 1 | `awslocal` leaks to real cloud when `AWS_ENDPOINT_URL`/`AWS_PROFILE` ambient (P0, TS-GAP-015) | unset AWS vars; never trust bare venv awslocal |
| 2 | All state lost on restart — S3/SQS/DDB/Lambda/CFN gone (P1, TS-GAP-016) | treat `make start` as ephemeral; recreate state after restart |
| 3 | Lambda invoke right after create → `Pending` ResourceConflictException | poll `get-function` State until `Active` (~1-3s) |
| 4 | `scripts/awslocal` wrapper crashes with `ProfileNotFound` when `AWS_PROFILE` is dangling | unset AWS_PROFILE yourself, or use clean env |
| 5 | S3 missing-bucket error says `Key "key" does not exist` instead of NoSuchBucket (P2, TS-GAP-017) | read the bucket name from your own command; error is misleading |
| 6 | Boot log prints ERROR (DNS needs root port 53) + cbor2 WARN before `Ready.` (P2, TS-GAP-018) | ignore; emulator is fine once `Ready.` appears |
| 7 | Plain `aws` CLI needs credentials (only awslocal injects test creds) | use awslocal, or `aws configure` with dummy keys + `--endpoint-url` |

## Time-to-first-success & friction count

- **T2FS (clean env): ~15-20s** — 14.3s cold boot to healthy + first command.
- **T2FS (ambient AWS env, the common case): ~4 minutes** — first command leaked to
  real cloud, required diagnosis + env sanitization. This is the single biggest
  usability hit.
- **Friction count: 7** (table above). 2 are P0/P1 blockers, 2 cosmetic, 3 minor.

## Would I use it again?

Yes — for offline smoke-testing of AWS plumbing it's genuinely pleasant: boot is
fast, no Docker, CFN works, Lambda runs. But ONLY after sanitizing the environment,
and with the expectation that state is disposable. The traffic-leak footgun must be
fixed before recommending it to anyone whose machine has AWS credentials configured.

## What a new user needs that isn't documented

1. A loud warning that venv `awslocal` can route to real cloud (README note exists
   but the quickstart still installs the unsafe path — TS-GAP-015).
2. An explicit "state is lost on restart" persistence section (TS-GAP-016).
3. The Lambda Active-state polling pattern (minor).
