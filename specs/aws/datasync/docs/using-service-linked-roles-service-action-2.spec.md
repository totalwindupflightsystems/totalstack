---
id: "@specs/aws/datasync/docs/using-service-linked-roles-service-action-2"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSync role"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# DataSync role

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/using-service-linked-roles-service-action-2
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using roles for DataSync
<a name="using-service-linked-roles-service-action-2"></a>

AWS DataSync uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to DataSync. Service-linked roles are predefined by DataSync and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up DataSync easier because you don’t have to manually add the necessary permissions. DataSync defines the permissions of its service-linked roles, and unless defined otherwise, only DataSync can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your DataSync resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for DataSync
<a name="service-linked-role-permissions-service-action-2"></a>

DataSync uses the service-linked role named **AWSServiceRoleForDataSync** – Allows DataSync to perform essential operations for transfer task execution, including reading secrets from AWS Secrets Manager, and creating CloudWatch log groups and events.

The AWSServiceRoleForDataSync service-linked role trusts the following services to assume the role:
+ `datasync.amazonaws.com`

The service-linked role uses the AWS managed policy named [AWSDataSyncServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdatasyncservicerolepolicy), which allows DataSync to complete the following actions on the specified resources:

```
{
    "Version": "2012-10-17",
    "Statement": [{
            "Sid": "DataSyncCloudWatchLogCreateAccess",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream"
            ],
            "Resource": [
                "arn:*:logs:*:*:log-group:/aws/datasync*"
            ]
        },
        {
            "Sid": "DataSyncCloudWatchLogStreamUpdateAccess",
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:*:logs:*:*:log-group:/aws/datasync*:log-stream:*"
            ]
        },
        {
            "Sid": "DataSyncSecretsManagerReadAccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue"
            ],
            "Resource": [
                "arn:*:secretsmanager:*:*:secret:aws-datasync!*"
            ],
            "Condition": {
                "StringEquals": {
                    "secretsmanager:ResourceTag/aws:secretsmanager:owningService": "aws-datasync",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for DataSync
<a name="create-service-linked-role-service-action-2"></a>

You don't need to manually create a service-linked role. When you create a DataSync task in the AWS Management Console, the AWS CLI, or the AWS API, DataSync creates the service-linked role for you. 

In the AWS CLI or the AWS API, you can create a service-linked role with the `datasync.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a DataSync task, DataSync creates the service-linked role for you again. 

If you delete this service-linked role, you can use the same IAM process to create the role again.

## Editing a service-linked role for DataSync
<a name="edit-service-linked-role-service-action-2"></a>

DataSync does not allow you to edit the AWSServiceRoleForDataSync service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for DataSync
<a name="delete-service-linked-role-service-action-2"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role
<a name="service-linked-role-review-before-delete-service-action-2"></a>

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role.

**Note**  
If the DataSync service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete DataSync resources used by the AWSServiceRoleForDataSync**

1. [Delete the DataSync agents](clean-up.md#deleting-agent) used by the task (if there are any).

1. [Delete the task's locations](clean-up.md#deleting-location).

1. [Delete the task](clean-up.md#delete-task).

### Manually delete the service-linked role
<a name="slr-manual-delete-service-action-2"></a>

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForDataSync service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for DataSync service-linked roles
<a name="slr-regions-service-action-2"></a>

DataSync supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).