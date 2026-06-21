---
id: "@spec/aws/codebuild/meta"
version: 1.0.0
target_lang: meta
owned-by: codegen
status: active
---

# AWS CodeBuild — Service Overview

## What is CodeBuild?

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages ready for deployment. It eliminates the need to provision, manage, and scale build servers.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  CodeBuild                       │
│                                                  │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐    │
│  │ Projects │   │  Builds  │   │  Fleets  │    │
│  │ (config) │──▶│(workload)│   │(compute) │    │
│  └──────────┘   └──────────┘   └──────────┘    │
│        │              │               │          │
│        ▼              ▼               ▼          │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐    │
│  │Webhooks  │   │  Reports │   │Sandboxes │    │
│  │(trigger) │   │(results) │   │(interactive)│  │
│  └──────────┘   └──────────┘   └──────────┘    │
└─────────────────────────────────────────────────┘
```

## Core Entities

1. **Project** — Build configuration: source location, environment, buildspec, artifacts, IAM role
2. **Build** — A single execution of a build project. Lifecycle: QUEUED→PROVISIONING→IN_PROGRESS→SUCCEEDED/FAILED
3. **Fleet** — Managed compute fleet (EC2 instances) for running builds
4. **Sandbox** — Interactive development environment for debugging builds
5. **Report Group** — Container for build/test reports
6. **Webhook** — Git-based trigger that starts builds on code changes
7. **Source Credentials** — OAuth tokens for GitHub/Bitbucket access

## Protocol

JSON-based protocol (AWS JSON 1.1). All operations are POST to `/`.

## Key Operations (59 total)

### Project Management (CRUD)
- CreateProject, UpdateProject, DeleteProject
- BatchGetProjects, ListProjects
- ListSharedProjects, UpdateProjectVisibility

### Build Lifecycle
- StartBuild, StopBuild, RetryBuild
- BatchGetBuilds, BatchDeleteBuilds
- ListBuilds, ListBuildsForProject
- InvalidateProjectCache

### Build Batches
- StartBuildBatch, StopBuildBatch, RetryBuildBatch
- BatchGetBuildBatches, DeleteBuildBatch
- ListBuildBatches, ListBuildBatchesForProject

### Fleets
- CreateFleet, UpdateFleet, DeleteFleet
- BatchGetFleets, ListFleets

### Sandboxes
- StartSandbox, StopSandbox, StartSandboxConnection
- BatchGetSandboxes, ListSandboxes, ListSandboxesForProject
- ListCommandExecutionsForSandbox, StartCommandExecution, BatchGetCommandExecutions

### Reports & Report Groups
- CreateReportGroup, UpdateReportGroup, DeleteReportGroup
- BatchGetReportGroups, ListReportGroups, ListReportsForReportGroup
- BatchGetReports, ListReports
- DescribeCodeCoverages, DescribeTestCases, GetReportGroupTrend

### Webhooks
- CreateWebhook, DeleteWebhook, UpdateWebhook

### Source Credentials
- ImportSourceCredentials, DeleteSourceCredentials, ListSourceCredentials

### Resource Policy
- PutResourcePolicy, DeleteResourcePolicy, GetResourcePolicy

### Reference
- ListCuratedEnvironmentImages

## Error Model

| Exception | HTTP | Meaning |
|-----------|------|---------|
| InvalidInputException | 400 | Malformed request or invalid field |
| ResourceNotFoundException | 404 | Project/Build/Fleet not found |
| ResourceAlreadyExistsException | 409 | Duplicate name |
| AccountLimitExceededException | 400 | Project/build quota reached |
| OAuthProviderException | 400 | OAuth token issue |

## Implementation Strategy

This is a greenfield service — no LocalStack provider exists. We build from scratch:
1. In-memory Store classes with dict backing
2. Handler functions per operation following AWS API contracts
3. Forward-compatible with future emulator backend integration
