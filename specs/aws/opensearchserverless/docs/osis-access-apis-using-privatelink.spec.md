---
id: "@specs/aws/opensearchserverless/docs/osis-access-apis-using-privatelink"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VPC endpoints (AWS PrivateLink)"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# VPC endpoints (AWS PrivateLink)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/osis-access-apis-using-privatelink
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Amazon OpenSearch Ingestion and interface endpoints API (AWS PrivateLink)
<a name="osis-access-apis-using-privatelink"></a>

You can establish a private connection between your VPC and OpenSearch Ingestion API endpoints by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink). 

AWS PrivateLink enables you to privately access OpenSearch Ingestion API operations without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Resources in your VPC don't need public IP addresses to communicate with OpenSearch Ingestion API endpoints to create, modify, or delete pipelines. Traffic between your VPC and OpenSearch Ingestion doesn't leave the Amazon network. 

**Note**  
This topic covers VPC endpoints for accessing the OpenSearch Ingestion *API*, which allows you to manage pipelines (create, update, delete) from within your VPC. This is different from configuring VPC access *for pipelines themselves*, which controls how data is ingested into pipelines from sources within your VPC. For information about configuring VPC access for pipelines, see [Configuring VPC access for Amazon OpenSearch Ingestion pipelines](pipeline-security.md).

Each interface endpoint is represented by one or more elastic network interfaces in your subnets. For more information on elastic network interfaces, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide.* 

For more information about VPC endpoints, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. For more information about OpenSearch Ingestion API operations, see the [OpenSearch Ingestion API reference](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Operations_Amazon_OpenSearch_Ingestion.html).

## Considerations for VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for OpenSearch Ingestion API endpoints, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

All OpenSearch Ingestion API operations relevant to managing OpenSearch Ingestion resources are available from your VPC using AWS PrivateLink.

VPC endpoint policies are supported for OpenSearch Ingestion API endpoints. By default, full access to OpenSearch Ingestion API operations is allowed through the endpoint. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

## Availability
<a name="osis-vpc-interface-endpoints-availability"></a>

OpenSearch Ingestion API currently supports VPC endpoints in all OpenSearch Ingestion Regions.

At this time, FIPS endpoints are not supported.

## Creating an interface VPC endpoint for OpenSearch Ingestion API
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the OpenSearch Ingestion API using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for OpenSearch Ingestion API using the service name `com.amazonaws.{{region}}.osis`.

If you enable private DNS for the endpoint, you can make API requests to OpenSearch Ingestion with the VPC endpoint using its default DNS name for the AWS Region, for example `osis.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for OpenSearch Ingestion API
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to OpenSearch Ingestion API. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for OpenSearch Ingestion API actions**  
The following is an example of an endpoint policy for OpenSearch Ingestion API. When attached to an endpoint, this policy grants access to the listed OpenSearch Ingestion API actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "osis:CreatePipeline",
            "osis:UpdatePipeline",
            "osis:DeletePipeline"
         ],
         "Resource":"*"
      }
   ]
}
```

**Example: VPC endpoint policy that denies all access from a specified AWS account**  
The following VPC endpoint policy denies AWS account `123456789012` all access to resources using the endpoint. The policy allows all actions from other accounts.

```
{
  "Statement": [
    {
      "Action": "*",
      "Effect": "Allow",
      "Resource": "*",
      "Principal": "*"
    },
    {
      "Action": "*",
      "Effect": "Deny",
      "Resource": "*",
      "Principal": { "AWS": [ "123456789012" ] }
     }
   ]
}
```