---
id: "@specs/aws/datasync/docs/managing-access-overview"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Access management"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Access management

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/managing-access-overview
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Access management for AWS DataSync
<a name="managing-access-overview"></a>

Every AWS resource is owned by an AWS account. Permissions to create or access a resource are governed by permissions policies. An account administrator can attach permissions policies to AWS Identity and Access Management (IAM) identities. Some services (such as AWS Lambda) also support attaching permissions policies to resources.

**Note**  
An *account administrator* is a user with administrator privileges in an AWS account. For more information, see [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

**Topics**
+ [DataSync resources and operations](#access-control-specify-datasync-actions)
+ [Understanding resource ownership](#access-control-owner)
+ [Managing access to resources](#access-control-managing-permissions)
+ [Specifying policy elements: Actions, effects, resources, and principals](#policy-elements)
+ [Specifying conditions in a policy](#specifying-conditions)
+ [Creating an VPC endpoint policy](#endpoint-policy-example)

## DataSync resources and operations
<a name="access-control-specify-datasync-actions"></a>

In DataSync, the primary resources are agent, location, task, and task execution.

These resources have unique Amazon Resource Names (ARNs) associated with them, as shown in the following table.


| Resource type | ARN format | 
| --- | --- | 
| Agent ARN | `arn:aws:datasync:{{region}}:{{account-id}}:agent/{{agent-id}}` | 
| Location ARN | `arn:aws:datasync:{{region}}:{{account-id}}:location/{{location-id}}` | 
| Task ARN | `arn:aws:datasync:{{region}}:{{account-id}}:task/{{task-id}} ` | 
| Task execution ARN | `arn:aws:datasync:{{region}}:{{account-id}}:task/{{task-id}}/execution/{{exec-id}}` | 

To grant permissions for specific API operations, such as creating a task, DataSync defines a set of actions that you can specify in a permissions policy. An API operation can require permissions for more than one action.

## Understanding resource ownership
<a name="access-control-owner"></a>

A *resource owner* is the AWS account that created the resource. That is, the resource owner is the AWS account of the *principal entity* (for example, an IAM role) which authenticates the request that creates the resource. The following examples illustrate how this behavior works:
+ If you use the root account credentials of your AWS account to create a task, your AWS account is the owner of the resource (in DataSync, the resource is the task).
+ If you create an IAM roles in your AWS account and grant permissions to the `CreateTask` action to that user, the user can create a task. However, your AWS account, to which the user belongs, owns the task resource.
+ If you create an IAM role in your AWS account with permissions to create a task, anyone who can assume the role can create a task. Your AWS account, to which the role belongs, owns the task resource. 

## Managing access to resources
<a name="access-control-managing-permissions"></a>

A permissions policy describes who has access to what. The following section explains the available options for creating permissions policies.

**Note**  
This section discusses using IAM in the context of DataSync. It doesn't provide detailed information about the IAM service. For complete IAM documentation, see [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide.* For information about IAM policy syntax and descriptions, see [AWS Identity and Access Management policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide.*

Policies attached to an IAM identity are referred to as *identity-based* policies (IAM policies) and policies attached to a resource are referred to as *resource-based* policies. DataSync supports only identity-based policies (IAM policies). 

**Topics**
+ [Identity-based policies](#identity-based-policies)
+ [Resource-based policies](#resource-based-policies)

### Identity-based policies
<a name="identity-based-policies"></a>

You can manage DataSync resource access with IAM policies. These policies can help an AWS account administrator do the following with DataSync:
+ **Grant permissions to create and manage DataSync resources** – Create an IAM policy that allows an IAM role in your AWS account to create and manage DataSync resources, such as agents, locations, and tasks.
+ **Grant permissions to a role in another AWS account or an AWS service** – Create an IAM policy that grants permissions to an IAM role in a different AWS account or an AWS service. For example:

  1. The Account A administrator creates an IAM role and attaches a permissions policy to the role that grants permissions on resources in Account A.

  1. The Account A administrator attaches a trust policy to the role that identifies Account B as the principal who can assume the role. 

     To grant an AWS service permissions to assume the role, the Account A administrator can specify an AWS service as the principal in the trust policy.

  1. The Account B administrator can then delegate permissions to assume the role to any users in Account B. This allows anyone using the role in Account B to create or access resources in Account A. 

  For more information about using IAM to delegate permissions, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.

The following example policy grants permissions to all `List*` actions on all resources. This action is a read-only action and doesn't allow resource modification.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAllListActionsOnAllResources",
            "Effect": "Allow",
            "Action": [
                "datasync:List*"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about using identity-based policies with DataSync, see [AWS managed policies](security-iam-awsmanpol.md) and [customer managed policies](using-identity-based-policies.md). For more information about IAM identities, see the [https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) .

### Resource-based policies
<a name="resource-based-policies"></a>

Other services, such as Amazon S3, support resource-based permissions policies. For example, you can attach a policy to an Amazon S3 bucket to manage access permissions to that bucket. However, DataSync doesn't support resource-based policies. 

## Specifying policy elements: Actions, effects, resources, and principals
<a name="policy-elements"></a>

For each DataSync resource, the service defines a set of API operations (see [Actions](https://docs.aws.amazon.com/datasync/latest/userguide/API_Operations.html)). To grant permissions for these API operations, DataSync defines a set of actions that you can specify in a policy. For example, for the DataSync resource, the following actions are defined: `CreateTask`, `DeleteTask`, and `DescribeTask`. Performing an API operation can require permissions for more than one action.

The following are the most basic policy elements:
+ **Resource** – In a policy, you use an Amazon Resource Name (ARN) to identify the resource to which the policy applies. For DataSync resources, you can use the wildcard character `(*)` in IAM policies. For more information, see [DataSync resources and operations](#access-control-specify-datasync-actions).
+ **Action** – You use action keywords to identify resource operations that you want to allow or deny. For example, depending on the specified `Effect` element, the `datasync:CreateTask` permission allows or denies the user permissions to perform the DataSync `CreateTask` operation.
+ **Effect** – You specify the effect when the user requests the specific action—this effect can be either `Allow` or `Deny`. If you don't explicitly grant access to (`Allow`) a resource, access is implicitly denied. You can also explicitly deny access to a resource, which you might do to make sure that a user cannot access it, even if a different policy grants that user access. For more information, see [ Authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-authorization) in the *IAM User Guide*. 
+ **Principal** – In identity-based policies (IAM policies), the user that the policy is attached to is the implicit principal. For resource-based policies, you specify the user, account, service, or other entity that you want to receive permissions (applies to resource-based policies only). DataSync doesn't support resource-based policies.

To learn more about IAM policy syntax and descriptions, see [AWS Identity and Access Management policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*.

## Specifying conditions in a policy
<a name="specifying-conditions"></a>

When you grant permissions, you can use the IAM policy language to specify the conditions when a policy should take effect when granting permissions. For example, you might want a policy to be applied only after a specific date. For more information about specifying conditions in policy language, see [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition) in the *IAM User Guide*.

To express conditions, you use predefined condition keys. There are no condition keys specific to DataSync. However, there are AWS wide condition keys that you can use as appropriate. For a complete list of AWS wide keys, see [Available keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*. 

## Creating an VPC endpoint policy
<a name="endpoint-policy-example"></a>

VPC endpoint policies help control access to DataSync API operations through DataSync VPC service endpoints and FIPS-enabled VPC service endpoints. VPC endpoint policies allow you to restrict specific DataSync API actions accessed through your VPC service endpoints, such as `CreateTask` or `StartTaskExecution`.

An endpoint policy specifies the following information:
+ The principals that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).

**Example policy**  
The following is an example of a endpoint policy.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": "*",
        "Action": [
          "datasync:CreateTask",
          "datasync:StartTaskExecution",
          "datasync:DescribeTask"
        ],
        "Resource": "arn:aws:datasync:{{us-east-1}}:{{123456789012}}:task/*"
     }
   ]
}
```