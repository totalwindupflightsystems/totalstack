---
id: "@specs/aws/frauddetector/meta"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
status: active
depends_on: []
---

# Amazon FraudDetector

Managed fraud detection with ML models, rules, and event ingestion.

## Core Entities

| Entity | Key Fields | Built |
|--------|-----------|-------|
| Detector | detectorId, eventTypeName | ✅ |
| Variable | name, dataType, dataSource, defaultValue | ✅ |
| Model | modelId, modelType, eventTypeName | ✅ |
| EventType | name, eventVariables, entityTypes | ✅ |
| Rule | ruleId, detectorId, expression, language, outcomes | ✅ |

## Tests

| Entity | Integration | E2E |
|--------|------------|-----|
| Detector | 6 tests | 1 test (skip) |
| Variable | 2 tests (crud, duplicate) | 1 test (skip) |
| Model | 2 tests (crud, duplicate) | included |
| EventType | 2 tests (crud, duplicate) | included |
| Rule | 2 tests (crud, duplicate) | included |
| Tags | 1 test (tag/untag/list) | included |
| **Total** | **15 integration** | **3 E2E** |

## Deferred
- 52 additional operations (versions, batch jobs, labels, outcomes, events, external models)
