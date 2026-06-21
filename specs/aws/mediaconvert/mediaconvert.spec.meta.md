---
id: "@specs/aws/mediaconvert"
version: 1.0.0
target_lang: meta
owned-by: specwriter
status: active
---

# AWS Elemental MediaConvert — TotalStack Emulator

## Why (Service Overview)

AWS Elemental MediaConvert is a file-based video transcoding service with
broadcast-grade features. It converts media files from one format to another,
supporting a vast range of input and output formats.

## Architecture

MediaConvert is organized around four primary resources:

### Jobs
A transcoding job takes an input file, applies settings (codec, resolution, etc.),
and produces output files. Jobs have a lifecycle: SUBMITTED → PROGRESSING → COMPLETE/ERROR/CANCELED.
Each job runs in a specific queue.

### Job Templates
Reusable transcoding settings. A template specifies input/output groups, codecs,
containers, and advanced features. Jobs can reference a template instead of
specifying all settings inline.

### Presets
System-defined or custom output settings. Presets encode specific format
combinations (e.g., "MP4 1080p H.264 5Mbps").

### Queues
Processing queues that control job concurrency, priority, and pricing plan
(ON_DEMAND or RESERVED).

## Resource Relationships

```
Queue ← Job (runs in)
JobTemplate ← Job (can reference)
Preset → Output settings (referenced by Job/JobTemplate Settings)
Tags → Any resource (ARN-based)
```

## Operations

34 AWS API operations total. This build covers 22 core CRUD operations:
- Jobs: Create, Get, List, Cancel
- Job Templates: Create, Get, List, Update, Delete
- Presets: Create, Get, List, Update, Delete
- Queues: Create, Get, List, Update, Delete
- Tags: Tag, Untag, List

Deferred (12 ops): SearchJobs, StartJobsQuery, GetJobsQueryResults,
AssociateCertificate, DisassociateCertificate, CreateResourceShare,
PutPolicy, GetPolicy, DeletePolicy, DescribeEndpoints, ListVersions, Probe.

## Error Model

- InvalidParameterException — bad request / validation error
- ResourceNotFoundException — resource does not exist
- ConflictException — resource already exists or state conflict
- TooManyRequestsException — rate limit
- InternalServerException — unexpected error