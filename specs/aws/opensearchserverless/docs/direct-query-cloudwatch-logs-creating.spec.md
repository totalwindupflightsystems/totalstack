---
id: "@specs/aws/opensearchserverless/docs/direct-query-cloudwatch-logs-creating"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a CloudWatch Logs data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Creating a CloudWatch Logs data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-cloudwatch-logs-creating
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating an Amazon CloudWatch Logs data source integration in OpenSearch Service
<a name="direct-query-cloudwatch-logs-creating"></a>

If you use Amazon OpenSearch Serverless for your observability needs, you can now analyze your Amazon CloudWatch Logs without copying or ingesting the data into OpenSearch Service. This capability leverages direct query for querying data, similar to analyzing data in Amazon S3 from OpenSearch Service. You can get started by creating a new connected data source from the AWS Management Console.

You can create a new data source to analyze CloudWatch Logs data without having to build Amazon OpenSearch Serverless to directly query operational logs in CloudWatch Logs. This enables you to analyze your accessed operational data that rests outside of OpenSearch Service. By querying across OpenSearch Service and CloudWatch Logs, you can start analyzing logs in CloudWatch Logs and then move back to monitoring data sources in OpenSearch without having to switch tools.

To use this feature, you create a CloudWatch Logs direct query data source for OpenSearch Service through the AWS Management Console. 

