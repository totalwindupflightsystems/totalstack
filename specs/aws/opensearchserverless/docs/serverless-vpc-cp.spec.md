---
id: "@specs/aws/opensearchserverless/docs/serverless-vpc-cp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Control plane VPC endpoint"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Control plane VPC endpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-vpc-cp
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Control plane access through AWS PrivateLink
<a name="serverless-vpc-cp"></a>

Amazon OpenSearch Serverless supports two types of AWS PrivateLink connections for control plane and data plane operations. Control plane operations include the creation and deletion of collections and the management of access policies. Data plane operations are for indexing and querying data within a collection. This page covers the control plane AWS PrivateLink endpoint. For information about data plane VPC endpoints, see [Data plane access through AWS PrivateLink](serverless-vpc.md).

## Creating a control plane AWS PrivateLink endpoint
<a name="serverless-vpc-privatelink"></a>

You can improve the security posture of your VPC by configuring OpenSearch Serverless to use an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink. This technology enables you to privately access OpenSearch Serverless APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

For more information about AWS PrivateLink and VPC endpoints, see [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html#concepts-vpc-endpoints) in the Amazon VPC User Guide.

### Considerations
<a name="serverless-vpc-cp-considerations"></a>
+ VPC endpoints are supported within the same Region only.
+ VPC endpoints only support Amazon-provided DNS through Amazon Route 53.
+ VPC endpoints support endpoint policies to control access to OpenSearch Serverless Collections, Policies and VpcEndpoints.
+ OpenSearch Serverless supports interface endpoints only. Gateway endpoints are not supported.

### Creating the VPC endpoint
<a name="serverless-vpc-cp-create"></a>

To create the control plane VPC endpoint for Amazon OpenSearch Serverless, use the [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) procedure in the *Amazon VPC Developer Guide*. Create the following endpoint:
+ `com.amazonaws.{{region}}.aoss`

**To create a control plane VPC endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create Endpoint**.

1. For **Service category**, choose **AWS services**.

1. For **Services**, choose `com.amazonaws.{{region}}.aoss`. For example, `com.amazonaws.us-east-1.aoss`.

1. For **VPC**, choose the VPC in which to create the endpoint.

1. For **Subnets**, choose the subnets (Availability Zones) in which to create the endpoint network interfaces.

1. For **Security groups**, choose the security groups to associate with the endpoint network interfaces. Ensure HTTPS (port 443) is allowed.

1. For **Policy**, choose **Full access** to allow all operations, or choose **Custom** to attach a custom policy.

1. Choose **Create endpoint**.

### Creating an endpoint policy
<a name="serverless-vpc-cp-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon OpenSearch Serverless. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

**Example VPC endpoint policy for OpenSearch Serverless**  

```
{  
  "Version": "2012-10-17",		 	 	   
  "Statement": [  
    {  
      "Effect": "Allow",  
      "Principal": "*",  
      "Action": [  
        "aoss:ListCollections",  
        "aoss:BatchGetCollection"  
      ],  
      "Resource": "*"  
    }  
  ]  
}
```

**Example Restrictive policy allowing only list operations**  

```
{  
  "Version": "2012-10-17",		 	 	   
  "Statement": [  
    {  
      "Effect": "Allow",  
      "Principal": "*",  
      "Action": "aoss:ListCollections",  
      "Resource": "*"  
    }  
  ]  
}
```