---
id: "@specs/aws/network-firewall/docs/API_DisassociateAvailabilityZones"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateAvailabilityZones"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DisassociateAvailabilityZones

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DisassociateAvailabilityZones
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateAvailabilityZones
<a name="API_DisassociateAvailabilityZones"></a>

Removes the specified Availability Zone associations from a transit gateway-attached firewall. This removes the firewall endpoints from these Availability Zones and stops traffic filtering in those zones. Before removing an Availability Zone, ensure you've updated your transit gateway route tables to redirect traffic appropriately.

**Note**  
If `AvailabilityZoneChangeProtection` is enabled, you must first disable it using [UpdateAvailabilityZoneChangeProtection](API_UpdateAvailabilityZoneChangeProtection.md).

To verify the status of your Availability Zone changes, use [DescribeFirewall](API_DescribeFirewall.md).

## Request Syntax
<a name="API_DisassociateAvailabilityZones_RequestSyntax"></a>

```
{
   "AvailabilityZoneMappings": [ 
      { 
         "AvailabilityZone": "{{string}}"
      }
   ],
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}",
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateAvailabilityZones_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZoneMappings](#API_DisassociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-request-AvailabilityZoneMappings"></a>
Required. The Availability Zones to remove from the firewall's configuration.  
Type: Array of [AvailabilityZoneMapping](API_AvailabilityZoneMapping.md) objects  
Required: Yes

 ** [FirewallArn](#API_DisassociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_DisassociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [UpdateToken](#API_DisassociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-request-UpdateToken"></a>
An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request.   
To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.  
To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: No

## Response Syntax
<a name="API_DisassociateAvailabilityZones_ResponseSyntax"></a>

```
{
   "AvailabilityZoneMappings": [ 
      { 
         "AvailabilityZone": "string"
      }
   ],
   "FirewallArn": "string",
   "FirewallName": "string",
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_DisassociateAvailabilityZones_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailabilityZoneMappings](#API_DisassociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-response-AvailabilityZoneMappings"></a>
The remaining Availability Zones where the firewall has endpoints after the disassociation.  
Type: Array of [AvailabilityZoneMapping](API_AvailabilityZoneMapping.md) objects

 ** [FirewallArn](#API_DisassociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FirewallName](#API_DisassociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-response-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

 ** [UpdateToken](#API_DisassociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-DisassociateAvailabilityZones-response-UpdateToken"></a>
An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request.   
To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.  
To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_DisassociateAvailabilityZones_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidTokenException **   
The token you provided is stale or isn't valid for the operation.   
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_DisassociateAvailabilityZones_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DisassociateAvailabilityZones) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DisassociateAvailabilityZones) 