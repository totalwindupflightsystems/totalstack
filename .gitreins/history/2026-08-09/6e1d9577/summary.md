# Verdict: ts-gap-011

**Task:** Bootstrap pip into project venv (TS-GAP-011)
**Evaluated:** 2026-08-09T23:54:58.848587
**Result:** ✗ FAIL

## Pipeline Stages

- ✗ **tier1**
  -   ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m6:53PM[0m [32mINF[0m [1mscanned ~107678678 bytes (107.68 MB) in 9.68s[0m
[90m6:53PM[0m 
  ✗ tests: ============================= test session starts ==============================
platform linux -- P
- ✓ **tier2**
  - COMPLETE
  ✓ make venv succeeds on a pip-less venv: .venv/bin/pip3 exists: Makefile:30 recipe now runs `$(VENV_DIR)/bin/python -m ensurepip --upgrade` before pip install. Tested exact recipe on a pip-less venv (python3 -m venv --without-pip): ensurepip bootstrapped pip and .venv/bin/pip3 exists afterward. `make -n venv` dry-run confirms recipe wired correctly.
  ✓ python -m pip --version succeeds in the activated venv: After running the recipe on a pip-less venv and activating it, `python -m pip --version` succeeded outputting 'pip 26.2.1 from .../site-packages/pip (python 3.11)'. ensurepip installs pip into the venv so python -m pip works.
The Makefile venv recipe now bootstraps pip via ensurepip, verified by executing the exact recipe on a pip-less venv: .venv/bin/pip3 is created and python -m pip --version succeeds in the activated venv.

## Summary

Judge Result: ts-gap-011

Stage tier1: FAIL
    ✓ lint: F841 Local variable `errors` is assigned to but never used
   --> development/aws-spec-to-speclang.p
  ✓ secrets: [90m6:53PM[0m [32mINF[0m [1mscanned ~107678678 bytes (107.68 MB) in 9.68s[0m
[90m6:53PM[0m 
  ✗ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: PASS
  COMPLETE
  ✓ make venv succeeds on a pip-less venv: .venv/bin/pip3 exists: Makefile:30 recipe now runs `$(VENV_DIR)/bin/python -m ensurepip --upgrade` before pip install. Tested exact recipe on a pip-less venv (python3 -m venv --without-pip): ensurepip bootstrapped pip and .venv/bin/pip3 exists afterward. `make -n venv` dry-run confirms recipe wired correctly.
  ✓ python -m pip --version succeeds in the activated venv: After running the recipe on a pip-less venv and activating it, `python -m pip --version` succeeded outputting 'pip 26.2.1 from .../site-packages/pip (python 3.11)'. ensurepip installs pip into the venv so python -m pip works.
The Makefile venv recipe now bootstraps pip via ensurepip, verified by executing the exact recipe on a pip-less venv: .venv/bin/pip3 is created and python -m pip --version succeeds in the activated venv.

Overall: FAIL ✗
