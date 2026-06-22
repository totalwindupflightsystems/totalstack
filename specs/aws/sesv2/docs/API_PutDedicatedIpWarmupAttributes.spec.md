---
id: "@specs/aws/sesv2/docs/API_PutDedicatedIpWarmupAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutDedicatedIpWarmupAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutDedicatedIpWarmupAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutDedicatedIpWarmupAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutDedicatedIpWarmupAttributes
<a name="API_PutDedicatedIpWarmupAttributes"></a>



## Request Syntax
<a name="API_PutDedicatedIpWarmupAttributes_RequestSyntax"></a>

```
PUT /v2/email/dedicated-ips/{{IP}}/warmup HTTP/1.1
Content-type: application/json

{
   "WarmupPercentage": {{number}}
}
```

## URI Request Parameters
<a name="API_PutDedicatedIpWarmupAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IP](#API_PutDedicatedIpWarmupAttributes_RequestSyntax) **   <a name="SES-PutDedicatedIpWarmupAttributes-request-uri-Ip"></a>
The dedicated IP address that you want to update the warm-up attributes for.  
Required: Yes

## Request Body
<a name="API_PutDedicatedIpWarmupAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [WarmupPercentage](#API_PutDedicatedIpWarmupAttributes_RequestSyntax) **   <a name="SES-PutDedicatedIpWarmupAttributes-request-WarmupPercentage"></a>
The warm-up percentage that you want to associate with the dedicated IP address.  
Type: Integer  
Required: Yes

## Response Syntax
<a name="API_PutDedicatedIpWarmupAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutDedicatedIpWarmupAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutDedicatedIpWarmupAttributes_Errors"></a>

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
<a name="API_PutDedicatedIpWarmupAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutDedicatedIpWarmupAttributes) 