---
id: "@specs/aws/sesv2/docs/API_DeleteSuppressedDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteSuppressedDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DeleteSuppressedDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DeleteSuppressedDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteSuppressedDestination
<a name="API_DeleteSuppressedDestination"></a>

Removes an email address from the suppression list for your account or for a specific tenant. To target a tenant's suppression list, specify the `TenantName` parameter. If you omit `TenantName`, the address is removed from the account-level suppression list.

## Request Syntax
<a name="API_DeleteSuppressedDestination_RequestSyntax"></a>

```
DELETE /v2/email/suppression/addresses/{{EmailAddress}}?TenantName={{TenantName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSuppressedDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailAddress](#API_DeleteSuppressedDestination_RequestSyntax) **   <a name="SES-DeleteSuppressedDestination-request-uri-EmailAddress"></a>
The suppressed email destination to remove from the suppression list for your account or for the specified tenant.  
Required: Yes

 ** [TenantName](#API_DeleteSuppressedDestination_RequestSyntax) **   <a name="SES-DeleteSuppressedDestination-request-uri-TenantName"></a>
The name of the tenant whose suppression list you want to remove the address from. If you omit this parameter, the address is removed from the account-level suppression list.  
Length Constraints: Minimum length of 1.

## Request Body
<a name="API_DeleteSuppressedDestination_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSuppressedDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteSuppressedDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteSuppressedDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_DeleteSuppressedDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteSuppressedDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeleteSuppressedDestination) 