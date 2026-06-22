---
id: "@specs/aws/opensearchserverless/docs/direct-query-s3-creating"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating an S3 data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Creating an S3 data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-s3-creating
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating an Amazon S3 data source integration in OpenSearch Service
<a name="direct-query-s3-creating"></a>

You can create a new Amazon S3 direct-query data source for OpenSearch Service through the AWS Management Console or the API. Each new data source uses the AWS Glue Data Catalog to manage tables that represent Amazon S3 buckets. 

**Topics**
+ [Prerequisites](#direct-query-s3-prereq)
+ [Procedure](#direct-query-s3-create)
+ [Next steps](#direct-query-s3-next-steps)
+ [Map the AWS Glue Data Catalog role](#direct-query-s3-permissions)
+ [Additional resources](#direct-query-s3-additional-resources)

## Prerequisites
<a name="direct-query-s3-prereq"></a>

Before you get started, make sure that you have reviewed the following documentation:
+ [Limitations](direct-query-s3-overview.md#direct-query-s3-limitations)
+ [Recommendations](direct-query-s3-overview.md#direct-query-s3-recommendations)
+ [Quotas](direct-query-s3-overview.md#direct-query-s3-quotas)

Before you can create a data source, you must have the following resources in your AWS account:
+ **An OpenSearch domain with version 2.13 or later.** This is the foundation for setting up the direct query integration. For instructions on setting this up, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains).
+ **One or more S3 buckets.** You’ll need to specify the buckets containing data that you want to query, and a bucket to store your query checkpoints in. For instructions on creating an S3 bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 user guide.
+ **(Optional) One or more AWS Glue tables. **Querying data on Amazon S3 requires that you have tables setup in AWS Glue Data Catalog to point to the S3 data. You must create the tables using OpenSearch Query Workbench. Existing Hive tables are not compatible. 

  If this is the first time you're setting up an Amazon S3 data source, you must create an admin data source to configure all of your AWS Glue Data Catalog tables. You can do this by installing OpenSearch out-of-the-box integrations or by using OpenSearch Query Workbench to create custom SQL tables for advanced use cases. For examples on creating tables for VPC, CloudTrail, and AWS WAF logs, see the documentation on GitHub for [VPC](https://github.com/opensearch-project/opensearch-catalog/blob/main/integrations/observability/amazon_vpc_flow/assets/create_table_vpc_schema-1.0.0.sql), [CloudTrail](https://github.com/opensearch-project/opensearch-catalog/blob/main/integrations/observability/aws_cloudtrail/assets/create_table_cloud-trail-records-1.0.0.sql), and [AWS WAF](https://github.com/opensearch-project/opensearch-catalog/blob/main/integrations/observability/aws_waf/assets/create_table-1.0.0.sql). After you create your tables, you can create new Amazon S3 data sources and restrict access to limited tables.
+ **(Optional) A manually created IAM role. **You can use this role to manage access to your data source. Alternatively, you can have OpenSearch Service create a role for you automatically with the required permissions. If you choose to use a manually created IAM role, follow the guidance in [Required permissions for manually created IAM roles](#direct-query-s3-additional-resources-required-permissions).

## Procedure
<a name="direct-query-s3-create"></a>

You can set up a direct-query data source on a domain with the AWS Management Console or the OpenSearch Service API.

### To set up a data source using the AWS Management Console
<a name="creating-direct-query-s3-console-create"></a>

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, choose **Domains**. 

1. Select the domain that you want to set up a new data source for. This opens the domain details page. 

1. Choose the **Connections** tab below the general domain details and find the **Direct query** section.

1. Choose **Configure data source**.

1. Enter a name and an optional description for your new data source. 

1. Choose **Amazon S3 with AWS Glue Data Catalog**. 

1. Under **IAM permission access settings**, choose how to manage access.

   1. If you want to automatically create a role for this data source, follow these steps:

      1. Select **Create a new role**.

      1. Enter a name for the IAM role.

      1. Select one or more S3 buckets that contain data you want to query.

      1. Select an checkpoint S3 bucket to store query checkpoints in.

      1. Select one or more AWS Glue databases or tables to define which data can be queried. If tables haven't been created yet, provide access to the default database.

   1. If you want to use an existing role that you manage yourself, follow these steps:

      1. Select **Use an existing role.**

      1. Select an existing role from the drop-down menu.
**Note**  
When using your own role, you must ensure it has all necessary permissions by attaching required policies from the IAM console. For more information, refer to the sample policy in [Required permissions for manually created IAM roles](#direct-query-s3-additional-resources-required-permissions).

1. Choose **Configure**. This opens the data source details screen with an OpenSearch Dashboards URL. You can navigate to this URL to complete the next steps.

### OpenSearch Service API
<a name="creating-direct-query-s3-api-create"></a>

Use the [AddDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddDataSource.html) API operation to create a new data source in your domain.

```
POST https://es.{{region}}.amazonaws.com/2021-01-01/opensearch/domain/{{domain-name}}/dataSource

{
   "DataSourceType": {
        "S3GlueDataCatalog": {
            "RoleArn": "arn:aws:iam::{{account-id}}:role/{{role-name}}"
        }
    }
   "Description": "{{data-source-description}}",
   "Name": "{{my-data-source}}"
}
```

## Next steps
<a name="direct-query-s3-next-steps"></a>

### Visit OpenSearch Dashboards
<a name="direct-query-s3-next-steps-dashboard"></a>

After you create a data source, OpenSearch Service provides you with an OpenSearch Dashboards link. You can use this to configure access control, define tables, install out-of-the-box integrations, and query your data.

For more information, see [Configuring and querying an S3 data source in OpenSearch Dashboards](direct-query-s3-configure.md).

## Map the AWS Glue Data Catalog role
<a name="direct-query-s3-permissions"></a>

If you have enabled [fine-grained access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html) after creating a data source, you must map non-admin users to an IAM role with AWS Glue Data Catalog access in order to run direct queries. To manually create a back-end `glue_access` role that you can map to the IAM role, perform the following steps:

**Note**  
Indexes are used for any queries against the data source. A user with read access to the request index for a given data source can read *all* queries against that data source. A user with read access to the result index can read results for *all* queries against that data source.

1. From the main menu in OpenSearch Dashboards, choose **Security**, **Roles**, and **Create roles**.

1. Name the role **glue\_access**.

1. For **Cluster permissions**, select `indices:data/write/bulk*`, `indices:data/read/scroll`, `indices:data/read/scroll/clear`.

1. For **Index**, enter the following indexes you want to grant the user with the role access to:
   + `.query_execution_request_{{<name of data source>}}`
   + `query_execution_result_{{<name of data source>}}`
   + `.async-query-scheduler`
   + `flint_*`

1. For **Index permissions**, select `indices_all`. 

1. Choose **Create**.

1. Choose **Mapped users**, **Manage mapping**. 

1. Under **Backend roles**, add the ARN of the AWS Glue role that needs permission to call your domain.

   ```
   arn:aws:iam::{{account-id}}:role/{{role-name}}
   ```

1. Select **Map** and confirm the role shows up under **Mapped users**.

For more information on mapping roles, see [Mapping roles to users](fgac.md#fgac-mapping).

## Additional resources
<a name="direct-query-s3-additional-resources"></a>

### Required permissions for manually created IAM roles
<a name="direct-query-s3-additional-resources-required-permissions"></a>

 When creating a data source for your domain, you choose an IAM role to manage access to your data. You have two options:

1. Create a new IAM role automatically

1. Use an existing IAM role that you created manually

If you use a manually created role, you need to attach the correct permissions to the role. The permissions must allow access to the specific data source, and allow OpenSearch Service to assume the role. This is required so that the OpenSearch Service can securely access and interact with your data. 

The following sample policy demonstrates the least-privilege permissions required to create and manage a data source. If you have broader permissions, such as `s3:*` or the `AdminstratorAccess` policy, these permissions encompasses the least-privilege permissions in the sample policy.

In the following sample policy, replace the {{placeholder text }}with your own information.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Sid":"HttpActionsForOpenSearchDomain",
         "Effect":"Allow",
         "Action":"es:ESHttp*",
"Resource":"arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{example.com}}/*"
      },
      {
         "Sid":"AmazonOpenSearchS3GlueDirectQueryReadAllS3Buckets",
         "Effect":"Allow",
         "Action":[
            "s3:GetObject",
            "s3:GetObjectVersion",
            "s3:ListBucket"
         ],
         "Condition":{
            "StringEquals":{
               "aws:ResourceAccount":"{{111122223333}}"
            }
         },
         "Resource":"*"
      },
      {
         "Sid":"AmazonOpenSearchDirectQueryGlueCreateAccess",
         "Effect":"Allow",
         "Action":[
            "glue:CreateDatabase",
            "glue:CreatePartition",
            "glue:CreateTable",
            "glue:BatchCreatePartition"
         ],
         "Resource":"*"
      },
      {
         "Sid":"AmazonOpenSearchS3GlueDirectQueryModifyAllGlueResources",
         "Effect":"Allow",
         "Action":[
            "glue:DeleteDatabase",
            "glue:DeletePartition",
            "glue:DeleteTable",
            "glue:GetDatabase",
            "glue:GetDatabases",
            "glue:GetPartition",
            "glue:GetPartitions",
            "glue:GetTable",
            "glue:GetTableVersions",
            "glue:GetTables",
            "glue:UpdateDatabase",
            "glue:UpdatePartition",
            "glue:UpdateTable",
            "glue:BatchGetPartition",
            "glue:BatchDeletePartition",
            "glue:BatchDeleteTable"
         ],
         "Resource":[
            "arn:aws:glue:us-east-1:{{111122223333}}:table/*",
            "arn:aws:glue:us-east-1:{{111122223333}}:database/*",
            "arn:aws:glue:us-east-1:{{111122223333}}:catalog",
            "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain_name}}"
         ],
         "Condition":{
            "StringEquals":{
               "aws:ResourceAccount":"{{111122223333}}"
            }
         }
      },
      {
         "Sid":"ReadAndWriteActionsForS3CheckpointBucket",
         "Effect":"Allow",
         "Action":[
            "s3:ListMultipartUploadParts",
            "s3:DeleteObject",
            "s3:GetObject",
            "s3:PutObject",
            "s3:GetBucketLocation",
            "s3:ListBucket"
         ],
         "Condition":{
            "StringEquals":{
               "aws:ResourceAccount":"{{111122223333}}"
            }
         },
         "Resource":[
            "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
            "arn:aws:s3:::{{amzn-s3-demo-bucket/*}}"
         ]
      }
   ]
}
```

------

To support Amazon S3 buckets in different accounts, you will need to include a condition to the Amazon S3 policy and add the appropriate account. 

In the following sample condition, replace the {{placeholder text }}with your own information.

```
"Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{{{accountId}}}}"
                }
```

The role must also have the following trust policy, which specifies the target ID.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement":[
       {
          "Effect":"Allow",
          "Principal":{
             "Service": "directquery.opensearchservice.amazonaws.com"
          },
          "Action":"sts:AssumeRole"
       }
     ]
}
```

------

For instructions to create the role, see [Creating a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html).

If you have fine-grained access control enabled in OpenSearch Service, a new OpenSearch fine-grained access control role will automatically be created for your data source. The name of the new fine-grained access control role will be `AWSOpenSearchDirectQuery {{<name of data source>}}`.

By default, the role has access to direct query data source indexes only. Although you can configure the role to limit or grant access to your data source, it is recommended you not adjust the access of this role. **If you delete the data source, this role will be deleted**. This will remove access for any other users if they are mapped to the role.