---
id: "@specs/aws/mediaconvert/plan"
version: 1.0.0
target_lang: plan
owned-by: specwriter
status: active
depends_on:
  - "@specs/aws/mediaconvert"
---

# MediaConvert — Implementation Plan

## Phase 1: Core CRUD (22 operations)

### Jobs (4 ops)
- CreateJob — validate Settings + Role, generate ID, store record
- GetJob — lookup by ID, return full Job object
- ListJobs — paginated listing with optional filters (Queue, Status)
- CancelJob — set status to CANCELED

### Job Templates (5 ops)
- CreateJobTemplate — validate Settings + Name, store
- GetJobTemplate — lookup by Name
- ListJobTemplates — paginated listing with optional Category, ListOrder
- UpdateJobTemplate — validate exists, replace fields
- DeleteJobTemplate — remove from store

### Presets (5 ops)
- CreatePreset — validate Settings + Name, store
- GetPreset — lookup by Name
- ListPresets — paginated listing with optional Category, ListOrder
- UpdatePreset — validate exists, replace fields
- DeletePreset — remove from store

### Queues (5 ops)
- CreateQueue — validate Name, store with defaults
- GetQueue — lookup by Name
- ListQueues — paginated listing with optional ListOrder
- UpdateQueue — validate exists, replace fields
- DeleteQueue — remove from store

### Tags (3 ops, multi-handler)
- TagResource — add tags to resource ARN
- UntagResource — remove specific tag keys
- ListTagsForResource — return tags for given ARN

## Pagination

All List operations support:
- MaxResults (default 20, max 100)
- NextToken (opaque string for subsequent pages)
- Optional filters per operation

## Protocol

MediaConvert uses REST JSON protocol (service-2.json). Operations expect
JSON request bodies and return JSON responses.

## Store Design

Single MediaConvertStore with dict-backed collections:
- self.jobs: job_id → JobRecord
- self.job_templates: name → JobTemplateRecord
- self.presets: name → PresetRecord
- self.queues: name → QueueRecord
- self.tags: arn → {key: value}