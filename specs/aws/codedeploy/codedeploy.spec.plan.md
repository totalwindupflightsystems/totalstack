---
id: "@spec/aws/codedeploy/plan"
version: 1.0.0
target_lang: plan
owned-by: codegen
status: active
depends_on:
  - "@spec/aws/codedeploy/meta"
---

# CodeDeploy — Implementation Plan

## Phase 1: Core Store & Models
- `models.code.py`: Store classes, data classes, exception classes
- Exceptions: `InvalidApplicationNameException`, `ApplicationDoesNotExistException`, `ApplicationAlreadyExistsException`, `ApplicationNameRequiredException`, `InvalidInputException`, `DeploymentGroupDoesNotExistException`, `DeploymentGroupAlreadyExistsException`, `DeploymentConfigDoesNotExistException`, `DeploymentConfigAlreadyExistsException`, `DeploymentDoesNotExistException`, `DeploymentLimitExceededException`, `InvalidDeploymentConfigNameException`, `InvalidRoleException`, `InvalidDeploymentGroupNameException`, `DeploymentGroupNameRequiredException`, `InvalidRevisionException`, `RevisionDoesNotExistException`, `DeploymentAlreadyCompletedException`, `DeploymentIdRequiredException`, `InvalidDeploymentIdException`, `InvalidNextTokenException`, `ThrottlingException`, `ResourceNotFoundException` (generic)

## Phase 2: Application Management
- `CreateApplication.code.py`: validate name → store → return applicationId
- `GetApplication.code.py`: lookup by name → return application info
- `UpdateApplication.code.py`: validate → lookup → update → return
- `DeleteApplication.code.py`: validate → lookup → delete
- `ListApplications.code.py`: paginated listing
- `BatchGetApplications.code.py`: lookup by names → return list

## Phase 3: DeploymentConfig Management
- `CreateDeploymentConfig.code.py`: validate → store → return
- `GetDeploymentConfig.code.py`: lookup by name → return
- `DeleteDeploymentConfig.code.py`: validate → delete
- `ListDeploymentConfigs.code.py`: paginated listing

## Phase 4: DeploymentGroup Management
- `CreateDeploymentGroup.code.py`: validate → store → return
- `GetDeploymentGroup.code.py`: lookup → return
- `UpdateDeploymentGroup.code.py`: validate → lookup → update
- `DeleteDeploymentGroup.code.py`: validate → delete
- `ListDeploymentGroups.code.py`: paginated listing by application

## Phase 5: Deployment Lifecycle
- `CreateDeployment.code.py`: validate → create deployment record → return deploymentId
- `GetDeployment.code.py`: lookup by ID → return deployment info
- `StopDeployment.code.py`: validate status → stop → return
- `ListDeployments.code.py`: paginated listing with filters

## Phase 6: Remaining Entities (future)
- Application Revisions, On-Premises Instances, Tags, GitHub tokens

## Store Design

### ApplicationStore
```python
{
    "app-name": {
        "applicationName": "app-name",
        "applicationId": "uuid",
        "computePlatform": "Server",
        "createTime": timestamp,
        "linkedToGitHub": false
    }
}
```

### DeploymentConfigStore
```python
{
    "config-name": {
        "deploymentConfigName": "config-name",
        "deploymentConfigId": "uuid",
        "minimumHealthyHosts": {"type": "HOST_COUNT", "value": 1},
        "computePlatform": "Server",
        "createTime": timestamp
    }
}
```

### DeploymentGroupStore
```python
# defaultdict(dict) — keyed by applicationName then deploymentGroupName
{
    "app-name": {
        "group-name": {
            "applicationName": "app-name",
            "deploymentGroupName": "group-name",
            "deploymentGroupId": "uuid",
            "serviceRoleArn": "arn:...",
            ...
        }
    }
}
```

### DeploymentStore
```python
{
    "d-XXXXXXXX": {
        "deploymentId": "d-XXXXXXXX",
        "applicationName": "app-name",
        "deploymentGroupName": "group-name",
        "status": "InProgress",
        "createTime": timestamp,
        ...
    }
}
```

## Key Patterns

### ARN Construction
```
arn:aws:codedeploy:{region}:{account}:application/{name}
arn:aws:codedeploy:{region}:{account}:deploymentgroup/{app}/{group}
arn:aws:codedeploy:{region}:{account}:deploymentconfig/{name}
```

### Pagination
- `nextToken`: opaque pagination token (base64-encoded index key)
- Default page size: 100

### Deployment Status State Machine
```
Created → Queued → InProgress → Succeeded
                              → Failed
                              → Stopped
                              → Ready (for blue/green)
```
