---
id: "@specs/aws/sesv2/docs/API_PutDedicatedIpPoolScalingAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutDedicatedIpPoolScalingAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutDedicatedIpPoolScalingAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutDedicatedIpPoolScalingAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutDedicatedIpPoolScalingAttributes
<a name="API_PutDedicatedIpPoolScalingAttributes"></a>

Used to convert a dedicated IP pool to a different scaling mode.

**Note**  
 `MANAGED` pools cannot be converted to `STANDARD` scaling mode.

## Request Syntax
<a name="API_PutDedicatedIpPoolScalingAttributes_RequestSyntax"></a>

```
PUT /v2/email/dedicated-ip-pools/{{PoolName}}/scaling HTTP/1.1
Content-type: application/json

{
   "ScalingMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutDedicatedIpPoolScalingAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PoolName](#API_PutDedicatedIpPoolScalingAttributes_RequestSyntax) **   <a name="SES-PutDedicatedIpPoolScalingAttributes-request-uri-PoolName"></a>
The name of the dedicated IP pool.  
Required: Yes

## Request Body
<a name="API_PutDedicatedIpPoolScalingAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ScalingMode](#API_PutDedicatedIpPoolScalingAttributes_RequestSyntax) **   <a name="SES-PutDedicatedIpPoolScalingAttributes-request-ScalingMode"></a>
The scaling mode to apply to the dedicated IP pool.  
Changing the scaling mode from `MANAGED` to `STANDARD` is not supported.
Type: String  
Valid Values: `STANDARD | MANAGED`   
Required: Yes

## Response Syntax
<a name="API_PutDedicatedIpPoolScalingAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutDedicatedIpPoolScalingAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutDedicatedIpPoolScalingAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** ConcurrentModificationException **   
The resource is being modified by another operation or thread.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_PutDedicatedIpPoolScalingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutDedicatedIpPoolScalingAttributes) 