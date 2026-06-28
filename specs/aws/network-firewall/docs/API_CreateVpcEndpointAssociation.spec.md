---
id: "@specs/aws/network-firewall/docs/API_CreateVpcEndpointAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateVpcEndpointAssociation"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CreateVpcEndpointAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CreateVpcEndpointAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateVpcEndpointAssociation
<a name="API_CreateVpcEndpointAssociation"></a>

Creates a firewall endpoint for an AWS Network Firewall firewall. This type of firewall endpoint is independent of the firewall endpoints that you specify in the `Firewall` itself, and you define it in addition to those endpoints after the firewall has been created. You can define a VPC endpoint association using a different VPC than the one you used in the firewall specifications. 

## Request Syntax
<a name="API_CreateVpcEndpointAssociation_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "FirewallArn": "{{string}}",
   "SubnetMapping": { 
      "IPAddressType": "{{string}}",
      "SubnetId": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateVpcEndpointAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateVpcEndpointAssociation_RequestSyntax) **   <a name="networkfirewall-CreateVpcEndpointAssociation-request-Description"></a>
A description of the VPC endpoint association.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** [FirewallArn](#API_CreateVpcEndpointAssociation_RequestSyntax) **   <a name="networkfirewall-CreateVpcEndpointAssociation-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [SubnetMapping](#API_CreateVpcEndpointAssociation_RequestSyntax) **   <a name="networkfirewall-CreateVpcEndpointAssociation-request-SubnetMapping"></a>
The ID for a subnet that's used in an association with a firewall. This is used in [CreateFirewall](API_CreateFirewall.md), [AssociateSubnets](API_AssociateSubnets.md), and [CreateVpcEndpointAssociation](#API_CreateVpcEndpointAssociation). AWS Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnet's Availability Zone.  
Type: [SubnetMapping](API_SubnetMapping.md) object  
Required: Yes

 ** [Tags](#API_CreateVpcEndpointAssociation_RequestSyntax) **   <a name="networkfirewall-CreateVpcEndpointAssociation-request-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [VpcId](#API_CreateVpcEndpointAssociation_RequestSyntax) **   <a name="networkfirewall-CreateVpcEndpointAssociation-request-VpcId"></a>
The unique identifier of the VPC where you want to create a firewall endpoint.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^vpc-[0-9a-f]+$`   
Required: Yes

## Response Syntax
<a name="API_CreateVpcEndpointAssociation_ResponseSyntax"></a>

```
{
   "VpcEndpointAssociation": { 
      "Description": "string",
      "FirewallArn": "string",
      "SubnetMapping": { 
         "IPAddressType": "string",
         "SubnetId": "string"
      },
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "VpcEndpointAssociationArn": "string",
      "VpcEndpointAssociationId": "string",
      "VpcId": "string"
   },
   "VpcEndpointAssociationStatus": { 
      "AssociationSyncState": { 
         "string" : { 
            "Attachment": { 
               "EndpointId": "string",
               "Status": "string",
               "StatusMessage": "string",
               "SubnetId": "string"
            }
         }
      },
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_CreateVpcEndpointAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcEndpointAssociation](#API_CreateVpcEndpointAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateVpcEndpointAssociation-response-VpcEndpointAssociation"></a>
The configuration settings for the VPC endpoint association. These settings include the firewall and the VPC and subnet to use for the firewall endpoint.   
Type: [VpcEndpointAssociation](API_VpcEndpointAssociation.md) object

 ** [VpcEndpointAssociationStatus](#API_CreateVpcEndpointAssociation_ResponseSyntax) **   <a name="networkfirewall-CreateVpcEndpointAssociation-response-VpcEndpointAssociationStatus"></a>
Detailed information about the current status of a [VpcEndpointAssociation](API_VpcEndpointAssociation.md). You can retrieve this by calling [DescribeVpcEndpointAssociation](API_DescribeVpcEndpointAssociation.md) and providing the VPC endpoint association ARN.  
Type: [VpcEndpointAssociationStatus](API_VpcEndpointAssociationStatus.md) object

## Errors
<a name="API_CreateVpcEndpointAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientCapacityException **   
 AWS doesn't currently have enough available capacity to fulfill your request. Try your request later.   
HTTP Status Code: 500

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidOperationException **   
The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.  
HTTP Status Code: 400

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** LimitExceededException **   
Unable to perform the operation because doing so would violate a limit setting.   
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_CreateVpcEndpointAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateVpcEndpointAssociation) 