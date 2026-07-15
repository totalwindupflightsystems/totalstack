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
[x] CI-GAP-001 — Fix aws-sam-translator dependency conflict in pyproject.toml (moto-ext vs localstack-core) (4ac952039)
[x] CI-GAP-002 — Fix stale-bot.yml workflow (recurring 0s failures) (f81c8626c)
[x] CI-GAP-003 — Investigate AWS Build/Test/Push startup_failure (708c2c309)

## [x] Fix CI: Community Integration Tests against Pro — failing
    Fixed (d09aee0ba): Added github.repository == 'localstack/localstack' guard to test-pro and
    publish-pro-test-results jobs in tests-pro-integration.yml. Root cause: PRO_ACCESS_TOKEN secret
    not available in TotalStack fork — workflow requires it to access private localstack/localstack-pro repo.
    Also added explanatory comment to workflow file.

## [x] Fix CI: AWS Build, Test, Push — startup_failure
    Investigated (tick 2026-07-14): startup_failure is cosmetic — caused by missing secrets
    (DOCKERHUB_PULL_USERNAME, DOCKERHUB_PULL_TOKEN, TINYBIRD_CI_TOKEN) referenced in test job's
    secrets: block calling aws-tests.yml. GitHub validates secret existence at workflow parse time,
    even when job-level if: condition would skip. No runner time wasted — job guard already in place
    from CI-GAP-003 (708c2c309). Startup_failure is expected behavior for fork without these secrets.

## [x] Fix CI: upgrade-python-dependencies.yml — startup_failure (0s)
    Fixed (cc9d03b47): Added github.repository == 'localstack/localstack' guard to job.
    Uses reusable workflow from localstack/meta with PRO_ACCESS_TOKEN secret not available in fork.

## [x] Fix CI: update-cfn-resources.yml — CloudFormation resource updater fails (53742bccb)
    Added github.repository == 'localstack/localstack' guard. Requires AWS creds not available on fork.

## [x] Fix CI: rebase-release-prs.yml — hardcoded localstack/localstack references (cc8321e1e)
    Added github.repository guard on both find-release-branches and rebase jobs.
## [x] Fix CI: startup_failure — pipeline fails at startup on main branch (investigated)
    AWS / Build, Test, Push consistently shows startup_failure (0-2s). Root cause:
    missing secrets (DOCKERHUB_PULL_USERNAME, DOCKERHUB_PULL_TOKEN,
    TINYBIRD_CI_TOKEN) referenced in test job's secrets: block in aws-tests.yml.
    GitHub validates secret existence at workflow parse time even when job-level
    if: condition would skip. Cosmetic — no fix needed, expected fork behavior.

## [x] Fix CI: totalwindupflightsystems/totalstack — run #23 (stale)
    Run #23 returns HTTP 404 from gh API — likely auto-purged (GitHub retains
    runs for 90 days). Cannot investigate an expired run. If issue recurs on a
    new run, investigate then.

## [x] Fix TotalStack CI: gitreins guard secrets — binary not found (36f3fd3b5)
    Fixed: ci.yml quality job used `uv run gitreins guard secrets` but uv run
    couldn't find the gitreins binary. Changed to `uv tool install ruff gitreins`
    + `uvx gitreins guard secrets` (proper uv tool invocation).

## [x] Fix CI: aws-tests-mamr.yml and sync-labels.yml — missing repo guards (516ab26c5)
    Added github.repository == 'localstack/localstack' guard to test-ma-mr job in
    aws-tests-mamr.yml and sync-labels job in sync-labels.yml. Both reference secrets
    (DOCKERHUB_PULL_USERNAME, DOCKERHUB_PULL_TOKEN, TINYBIRD_CI_TOKEN, PRO_ACCESS_TOKEN)
    not available on TotalStack fork, causing startup_failure/failure.

## [x] Fix CI: TotalStack CI gitreins binary not found — uvx resolution fails (RESOLVED)
    uvx gitreins guard WORKS — proven in run 29428582530 (GitReins Guards: 30s, all green).
    Root cause of earlier failures was NOT uvx vs Python version — it was (1) `gitreins guard
    secrets/lint/static_analysis` using invalid positional args (guard takes no args), and
    (2) missing pytest in project venv for guard's test_command. Fix: single `uvx gitreins guard`
    step + `uv pip install pytest` in venv. No tool install needed — uvx auto-installs gitreins.
    Quality guard now passes. Test job failures (No module named pytest, Python 3.13 resolution)
    are pre-existing and unrelated.

