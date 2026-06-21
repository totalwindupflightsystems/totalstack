---
id: "@spec/aws/codebuild/plan"
version: 1.0.0
target_lang: plan
owned-by: codegen
status: active
depends_on:
  - "@spec/aws/codebuild/meta"
---

# CodeBuild — Implementation Plan

## Phase 1: Core Store & Models
- `models.code.py`: Store classes, data classes, exception classes
- Exceptions: `InvalidInputException`, `ResourceNotFoundException`, `ResourceAlreadyExistsException`, `AccountLimitExceededException`, `OAuthProviderException`

## Phase 2: Project Management
- `CreateProject.code.py`: validate → store → return project
- `UpdateProject.code.py`: validate → lookup → update → return
- `DeleteProject.code.py`: validate → lookup → delete
- `BatchGetProjects.code.py`: lookup by names → return list
- `ListProjects.code.py`: paginated listing with sort/filter

## Phase 3: Build Lifecycle
- `StartBuild.code.py`: validate → create build record → return
- `StopBuild.code.py`: lookup → transition state → return
- `RetryBuild.code.py`: lookup → create new build → return
- `BatchGetBuilds.code.py`: lookup by IDs → return list
- `BatchDeleteBuilds.code.py`: lookup → delete → return
- `ListBuilds.code.py`: paginated listing
- `ListBuildsForProject.code.py`: paginated listing filtered by project

## Phase 4: Remaining Entities (future)
- Fleets, Sandboxes, ReportGroups, Reports, Webhooks
- SourceCredentials, ResourcePolicy

## Store Design

### ProjectStore
```python
{
    "project-name": {
        "name": "project-name",
        "arn": "arn:aws:codebuild:...",
        "source": {...},
        "environment": {...},
        "serviceRole": "...",
        "created": timestamp,
        ...
    }
}
```

### BuildStore
```python
{
    "build-id": {
        "id": "build-id",
        "arn": "arn:aws:codebuild:...",
        "projectName": "project-name",
        "buildStatus": "IN_PROGRESS",
        "startTime": timestamp,
        ...
    }
}
```

### AccountDefaults
```python
{
    "defaultAwsAccountId": "123456789012",
    "defaultRegion": "us-east-1",
}
```

## Key Patterns

### ARN Construction
```
arn:aws:codebuild:{region}:{account}:project/{name}
arn:aws:codebuild:{region}:{account}:build/{id}
arn:aws:codebuild:{region}:{account}:report-group/{name}
arn:aws:codebuild:{region}:{account}:fleet/{name}
```

### Pagination
- `sortOrder`: ASCENDING | DESCENDING
- `nextToken`: opaque pagination token
- Default `maxResults`: 100

### Build Status State Machine
```
QUEUED → PROVISIONING → IN_PROGRESS → SUCCEEDED
                                    → FAILED
                                    → STOPPED
                                    → FAULT
                                    → TIMED_OUT
```
