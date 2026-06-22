---
id: "@specs/aws/sesv2/docs/API_PutEmailIdentityDkimAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutEmailIdentityDkimAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutEmailIdentityDkimAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutEmailIdentityDkimAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutEmailIdentityDkimAttributes
<a name="API_PutEmailIdentityDkimAttributes"></a>

Used to enable or disable DKIM authentication for an email identity.

## Request Syntax
<a name="API_PutEmailIdentityDkimAttributes_RequestSyntax"></a>

```
PUT /v2/email/identities/{{EmailIdentity}}/dkim HTTP/1.1
Content-type: application/json

{
   "SigningEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutEmailIdentityDkimAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_PutEmailIdentityDkimAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityDkimAttributes-request-uri-EmailIdentity"></a>
The email identity.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_PutEmailIdentityDkimAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SigningEnabled](#API_PutEmailIdentityDkimAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityDkimAttributes-request-SigningEnabled"></a>
Sets the DKIM signing configuration for the identity.  
When you set this value `true`, then the messages that are sent from the identity are signed using DKIM. If you set this value to `false`, your messages are sent without DKIM signing.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_PutEmailIdentityDkimAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutEmailIdentityDkimAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutEmailIdentityDkimAttributes_Errors"></a>

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
<a name="API_PutEmailIdentityDkimAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutEmailIdentityDkimAttributes) 