---
id: "@specs/aws/network-firewall/docs/API_UpdateFirewallEncryptionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFirewallEncryptionConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateFirewallEncryptionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateFirewallEncryptionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFirewallEncryptionConfiguration
<a name="API_UpdateFirewallEncryptionConfiguration"></a>

A complex type that contains settings for encryption of your firewall resources.

## Request Syntax
<a name="API_UpdateFirewallEncryptionConfiguration_RequestSyntax"></a>

```
{
   "EncryptionConfiguration": { 
      "KeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}",
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateFirewallEncryptionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EncryptionConfiguration](#API_UpdateFirewallEncryptionConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-request-EncryptionConfiguration"></a>
A complex type that contains optional AWS Key Management Service (KMS) encryption settings for your Network Firewall resources. Your data is encrypted by default with an AWS owned key that AWS owns and manages for you. You can use either the AWS owned key, or provide your own customer managed key. To learn more about KMS encryption of your Network Firewall resources, see [Encryption at rest with AWS Key Managment Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-encryption-at-rest.html) in the *Network Firewall Developer Guide*.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** [FirewallArn](#API_UpdateFirewallEncryptionConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_UpdateFirewallEncryptionConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [UpdateToken](#API_UpdateFirewallEncryptionConfiguration_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-request-UpdateToken"></a>
An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request.   
To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.  
To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: No

## Response Syntax
<a name="API_UpdateFirewallEncryptionConfiguration_ResponseSyntax"></a>

```
{
   "EncryptionConfiguration": { 
      "KeyId": "string",
      "Type": "string"
   },
   "FirewallArn": "string",
   "FirewallName": "string",
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_UpdateFirewallEncryptionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EncryptionConfiguration](#API_UpdateFirewallEncryptionConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-response-EncryptionConfiguration"></a>
A complex type that contains optional AWS Key Management Service (KMS) encryption settings for your Network Firewall resources. Your data is encrypted by default with an AWS owned key that AWS owns and manages for you. You can use either the AWS owned key, or provide your own customer managed key. To learn more about KMS encryption of your Network Firewall resources, see [Encryption at rest with AWS Key Managment Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-encryption-at-rest.html) in the *Network Firewall Developer Guide*.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [FirewallArn](#API_UpdateFirewallEncryptionConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FirewallName](#API_UpdateFirewallEncryptionConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-response-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

 ** [UpdateToken](#API_UpdateFirewallEncryptionConfiguration_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallEncryptionConfiguration-response-UpdateToken"></a>
An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request.   
To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.  
To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_UpdateFirewallEncryptionConfiguration_Errors"></a>

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

 ** InvalidTokenException **   
The token you provided is stale or isn't valid for the operation.   
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ResourceOwnerCheckException **   
Unable to change the resource because your account doesn't own it.   
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateFirewallEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateFirewallEncryptionConfiguration) 