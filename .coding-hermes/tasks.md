# TotalStack — Model Router Task Matrix

**Core purpose:** Local AWS cloud stack emulator (S3, Lambda, DynamoDB, etc.) for offline development and CI — 76 services, 1864 integration tests, Docker-based.

## Active Tasks

| ID | Task | Priority | Complexity | Deps | Tags | Model | Reasoning | Fallback |
|----|------|----------|------------|------|------|-------|-----------|----------|
| CI-GAP-064a | Fix shape validator for emr (12 errors: ClusterId/JobFlowId — need test inputs) | Medium | 3 | — | +testing | DeepSeek V4 Pro | Test input gaps for cluster/job flow prerequisite resources | GLM-5.2 |
| CI-GAP-064b | Fix shape validator for athena (13 errors: Name required, unhashable dict, missing databases attr, prepared statement) | Medium | 4 | — | ++code-generation, +testing | DeepSeek V4 Pro | Multiple distinct bug types in athena store; needs model + test_input investigation | GLM-5.2 |
| CI-GAP-064c | Fix shape validator for network-firewall (3 errors: missing FirewallPolicyName, FirewallName, RuleGroupName) | Medium | 3 | — | +testing | DeepSeek V4 Pro | Missing test inputs; no test_inputs file for n-fw | GLM-5.2 |
| CI-GAP-064d | Fix shape validator for rds (3 errors: resource not found for tag ops) | Medium | 3 | — | +testing | DeepSeek V4 Pro | Need DB instance prerequisites created in test_inputs | GLM-5.2 |
| CI-GAP-064e | Fix shape validator for organizations (1 error: account already in organization) | Medium | 2 | — | +testing | DeepSeek V4 Pro | State-ordering issue; CreateOrganization runs after other ops have created org | GLM-5.2 |
| CI-GAP-064f | Fix shape validator for fis (1 error: fuzzy-match collision — DeleteExperiment handler matched to DeleteExperimentTemplate test_input) | Low | 2 | — | +testing | DeepSeek V4 Pro | Validator fuzzy-match picks wrong handler; needs validator-level fix or handler rename | GLM-5.2 |
| CI-003 | Push 29 unpushed commits and verify CI on fork | Medium | 1 (admin) | — | +terminal | — | AGENTS.md forbids `git push` from agent; requires human/explicit override | — |
| NEVER-DONE | 11-point audit sweep | High | 2 | — | ++code-review, +testing | DeepSeek V4 Pro | Audit runs every tick | GLM-5.2 |

**Assumptions:** 1864/1864 integration tests pass locally; 70/76 services pass shape validator; 31 commits unpushed (2 new); fork CI requires manual push; AWS credential workflows disabled on fork.

**Routing Notes:** 6 sub-tasks remain for CI-GAP-064 (split from original 13-service batch). CI-GAP-064a–d are straightforward test-input additions. CI-GAP-064e (organizations) needs store reordering strategy. CI-GAP-064f (fis) needs validator fuzzy-match fix.

**Execution Order:** CI-GAP-064a → CI-GAP-064b → CI-GAP-064c → CI-GAP-064d → CI-GAP-064e → CI-GAP-064f.

**Escalation Conditions:** Any sub-task that introduces new integration test failures → escalate to CI-FIX pattern.

## Completed Summary

**CI-GAP-064 tick 1 (2026-07-21):** 7/13 services fixed (→ 70/76 pass, from 63).
- Validator: Record class injection into test_inputs module namespace (fixes codeartifact, textract, mediaconvert — 3 services, ~32 errors)
- Validator: _get_lock helper injection into test_inputs (fixes wafv2 — 11 errors)
- wafv2: TagResource/UntagResource/ListTagsForResource test_inputs (3 errors)
- personalize: SolutionRecord.__init__ recipeArn kwarg (3 errors)
- glue: CreateJob test input (1 error)
- grafana: DeleteWorkspaceServiceAccountToken tokenId nesting + response fields (1 error)
- Commits: d4bffdf87 (validator + wafv2), daa51a284 (glue, grafana, personalize, fis)

**CI-FIX (Integration Tests):** 6 fixes for amp, fsx, kafka, sesv2, verifiedpermissions, fsx regression. Shape-parity alignment (CI-FIX-011: adapted all 6 test files to AWS-correct model shapes).
**CI-GAP (Shape Validator):** 55+ services fixed earlier. Started original CI-GAP at 6/76 pass (1213 errors), now 70/76 pass.
**Infrastructure:** 74 per-service test_inputs/*.py files (QUALITY-001 refactor, 5350→400 lines). All CI workflows modernized.
**Quality:** CONTRIBUTING.md (147 lines). 1864/1864 integration tests local green.
**CI Status:** Local all green. 31 unpushed commits. Fork push events need manual trigger.

## [ ] NEVER-DONE — Run coding-hermes-never-done 11-point audit
