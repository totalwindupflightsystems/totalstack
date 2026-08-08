# Verdict: TS-GAP-009

**Task:** awslocal CLI missing from documented setup
**Evaluated:** 2026-08-08T20:07:21.890755
**Result:** ✓ PASS

## Pipeline Stages

- ✓ **tier1**
  -   ✓ secrets: /bin/sh: 1: gitleaks: not found
Traceback (most recent call last):
  File "<string>", line 1, in <mo
  ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ pyproject.toml [test] extras include awscli-local>=0.22.2 (provides the awslocal binary): pyproject.toml:127 has "awscli-local>=0.22.2" in the [test] extras section, with line 126 comment confirming the awslocal CLI binary is required by tests
  ✓ README.md Quickstart documents that make install-test installs the awslocal CLI into the venv: README.md Quickstart (lines 94-108) documents that `make install-test` installs the awslocal CLI (from the awscli-local package) into the project venv, usable via .venv/bin/awslocal
  ✓ .venv/bin/awslocal --version exits 0 and reports the aws-cli version: .venv/bin/awslocal --version exits 0 and reports 'aws-cli/1.44.49 Python/3.13.13 Linux/7.0.0-28-generic awscrt/0.31.2 botocore/1.42.59'
All three criteria for TS-GAP-009 are satisfied: awscli-local>=0.22.2 is in [test] extras, README Quickstart documents make install-test installing awslocal into the venv, and .venv/bin/awslocal --version exits 0 reporting the aws-cli version.

## Summary

Judge Result: TS-GAP-009

Stage tier1: PASS
    ✓ secrets: /bin/sh: 1: gitleaks: not found
Traceback (most recent call last):
  File "<string>", line 1, in <mo
  ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ pyproject.toml [test] extras include awscli-local>=0.22.2 (provides the awslocal binary): pyproject.toml:127 has "awscli-local>=0.22.2" in the [test] extras section, with line 126 comment confirming the awslocal CLI binary is required by tests
  ✓ README.md Quickstart documents that make install-test installs the awslocal CLI into the venv: README.md Quickstart (lines 94-108) documents that `make install-test` installs the awslocal CLI (from the awscli-local package) into the project venv, usable via .venv/bin/awslocal
  ✓ .venv/bin/awslocal --version exits 0 and reports the aws-cli version: .venv/bin/awslocal --version exits 0 and reports 'aws-cli/1.44.49 Python/3.13.13 Linux/7.0.0-28-generic awscrt/0.31.2 botocore/1.42.59'
All three criteria for TS-GAP-009 are satisfied: awscli-local>=0.22.2 is in [test] extras, README Quickstart documents make install-test installing awslocal into the venv, and .venv/bin/awslocal --version exits 0 reporting the aws-cli version.

Overall: PASS ✓
