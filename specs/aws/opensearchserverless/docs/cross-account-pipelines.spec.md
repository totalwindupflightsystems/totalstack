---
id: "@specs/aws/opensearchserverless/docs/cross-account-pipelines"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring pipelines for cross-account ingestion"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Configuring pipelines for cross-account ingestion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/cross-account-pipelines
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring OpenSearch Ingestion pipelines for cross-account ingestion
<a name="cross-account-pipelines"></a>

For push-based sources such as HTTP and OTel, Amazon OpenSearch Ingestion enables you to share pipelines across AWS accounts from a virtual private cloud (VPC) to a pipeline endpoint in a separate VPC. Teams that share analytics with other teams in their organization use this feature for a more streamlined means of, for example, sharing log analytics.

This section uses the following terminology:
+ **Pipeline owner**—The account that owns and manages the OpenSearch Ingestion pipeline. Only one account can own a pipeline.
+ **Connecting account**—An account that connects to and uses a shared pipeline. Multiple accounts can connect to the same pipeline.

To configure VPCs to share OpenSearch Ingestion pipelines across AWS accounts, complete the following tasks, as described here:
+ (Pipeline owner) [Grant connecting accounts access to a pipeline](#cross-account-pipelines-setting-up-grant-access)
+ (Connecting account) [Create a pipeline endpoint connection for each connecting VPC](#cross-account-pipelines-setting-up-create-pipeline-endpoints)

## Before you begin
<a name="cross-account-pipelines-before-you-begin"></a>

Before you configure VPCs to share OpenSearch Ingestion pipelines across AWS accounts, complete the following tasks:


****  

| Task | Details | 
| --- | --- | 
| Create one or more OpenSearch Ingestion pipelines | Set the minimum OpenSearch Compute Units (OSUs) to 2 or higher. For more information, see [Creating Amazon OpenSearch Ingestion pipelines](creating-pipeline.md). For information about updating a pipeline, see [Updating Amazon OpenSearch Ingestion pipelines](update-pipeline.md). | 
| Create one or more VPCs for OpenSearch Ingestion | To enable cross-account pipeline sharing, any VPC involved for the pipeline and the pipeline endpoints must be configured with the following DNS values:[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-account-pipelines.html)<br />For more information, see [DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) in the *Amazon VPC User Guide*. | 

## Grant connecting accounts access to a pipeline
<a name="cross-account-pipelines-setting-up-grant-access"></a>

The procedures in this section describe how to use the OpenSearch Service console and the AWS CLI to set up cross-account pipeline access by creating a resource policy. A *resource policy* enables a pipeline owner to specify other accounts that can access a pipeline. Once created, pipeline policies exist for as long as the pipeline exists or until the policy is deleted.

**Note**  
Resource policies don't replace standard OpenSearch Ingestion authoriziation using [IAM permissions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#create-pipeline-permissions). Resource policies are an added authorization mechanism for enabling cross-account pipeline access.

**Topics**
+ [Grant connecting accounts access to a pipeline (console)](#cross-account-pipelines-setting-up-grant-access-console)
+ [Grant connecting accounts access to a pipeline (CLI)](#cross-account-pipelines-setting-up-grant-access-cli)

### Grant connecting accounts access to a pipeline (console)
<a name="cross-account-pipelines-setting-up-grant-access-console"></a>

Use the following procedure to grant connecting accounts access to a pipeline by using the Amazon OpenSearch Service console.

**To create a pipeline endpoint connection**

1. In the Amazon OpenSearch Service console, in the navigation pane, expand **Ingestion**, and then select **Pipelines**.

1. In the **Pipelines** section, choose the name of a pipeline that you want to grant access for a connecting account.

1. Choose the **VPC endpoints** tab.

1. In the **Authorized principals** section, choose **Authorize account**.

1. In the **AWS account ID** field, enter the 12-digit number account ID, and then select **Authorize**.

### Grant connecting accounts access to a pipeline (CLI)
<a name="cross-account-pipelines-setting-up-grant-access-cli"></a>

Use the following procedure to grant connecting accounts access to a pipeline by using the AWS CLI.

**To grant connecting accounts access to the pipeline**

1. Update to the latest version of the AWS CLI (version 2.0). For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. Open the CLI in the account and AWS Region with the pipeline you want to share.

1. Run the following command to create a resource policy for the pipeline. This policy gives the `osis:CreatePipelineEndpoint` permission on the pipeline. The policy includes a parameter where you can list AWS account IDs to allow.
**Note**  
In the following command, you must use the short form of the account ID by providing only the twelve- digit account ID. Using an ARN will not work. You must also provide the Amazon Resource Name (ARN) of the pipeline in the CLI parameter for `resource-arn` and in the policy JSON under `Resource`, as shown.

   ```
   aws --region {{region}} osis put-resource-policy \
     --resource-arn arn:aws:osis:{{region}}:{{pipeline-owner-account-ID}}:pipeline/{{pipeline-name}}
     --policy '{{IAM-policy}}'
   ```

   Use a policy like the following for {{IAM-policy}}

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
     {
     "Sid": "AllowAccess",
     "Effect": "Allow",
     "Principal": {
     "AWS": [
     "{{111122223333}}",
     "{{444455556666}}"
     ]
     },
     "Action": 
     "osis:CreatePipelineEndpoint",
     "Resource": "arn:aws:osis:{{us-east-1}}:{{123456789012}}:pipeline/{{pipeline-name}}"
     }
     ]
    }
   ```

------

## Create a pipeline endpoint connection for each connecting VPC
<a name="cross-account-pipelines-setting-up-create-pipeline-endpoints"></a>

After the pipeline owner grants access to a pipeline in their VPC using the previous procedure, a user in the connecting account creates a pipeline endpoint in their VPC. This section includes procedures for creating endpoints by using the OpenSearch Service console and the AWS CLI. When you create an endpoint, OpenSearch Ingestion performs the following actions:
+ Creates the [AWSServiceRoleForAmazonOpenSearchIngestionService](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr-osis.html) service-linked role in your account, if it doesn't already exist. This role gives the user in the connecting account permission to call the [CreatePipelineEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_CreatePipelineEndpoint.html) API action.
+ Creates the pipeline endpoint.
+ Configures the pipeline endpoint to ingest data from the shared pipeline in the pipeline owner VPC.

**Topics**
+ [Creating a pipeline endpoint connection (console)](#cross-account-pipelines-setting-up-create-pipeline-endpoints-console)
+ [Creating a pipeline endpoint connection (CLI)](#cross-account-pipelines-setting-up-create-pipeline-endpoints-cli)

### Creating a pipeline endpoint connection (console)
<a name="cross-account-pipelines-setting-up-create-pipeline-endpoints-console"></a>

Use the following procedure to create a pipeline endpoint connection by using the OpenSearch Service console.

**To create a pipeline endpoint connection**

1. In the Amazon OpenSearch Service console, in the navigation pane, expand **Ingestion**, and then select **VPC endpoints**.

1. In the **VPC endpoints** page, choose **Create**.

1. For **Pipeline location**, choose an option. If you choose **Current account**, choose the pipeline from the list. If you choose **Cross-account**, specify the pipeline ARN in the field. The pipeline owner must have granted access to the pipeline, as described in [Grant connecting accounts access to a pipeline](#cross-account-pipelines-setting-up-grant-access). 

1. In the **VPC settings** section, for **VPC**, choose a VPC from the list.

1. For **Subnets**, choose a subnet.

1. For **Security groups**, choose a group.

1. Choose **Create endpoint**.

Wait for the status of the endpoint you created to transition to `ACTIVE`. Once the pipeline is `ACTIVE`, you will see a new field named `ingestEndpointUrl`. Use this endpoint to access the pipeline and ingest data using a client like FluentBit. For more information about using FluentBit to ingest data, see [Using an OpenSearch Ingestion pipeline with Fluent Bit](configure-client-fluentbit.md).

**Note**  
The `ingestEndpointUrl` is the same URL for all connecting accounts.

### Creating a pipeline endpoint connection (CLI)
<a name="cross-account-pipelines-setting-up-create-pipeline-endpoints-cli"></a>

Use the following procedure to crate a pipeline endpoint connection by using the AWS CLI.

**To create a pipeline endpoint connection**

1. If you haven't already, update to the latest version of the AWS CLI (version 2.0). For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. Open the CLI in the connecting account in the AWS Region with the shared pipeline.

1. Run the following command to create a pipeline endpoint.
**Note**  
You must provide at least one subnet and one security group for the connecting account VPC. The security group must include port 443 and support clients in connecting account VPC.

   ```
   aws osis --region {{region}} create-pipeline-endpoint \
     --pipeline-arn arn:aws:osis:{{region}}:{{connecting-account-ID}}:pipeline/{{shared-pipeline-name}}
     --vpc-options SecurityGroupIds={sg-{{security-group-ID-1}},sg-{{security-group-ID-2}}},SubnetIds=subnet-{{subnet-ID}}
   ```

1. Run the following command to list endpoints in the Region specified in the previous command:

   ```
   aws osis --region {{region}} list-pipeline-endpoints
   ```

Wait for the status of the endpoint you created to transition to `ACTIVE`. Once the pipeline is `ACTIVE`, you will see a new field named `ingestEndpointUrl`. Use this endpoint to access the pipeline and ingest data using a client like FluentBit. For more information about using FluentBit to ingest data, see [Using an OpenSearch Ingestion pipeline with Fluent Bit](configure-client-fluentbit.md).

**Note**  
The `ingestEndpointUrl` is the same URL for all connecting accounts.

## Removing pipeline endpoints
<a name="cross-account-pipelines-remove"></a>

If you no longer want to provide access to a shared pipeline, you can remove a pipeline endpoint using one of the following methods:
+ Delete the pipeline endpoint (connecting account).
+ Revoke the pipeline endpoint (pipeline owner).

Use the following procedure to delete a pipeline endpoint in a connecting account.

**To delete a pipeline endpoint (connecting account)**

1. Open the CLI in the connecting account in the AWS Region with the shared pipeline.

1. Run the following command to list pipeline endpoints in the Region:

   ```
   aws osis --region {{region}} list-pipeline-endpoints
   ```

   Make a note of the pipeline ID you want to delete.

1. Run the following command to delete the pipeline endpoint:

   ```
   aws osis --region {{region}} delete-pipeline-endpoint \
     --endpoint-id '{{ID}}'
   ```

As the pipeline owner of the shared pipeline, use the following procedure to revoke a pipeline endpoint.

**To revoke a pipeline endpoint (pipeline owner)**

1. Open the CLI in the connecting account in the AWS Region with the shared pipeline.

1. Run the following command to list pipeline endpoint connections in the Region:

   ```
   aws osis --region {{region}} list-pipeline-endpoint-connections
   ```

   Make a note of the pipeline ID you want to delete.

1. Run the following command to delete the pipeline endpoint:

   ```
   aws osis --region {{region}} revoke-pipeline-endpoint-connections \
     --pipeline-arn {{pipeline-arn}} --endpoint-ids {{ID}}
   ```

   The command supports specifying only one endpoint ID.