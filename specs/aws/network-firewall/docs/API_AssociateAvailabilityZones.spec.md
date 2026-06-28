---
id: "@specs/aws/network-firewall/docs/API_AssociateAvailabilityZones"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateAvailabilityZones"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# AssociateAvailabilityZones

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_AssociateAvailabilityZones
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateAvailabilityZones
<a name="API_AssociateAvailabilityZones"></a>

Associates the specified Availability Zones with a transit gateway-attached firewall. For each Availability Zone, Network Firewall creates a firewall endpoint to process traffic. You can specify one or more Availability Zones where you want to deploy the firewall.

After adding Availability Zones, you must update your transit gateway route tables to direct traffic through the new firewall endpoints. Use [DescribeFirewall](API_DescribeFirewall.md) to monitor the status of the new endpoints.

## Request Syntax
<a name="API_AssociateAvailabilityZones_RequestSyntax"></a>

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
<a name="API_AssociateAvailabilityZones_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZoneMappings](#API_AssociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-request-AvailabilityZoneMappings"></a>
Required. The Availability Zones where you want to create firewall endpoints. You must specify at least one Availability Zone.  
Type: Array of [AvailabilityZoneMapping](API_AvailabilityZoneMapping.md) objects  
Required: Yes

 ** [FirewallArn](#API_AssociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_AssociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [UpdateToken](#API_AssociateAvailabilityZones_RequestSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-request-UpdateToken"></a>
An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request.   
To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.  
To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: No

## Response Syntax
<a name="API_AssociateAvailabilityZones_ResponseSyntax"></a>

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
<a name="API_AssociateAvailabilityZones_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailabilityZoneMappings](#API_AssociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-response-AvailabilityZoneMappings"></a>
The Availability Zones where Network Firewall created firewall endpoints. Each mapping specifies an Availability Zone where the firewall processes traffic.  
Type: Array of [AvailabilityZoneMapping](API_AvailabilityZoneMapping.md) objects

 ** [FirewallArn](#API_AssociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FirewallName](#API_AssociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-response-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

 ** [UpdateToken](#API_AssociateAvailabilityZones_ResponseSyntax) **   <a name="networkfirewall-AssociateAvailabilityZones-response-UpdateToken"></a>
An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request.   
To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.  
To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_AssociateAvailabilityZones_Errors"></a>

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
<a name="API_AssociateAvailabilityZones_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/AssociateAvailabilityZones) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AssociateAvailabilityZones) 