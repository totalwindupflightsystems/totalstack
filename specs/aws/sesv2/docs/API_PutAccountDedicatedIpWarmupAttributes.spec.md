---
id: "@specs/aws/sesv2/docs/API_PutAccountDedicatedIpWarmupAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAccountDedicatedIpWarmupAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutAccountDedicatedIpWarmupAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutAccountDedicatedIpWarmupAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAccountDedicatedIpWarmupAttributes
<a name="API_PutAccountDedicatedIpWarmupAttributes"></a>

Enable or disable the automatic warm-up feature for dedicated IP addresses.

## Request Syntax
<a name="API_PutAccountDedicatedIpWarmupAttributes_RequestSyntax"></a>

```
PUT /v2/email/account/dedicated-ips/warmup HTTP/1.1
Content-type: application/json

{
   "AutoWarmupEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutAccountDedicatedIpWarmupAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountDedicatedIpWarmupAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AutoWarmupEnabled](#API_PutAccountDedicatedIpWarmupAttributes_RequestSyntax) **   <a name="SES-PutAccountDedicatedIpWarmupAttributes-request-AutoWarmupEnabled"></a>
Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon SES account in the current AWS Region. Set to `true` to enable the automatic warm-up feature, or set to `false` to disable it.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_PutAccountDedicatedIpWarmupAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAccountDedicatedIpWarmupAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccountDedicatedIpWarmupAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_PutAccountDedicatedIpWarmupAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutAccountDedicatedIpWarmupAttributes) 