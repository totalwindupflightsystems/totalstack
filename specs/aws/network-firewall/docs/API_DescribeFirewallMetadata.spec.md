---
id: "@specs/aws/network-firewall/docs/API_DescribeFirewallMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeFirewallMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeFirewallMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeFirewallMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeFirewallMetadata
<a name="API_DescribeFirewallMetadata"></a>

Returns the high-level information about a firewall, including the Availability Zones where the Firewall is currently in use. 

## Request Syntax
<a name="API_DescribeFirewallMetadata_RequestSyntax"></a>

```
{
   "FirewallArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFirewallMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallArn](#API_DescribeFirewallMetadata_RequestSyntax) **   <a name="networkfirewall-DescribeFirewallMetadata-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

## Response Syntax
<a name="API_DescribeFirewallMetadata_ResponseSyntax"></a>

```
{
   "Description": "string",
   "FirewallArn": "string",
   "FirewallPolicyArn": "string",
   "Status": "string",
   "SupportedAvailabilityZones": { 
      "string" : { 
         "IPAddressType": "string"
      }
   },
   "TransitGatewayAttachmentId": "string"
}
```

## Response Elements
<a name="API_DescribeFirewallMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DescribeFirewallMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallMetadata-response-Description"></a>
A description of the firewall.  
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$` 

 ** [FirewallArn](#API_DescribeFirewallMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallMetadata-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FirewallPolicyArn](#API_DescribeFirewallMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallMetadata-response-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the firewall policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [Status](#API_DescribeFirewallMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallMetadata-response-Status"></a>
The readiness of the configured firewall to handle network traffic across all of the Availability Zones where you have it configured. This setting is `READY` only when the `ConfigurationSyncStateSummary` value is `IN_SYNC` and the `Attachment` `Status` values for all of the configured subnets are `READY`.   
Type: String  
Valid Values: `PROVISIONING | DELETING | READY` 

 ** [SupportedAvailabilityZones](#API_DescribeFirewallMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallMetadata-response-SupportedAvailabilityZones"></a>
The Availability Zones that the firewall currently supports. This includes all Availability Zones for which the firewall has a subnet defined.   
Type: String to [AvailabilityZoneMetadata](API_AvailabilityZoneMetadata.md) object map

 ** [TransitGatewayAttachmentId](#API_DescribeFirewallMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallMetadata-response-TransitGatewayAttachmentId"></a>
The unique identifier of the transit gateway attachment associated with this firewall. This field is only present for transit gateway-attached firewalls.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^tgw-attach-[0-9a-z]+$` 

## Errors
<a name="API_DescribeFirewallMetadata_Errors"></a>

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
<a name="API_DescribeFirewallMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeFirewallMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeFirewallMetadata) 