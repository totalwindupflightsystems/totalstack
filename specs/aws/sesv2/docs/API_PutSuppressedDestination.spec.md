---
id: "@specs/aws/sesv2/docs/API_PutSuppressedDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutSuppressedDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutSuppressedDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutSuppressedDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutSuppressedDestination
<a name="API_PutSuppressedDestination"></a>

Adds an email address to the suppression list for your account or for a specific tenant. To target a tenant's suppression list, specify the `TenantName` parameter. If you omit `TenantName`, the address is added to the account-level suppression list.

## Request Syntax
<a name="API_PutSuppressedDestination_RequestSyntax"></a>

```
PUT /v2/email/suppression/addresses HTTP/1.1
Content-type: application/json

{
   "EmailAddress": "{{string}}",
   "Reason": "{{string}}",
   "TenantName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutSuppressedDestination_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutSuppressedDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EmailAddress](#API_PutSuppressedDestination_RequestSyntax) **   <a name="SES-PutSuppressedDestination-request-EmailAddress"></a>
The email address that should be added to the suppression list for your account or for the specified tenant.  
Type: String  
Required: Yes

 ** [Reason](#API_PutSuppressedDestination_RequestSyntax) **   <a name="SES-PutSuppressedDestination-request-Reason"></a>
The factors that should cause the email address to be added to the suppression list for your account or for the specified tenant.  
Type: String  
Valid Values: `BOUNCE | COMPLAINT`   
Required: Yes

 ** [TenantName](#API_PutSuppressedDestination_RequestSyntax) **   <a name="SES-PutSuppressedDestination-request-TenantName"></a>
The name of the tenant whose suppression list you want to add the address to. If you omit this parameter, the address is added to the account-level suppression list.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_PutSuppressedDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutSuppressedDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutSuppressedDestination_Errors"></a>

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
<a name="API_PutSuppressedDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutSuppressedDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutSuppressedDestination) 