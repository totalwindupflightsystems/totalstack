---
id: "@specs/aws/opensearchserverless/docs/serverless-vpc"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Data plane VPC endpoint"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Data plane VPC endpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-vpc
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Data plane access through AWS PrivateLink
<a name="serverless-vpc"></a>

Amazon OpenSearch Serverless supports two types of AWS PrivateLink connections for control plane and data plane operations. Control plane operations include the creation and deletion of collections and the management of access policies. Data plane operations are for indexing and querying data within a collection. This page covers data plane VPC endpoints. For information about control plane AWS PrivateLink endpoints, see [Control plane access through AWS PrivateLink](serverless-vpc-cp.md).

You can use AWS PrivateLink to create a private connection between your VPC and Amazon OpenSearch Serverless. You can access OpenSearch Serverless as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access OpenSearch Serverless. For more information on VPC network access, see [Network connectivity patterns for Amazon OpenSearch Serverless](https://aws.amazon.com/blogs/big-data/network-connectivity-patterns-for-amazon-opensearch-serverless/).

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you specify for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for OpenSearch Serverless.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

**Topics**
+ [VPC endpoint creation methods](#vpc-endpoint-creation-methods)
+ [DNS resolution of Classic collection endpoints](#vpc-endpoint-dnc)
+ [VPCs and network access policies](#vpc-endpoint-network)
+ [VPCs and endpoint policies](#vpc-endpoint-policy)
+ [Considerations](#vpc-endpoint-considerations)
+ [Permissions required](#serverless-vpc-permissions)
+ [Create a standard AWS PrivateLink interface endpoint (OpenSearch Serverless NextGen)](#serverless-vpc-create-standard)
+ [Create an OpenSearch Serverless-managed interface endpoint (OpenSearch Serverless Classic)](#serverless-vpc-create)
+ [Shared VPC setup for Amazon OpenSearch Serverless](#shared-vpc-setup)

## VPC endpoint creation methods
<a name="vpc-endpoint-creation-methods"></a>

Amazon OpenSearch Serverless supports two ways to create a data plane VPC endpoint, depending on which type of collection endpoint you want to access. For more information about collection endpoint formats, see [Collection endpoints for Amazon OpenSearch Serverless](serverless-collection-endpoints.md).
+ **Standard AWS PrivateLink VPC endpoint (NextGen)** – Use this method to access the OpenSearch Serverless NextGen collection endpoints on `on.aws` (per-collection and per-account formats). You create the VPC endpoint through the Amazon VPC console or the Amazon EC2 `CreateVpcEndpoint` API, the same way you create an interface VPC endpoint for any other AWS service. To create this type of endpoint, see [Create a standard AWS PrivateLink interface endpoint (OpenSearch Serverless NextGen)](#serverless-vpc-create-standard).
+ **OpenSearch Serverless-managed VPC endpoint (Classic)** – Use this method to access OpenSearch Serverless Classic per-collection endpoints on `aoss.amazonaws.com`. You create the VPC endpoint through the OpenSearch Serverless console, the OpenSearch Serverless `CreateVpcEndpoint` API, or the OpenSearch Serverless AWS CLI. The service creates the interface VPC endpoint and a Amazon Route 53 private hosted zone in your account on your behalf. To create this type of endpoint, see [Create an OpenSearch Serverless-managed interface endpoint (OpenSearch Serverless Classic)](#serverless-vpc-create).

## DNS resolution of Classic collection endpoints
<a name="vpc-endpoint-dnc"></a>

When you create a data plane VPC endpoint through the OpenSearch Serverless console, the service creates a new Amazon Route 53 [private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html) and attaches it to the VPC. This private hosted zone consists of a record to resolve the wildcard DNS record for OpenSearch Serverless collections (`*.us-east-1.aoss.amazonaws.com`) to the interface addresses used for the endpoint. You only need one OpenSearch Serverless VPC endpoint in a VPC to access any and all collections and Dashboards in each AWS Region. Every VPC with an endpoint for OpenSearch Serverless has its own private hosted zone attached.

**Note**  
A single VPC endpoint does not provide Multi-AZ redundancy. If high availability is required, consider deploying VPC endpoints in multiple subnets across different Availability Zones.

The OpenSearch Serverless interface endpoint also creates a public Route 53 wildcard DNS record for all collections in the Region. The DNS name resolves to the OpenSearch Serverless public IP addresses. Clients in VPCs that don't have an OpenSearch Serverless VPC endpoint or clients in public networks can use the public Route 53 resolver and access the collections and Dashboards with those IP addresses. The IP address type (IPv4, IPv6, or Dualstack) of VPC endpoint is determined based on the subnets provided when you [create an interface endpoint for OpenSearch Serverless](#serverless-vpc-create).

**Note**  
OpenSearch Serverless creates an additonal Amazon Route 53 private hosted zone (``<region>.opensearch.amazonaws.com``) for an OpenSearch Service domain resolution. You can update your existing IPv4 VPC endpoint to Dualstack by using the [update-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/update-vpc-endpoint.html) command in the AWS CLI.

The DNS resolver address for a given VPC is the second IP address of the VPC CIDR. Any client in the VPC needs to use that resolver to get the VPC endpoint address for any collection. The resolver uses private hosted zone created by OpenSearch Serverless. It's sufficient to use that resolver for all collections in any account. It's also possible to use the VPC resolver for some collection endpoints and the public resolver for others, although it's not typically necessary.

## VPCs and network access policies
<a name="vpc-endpoint-network"></a>

To grant network permission to OpenSearch APIs and Dashboards for your collections, you can use OpenSearch Serverless [network access policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html). You can control this network access either from your VPC endpoint(s) or the public internet. Since your network policy only controls traffic permissions, you must also set up a [data access policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) that specifies permission to operate on the data in a collection and its indices. Think of an OpenSearch Serverless VPC endpoint as an access point to the service, a network access policy as the network-level access point to collections and Dashboards, and a data access policy as the access point for fine-grained access control for any operation on data in the collection. 

Since you can specify multiple VPC endpoint IDs in a network policy, we recommend that you create a VPC endpoint for every VPC that needs to access a collection. These VPCs can belong to different AWS accounts than the account that owns the OpenSearch Serverless collection and network policy. We don't recommend that you create a VPC-to-VPC peering or other proxying solution between two accounts so that one account's VPC can use another account's VPC endpoint. This is less secure and cost effective than each VPC having its own endpoint. The first VPC will not be easily visible to the other VPC's admin, who has set up access to that VPC's endpoint in the network policy. 

## VPCs and endpoint policies
<a name="vpc-endpoint-policy"></a>

 Amazon OpenSearch Serverless supports endpoint policies for VPCs. An endpoint policy is an IAM resource-based policy that you attach to a VPC endpoint to control which AWS principals can use the endpoint to access your AWS service. For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html). 

To use an endpoint policy, you must first create an interface endpoint. You can create an interface endpoint using either the OpenSearch Serverless console or the OpenSearch Serverless API. After you create your interface endpoint, you will need to add the endpoint policy to the endpoint. For more information, see [Create an OpenSearch Serverless-managed interface endpoint (OpenSearch Serverless Classic)](#serverless-vpc-create).

**Note**  
You can't define an endpoint policy directly in the OpenSearch Service console. 

An endpoint policy does not override or replace other identity-based policies, resource-based policies, network policies, or data access policies you may have configured. For more information on updating endpoint policies, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html).

By default, an endpoint policy grants full access to your VPC endpoint. 

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

Although the default VPC endpoint policy grants full endpoint access, you can configure a VPC endpoint policy to allow access to specific roles and users. To do this, see the following example:

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
                "AWS": [
                    "{{123456789012}}",
                    "{{987654321098}}"
                ]
            },
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

------

You can specify an OpenSearch Serverless collection to be included as a conditional element in your VPC endpoint policy. To do this, see the following example:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aoss:collection": [
                        "{{coll-abc}}"
                    ]
                }
            }
        }
    ]
}
```

------

Support for `aoss:CollectionId` is supported.

```
Condition": {
         "StringEquals": {
               "aoss:CollectionId": "collection-id"
          }
}
```

You can use SAML identities in your VPC endpoint policy to determine VPC endpoint access. You must use a wildcard `(*)` in the principal section of your VPC endpoint policy. To do this, see the following example:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "saml:cn": [
                        "{{saml/111122223333/idp123/group/football}}",
                        "{{saml/111122223333/idp123/group/soccer}}",
                        "{{saml/111122223333/idp123/group/cricket}}"
                    ]
                }
            }
        }
    ]
}
```

------

Additionally, you can configure your endpoint policy to include a specific SAML principal policy. To do this, see the following:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalTag/Department": [
                        "{{Engineering}}"]
                    }
                }
            }
        ]
    }
