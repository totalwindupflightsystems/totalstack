---
id: "@specs/aws/shield/docs/API_UntagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UntagResource"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# UntagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_UntagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UntagResource
<a name="API_UntagResource"></a>

Removes tags from a resource in AWS Shield.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_UntagResource_RequestSyntax) **   <a name="AWSShield-UntagResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource that you want to remove tags from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="AWSShield-UntagResource-request-TagKeys"></a>
The tag key for each tag that you want to remove from the resource.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
Exception that indicates that the parameters passed to the API are invalid. If available, this exception includes details in additional properties.     
 ** fields **   
Fields that caused the exception.  
 ** reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** InvalidResourceException **   
Exception that indicates that the resource is invalid. You might not have access to the resource, or the resource might not exist.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/UntagResource) 