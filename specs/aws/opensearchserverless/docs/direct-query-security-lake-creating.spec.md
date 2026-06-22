---
id: "@specs/aws/opensearchserverless/docs/direct-query-security-lake-creating"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a Security Lake data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Creating a Security Lake data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-security-lake-creating
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating an Amazon Security Lake data source integration in OpenSearch Service
<a name="direct-query-security-lake-creating"></a>

You can use Amazon OpenSearch Serverless to directly query security data in Amazon Security Lake. To do this, you create a data source that enables you to use OpenSearch zero-ETL capabilities on Security Lake data. When you create a data source you can directly search, gain insights from, and analyze data stored in Security Lake. You can accelerate your query performance and use advanced OpenSearch analytics on select Security Lake data sets using on-demand indexing.

**Topics**
+ [Prerequisites](#direct-query-s3security-lake-prereq)
+ [Procedure](#direct-query-security-lake-create)
+ [Next steps](#direct-query-security-lake-next-steps)
+ [Additional resources](#direct-query-security-lake-additional-resources)

## Prerequisites
<a name="direct-query-s3security-lake-prereq"></a>

Before you get started, make sure that you have reviewed the following documentation:
+ [Limitations](direct-query-security-lake-overview.md#direct-query-security-lake-limitations)
+ [Recommendations](direct-query-security-lake-overview.md#direct-query-security-lake-recommendations)
+ [Quotas](direct-query-security-lake-overview.md#direct-query-security-lake-quotas)

Before you can create a data source, take the following actions in Security Lake:
+ **Enable Security Lake**. Configure Security Lake to collect logs on the same AWS Region as your OpenSearch resource. For instructions, see [Getting started with Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html) in the Amazon Security Lake user guide.
+ **Set up Security Lake permissions**. Make sure you have accepted the service linked role permissions for resource management and the console does not show any issues under the **Issues** page. For more information, see [Service-linked role for Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/using-service-linked-roles.html) in the Amazon Security Lake user guide.
+ **Share Security Lake data sources**. When accessing OpenSearch within the same account as Security Lake, ensure that there is no message to register your Security Lake buckets with Lake Formation in the Security Lake console. For cross-account OpenSearch access, set up a Lake Formation query subscriber in the Security Lake console. Use the account associated with your OpenSearch resource as the subscriber. For more information, see [Subscriber management in Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/create-query-subscriber-procedures.html) in the Amazon Security Lake user guide.

In addition, you must also you must have the following resources in your AWS account:
+ **(Optional) A manually created IAM role.** You can use this role to manage access to your data source. Alternatively, you can have OpenSearch Service create a role for you automatically with the required permissions. If you choose to use a manually created IAM role, follow the guidance in [Required permissions for manually created IAM roles](#direct-query-security-lake-additional-resources-required-permissions).

## Procedure
<a name="direct-query-security-lake-create"></a>

You can set up a data source to connect with a Security Lake database from within the AWS Management Console.

### To set up a data source using the AWS Management Console
<a name="creating-direct-query-security-lake-console-create"></a>

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, go to **Central management** and choose **Connected data sources**. 

1. Choose **Connect**.

1. Choose **Security Lake** as the data source type. 

1. Choose **Next**.

1. Under **Data connection details**, enter a name and an optional description. 

1. Under **IAM permission access settings**, choose how to manage access to your data source.

   1. If you want to automatically create a role for this data source, follow these steps:

      1. Select **Create a new role**.

      1. Enter a name for the IAM role.

      1. Select one or more AWS Glue tables to define which data can be queried.

   1. If you want to use an existing role that you manage yourself, follow these steps:

      1. Select **Use an existing role.**

      1. Select an existing role from the drop-down menu.
**Note**  
When using your own role, you must ensure it has all necessary permissions by attaching required policies from the IAM console. For more information, see [Required permissions for manually created IAM roles](#direct-query-security-lake-additional-resources-required-permissions).

1. (Optional) Under **Tags**, add tags to your data source.

1. Choose **Next**.

1. Under **Set up OpenSearch**, choose how to set up OpenSearch.

   1. Review the default resource names and data retention settings.

     When you use the default settings, a new OpenSearch application and Essentials workspace is created for you at no additional cost. OpenSearch enables you to analyze multiple data sources. It includes workspaces, which provide a tailored experiences for popular use cases. Workspaces support access control, enabling you to create private spaces for your use cases and share them only with your collaborators.

1. Use customized settings:

   1. Choose **Customize**.

   1. Edit the collection name and the data retention settings as needed.

   1. Select the OpenSearch application and workspace that you want to use.

1. Choose **Next**.

1. Review your choices and choose **Edit** if you need to make any changes.

1. Choose **Connect** to set up the data source. Stay on this page while your data source is created. When it’s ready, you’ll be taken to the data source details page. 

## Next steps
<a name="direct-query-security-lake-next-steps"></a>

### Visit OpenSearch Dashboards and create a dashboard
<a name="direct-query-security-lake-next-steps-dashboard"></a>

After you create a data source, OpenSearch Service provides you with an OpenSearch Dashboards URL. You use this to query your data using SQL or PPL. The Security Lake integration comes with pre-packaged query templates for SQL and PPL to get you get started analyzing your logs. 

For more information, see [Configuring and querying a Security Lake data source in OpenSearch Dashboards](direct-query-security-lake-configure.md).

## Additional resources
<a name="direct-query-security-lake-additional-resources"></a>

### Required permissions for manually created IAM roles
<a name="direct-query-security-lake-additional-resources-required-permissions"></a>

When creating a data source, you choose an IAM role to manage access to your data. You have two options:

1. Create a new IAM role automatically

1. Use an existing IAM role that you created manually

If you use a manually created role, you need to attach the correct permissions to the role. The permissions must allow access to the specific data source, and allow OpenSearch Service to assume the role so that OpenSearch Service can securely access and interact with your data. Additionally, grant LakeFormation permissions to the role for any databases and tables that you want to query. Grant `DESCRIBE` permissions to the role on SecurityLake databases that you want to query from the direct query connection. Grant at least `SELECT and DESCRIBE` permissions to the data source role for tables within the database.

The following sample policy demonstrates the least-privilege permissions required to create and manage a data source. If you have broader permissions, such as the `AdminstratorAccess` policy, these permissions encompasses the least-privilege permissions in the sample policy.

In the following sample policy, replace the {{placeholder text }}with your own information.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AmazonOpenSearchDirectQueryServerlessAccess",
            "Effect": "Allow",
            "Action": [
                "aoss:APIAccessAll",
                "aoss:DashboardsAccessAll"
            ],
            "Resource": "arn:aws:aoss:{{us-east-1}}:{{111122223333}}:collection/{{collectionname}}/*"
        },
        {
            "Sid": "AmazonOpenSearchDirectQueryGlueAccess",
            "Effect": "Allow",
            "Action": [
                "glue:GetDatabase",
                "glue:GetDatabases",
                "glue:GetPartition",
                "glue:GetPartitions",
                "glue:GetTable",
                "glue:GetTableVersions",
                "glue:GetTables",
                "glue:SearchTables",
                "glue:BatchGetPartition"
            ],
            "Resource": [
                "arn:aws:glue:{{us-east-1}}:{{111122223333}}:table/{{databasename}}/*",
                "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/{{databasename}}",
                "arn:aws:glue:{{us-east-1}}:{{111122223333}}:catalog",
                "arn:aws:glue:{{us-east-1}}:{{111122223333}}:database/default"
            ]
        },
        {
            "Sid": "AmazonOpenSearchDirectQueryLakeFormationAccess",
            "Effect": "Allow",
            "Action": [
                "lakeformation:GetDataAccess"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

------

The role must also have the following trust policy, which specifies the target ID.

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
                "Service": "directquery.opensearchservice.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

For instructions to create the role, see [Creating a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html).

By default, the role has access to direct query data source indexes only. Although you can configure the role to limit or grant access to your data source, it is recommended you not adjust the access of this role. **If you delete the data source, this role will be deleted**. This will remove access for any other users if they are mapped to the role.

### Querying Security Lake data that's encrypted with a customer managed key
<a name="querying-data-in-cmk-lake"></a>

If the Security Lake bucket associated with the data connection is encrypted using server-side encryption with a customer managed AWS KMS key, you must add the LakeFormation service role to the key policy. This allows the service to access and read the data for your queries.

In the following sample policy, replace the {{placeholder text }}with your own information.

```
{
    "Sid": "Allow LakeFormation to access the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::{{account}}:role/aws-service-role/lakeformation.amazonaws.com/AWSServiceRoleForLakeFormationDataAccess"
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*"
}
```