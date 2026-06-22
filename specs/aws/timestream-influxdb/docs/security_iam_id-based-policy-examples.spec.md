---
id: "@specs/aws/timestream-influxdb/docs/security_iam_id-based-policy-examples"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Identity-based policy examples"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Identity-based policy examples

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/security_iam_id-based-policy-examples
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon Timestream for LiveAnalytics identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, IAM users and roles don't have permission to create or modify Timestream for LiveAnalytics resources. They also can't perform tasks using the AWS Management Console, CQLSH, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the Timestream for LiveAnalytics console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Common operations in Timestream for LiveAnalytics](#security_iam_id-based-policy-examples-common-operations)
+ [Timestream for LiveAnalytics resource access based on tags](#security_iam_id-based-policy-examples-tags)
+ [Scheduled queries](#security_iam_id-based-policy-examples-sheduledqueries)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Timestream for LiveAnalytics resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the Timestream for LiveAnalytics console
<a name="security_iam_id-based-policy-examples-console"></a>

Timestream for LiveAnalytics does not require specific permissions to access the Amazon Timestream for LiveAnalytics console. You need at least read-only permissions to list and view details about the Timestream for LiveAnalytics resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (IAM users or roles) with that policy.

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Common operations in Timestream for LiveAnalytics
<a name="security_iam_id-based-policy-examples-common-operations"></a>

Below are sample IAM policies that allow for common operations in the Timestream for LiveAnalytics service.

**Topics**
+ [Allowing all operations](#security_iam_id-based-policy-examples-common-operations.all)
+ [Allowing SELECT operations](#security_iam_id-based-policy-examples-common-operations.select)
+ [Allowing SELECT operations on multiple resources](#security_iam_id-based-policy-examples-common-operations.select-multiple-resources)
+ [Allowing metadata operations](#security_iam_id-based-policy-examples-common-operations.metadata)
+ [Allowing INSERT operations](#security_iam_id-based-policy-examples-common-operations.insert)
+ [Allowing CRUD operations](#security_iam_id-based-policy-examples-common-operations.crud)
+ [Cancel queries and select data without specifying resources](#security_iam_id-based-policy-examples-common-operations.cancel-selectvalues)
+ [Create, describe, delete and describe a database](#security_iam_id-based-policy-examples-common-operations.cddd)
+ [Limit listed databases by tag`{"Owner": "${username}"}`](#security_iam_id-based-policy-examples-common-operations.list-by-tag)
+ [List all tables in a database](#security_iam_id-based-policy-examples-common-operations.list-all-tables)
+ [Create, describe, delete, update and select on a table](#security_iam_id-based-policy-examples-common-operations.cddus-table)
+ [Limit a query by table](#security_iam_id-based-policy-examples-common-operations.limit-query-table)

### Allowing all operations
<a name="security_iam_id-based-policy-examples-common-operations.all"></a>

The following is a sample policy that allows all operations in Timestream for LiveAnalytics.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:*"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Allowing SELECT operations
<a name="security_iam_id-based-policy-examples-common-operations.select"></a>

The following sample policy allows `SELECT`-style queries on a specific resource.

**Note**  
Replace `<account_ID>` with your Amazon account ID.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:Select",
                "timestream:DescribeTable",
                "timestream:ListMeasures"
            ],
            "Resource": "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/DevOps"
        },
        {
            "Effect": "Allow",
            "Action": [
                "timestream:DescribeEndpoints",
                "timestream:SelectValues",
                "timestream:CancelQuery"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Allowing SELECT operations on multiple resources
<a name="security_iam_id-based-policy-examples-common-operations.select-multiple-resources"></a>

The following sample policy allows `SELECT`-style queries on multiple resources. 

**Note**  
Replace `<account_ID>` with your Amazon account ID.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:Select",
                "timestream:DescribeTable",
                "timestream:ListMeasures"
            ],
            "Resource": [
                "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/DevOps",
                "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/DevOps1",
                "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/DevOps2"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "timestream:DescribeEndpoints",
                "timestream:SelectValues",
                "timestream:CancelQuery"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Allowing metadata operations
<a name="security_iam_id-based-policy-examples-common-operations.metadata"></a>

The following sample policy allows the user to perform metadata queries, but does not allow the user to perform operations that read or write actual data in Timestream for LiveAnalytics.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:DescribeEndpoints",
                "timestream:DescribeTable",
                "timestream:ListMeasures",
                "timestream:SelectValues",
                "timestream:ListTables",
                "timestream:ListDatabases",
                "timestream:CancelQuery"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Allowing INSERT operations
<a name="security_iam_id-based-policy-examples-common-operations.insert"></a>

The following sample policy allows a user to perform an `INSERT` operation on `database/sampleDB/table/DevOps` in account `<account_id>`.

**Note**  
Replace `<account_ID>` with your Amazon account ID.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "timestream:WriteRecords"
            ],
            "Resource": [
                "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/DevOps"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "timestream:DescribeEndpoints"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

------

### Allowing CRUD operations
<a name="security_iam_id-based-policy-examples-common-operations.crud"></a>

The following sample policy allows a user to perform CRUD operations in Timestream for LiveAnalytics.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:DescribeEndpoints",
                "timestream:CreateTable",
                "timestream:DescribeTable",
                "timestream:CreateDatabase",
                "timestream:DescribeDatabase",
                "timestream:ListTables",
                "timestream:ListDatabases",
                "timestream:DeleteTable",
                "timestream:DeleteDatabase",
                "timestream:UpdateTable",
                "timestream:UpdateDatabase"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Cancel queries and select data without specifying resources
<a name="security_iam_id-based-policy-examples-common-operations.cancel-selectvalues"></a>

The following sample policy allows a user to cancel queries and perform `Select` queries on data that does not require resource specification:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:SelectValues",
                "timestream:CancelQuery"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### Create, describe, delete and describe a database
<a name="security_iam_id-based-policy-examples-common-operations.cddd"></a>

The following sample policy allows a user to create, describe, delete and describe database `sampleDB`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:CreateDatabase",
                "timestream:DescribeDatabase",
                "timestream:DeleteDatabase",
                "timestream:UpdateDatabase"
            ],
            "Resource": "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB"
        }
    ]
}
```

------

### Limit listed databases by tag`{"Owner": "${username}"}`
<a name="security_iam_id-based-policy-examples-common-operations.list-by-tag"></a>

The following sample policy allows a user to list all databases that that are tagged with key value pair `{"Owner": "${username}"}`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:ListDatabases"
            ],
            "Resource": "arn:aws:timestream:us-east-1:{{111122223333}}:database/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Owner": "${aws:username}"
                }
            }
        }
    ]
}
```

------

### List all tables in a database
<a name="security_iam_id-based-policy-examples-common-operations.list-all-tables"></a>

The following sample policy to list all tables in database `sampleDB`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:ListTables"
            ],
            "Resource": "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/"
        }
    ]
}
```

------

### Create, describe, delete, update and select on a table
<a name="security_iam_id-based-policy-examples-common-operations.cddus-table"></a>

The following sample policy allows a user to create tables, describe tables, delete tables, update tables, and perform `Select` queries on table `DevOps` in database `sampleDB`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:CreateTable",
                "timestream:DescribeTable",
                "timestream:DeleteTable",
                "timestream:UpdateTable",
                "timestream:Select"
            ],
            "Resource": "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/DevOps"
        }
    ]
}
```

------

### Limit a query by table
<a name="security_iam_id-based-policy-examples-common-operations.limit-query-table"></a>

The following sample policy allows a user to query all tables except `DevOps` in database `sampleDB`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:Select"
            ],
            "Resource": "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "timestream:Select"
            ],
            "Resource": "arn:aws:timestream:us-east-1:{{111122223333}}:database/sampleDB/table/DevOps"
        }
    ]
}
```

------

## Timestream for LiveAnalytics resource access based on tags
<a name="security_iam_id-based-policy-examples-tags"></a>

You can use conditions in your identity-based policy to control access to Timestream for LiveAnalytics resources based on tags. This section provides some examples. 

The following example shows how you can create a policy that grants permissions to a user to view a table if the table's `Owner` contains the value of that user's user name.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ReadOnlyAccessTaggedTables",
            "Effect": "Allow",
            "Action": "timestream:Select",
            "Resource": "arn:aws:timestream:us-east-2:{{111122223333}}:database/mydatabase/table/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Owner": "${aws:username}"
                }
            }
        }
    ]
}
```

------

You can attach this policy to the IAM users in your account. If a user named `richard-roe` attempts to view an Timestream for LiveAnalytics table, the table must be tagged `Owner=richard-roe` or `owner=richard-roe`. Otherwise, he is denied access. The condition tag key `Owner` matches both `Owner` and `owner` because condition key names are not case-sensitive. For more information, see [IAM JSON Policy Elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

The following policy grants permissions to a user to create tables with tags if the tag passed in request has a key `Owner` and a value `username`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CreateTagTableUser",
            "Effect": "Allow",
            "Action": [
                "timestream:CreateTable",
                "timestream:TagResource"
            ],
            "Resource": "arn:aws:timestream:us-east-2:{{111122223333}}:database/mydatabase/table/*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:RequestTag/Owner": "${aws:username}"
                }
            }
        }
    ]
}
```

------

The policy below allows use of the `DescribeDatabase` API on any Database that has the `env` tag set to either `dev` or `test`:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowDescribe",
            "Effect": "Allow",
            "Action": [
                "timestream:DescribeEndpoints",
                "timestream:DescribeDatabase"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowTagAccessForDevResources",
            "Effect": "Allow",
            "Action": [
                "timestream:TagResource"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/env": [
                        "test",
                        "dev"
                    ]
                }
            }
        }
    ]
}
```

------

This policy uses a `Condition` key to allow a tag that has the key `env` and a value of `test`, `qa`, or `dev` to be added to a resource.

## Scheduled queries
<a name="security_iam_id-based-policy-examples-sheduledqueries"></a>

### List, delete, update, execute ScheduledQuery
<a name="security_iam_id-based-policy-examples-sheduledqueries-alloperations"></a>

The following sample policy allows a user to list, delete, update and execute scheduled queries.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "timestream:DeleteScheduledQuery",
                "timestream:ExecuteScheduledQuery",
                "timestream:UpdateScheduledQuery",
                "timestream:ListScheduledQueries",
                "timestream:DescribeEndpoints"
            ],
            "Resource": "*"
        }
    ]
}
```

------

### CreateScheduledQuery using a customer managed KMS key
<a name="security_iam_id-based-policy-examples-sheduledqueries-create"></a>

The following sample policy allows a user to create a scheduled query that is encrypted using a customer managed KMS key; {{<keyid for ScheduledQuery>}}.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::123456789012:role/ScheduledQueryExecutionRole"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "timestream:CreateScheduledQuery",
                "timestream:DescribeEndpoints"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "kms:DescribeKey",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-west-2:123456789012:key/{{<keyid for ScheduledQuery>}}",
            "Effect": "Allow"
        }
    ]
}
```

------

### DescribeScheduledQuery using a customer managed KMS key
<a name="security_iam_id-based-policy-examples-sheduledqueries-describe"></a>

The following sample policy allows a user to describe a scheduled query that was created using a customer managed KMS key; {{<keyid for ScheduledQuery>}}.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "timestream:DescribeScheduledQuery",
                "timestream:DescribeEndpoints"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": "arn:aws:kms:us-west-2:123456789012:key/{{<keyid for ScheduledQuery>}}",
            "Effect": "Allow"
        }
    ]
}
```

------

### Execution role permissions (using a customer managed KMS key for scheduled query and SSE-KMS for error reports)
<a name="security_iam_id-based-policy-examples-sheduledqueries-execrole"></a>

Attach the following sample policy to the IAM role specified in the `ScheduledQueryExecutionRoleArn` parameter, of the `CreateScheduledQuery` API that uses customer managed KMS key for the scheduled query encryption and `SSE-KMS` encryption for error reports. 

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-west-2:123456789012:key/{{<keyid for ScheduledQuery>}}",
            "Effect": "Allow"
        },
        {
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:us-west-2:123456789012:key/{{<keyid for database-1>}}",
                "arn:aws:kms:us-west-2:123456789012:key/{{<keyid for database-n>}}",
                "arn:aws:kms:us-west-2:123456789012:key/{{<keyid for ScheduledQuery>}}"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "sns:Publish"
            ],
            "Resource": [
                "arn:aws:sns:us-west-2:123456789012:{{scheduled-query-notification-topic}}-*"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "timestream:Select",
                "timestream:SelectValues",
                "timestream:WriteRecords"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "s3:PutObject",
                "s3:GetBucketAcl"
            ],
            "Resource": [
                "arn:aws:s3:::{{scheduled-query-error-bucket}}",
                "arn:aws:s3:::{{scheduled-query-error-bucket}}/*"
            ],
            "Effect": "Allow"
        }
    ]
}
```

------

### Execution role trust relationship
<a name="security_iam_id-based-policy-examples-sheduledqueries-exectrust"></a>

The following is the trust relationship for the IAM role specified in the `ScheduledQueryExecutionRoleArn` parameter of the `CreateScheduledQuery` API.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "timestream.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

### Allow access to all scheduled queries created within an account
<a name="security_iam_id-based-policy-examples-sheduledqueries-accountid"></a>

Attach the following sample policy to the IAM role specified in the `ScheduledQueryExecutionRoleArn` parameter, of the `CreateScheduledQuery` API, to allow access to all scheduled queries created within the an account {{Account\_ID}}.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "timestream.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{Account_ID}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:timestream:us-west-2:{{111122223333}}:scheduled-query/*"
                }
            }
        }
    ]
}
```

------

### Allow access to all scheduled queries with a specific name
<a name="security_iam_id-based-policy-examples-sheduledqueries-queryname"></a>

Attach the following sample policy to the IAM role specified in the `ScheduledQueryExecutionRoleArn` parameter, of the `CreateScheduledQuery` API, to allow access to all scheduled queries with a name that starts with {{Scheduled\_Query\_Name}}, within account {{Account\_ID}}.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "timestream.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{Account_ID}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:timestream:us-west-2:{{111122223333}}:scheduled-query/{{Scheduled_Query_Name}}*"
                }
            }
        }
    ]
}
```

------