```

------

For more information on using SAML authentication with Amazon OpenSearch Serverless, see [SAML authentication for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html).

You can also include IAM and SAML users in the same VPC endpoint policy. To do this, see the following example:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "saml:cn": [
                        "{{saml/{{111122223333}}/idp123/group/football}}",
                        "{{saml/{{111122223333}}/idp123/group/soccer}}",
                        "{{saml/{{111122223333}}/idp123/group/cricket}}"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "{{111122223333}}"
                ]
            },
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

------

You can also access an Amazon OpenSearch Serverless collection from Amazon EC2 via interface VPC endpoints. For more information see, [Access an OpenSearch Serverless collection from Amazon EC2 (via interface VPC endpoints)](https://aws.amazon.com/blogs/big-data/network-connectivity-patterns-for-amazon-opensearch-serverless/).

## Considerations
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for OpenSearch Serverless, consider the following:
+ OpenSearch Serverless supports making calls to all supported [OpenSearch API operations](serverless-genref.md#serverless-operations) (not configuration API operations) through the interface endpoint.
+ After you create an interface endpoint for OpenSearch Serverless, you still need to include it in [network access policies](serverless-network.md) in order for it to access serverless collections.
+ By default, full access to OpenSearch Serverless is allowed through the interface endpoint. You can associate a security group with the endpoint network interfaces to control traffic to OpenSearch Serverless through the interface endpoint.
+ A single AWS account can have a maximum of 50 OpenSearch Serverless VPC endpoints.
+ If you enable public internet access to your collection's API or Dashboards in a network policy, your collection is accessible by any VPC and by the public internet.
+ If you're on-premises and outside of the VPC, you can't use a DNS resolver for the OpenSearch Serverless VPC endpoint resolution directly. If you need VPN access, the VPC needs a DNS proxy resolver for external clients to use. Route 53 provides an inbound endpoint option that you can use to resolve DNS queries to your VPC from your on-premises network or another VPC.
+ The private hosted zone that OpenSearch Serverless creates and attaches to the VPC is managed by the service, but it shows up in your Amazon Route 53 resources and is billed to your account.
+ For other considerations, see [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

## Permissions required
<a name="serverless-vpc-permissions"></a>

VPC access for OpenSearch Serverless uses the following AWS Identity and Access Management (IAM) permissions. You can specify IAM conditions to restrict users to specific collections.
+ `aoss:CreateVpcEndpoint` – Create a VPC endpoint.
+ `aoss:ListVpcEndpoints` – List all VPC endpoints.
+ `aoss:BatchGetVpcEndpoint` – See details about a subset of VPC endpoints.
+ `aoss:UpdateVpcEndpoint` – Modify a VPC endpoint.
+ `aoss:DeleteVpcEndpoint` – Delete a VPC endpoint.

In addition, you need the following Amazon EC2 and Route 53 permissions in order to create a VPC endpoint.
+ `ec2:CreateTags`
+ `ec2:CreateVpcEndpoint`
+ `ec2:DeleteVpcEndPoints`
+ `ec2:DescribeSecurityGroups`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeVpcEndpoints`
+ `ec2:DescribeVpcs`
+ `ec2:ModifyVpcEndPoint`
+ `route53:AssociateVPCWithHostedZone`
+ `route53:ChangeResourceRecordSets`
+ `route53:CreateHostedZone`
+ `route53:DeleteHostedZone`
+ `route53:GetChange`
+ `route53:GetHostedZone`
+ `route53:ListHostedZonesByName`
+ `route53:ListHostedZonesByVPC`
+ `route53:ListResourceRecordSets`

