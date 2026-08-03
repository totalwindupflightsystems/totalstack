# Verdict: BUG-003

**Task:** Fix 14 lightsail handlers with undefined local variables (NameError crashes) exposed by expanded shape-validator coverage
**Evaluated:** 2026-08-03T21:30:02.743561
**Result:** ✗ FAIL

## Pipeline Stages

- ✓ **tier1**
  -   ✓ lint: F401 [*] `importlib.util` imported but unused
 --> development/auto_wire_providers.py:6:8
  |
4 | pa
  ✓ secrets: [90m4:26PM[0m [32mINF[0m [1mscanned ~107544676 bytes (107.54 MB) in 3.81s[0m
[90m4:26PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P
- ✗ **tier2**
  - INCOMPLETE

Cap exceeded: Input token budget (1.0M) exceeded (1.0M used). Increase max_input_tokens or reduce message context.

## Summary

Judge Result: BUG-003

Stage tier1: PASS
    ✓ lint: F401 [*] `importlib.util` imported but unused
 --> development/auto_wire_providers.py:6:8
  |
4 | pa
  ✓ secrets: [90m4:26PM[0m [32mINF[0m [1mscanned ~107544676 bytes (107.54 MB) in 3.81s[0m
[90m4:26PM[0m 
  ✓ tests: ============================= test session starts ==============================
platform linux -- P

Stage tier2: FAIL
  INCOMPLETE

Cap exceeded: Input token budget (1.0M) exceeded (1.0M used). Increase max_input_tokens or reduce message context.

Overall: FAIL ✗
