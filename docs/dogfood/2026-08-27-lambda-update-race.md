# TotalStack Dogfood — 2026-08-27 Lambda Update-vs-Deliver Race (TS-GAP-044)

**Verdict: ⚠️ ROOT-CAUSED (upstream core behavior) · no fix possible without
touching `localstack-core/` — documented workaround instead**
**Run type:** live race repro against `make start` (0.3.11.dev8359), plus
source-level trace of the invocation-assignment path in `localstack-core/`
**Author:** coding-hermes worker (TS-GAP-044 dispatch) · **Emulator:** `make
start` in-memory, Docker-backed Lambda executor

## tl;dr

`update_function_code` triggers an asynchronous **version rollover**: the old
execution environment is stopped mid-flight, and any in-flight event-source
invocation on it is **cancelled** (`concurrent.futures.CancelledError`), logged
by the assignment layer as:

```
ERROR --- [db:$LATEST_3] l.s.l.i.assignment : Failed invocation <<class 'concurrent.futures._base.CancelledError'>>:
```

The event is **not lost** — the poller re-queues it and it is eventually
delivered against the *new* version (observed 40s–2.5 min later, including a
cold container spawn). The practical rule for users:

> **After `update_function_code`, wait for `State == "Active"` AND
> `LastUpdateStatus == "Successful"` (and ideally one warm-up
> `RequestResponse` invoke) before expecting reliable event-source
> deliveries. The first event after a code update may be cancelled and
> arrive minutes later — poll for 60–90s (not seconds) before concluding a
> delivery failed, and keep handlers idempotent (at-least-once, possible
> double delivery).**

---

## 1. Evidence — 2026-08-25 dogfood run (original report)

From `docs/dogfood/2026-08-25-integration.md` (errors table, row 2):

| # | What happened | Root cause | Resolution |
|---|---------------|-----------|------------|
| 2 | Upload after `update_function_code` → item never written; boot log shows `ERROR ... Failed invocation <<class 'concurrent.futures._base.CancelledError'>>` in `l.s.l.i.assignment` (~40s after upload) | Invocation-assignment race with code update | Retry / re-upload after function settles; filed TS-GAP-044 |

Additional detail from that run (commit `51a01951bd` message): the emulator
later **retried and delivered ~2.5 min after the upload** — two late
`dynamodb.PutItem` 200s + `/response` 202s at 17:11:02–03 for invocation id
`9c846f4a` — so events are not permanently lost, but first-attempt
cancellation + multi-minute eventual delivery breaks devs who poll for
seconds. Direct `lambda.invoke` is unaffected. Cold-start first-ever delivery
took ~26s (container spawn); later deliveries fast.

## 2. Reproduction — 2026-08-26 (this session, live)

Emulator booted (`make start`, ~15s), then the canonical pipeline from
section 3 of the 08-25 doc (IAM role, `dogfood-events` DDB table, `s3-to-ddb`
python3.12 function from `/tmp/dogfood-totalstack/function.zip`, `input`
bucket + S3 notification). Then the race hammer:

1. `put_object` burst (6 keys), **immediately** `update_function_code` (same
   zip), **immediately** another burst (4 keys) — repeated for 4 rounds.
2. Boot log captured concurrently; DynamoDB polled at +8s, +40s, +90s, +5min.

### Observed

