---
id: "@specs/aws/network-firewall/docs/API_DescribeVpcEndpointAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeVpcEndpointAssociation"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeVpcEndpointAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeVpcEndpointAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeVpcEndpointAssociation
<a name="API_DescribeVpcEndpointAssociation"></a>

Returns the data object for the specified VPC endpoint association. 

## Request Syntax
<a name="API_DescribeVpcEndpointAssociation_RequestSyntax"></a>

```
{
   "VpcEndpointAssociationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeVpcEndpointAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VpcEndpointAssociationArn](#API_DescribeVpcEndpointAssociation_RequestSyntax) **   <a name="networkfirewall-DescribeVpcEndpointAssociation-request-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

## Response Syntax
<a name="API_DescribeVpcEndpointAssociation_ResponseSyntax"></a>

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
<a name="API_DescribeVpcEndpointAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VpcEndpointAssociation](#API_DescribeVpcEndpointAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeVpcEndpointAssociation-response-VpcEndpointAssociation"></a>
The configuration settings for the VPC endpoint association. These settings include the firewall and the VPC and subnet to use for the firewall endpoint.   
Type: [VpcEndpointAssociation](API_VpcEndpointAssociation.md) object

 ** [VpcEndpointAssociationStatus](#API_DescribeVpcEndpointAssociation_ResponseSyntax) **   <a name="networkfirewall-DescribeVpcEndpointAssociation-response-VpcEndpointAssociationStatus"></a>
Detailed information about the current status of a [VpcEndpointAssociation](API_VpcEndpointAssociation.md). You can retrieve this by calling [DescribeVpcEndpointAssociation](#API_DescribeVpcEndpointAssociation) and providing the VPC endpoint association ARN.  
Type: [VpcEndpointAssociationStatus](API_VpcEndpointAssociationStatus.md) object

## Errors
<a name="API_DescribeVpcEndpointAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeVpcEndpointAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeVpcEndpointAssociation) 