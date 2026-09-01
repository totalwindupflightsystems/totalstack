
## Dogfood Findings (2026-09-01)
Verdict: SHIPPABLE
Promise: {"entry_point":"HTTP server: the emulator itself, booted via `make start` (in-memory, no Docker required) on http://localhost:4566, consumed through the bundled `awslocal` CLI wrapper or boto3 pointed at the local endpoint; there is no pip-installable package and no published Docker image — the supp

- [P1] Ambient ~/.aws/config region silently breaks awslocal s3 mb, contradicting the README's 'safe by default' claim — On a machine with region=hel1 (Hetzner) in ~/.aws/config, `awslocal s3 mb` failed with InvalidLocationConstraint because the config-file region is sent as CreateBucket LocationConstraint. The prefligh
- [P2] Boot log scrolls ERROR-level 501s that read as a broken startup — make start emits ERROR-level lines ('Sorry, the personalize/quicksight/rds/servicecatalog/amp service is not supported... upgrade to the latest stable version / license') for unsupported/license-gated
- [P2] Lambda invoke immediately after create-function returns ResourceConflictException (Pending state) — correct AWS semantics but undocumented for creates — Invoke right after create failed with 'function is currently in the following state: Pending'; recovers in ~4s and the headline Lambda claim held (create Pending→Active, invoke StatusCode 200 with cor
- [P2] 'No Docker required' is ambiguous about Lambda's runtime container — README says the emulator needs no Docker (true for the core services), but a Lambda execution in in-memory mode still needs Docker for the runtime container. A user could reasonably read 'no Docker re
