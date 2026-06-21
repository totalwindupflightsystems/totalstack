---
id: "@specs/aws/shield/docs/API_DisableApplicationLayerAutomaticResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisableApplicationLayerAutomaticResponse"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DisableApplicationLayerAutomaticResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DisableApplicationLayerAutomaticResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisableApplicationLayerAutomaticResponse
<a name="API_DisableApplicationLayerAutomaticResponse"></a>

Disable the Shield Advanced automatic application layer DDoS mitigation feature for the protected resource. This stops Shield Advanced from creating, verifying, and applying AWS WAF rules for attacks that it detects for the resource. 

## Request Syntax
<a name="API_DisableApplicationLayerAutomaticResponse_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DisableApplicationLayerAutomaticResponse_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DisableApplicationLayerAutomaticResponse_RequestSyntax) **   <a name="AWSShield-DisableApplicationLayerAutomaticResponse-request-ResourceArn"></a>
The ARN (Amazon Resource Name) of the protected resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: Yes

## Response Elements
<a name="API_DisableApplicationLayerAutomaticResponse_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisableApplicationLayerAutomaticResponse_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidOperationException **   
Exception that indicates that the operation would not cause any change to occur.  
HTTP Status Code: 400

 ** InvalidParameterException **   
Exception that indicates that the parameters passed to the API are invalid. If available, this exception includes details in additional properties.     
 ** fields **   
Fields that caused the exception.  
 ** reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** OptimisticLockException **   
Exception that indicates that the resource state has been modified by another client. Retrieve the resource and then retry your request.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DisableApplicationLayerAutomaticResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DisableApplicationLayerAutomaticResponse) 