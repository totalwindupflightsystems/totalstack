
## Dogfood Findings (2026-09-01)
Verdict: SHIPPABLE
Promise: {"entry_point":"HTTP server: the emulator itself, booted via `make start` (in-memory, no Docker required) on http://localhost:4566, consumed through the bundled `awslocal` CLI wrapper or boto3 pointed at the local endpoint; there is no pip-installable package and no published Docker image — the supp

- [P1] Ambient ~/.aws/config region silently breaks awslocal s3 mb, contradicting the README's 'safe by default' claim — On a machine with region=hel1 (Hetzner) in ~/.aws/config, `awslocal s3 mb` failed with InvalidLocationConstraint because the config-file region is sent as CreateBucket LocationConstraint. The prefligh
- [P2] Boot log scrolls ERROR-level 501s that read as a broken startup — make start emits ERROR-level lines ('Sorry, the personalize/quicksight/rds/servicecatalog/amp service is not supported... upgrade to the latest stable version / license') for unsupported/license-gated
- [P2] Lambda invoke immediately after create-function returns ResourceConflictException (Pending state) — correct AWS semantics but undocumented for creates — Invoke right after create failed with 'function is currently in the following state: Pending'; recovers in ~4s and the headline Lambda claim held (create Pending→Active, invoke StatusCode 200 with cor
- [P2] 'No Docker required' is ambiguous about Lambda's runtime container — README says the emulator needs no Docker (true for the core services), but a Lambda execution in in-memory mode still needs Docker for the runtime container. A user could reasonably read 'no Docker re

## Dogfood Findings (2026-09-04)
Verdict: PROMISING-BUT-ROUGH
Promise: {"entry_point":"HTTP server on localhost:4566 (in-memory via `make start`, or Docker via DOCKER.md workflow), plus `awslocal` CLI wrapper for interacting with the emulator","promise":"TotalStack claims a user can develop and test AWS applications locally without connecting to a remote cloud provider

- [P1] make lint and make format fail without undocumented make install-dev — Both make lint and make format (listed in the promise run_commands) exit with 'ruff is not installed - run make install-dev first'. AGENTS.md documents this prereq but the README run-command list does
- [P2] 36 services available at boot, not 69 as claimed — Health endpoint returns 36 services as 'available'. The 69 count refers to service provider files in totalstack/services/*/provider.py (verified: 69 files exist), but many are partial/Moto-fallback an
- [P2] Ambient AWS region from ~/.aws/config causes confusing S3 errors — If user has a non-us-east-1 region in ~/.aws/config, awslocal s3 mb fails with 'InvalidLocationConstraint' (server logs the region reset warning). The awslocal wrapper neutralizes AWS_ENDPOINT_URL/AWS
- [P2] Boot log spams ERROR-level 501s for unsupported services — make start outputs 'Sorry, the personalize/quicksight/servicecatalog/amp service is not supported' and 'rds service is not included within your LocalStack license' during boot. These are benign health
- [P2] Real-use report works:false contradicts live verification — The harness reported works:false with friction_count:7 and truncated data (inner JSON was unparsed). Independent verification: server boots in ~8s, SQS/S3 work verbatim, 21252/21253 tests pass. The ha
