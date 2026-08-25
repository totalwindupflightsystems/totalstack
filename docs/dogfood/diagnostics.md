# TotalStack Diagnostics — How It's Built, What Breaks, The Right Way

Dogfood diagnostic trail · 2026-08-11 · verdict 🟡 PROMISING-BUT-ROUGH
This is explanation, not raw logs. For the run evidence, see
`docs/dogfood/2026-08-11-integration.md`.

## What TotalStack is and how it's built

- **A fork of LocalStack** (upstream core vendored in `localstack-core/`, never
  edited) with a custom service layer in `totalstack/services/<svc>/provider.py`.
- **Spec-driven**: `specs/aws/` API specs are generated from AWS botocore service
  models; providers are registered in `totalstack/providers.py` with Moto fallbacks
  for services without full implementations.
- **In-memory edge runtime**: `make start` runs `python3 -m localstack.runtime.main`
  directly (no Docker, no volume) on port 4566. State lives in process memory
  (per-service stores) — hence zero persistence across restarts by design.
- **Service implementation pattern** (reference: ACM): `@handler` decorators,
  `get_store(context)` state management, service-specific exceptions from the
  auto-generated API modules, `short_uid()` IDs, ARN helpers.
- **Parity workflow**: tests recorded against real AWS (`TEST_TARGET=AWS_CLOUD
  SNAPSHOT_UPDATE=1`), snapshot/validation JSON files are generated — never edited
  by hand; plain `assert` is banned in validated tests, `snapshot.match()` is used.
- **Foreman process**: a scheduler-driven agent ticks every 7200s (170 ticks so
  far, mostly idle-maintenance audits; gates = test suite 1865 tests, ACM parity
  7/7, spec validator 76/76, guard 5/5). Board: `.coding-hermes/board/` (JSONL
  canonical per Bane directive 2026-08-07; board.db is a gitignored DuckDB cache).

## Errors hit during the dogfood run (and the right way)

### 1. "awslocal leaked to a real cloud endpoint" (P0 — TS-GAP-015)

**Symptom:** first command of the run — `awslocal sqs create-queue --queue-name
dogfood-queue` — returned Hetzner Object Storage XML errors
(`LocationConstraintConflict`, `NoSuchBucket`) and urllib3 printed `Unverified
HTTPS request to host 'hel1.your-objectstorage.com'`. No emulator was contacted.

**Why:** awscli-local's `awslocal` defaults to `http://localhost:4566`, but
botocore's ambient config wins: `AWS_ENDPOINT_URL` (set machine-wide on this host)
redirects the endpoint; `AWS_PROFILE` supplies credentials/endpoint config.
TotalStack's own README (L109-116) documents this risk and points at
`scripts/awslocal`, a wrapper that unsets `AWS_ENDPOINT_URL*` and warns — added by
TS-GAP-014 (2026-08-09). But: (a) the wrapper is NOT the installed quickstart path
(`make install-test` installs the plain awslocal into `.venv/bin/`), and (b) the
wrapper warns about `AWS_PROFILE` but does not unset it, so with a dangling
profile (e.g. `ls-sandbox` absent from `~/.aws/config`) it dies with
`botocore.exceptions.ProfileNotFound` instead of forcing local.

**Right way:** unset `AWS_ENDPOINT_URL*` + `AWS_PROFILE*` before any awslocal call
in this environment. Never assume the default is safe. Fix tracked as TS-GAP-015
(fix = wire wrapper into the venv install, unset profiles too, verify with a
dead-port endpoint test that no traffic leaves the machine).

### 2. "Everything is gone after restart" (P1 — TS-GAP-016)

**Symptom:** after `pkill` + restart, `list-tables`, `list-functions`,
`list-queues`, `s3 ls` all empty.

**Why:** in-memory runtime, no persistence layer (no PERSISTENCE/DATA_DIR support
in the fork's constants), no volume. By design — but undocumented: README says
"in-memory" once in a parenthetical; no Persistence section exists. A user who
builds demo state and restarts loses everything silently.

**Right way:** treat `make start` as ephemeral. For durable state use the Docker
workflow (`docker-compose.yml` volume `./volume:/var/lib/localstack`). Fix =
document it (TS-GAP-016).

### 3. "Lambda invoke: ResourceConflictException, state Pending" (minor)

**Symptom:** invoke immediately after create-function fails with "The operation
cannot be performed at this time. The function is currently in the following
state: Pending".

**Why:** function activation is async; first `get-function` poll showed Active
within ~1s; invoke then succeeded (200, correct payload echo, ~5s cold start).

**Right way:** poll `get-function` until `State: Active` before invoking. Not a
bug — but the docs don't mention it, so it reads like one (noted in integration
report).

### 4. "S3 missing bucket says missing key" (P2 — TS-GAP-017)

**Symptom:** `awslocal s3 cp s3://no-such-bucket-xyz/key /tmp/x` → 404
`HeadObject: Key "key" does not exist`. Real AWS returns `NoSuchBucket: The
specified bucket does not exist`.

**Why:** the S3 provider maps the 404 to a key-level error without checking
bucket existence first (parity drift vs botocore behavior).

**Right way:** fix via the parity process — record AWS behavior with
`TEST_TARGET=AWS_CLOUD SNAPSHOT_UPDATE=1`, then map missing-bucket 404s to
NoSuchBucket. Task: TS-GAP-017.

### 5. Boot noise: DNS + cbor2 (P2 — TS-GAP-018)

**Symptom:** every `make start` prints `ERROR ... cannot run command as root
(cannot get sudo password from non-tty input): sudo -n ... dns.server -p 53`,
then `WARN DNS server did not come up within 5 seconds`, then `WARN cbor2 patching
disabled`.

**Why:** the DNS service tries to bind port 53 (needs root/sudo) and the cbor2
patch is incompatible with cbor2 >= 5.5.0 (Kinesis CBOR datetime may use seconds
instead of ms). Both are harmless for normal use; the emulator reaches `Ready.`
right after.

**Right way:** ignore, or fix by skipping DNS when not root + downgrading the
warnings (TS-GAP-018).

### 6. Board write-path warts (P2 — TS-GAP-019)

**Symptom:** `create_board_tasks.py` appended tasks to the JSONL mirror but
skipped board.db ("no UNIQUE/PRIMARY KEY constraints... specify ON CONFLICT
columns manually"); the canonical resync `sync_tasks_jsonl_to_db.py` crashed with
`Could not convert string 'low' to INT8` (legacy row JSONL-NORM-001 has
`"complexity": "low"` as a string; schema declares TINYINT).

**Why:** board.db is a DuckDB cache whose schema drifted from the JSONL data; the
sync script doesn't coerce legacy values.

**Right way:** JSONL is authoritative (per board convention) so the foreman sees
the tasks; heal the DB by coercing complexity in the sync script (TS-GAP-019).

## The "right way" summary for this repo

1. **Environment first**: `unset AWS_ENDPOINT_URL AWS_ENDPOINT_URL_* AWS_PROFILE
   AWS_DEFAULT_PROFILE` before awslocal — P0 safety rule on this machine.
2. **Boot**: `make start`, health at `/_localstack/health`, ~15s cold.
3. **State**: ephemeral. Recreate after every restart.
4. **Lambda**: poll Active before invoke.
5. **Changes**: never hand-edit snapshot/validation JSON; run parity tests against
   AWS first; use fixtures; commit with the `Co-authored-by: Alexis Okuwa
   <wojonstech@gmail.com>` trailer used by the foreman.
6. **Board**: tasks live in `.coding-hermes/board/tasks.jsonl` (JSONL canonical);
   add via `create_board_tasks.py` with the board venv python.

## Known-good numbers (this run)

- Cold boot to healthy: **14.3s** · first successful command: ~15-20s clean env
- CFN stack deploy: ~33s to CREATE_COMPLETE · Lambda cold invoke: ~5s
- Test suite (foreman gate): 1865 passed / 0 failed / 208 skipped @ ~86-108s
- Verdict: core value real, usability blocked by env-leak footgun + ephemeral state

---

# 2026-08-25 dogfood — event-driven deep run (addendum)

Second dogfood run; this time the **event-driven path** (the README's flagship
"run your AWS applications or Lambdas" claim). Verdict: 🟡 PROMISING-BUT-ROUGH.

## How the Lambda execution path is wired (learned by probing)

- `make start` (in-memory) runs the edge on `localhost:4566`; Lambda functions
  execute in **Docker containers** (this machine's bridge network), NOT in the
  emulator process. The container reaches the emulator at the docker bridge
  gateway IP: `172.17.0.1` (log: `Determined main container target IP:
  172.17.0.1` at container spawn).
- The runtime injects `AWS_ENDPOINT_URL=http://172.17.0.1:4566` plus
  container-credentials env (`AWS_CONTAINER_CREDENTIALS_FULL_URI`,
  `AWS_LAMBDA_RUNTIME_API`) — verified by an env-dump probe Lambda. Plain
  boto3 (no explicit endpoint_url) works inside the container **because** of
  that injection.
- **The trap**: every repo doc teaches `endpoint_url='http://localhost:4566'`
  (correct for host-side clients). A handler that copies that pattern gets
  `EndpointConnectionError` inside the container, and `lambda.invoke` returns
  **HTTP 200 with the error buried in the payload** — so the failure is easy to
  miss. File: TS-GAP-043 (docs fix: teach `AWS_ENDPOINT_URL`/plain boto3 for
  handlers).
- **S3 event delivery**: `put_bucket_notification_configuration` with
  `LambdaFunctionConfigurations` works; uploads trigger container spawn +
  invocation. Stable-function roundtrip upload→DDB item: **1.1s**. First-ever
  delivery after function creation was slow (~26s).
- **Known flake**: upload immediately after `update_function_code` →
  `ERROR ... Failed invocation <<class 'concurrent.futures._base.CancelledError'>>`
  in `l.s.l.i.assignment` (lambda invocation-assignment layer); item never
  written; only visible in the boot log. Direct invoke unaffected. Filed
  TS-GAP-044 — suspicion: assignment/executor race when the function revision
  changes while an event-source delivery is queued.

## Error-path findings (AWS-parity checks)

- Missing function invoke → correct `ResourceNotFoundException` with AWS-shaped
  message. ✅
- Missing S3 bucket `head_object` → bare `404 Not Found` (08-11: misleading
  `Key "key" does not exist`; now just vague). Still not `NoSuchBucket` —
  TS-GAP-017, blocked because the S3 provider lives in vendored
  `localstack-core/` (AGENTS.md DO-NOT-EDIT).
- Duplicate `create_bucket` → **HTTP 200 silent success**; AWS raises
  `BucketAlreadyOwnedByYou` (400). New: TS-GAP-045.

## What held vs. broke (promise ledger)

| Promise | Result |
|---|---|
| Boot in ~15s, no Docker, health endpoint | ✅ held (14-15s) |
| awslocal quickstart safe with ambient AWS env (TS-GAP-015) | ✅ FIXED — wrapper warns + forces localhost (verified with live ambient env) |
| Ephemeral-state warning (TS-GAP-016) | ✅ FIXED — boot banner + README Persistence section |
| S3/SQS/DDB/Lambda/CFN basics | ✅ held (as 08-11) |
| S3→Lambda→DDB event-driven app | ✅ held with correct handler (1.1s) — ❌ first try fails via localhost trap |
| SNS→SQS fanout | ✅ held (~2s) |
| Lambda logs via `logs` API | ✅ held (START/END/REPORT) |
| IAM role + policy | ✅ held (Moto-backed) |
| Error parity (NoSuchBucket, BucketAlreadyOwnedByYou) | ❌ still off (TS-GAP-017, TS-GAP-045) |

## Known-good numbers (this run)

- Cold boot → healthy: ~15s · S3→Lambda→DDB roundtrip (warm): **1.1s**
- SNS→SQS publish→receive: ~2s · Lambda execution: ~130ms (128MB)
- Emulator: `0.3.11.dev8359`