## [x] CI — Fix integration tests + shape validator jobs: uv run recreates venv with Python 3.13 (0cad914d7)
    Fixed: Replaced all `uv run` invocations with `.venv/bin/` direct calls across all
    three jobs (quality, tests, shape-validator). Bypasses uv run's venv recreation
    which silently swaps Python 3.11 venv for Python 3.13, dropping installed deps.
    - [x] Tests job: `uv run python -m pytest` → `.venv/bin/python -m pytest`
    - [x] Shape-validator job: `uv run python development/aws-shape-validator.py` → `.venv/bin/python development/aws-shape-validator.py`
    - [x] Quality job: `uv run python -m gitreins guard` → `.venv/bin/gitreins guard`

## [x] DOC — Add uv.lock to .gitignore
    uv.lock is untracked (generated by uv sync). For a library project (not an application),
    lock files should be gitignored. Add `uv.lock` to .gitignore.
    Files: .gitignore

## [x] DOC — Fix README badges pointing to upstream localstack/localstack
    Fixed: Replaced 6 upstream localstack/localstack badges (GitHub Actions, Coveralls,
    PyPI version, Docker Pulls, PyPI downloads, PyPI license) with TotalStack CI badge
    pointing to totalwindupflightsystems/totalstack CI workflow. Kept style badges
    (Black, Ruff) and Bluesky community badge which aren't repo-specific.

## [x] CI — Fix hardcoded absolute path in test_application_autoscaling_integration.py
    Fixed (f0eaab094): 3 hardcoded /home/kara/totalstack/ paths replaced with
    __file__-relative paths using os.path.dirname(__file__) and os.path.join().
    FINDING: Tests cannot pass — application-autoscaling/ has only models.code.py
    (zero operation .code.py files). Test references 6 operations (register/deregister/
    describe scalable targets, put/describe/delete scaling policies) that were never
    generated. Pre-existing gap, not introduced by this fix. Created AUTO-SCALING-GEN.
    - [x] Replace `/home/kara/totalstack/` with `__file__`-relative paths
    - [x] Verify path resolution works (error trace confirms correct resolved path)

## [x] AUTO-SCALING-GEN — Generate missing operation .code.py files for application-autoscaling
    Done (27f024d4d): 6 thin wrappers created, 4/4 tests pass, guard PASS.
    - [x] Generate 6 operation .code.py files from AWS specs
    - [x] Verify `uv run pytest specs/aws/.speclang/assembled/_tests/test_application_autoscaling_integration.py -v` passes (4 tests)
    Files: specs/aws/.speclang/assembled/application-autoscaling/

## [ ] CI — Generate missing athena/models.code.py for integration test
    Discovery sweep 2026-07-15: test_athena_integration.py uses correct relative-path
    pattern but `athena/models.code.py` doesn't exist (only a stale .pyc from Python 3.13).
    The athena directory has 33 operation .code.py files but no store model. Need to
    generate the AthenaStore model with proper exception classes.
    - [ ] Create athena/models.code.py with AthenaStore, InvalidRequestException, ResourceNotFoundException
    - [ ] Verify `uv run pytest specs/aws/.speclang/assembled/_tests/test_athena_integration.py -v` passes
    Files: specs/aws/.speclang/assembled/athena/models.code.py

## [ ] HILO — Track .vfs/graph/edges.jsonl in git
    Discovery sweep 2026-07-15: 12,579 graph edges (2.1MB) exist but are untracked.
    Per Hilo skill: edges.jsonl is canonical graph data and must be committed for
    cross-machine sync via post-commit/merge hooks. Cache files (graph.db, graph.db.wal,
    .last_warm) are already gitignored.
    - [ ] `git add .vfs/graph/edges.jsonl .vfs/manifest.yaml`
    - [ ] Verify `git status` shows them as staged new files
    Files: .vfs/graph/edges.jsonl, .vfs/manifest.yaml