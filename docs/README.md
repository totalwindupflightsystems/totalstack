# TotalStack Developer Documentation

Welcome to the TotalStack developer documentation.

## Quick Start

If you are a developer working **on** TotalStack (implementing services,
writing parity tests, or working with the spec → code pipeline), start with
the repository root [AGENTS.md](../AGENTS.md). It is the canonical guide for:

- The **spec → code pipeline**: AWS API specs in `specs/aws/` are assembled
  by Speclang into provider implementations in `totalstack/services/`.
- The **ACM reference implementation** (`totalstack/services/acm/provider.py`
  + `tests/aws/services/acm/test_acm.py`) — the canonical example to copy
  when adding a new service or test.
- **Hard constraints**: never edit `*.snapshot.json` / `*.validation.json`,
  never create AWS resources directly in test bodies, never modify generated
  API specs.
- **Test commands**: `pytest`, `make lint`, `make format`, and running
  snapshot tests against real AWS with `TEST_TARGET=AWS_CLOUD`.

If you are a user running TotalStack locally, see [../README.md](../README.md)
and [../DOCKER.md](../DOCKER.md).

## Upstream LocalStack Guides

The remaining files and directories in `docs/` are inherited from upstream
LocalStack and cover its architecture and concepts:

- [localstack-concepts](localstack-concepts/) — LocalStack architecture and
  core concepts
- [testing](testing/) — upstream testing guide
- [development-environment-setup](development-environment-setup/) — upstream
  dev environment setup
- [CONTRIBUTING.md](CONTRIBUTING.md) — upstream contribution guide
- [end_user_license_agreement](end_user_license_agreement/) — EULA

> Note: the upstream guides describe LocalStack itself. For TotalStack-specific
> conventions and the spec-driven development workflow, always read
> [../AGENTS.md](../AGENTS.md) first.
