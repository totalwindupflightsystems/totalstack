# TotalStack Dogfood Log

| Date | Verdict | Promise | Top findings | T2FS |
|------|---------|---------|--------------|------|
| 2026-08-11 | 🟡 PROMISING-BUT-ROUGH | "`make start` boots a full local AWS emulator on :4566; awslocal/boto3 for offline dev" | 1) venv awslocal silently leaks to real cloud when AWS_ENDPOINT_URL/AWS_PROFILE ambient (TS-GAP-015, P0); 2) all state lost on restart, undocumented (TS-GAP-016, P1); 3) S3 missing-bucket error mislabels as missing key (TS-GAP-017) | ~15-20s clean env; ~4min with ambient AWS env (leak detour) |
| 2026-08-25 | 🟡 PROMISING-BUT-ROUGH | "run your AWS applications or Lambdas entirely on your local machine" — event-driven app (S3→Lambda→DynamoDB, SNS→SQS) | 1) Lambda handlers hardcoding localhost:4566 fail inside container — use injected AWS_ENDPOINT_URL (TS-GAP-043, P1); 2) S3 event dropped/cancelled after update_function_code (TS-GAP-044, P1); 3) dup create_bucket returns 200 not BucketAlreadyOwnedByYou (TS-GAP-045, P2) | ~20s quickstart; ~6min event-driven app with naive handler (localhost trap); 1.1s pipeline once correct |

## 2026-08-11 — first dogfood run

- **What was used:** `make start` (in-memory, no Docker); awslocal + boto3 + plain
  aws CLI; S3 (bucket/put/get/presign roundtrip), SQS (create/send/receive),
  DynamoDB (table/put/get), Lambda (create/invoke, python3.12), CloudFormation
  (stack deploy), error paths, restart-survival test.
- **Promise held:** emulator boots in 14.3s and S3/SQS/DDB/Lambda/CFN all work.
- **Promise broke:** documented quickstart `awslocal` routes to real cloud
  (hel1.your-objectstorage.com) when ambient AWS env vars exist; state is lost on
  restart with no warning.
- **Tasks written:** TS-GAP-015 (P0 env leak), TS-GAP-016 (P1 persistence docs),
  TS-GAP-017 (P2 S3 error parity), TS-GAP-018 (P2 boot noise), TS-GAP-019 (P2
  board sync tooling).
- **Knowledge left:** `docs/dogfood/2026-08-11-integration.md`,
  `docs/dogfood/diagnostics.md`, `skills/totalstack-usage/SKILL.md`.
- **Foreman:** not paused (cooldown 7200s < 14400s) — no wake needed; tasks will
  be picked up on the next normal tick.

## 2026-08-25 — second dogfood run (event-driven deep run)

- **What was used:** `make start` (in-memory); boto3 (SDK path); built a real
  event-driven app: IAM role → DynamoDB table → Lambda (python3.12) → S3 bucket
  notification → upload → DDB item (**1.1s** roundtrip); SNS→SQS fanout;
  Lambda logs via `logs` API; error paths (missing fn/bucket, dup bucket);
  re-verified TS-GAP-015/016 fixes live (wrapper safe with ambient AWS env;
  ephemeral-state boot banner present).
- **Promise held:** event-driven apps run end-to-end; SNS→SQS; logs; IAM.
- **Promise broke/rough:** naive handler (localhost:4566 per docs) fails inside
  the Lambda container (EndpointConnectionError — TS-GAP-043); S3 event
  cancelled after update_function_code (CancelledError — TS-GAP-044); dup
  create_bucket 200 vs BucketAlreadyOwnedByYou (TS-GAP-045); missing-bucket
  still not NoSuchBucket (TS-GAP-017 re-verified: now bare 404).
- **Tasks written:** TS-GAP-043 (P1), TS-GAP-044 (P1), TS-GAP-045 (P2) +
  TS-GAP-017 evidence note.
- **Knowledge left:** `docs/dogfood/2026-08-25-integration.md`, diagnostics
  addendum in `docs/dogfood/diagnostics.md`, `skills/totalstack-usage/SKILL.md`
  v1.1.0 (RULE 3 + RULE 4 + event-driven patterns).
- **Foreman:** not woken — cooldown 21600s is the documented operator pin
  (stand-in cycles G5 wake SKIP); 3 tasks added for next tick.
