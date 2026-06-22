---
id: "@specs/aws/opensearchserverless/docs/direct-query-prometheus-creating"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating a Managed Prometheus data source"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Creating a Managed Prometheus data source

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/direct-query-prometheus-creating
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating an Amazon Managed Service for Prometheus data source
<a name="direct-query-prometheus-creating"></a>

To create an Amazon Managed Service for Prometheus data source, you need an active workspace and an IAM role that grants OpenSearch Service the necessary permissions to query your metrics.

## Prerequisites
<a name="direct-query-prometheus-prereq"></a>

Before you connect the data source, make sure you have the following:
+ **Prometheus workspace** – An active Amazon Managed Service for Prometheus workspace. Note your Workspace ID and the AWS Region it resides in.
+ **IAM role** – An AWS Identity and Access Management role with a trust policy that allows the `directquery.opensearchservice.amazonaws.com` service principal to assume it.

## Connecting the data source
<a name="direct-query-prometheus-connect"></a>

After your prerequisites are met, you can connect the data source using the OpenSearch Service console.

**To set up an Amazon Managed Service for Prometheus data source**

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/).

1. In the left navigation pane, go to **Central management** and choose **Connected data sources**.

1. Choose **Connect new data source**.

1. Choose **Amazon Managed Service for Prometheus** as the data source type.

1. Choose **Next**.

1. Under **Data connection details**, enter a name and an optional description.

1. Under **IAM roles**, choose how to manage access:
   + To automatically create a role for this data source:

     1. Select **Create a new role**.

     1. Enter a name for the IAM role.

     1. Select one or more workspaces to define which data can be queried.
   + To use an existing role that you manage yourself:

     1. Select **Use an existing role**.

     1. Select an existing role from the drop-down menu.
**Note**  
When using your own role, make sure it has all necessary permissions by attaching required policies from the IAM console. For more information, see [Required permissions for manually created IAM roles](#direct-query-prometheus-manual-role-permissions).

1. (Optional) Under **Access policy**, configure an access policy for the data source. Access policies control whether a request to the OpenSearch Service direct query data source is accepted or rejected. If you don't configure an access policy, only the data source owner has access. You can configure the access policy to enable cross-account access, allowing principals in other AWS accounts to access the data source.

   You can create an access policy using the visual editor or by providing a JSON policy document. With the visual editor, you can allow or deny access by specifying a principal AWS account ID, account ARN, IAM user ARN, IAM role ARN, source IP address, or CIDR block. The visual editor supports up to 10 elements. To define a policy with more than 10 elements, use the JSON editor.

   You can also choose **Import policy** to import an existing access policy from another data source.

1. (Optional) Under **Tags**, add tags to your data source.

1. Choose **Next**.

1. Under **Set up OpenSearch**, choose how to set up OpenSearch UI:

   1. If no OpenSearch UI application exists in your account, create a new OpenSearch application. If an existing OpenSearch application exists, select it.

   1. If you create a new application, create a new observability workspace. If you selected an existing application, create a new observability workspace or select an existing one. Amazon Managed Service for Prometheus is only available in the observability workspace.

1. Choose **Next**.

1. Review your choices and choose **Edit** if you need to make any changes.

1. Choose **Connect** to set up the data source. Stay on this page while your data source is created. When it's ready, you're taken to the data source details page.

### Next steps
<a name="direct-query-prometheus-next-steps"></a>

**Visit OpenSearch UI**  
After you create a data source, OpenSearch Service provides you with an OpenSearch UI application URL. You use this to configure who has access to OpenSearch UI and analyze your Amazon Managed Service for Prometheus data using Discover Metrics with PromQL.

### Additional resources
<a name="direct-query-prometheus-additional-resources"></a>

#### Required permissions for manually created IAM roles
<a name="direct-query-prometheus-manual-role-permissions"></a>

When creating a data source, you choose an IAM role to manage access to your data. You have two options:
+ Create a new IAM role automatically
+ Use an existing IAM role that you created manually

If you use a manually created role, you need to attach the correct permissions to the role. The permissions must allow access to the specific data source and allow OpenSearch Service to assume the role. This is required so that OpenSearch Service can securely access and interact with your data.

The following sample policy demonstrates the least-privilege permissions required to create and manage a data source. If you have broader permissions, such as `aps:*` or the `AdministratorAccess` policy, these permissions encompass the least-privilege permissions in the sample policy.

In the following sample policy, replace the {{placeholder}} text with your own information.

**Sample IAM policy**  
Attach the following permissions to your IAM role to allow OpenSearch Service to fetch metric metadata and execute queries:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "AmazonOpenSearchDirectQueryPrometheusAccess",
            "Effect": "Allow",
            "Action": [
                "aps:DeleteAlertManagerSilence",
                "aps:GetAlertManagerSilence",
                "aps:GetAlertManagerStatus",
                "aps:GetLabels",
                "aps:GetMetricMetadata",
                "aps:GetSeries",
                "aps:ListAlertManagerAlertGroups",
                "aps:ListAlertManagerAlerts",
                "aps:ListAlertManagerReceivers",
                "aps:ListAlertManagerSilences",
                "aps:ListAlerts",
                "aps:QueryMetrics",
                "aps:PutAlertManagerSilences",
                "aps:DescribeAlertManagerDefinition",
                "aps:CreateRuleGroupsNamespace",
                "aps:DeleteRuleGroupsNamespace",
                "aps:ListRuleGroupsNamespaces",
                "aps:DescribeRuleGroupsNamespace",
                "aps:PutRuleGroupsNamespace"
            ],
            "Resource": "arn:aws:aps:{{region}}:{{account-id}}:workspace/{{workspace-id}}"
        },
        {
            "Sid": "AmazonOpenSearchDirectQueryPrometheusListAccess",
            "Effect": "Allow",
            "Action": [
                "aps:ListWorkspaces"
            ],
            "Resource": "*"
        }
    ]
}
```

**Sample trust policy**  
Attach the following trust policy to your IAM role:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "TrustPolicyForAmazonOpenSearchDirectQueryService",
            "Effect": "Allow",
            "Principal": {
                "Service": "directquery.opensearchservice.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:opensearch:{{region}}:{{account-id}}:datasource/{{data-source-name}}"
                },
                "StringEquals": {
                    "aws:SourceAccount": "{{account-id}}"
                }
            }
        }
    ]
}
```