**Topics**
+ [Prerequisites](#direct-query-cloudwatch-logs-prereq)
+ [Procedure](#direct-query-cloudwatch-logs-create)
+ [Next steps](#direct-query-cloudwatch-logs-next-steps)
+ [Additional resources](#direct-query-cloudwatch-logs-additional-resources)

## Prerequisites
<a name="direct-query-cloudwatch-logs-prereq"></a>

Before you get started, make sure that you have reviewed the following documentation:
+ [Limitations](direct-query-cloudwatch-logs-overview.md#direct-query-cloudwatch-logs-limitations)
+ [Recommendations](direct-query-cloudwatch-logs-overview.md#direct-query-cloudwatch-logs-recommendations)
+ [Quotas](direct-query-cloudwatch-logs-overview.md#direct-query-cloudwatch-logs-quotas)

Before you can create a data source, you must have the following resources in your AWS account:
+ **Enable CloudWatch Logs.** Configure CloudWatch Logs to collect logs on the same AWS account as your OpenSearch resource. For instructions, see [Getting started with CloudWatch Logs ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_GettingStarted.html)in the Amazon CloudWatch Logs user guide. 
+ **One or more CloudWatch log groups. **You can specify the log groups containing data that you want to query. For instructions on creating a log group, see [Create a log group in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the Amazon CloudWatch Logs user guide.
+ **(Optional) A manually created IAM role. **You can use this role to manage access to your data source. Alternatively, you can have OpenSearch Service create a role for you automatically with the required permissions. If you choose to use a manually created IAM role, follow the guidance in [Required permissions for manually created IAM roles](#direct-query-cloudwatch-logs-additional-resources-required-permissions).

## Procedure
<a name="direct-query-cloudwatch-logs-create"></a>

You can set up a collection-level query data source with the AWS Management Console.

### To set up a collection-level data source using the AWS Management Console
<a name="creating-direct-query-cloudwatch-logs-console-create"></a>

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, go to **Central management** and choose **Connected data sources**. 

1. Choose **Connect**.

1. Choose **CloudWatch** as the data source type. 

1. Choose **Next**.

1. Under **Data connection details**, enter a name and an optional description. 

1. Under **IAM roles**, choose how to manage access to the log groups.

   1. If you want to automatically create a role for this data source, follow these steps:

      1. Select **Create a new role**.

      1. Enter a name for the IAM role.

      1. Select one or more log groups to define which data can be queried.

   1. If you want to use an existing role that you manage yourself, follow these steps:

      1. Select **Use an existing role.**

      1. Select an existing role from the drop-down menu.
**Note**  
When using your own role, you must ensure it has all necessary permissions by attaching required policies from the IAM console. For more information, see [Required permissions for manually created IAM roles](#direct-query-cloudwatch-logs-additional-resources-required-permissions).

1. (Optional) Under **Access policy**, configure an access policy for the data source. Access policies control whether a request to the OpenSearch Service direct query data source is accepted or rejected. If you don't configure an access policy, only the data source owner has access. You can configure the access policy to enable cross-account access, allowing principals in other AWS accounts to access the data source.

   You can create an access policy using the visual editor or by providing a JSON policy document. With the visual editor, you can allow or deny access by specifying a principal AWS account ID, account ARN, IAM user ARN, IAM role ARN, source IP address, or CIDR block. The visual editor supports up to 10 elements. To define a policy with more than 10 elements, use the JSON editor.

   You can also choose **Import policy** to import an existing access policy from another data source.

1. (Optional) Under **Tags**, add tags to your data source.

1. Choose **Next**.

1. Under **Set up OpenSearch**, choose how to set up OpenSearch.

   1. Use the default settings:

      1. Review the default resource names and data retention settings. We suggest you use custom names.

        When you use the default settings, a new OpenSearch application and Essentials workspace is created for you at no additional cost. OpenSearch enables you to analyze multiple data sources. It includes workspaces, which provide a tailored experiences for popular use cases. Workspaces support access control, enabling you to create private spaces for your use cases and share them only with your collaborators.

   1. Use customized settings:

      1. Choose **Customize**.

      1. Edit the collection name and the data retention settings as needed.

      1. Select the OpenSearch application and workspace that you want to use.

1. Choose **Next**.

1. Review your choices and choose **Edit** if you need to make any changes.

1. Choose **Connect** to set up the data source. Stay on this page while your data source is created. When it’s ready, you’ll be taken to the data source details page. 

## Next steps
<a name="direct-query-cloudwatch-logs-next-steps"></a>

### Visit OpenSearch Dashboards
<a name="direct-query-cloudwatch-logs-next-steps-dashboard"></a>

After you create a data source, OpenSearch Service provides you with an OpenSearch Dashboards URL. You use this to configure access control, define tables, set up log-type based dashboards for popular log types, and query your data using SQL or PPL.

For more information, see [Configuring and querying a CloudWatch Logs data source in OpenSearch Dashboards](direct-query-cloudwatch-logs-configure.md).

## Additional resources
<a name="direct-query-cloudwatch-logs-additional-resources"></a>

### Required permissions for manually created IAM roles
<a name="direct-query-cloudwatch-logs-additional-resources-required-permissions"></a>

 When creating a data source, you choose an IAM role to manage access to your data. You have two options:

1. Create a new IAM role automatically

1. Use an existing IAM role that you created manually

If you use a manually created role, you need to attach the correct permissions to the role. The permissions must allow access to the specific data source, and allow OpenSearch Service to assume the role. This is required so that the OpenSearch Service can securely access and interact with your data. 

The following sample policy demonstrates the least-privilege permissions required to create and manage a data source. If you have broader permissions, such as `logs:*` or the `AdminstratorAccess` policy, these permissions encompasses the least-privilege permissions in the sample policy.

In the following sample policy, replace the {{placeholder text }}with your own information.

------
#### [ JSON ]

****  

```
    {
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AmazonOpenSearchDirectQueryAllLogsAccess",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:StartQuery",
                "logs:GetLogGroupFields"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{111122223333}}"
                }
            },
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:*"
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
            "Sid": "TrustPolicyForAmazonOpenSearchDirectQueryService",
            "Effect": "Allow",
            "Principal": {
                "Service": "directquery.opensearchservice.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:opensearch:{{us-east-1}}:{{111122223333}}:{{datasource}}/{{rolename}}"
                }
            }
        }
    ]
}
```

------

For instructions to create the role, see [Creating a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html).

By default, the role has access to direct query data source indexes only. Although you can configure the role to limit or grant access to your data source, it is recommended you not adjust the access of this role. **If you delete the data source, this role will be deleted**. This will remove access for any other users if they are mapped to the role.

### Sample access policy for a direct query data source
<a name="direct-query-cloudwatch-logs-additional-resources-access-policy"></a>

Access policies for direct query data sources follow IAM policy syntax. The policy document must be in valid JSON format. The following example policy grants a specific AWS account access to the direct query data source.

In the following sample policy, replace the {{placeholder text}} with your own information.

```
{
 "Version": "2012-10-17", 		 	 	 
 "Statement": [
   {
     "Effect": "Allow",
     "Principal": {
     "AWS": "arn:aws:iam::{{account-id}}:root"
     },
     "Action": [
       "opensearch:StartDirectQuery",
       "opensearch:GetDirectQuery",
       "opensearch:CancelDirectQuery",
       "opensearch:GetDirectQueryResult"
     ],
     "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:datasource/{{data-source-name}}"
   }
 ]
}
```

If you don't configure an access policy, only the data source owner has access to the data source.