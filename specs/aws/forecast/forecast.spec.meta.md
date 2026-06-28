---
id: "@specs/aws/forecast/meta"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
status: active
depends_on: []
---

# Amazon Forecast — Time-Series Forecasting Service

Fully managed deep learning service for time-series forecasting. Uses ARN-based resource
identification (no AwsAccountId in request payloads).

## Core Entities

| Entity | Key ARN Pattern | Built |
|--------|----------------|-------|
| Dataset | dataset/{name} | ✅ |
| Forecast | forecast/{name} | ✅ |
| Predictor | predictor/{name} | ✅ |

## Tests

| Entity | Integration | E2E |
|--------|------------|-----|
| Dataset | 6 tests | 1 test (skip) |
| Forecast | 6 tests | 1 test (skip) |
| Predictor | 6 tests | 1 test (skip) |
| Tags | 4 tests | included |
| **Total** | **22 integration** | **4 E2E** |

## Deferred (future pass)
- 48 additional operations (DatasetGroup, DatasetImportJob, Explainability, Monitor,
  WhatIfAnalysis, AutoPredictor, export jobs, backtest, etc.)
- Update operations (Forecast has UpdateDatasetGroup only — no UpdateDataset/UpdateForecast)
