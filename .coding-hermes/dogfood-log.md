# TotalStack Dogfood Log

| Date | Verdict | Promise | Top findings | T2FS |
|------|---------|---------|--------------|------|
| 2026-08-11 | 🟡 PROMISING-BUT-ROUGH | "`make start` boots a full local AWS emulator on :4566; awslocal/boto3 for offline dev" | 1) venv awslocal silently leaks to real cloud when AWS_ENDPOINT_URL/AWS_PROFILE ambient (TS-GAP-015, P0); 2) all state lost on restart, undocumented (TS-GAP-016, P1); 3) S3 missing-bucket error mislabels as missing key (TS-GAP-017) | ~15-20s clean env; ~4min with ambient AWS env (leak detour) |

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
