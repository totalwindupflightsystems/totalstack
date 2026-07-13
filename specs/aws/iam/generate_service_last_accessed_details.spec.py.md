---
id: "@specs/aws/iam/generate_service_last_accessed_details"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GenerateServiceLastAccessedDetails"
---

# GenerateServiceLastAccessedDetails

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/generate_service_last_accessed_details
> **spec:implements:** @kind:operation GenerateServiceLastAccessedDetails
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GenerateServiceLastAccessedDetails.spec.md

Generates a report that includes details about when an IAM resource (user, group, role, or policy) was last used in an attempt to access Amazon Web Services services. Recent activity usually appears within four hours. IAM reports activity for at least the last 400 days, or less if your Region began supporting this feature within the last year. For more information, see Regions where data is tracked . For more information about services and actions for which action last accessed information is displayed, see IAM action last accessed information services and actions . The service last accessed data includes all attempts to access an Amazon Web Services API, not just the successful ones. This includes all attempts that were made using the Amazon Web Services Management Console, the Amazon Web Services API through any of the SDKs, or any of the command line tools. An unexpected entry in the service last accessed data does not mean that your account has been compromised, because the request might have been denied. Refer to your CloudTrail logs as the authoritative source for information about all API calls and whether they were successful or denied access. For more information, see Logging IAM events with CloudTrail in the IAM User Guide . The GenerateServiceLastAccessedDetails operation returns a JobId . Use this parameter in the following operations to retrieve the following details from your report: GetServiceLastAccessedDetails – Use this operation for users, groups, roles, or policies to list every Amazon Web Services service that the resource could access using permissions policies. For each service, the response includes information about the most recent access attempt. The JobId returned by GenerateServiceLastAccessedDetail must be used by the same role within a session, or by the same user when used to call GetServiceLastAccessedDetail . GetServiceLastAccessedDetailsWithEntities – Use this operation for groups and policies to list information about the associated entities (users or roles) that attempted to access a specific Amazon Web Services service. To check the status of the GenerateServiceLastAccessedDetails request, use the JobId parameter in the same operations and test the JobStatus response parameter. For additional information about the permissions policies that allow an identity (user, group, or role) to access specific services, use the ListPoliciesGrantingServiceAccess operation. Service last accessed data does not use other policy types when determining whether a resource could access a service. These other policy types include resource-based policies, access control lists, Organizations policies, IAM permissions boundaries, and STS assume role policies. It only applies permissions policy logic. For more about the evaluation of policy types, see Evaluating policies in the IAM User Guide . For more information about service and action last accessed data, see Reducing permissions using service last accessed data in the IAM User Guide .

## Input Shape: GenerateServiceLastAccessedDetailsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Arn | Any  # complex shape | ✓ | The ARN of the IAM resource (user, group, role, or managed policy) used to generate information about when the resource  |
| Granularity | Any  # complex shape |  | The level of detail that you want to generate. You can specify whether you want to generate information about the last a |

## Output Shape: GenerateServiceLastAccessedDetailsResponse

- **JobId** (Any  # complex shape): The JobId that you can use in the GetServiceLastAccessedDetails or GetServiceLastAccessedDetailsWithEntities operations.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def generate_service_last_accessed_details(store, request: dict) -> dict:
    """Generates a report that includes details about when an IAM resource (user, group, role, or policy) was last used in an attempt to access Amazon Web Services services. Recent activity usually appears w"""
    arn = request.get("Arn", "").strip() if isinstance(request.get("Arn"), str) else request.get("Arn")
    if not arn:
        raise ValidationException("Arn is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("GenerateServiceLastAccessedDetails", request)
```
