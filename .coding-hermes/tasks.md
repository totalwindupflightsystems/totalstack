# Task Board — Totalstack

[x] INIT — Bootstrap .coding-hermes/ structure (DuckBrain namespace, GitReins tasks, Hilo .vfs/)
[x] SPEC — Audit specs vs implementation, queue gap tasks
    Findings (2026-07-12): 76 services in specs/aws/, 2,707 generated .code.py files in
    .speclang/assembled/. SERVICE-CLASSIFICATION.md covers all ~377 AWS services (19 Tier 1
    done, ~28 Tier 2 pure-API, ~7 OSS wrappers, ~30 Tier 3, ~110 Tier 4 skip).
    66 spec'd but NOT implemented, 30 implemented but NOT spec'd (core: ec2, lambda, iam, etc.)
[x] DOC — Verify documentation matches current code
    Findings (2026-07-12): AGENTS.md references non-existent paths (localstack-pro-core/,
    localstack/core/services/, localstack.pro.core.aws.api). No CodeBuild implementation
    exists. README says "archived" but this is an active TotalStack fork. make lint shows
    7208 errors. No TotalStack-specific docs exist.
[x] CI — Check CI pipeline health, fix failing jobs
    Findings (2026-07-12): TotalStack CI failing — dependency conflict aws-sam-translator
    (moto-ext wants <=1.103.0, localstack-core wants >=1.105.0) + Python 3.13 vs 3.14.
    AWS Build/Test/Push: startup_failure. Community Integration Tests: failure.
    stale-bot.yml: recurring 0s failures (infra). Sync Labels: failure (infra).
    Only Validate Codeowners passes.
[x] SPEC-GAP-001 — Generate specs for ec2 (LocalStack has provider, zero specs)
    Done (2026-07-12): 756 .spec.py.md files generated via aws-spec-to-speclang.py
[x] SPEC-GAP-002 — Generate specs for lambda (LocalStack has provider, zero specs)
    Done (2026-07-12): 85 .spec.py.md files generated via aws-spec-to-speclang.py
[x] SPEC-GAP-003 — Generate specs for iam (LocalStack has provider, zero specs)
    Done (2026-07-12): 168 .spec.py.md files generated (fixed KeyError for no-input ops)
[x] SPEC-GAP-004 — Generate specs for cloudformation (LocalStack has provider, zero specs)
    Done (2026-07-12): 90 .spec.py.md files generated via aws-spec-to-speclang.py
[x] SPEC-GAP-005 — Generate specs for sts (LocalStack has provider, zero specs)
    Done (2026-07-12): 11 .spec.py.md files generated via aws-spec-to-speclang.py
[x] DOC-GAP-001 — Fix AGENTS.md paths: localstack-pro-core/ → totalstack/, all service paths (fb38b5932)
[x] DOC-GAP-002 — Replace CodeBuild reference with ACM, fix Pipes→ACM test refs (fb38b5932)
[x] DOC-GAP-003 — Update README.md to reflect TotalStack fork (remove "archived" status) (44b9cfaca)
[x] DOC-GAP-004 — Add TotalStack-specific docs explaining the spec→code pipeline (f8933448e)
[ ] CI-GAP-001 — Fix aws-sam-translator dependency conflict in pyproject.toml (moto-ext vs localstack-core)
[ ] CI-GAP-002 — Fix stale-bot.yml workflow (recurring 0s failures)
[ ] CI-GAP-003 — Investigate AWS Build/Test/Push startup_failure