## Create a standard AWS PrivateLink interface endpoint (OpenSearch Serverless NextGen)
<a name="serverless-vpc-create-standard"></a>

For OpenSearch Serverless NextGen collection endpoints on `on.aws`, you create the VPC endpoint as a standard interface VPC endpoint – the same way you do for any other AWS service. You can use the Amazon VPC console or the Amazon EC2 `CreateVpcEndpoint` API. You don't need to use the OpenSearch Serverless `CreateVpcEndpoint` API for these endpoints.

The endpoint resolves all collections in the Region under `*.aoss.{{region}}.on.aws` (and `*.aoss-fips.{{region}}.on.aws` in Regions where FIPS is supported).

Use the following service name when you create the VPC endpoint:

```
com.amazonaws.{{region}}.aoss-data
```

For example, in the `{{us-east-1}}` Region, the service name is `com.amazonaws.{{us-east-1}}.aoss-data`.

**To create a standard interface VPC endpoint for OpenSearch Serverless NextGen**

1. Follow the procedure in [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

1. For the service name, choose `com.amazonaws.{{region}}.aoss-data`.

1. Select the VPC, subnets, and security groups for the endpoint. Make sure your security groups allow inbound HTTPS (port 443) traffic from the resources that will use the endpoint.

1. Enable private DNS for the endpoint to use AWS PrivateLink-managed DNS resolution for OpenSearch Serverless NextGen collection hostnames.

After you create the endpoint, you can use the `vpce-{{abc123def4EXAMPLE}}` ID in OpenSearch Serverless [network access policies](serverless-network.md) to grant the endpoint access to your collections, the same way you do for OpenSearch Serverless-managed VPC endpoints.

## Create an OpenSearch Serverless-managed interface endpoint (OpenSearch Serverless Classic)
<a name="serverless-vpc-create"></a>

For OpenSearch Serverless Classic per-collection endpoints on `aoss.amazonaws.com`, you create an OpenSearch Serverless-managed interface endpoint using either the OpenSearch Serverless console or the OpenSearch Serverless API.

**To create an interface endpoint for an OpenSearch Serverless Classic collection**

1. Open the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, expand **Serverless** and choose **VPC endpoints**.

1. Choose **Create VPC endpoint**.

1. Provide a name for the endpoint.

1. For **VPC**, select the VPC that you'll access OpenSearch Serverless from.

1. For **Subnets**, select one subnet that you'll access OpenSearch Serverless from.
   + Endpoint's IP address and DNS type is based on subnet type
     + Dualstack: If all subnets have both IPv4 and IPv6 address ranges
     + IPv6: If all subnets are IPv6 only subnets
     + IPv4: If all subnets have IPv4 address ranges

1. For **Security groups**, select the security groups to associate with the endpoint network interfaces. This is a critical step where you limit the ports, protocols, and sources for inbound traffic that you're authorizing into your endpoint. Make sure that the security group rules allow the resources that will use the VPC endpoint to communicate with OpenSearch Serverless to communicate with the endpoint network interface.

1. Choose **Create endpoint**.

To create a VPC endpoint using the OpenSearch Serverless API, use the `CreateVpcEndpoint` command.

**Note**  
After you create an endpoint, note its ID (for example, `vpce-abc123def4EXAMPLE`. In order to provide the endpoint access to your collections, you must include this ID in one or more network access policies. 

After you create an interface endpoint, you must provide it access to collections through network access policies. For more information, see [Network access for Amazon OpenSearch Serverless](serverless-network.md).

## Shared VPC setup for Amazon OpenSearch Serverless
<a name="shared-vpc-setup"></a>

You can use Amazon Virtual Private Cloud (VPC) to share VPC subnets with other AWS accounts in your organization, as well as share networking infrastructure such as a VPN between resources in multiple AWS accounts. 

Currently, Amazon OpenSearch Serverless doesn't support creating an AWS PrivateLink connection into a shared VPC unless you are an owner of that VPC. AWS PrivateLink also doesn't support sharing connections between AWS accounts. 

However, based on the flexible and modular architecture of OpenSearch Serverless, you can still set up a shared VPC. This is because the OpenSearch Serverless networking infrastructure is separate from that of the individual collection (OpenSearch Service) infrastructure. You can therefore create an AWS PrivateLink VPCe endpoint for one account where a VPC located, and then use a VPCe ID in the network policy of other accounts to restrict traffic to come only from that shared VPC. 

The following procedures refer to an *owner account* and a *consumer account*.

An owner account acts as a common networking account where you set up a VPC and share it with other accounts. Consumer accounts are those accounts that create and maintain their OpenSearch Serverless collections in the VPC shared with them by the owner account. 

**Prerequisites**  
Ensure the following requirements are met before setting up the shared VPC:
+ The intended owner account must have already set up a VPC, subnets, route table, and other required resources in Amazon Virtual Private Cloud. For more information, see the *[Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/)*.
+ The intended owner account and consumer accounts must belong to the same organization in AWS Organizations. For more information, see the *[AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/)*.

**To set up a shared VPC in an owner account/common networking account.**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. Follow the steps in [Create an OpenSearch Serverless-managed interface endpoint (OpenSearch Serverless Classic)](#serverless-vpc-create). As you do, make the following selections:
   + Select a VPC and subnets that are shared with the consumer accounts in your organization.

1. After you create the endpoint, make a note of the VPCe ID that is generated and provide it to the administrators who are to perform the setup task in consumer accounts.

   VPCe IDs are in the format `vpce-abc123def4EXAMPLE`.

**To set up a shared VPC in a consumer account**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. Use the information in [Managing Amazon OpenSearch Serverless collections](serverless-manage.md) to create a collection, if you don't have one already.

1. Use the information in [Creating network policies (console)](serverless-network.md#serverless-network-console) to create a network policy. As you do, make the following selections.
**Note**  
You can also update an existing network policy for this purpose.

   1. For **Access type**, select **VPC (recommended)**.

   1. For **VPC endpoints for access**, choose the VPCe ID provided to you by the owner account, in the format `vpce-abc123def4EXAMPLE`.

   1. In the **Resource type** area, do the following:
      + Select the **Enable access to OpenSearch endpoint** box, and then select the collection name or collection pattern to use to enable access from that shared VPC.
      + Select the **Enable access to OpenSearch Dashboard** box, and then select the collection name or collection pattern to use to enable access from that shared VPC.

1. For a new policy, choose **Create**. For an existing policy, choose **Update**.