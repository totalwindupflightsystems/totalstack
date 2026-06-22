---
id: "@specs/aws/sesv2/docs/API_PutEmailIdentityConfigurationSetAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutEmailIdentityConfigurationSetAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutEmailIdentityConfigurationSetAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutEmailIdentityConfigurationSetAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutEmailIdentityConfigurationSetAttributes
<a name="API_PutEmailIdentityConfigurationSetAttributes"></a>

Used to associate a configuration set with an email identity.

## Request Syntax
<a name="API_PutEmailIdentityConfigurationSetAttributes_RequestSyntax"></a>

```
PUT /v2/email/identities/{{EmailIdentity}}/configuration-set HTTP/1.1
Content-type: application/json

{
   "ConfigurationSetName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutEmailIdentityConfigurationSetAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_PutEmailIdentityConfigurationSetAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityConfigurationSetAttributes-request-uri-EmailIdentity"></a>
The email address or domain to associate with a configuration set.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_PutEmailIdentityConfigurationSetAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_PutEmailIdentityConfigurationSetAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityConfigurationSetAttributes-request-ConfigurationSetName"></a>
The configuration set to associate with an email identity.  
Type: String  
Required: No

## Response Syntax
<a name="API_PutEmailIdentityConfigurationSetAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutEmailIdentityConfigurationSetAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutEmailIdentityConfigurationSetAttributes_Errors"></a>

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
<a name="API_PutEmailIdentityConfigurationSetAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutEmailIdentityConfigurationSetAttributes) 