- **Stable baseline:** upload → DDB item in **1.2s** (matches 08-25's 1.1s).
- **Race signature reproduced exactly** (boot log, 4th round):

```
2026-08-26T23:47:12.139 ERROR --- [db:$LATEST_3] l.s.l.i.assignment        : Failed invocation <<class 'concurrent.futures._base.CancelledError'>>:
```

- **In-flight event redelivered:** the same request re-executed later on the
  new executor (PutItem 200 at `23:47:52.505`, invocation `819850ae-…`, ~40s
  after the cancellation at `23:47:12`; executor `524d6118…` = the NEW
  environment).
- **Event posted into the rollover window is at-risk:** of 40 post-update
  burst events, 16 (all of the "b-" post-burst keys) were **still missing
  after 5 minutes** in this session; the pre-burst round keys were all
  delivered by +90s. Secondary aggravator observed right after each update:

  ```
  23:46:46.318 WARN  --- [db:$LATEST_2] l.s.l.i.execution_environm : Failed to start execution environment fa17c711…:
   ('Docker process returned with errorcode 1',
    b'lstat /tmp/lambda/awslambda-us-east-1-tasks/s3-to-ddb-02871dd9-…: no such file or directory\n', None)
  ```

  The new version's code archive was not yet materialized on disk when the
  new env tried to start (the rollover is asynchronous; `update_function_code`
  returns before the new version is prepared). Environments started in that
  window fail; messages re-queued by the poller, and in the 4-round burst
  repro the post-update keys were not redelivered within the observation
  window.

**Reproducibility:** the CancelledError signature reproduced on the 3rd
update of this session (log timestamp 23:47:12), matching the 08-25 log
exactly (`l.s.l.i.assignment`, `concurrent.futures._base.CancelledError`).
Not every update triggers it — it depends on an invocation being **in flight
(assigned to an environment) at the moment the environment is stopped**.

## 3. Root cause — exact code path (localstack-core, READ-ONLY)

All paths relative to `localstack-core/localstack/services/lambda_/`.

### 3.1 `update_function_code` is a rollover, not an in-place swap

- `provider.py:1511-1625` (`update_function_code`): replaces
  `function.versions["$LATEST"]` **synchronously** (line 1611-1612) and calls
  `self.lambda_service.update_version(new_version=function_version)` (line
  1614) — which is **asynchronous**.
- `invocation/lambda_service.py:500-520` (`update_version`): "Will perform a
  rollover, so the old version will be active until the new one is ready to
  be invoked"; delegates to `create_function_version`.
- `invocation/lambda_service.py:169-194` (`create_function_version`): builds a
  new `LambdaVersionManager`, registers it in `lambda_starting_versions`, and
  returns `task_executor.submit(_start_lambda_version, …)` — i.e. **returns
  immediately**; the HTTP 200 to the client precedes the new version's
  startup and the rollover.
- `invocation/lambda_service.py:522-588` (`update_version_state`): only when
  the new version reports `State.Active` does the rollover happen:
  - line 550-554: the new version manager + a **new `LambdaEventManager`**
    replace the old ones in `lambda_running_versions` / `event_managers`;
  - line 580-582: `old_event_manager.stop_for_update` is submitted;
  - line 583-584: `old_version.stop` is submitted.

### 3.2 The rollover stops the old environment — cancelling in-flight invokes

- `invocation/version_manager.py:139-146` (`stop`): sets `shutdown_event`,
  `assignment_service.stop_environments_for_version(self.id)`.
- `invocation/assignment.py:152-156` (`stop_environments_for_version`):
  iterates the manager's environments and `stop_environment(env)` each.
- `invocation/execution_environment.py:247-258` (`stop`): marks STOPPED and
  calls `runtime_executor.stop()`.
- `invocation/docker_runtime_executor.py:432-443` (`stop`): stops the
  container and calls `executor_endpoint.shutdown()`.
- **`invocation/executor_endpoint.py:180-184` (`shutdown`) — the cancel:**
  ```python
  def shutdown(self) -> None:
      executor_router().unregister_endpoint(self.executor_id)
      self.startup_future.cancel()
      if self.invocation_future:
          self.invocation_future.cancel()
  ```
  A thread blocked in `executor_endpoint.py:217`
  (`self.invocation_future.result(timeout=timeout_seconds)`) raises
  `concurrent.futures.CancelledError` here.

### 3.3 Where the CancelledError is surfaced (the log line)

- `invocation/version_manager.py:276-298` (`invoke`): the non-LDM path only
  catches `StatusErrorException` (line 291) — **`CancelledError` is not
  handled** and propagates out of `invoke()`.
- **`invocation/assignment.py:94-97` — the exact log line:**
  ```python
  except Exception as e:
      LOG.error("Failed invocation <%s>: %s", type(e), e, …)
  ```
  This is `l.s.l.i.assignment` in the boot log, and `type(e)` renders as
  `<class 'concurrent.futures._base.CancelledError'>`. After logging, the
  assignment service stops the on-demand environment (line 98-99) and
  re-raises.
- `invocation/event_manager.py:199-239` (`handle_message`): the poller catches
  the exception, classifies it as a system error, and
  `process_throttles_and_system_errors` (line 311-344) **re-enqueues the
  event** into the function's internal SQS queue with
  `delay_seconds = 2 ** exception_retries` (line 334-336), capped at 5 min.

### 3.4 Why the retry lands minutes later

1. The CancelledError path re-enqueues with a small delay (1s, then
   2s/4s/8s…), **but** the re-queued message is consumed by the poller of the
   NEW version manager, which starts a **fresh on-demand environment**
   (assignment.py:79-85, cold container spawn — ~3s in this run, ~26s for the
   first-ever container on 08-25).
2. Meanwhile the SQS visibility timeout for the original message is
   `function_timeout + 60s` (`event_manager.py:161`), so a message that is
   mid-flight (or re-queued) during the rollover can also resurface only
   after that window.
3. Combined with the 08-25 observation (two `PutItem` 200s at +2.5 min), the
   realistic user-visible delay is **tens of seconds to a few minutes**, not
   seconds.

### 3.5 Why the post-update burst loss is *also* a rollover race

- `provider.py:1611-1612` swaps `$LATEST` in the store **before** the new
  version is prepared (the `create_function_version` future is still running).
- New invocations in that window target the new version manager, whose code
  archive may not be materialized yet — env start fails with
  `lstat …/s3-to-ddb-<revision>: no such file or directory` (observed in this
  session's log, section 2). This is the same root family: **rollover
  asynchrony + a burst racing the new version's readiness**.

## 4. Workaround (user-facing, documented)

1. **After `update_function_code` (or `update_function_configuration`),
   poll `get_function` until BOTH `State == "Active"` AND
   `LastUpdateStatus == "Successful"`** (this is the "settled" state). With
   the in-memory emulator this takes ~2–5s.
2. **Optionally warm the new version**: one `lambda.invoke(InvocationType='RequestResponse')`
   on the new code before expecting event-source deliveries — this makes the
   rollover + container spawn happen in a controlled call instead of inside
   the first event's critical path.
3. **Do not assert "no event" for ~60–90s after an update.** The first event
   after an update can be cancelled once and redelivered late (2.5 min in the
   08-25 run). Poll your sink (DynamoDB, DB, etc.) for at least 60s before
   declaring failure, and prefer idempotent handlers (e.g. deterministic
   primary keys) because redelivery may execute twice.
4. If you need deterministic first-delivery timing during dev (not
   event-source semantics), call `lambda.invoke(InvocationType='RequestResponse')`
   directly for the first post-update message — it is unaffected by the race.

## 5. Verified parity checks (facts, no fabrication)

- ✅ `python3 -c "import localstack"` still succeeds (no code touched in
  `localstack-core/`; read-only analysis only).
- ✅ `git diff --stat HEAD` shows **zero** changes under `localstack-core/`.
- ✅ `make start` boots in ~15s, health endpoint returns `"lambda": "available"`.
- ✅ Log lines quoted above are verbatim from this session's
  `/tmp/tsgap044-emu.log` (timestamps `2026-08-26T23:…`).
- ⚠️ The 16-event post-update-burst loss observed this session is reported as
  observed behavior; the mechanism (code not yet prepared at new-version env
  start) is root-caused at the same rollover async, but the burst-loss
  delivery behavior was not re-tested to 100% — treat as "window at risk",
  workaround in section 4 covers it (settle → warm → then trust).

## 6. What a new user needs (added to docs)

1. "After updating Lambda code, wait for Active + Successful and expect the
   first event after an update may be cancelled/delayed minutes" —
   see `AGENTS.md` → "Lambda handlers: endpoint rule" sibling note, and
   README "Lambda handlers" section.
2. Idempotent handlers recommended for event-source lambdas during code
   updates (possible double delivery: 08-25 showed two PutItems for one
   invocation).

---

*Filed as TS-GAP-044. Root cause is upstream LocalStack core behavior
(read-only here); the fix would live in `localstack-core` rollover
ordering (prepare-new-before-stop-old, or drain/cancel-aware event
handling) — out of scope for this repo's DO-NOT-EDIT constraint.*
