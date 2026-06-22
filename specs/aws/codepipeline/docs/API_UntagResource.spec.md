---
id: "@specs/aws/codepipeline/docs/API_UntagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UntagResource"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# UntagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_UntagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UntagResource
<a name="API_UntagResource"></a>

Removes tags from an AWS resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}",
   "tagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="CodePipeline-UntagResource-request-resourceArn"></a>
 The Amazon Resource Name (ARN) of the resource to remove tags from.  
Type: String  
Pattern: `arn:aws(-[\w]+)*:codepipeline:.+:[0-9]{12}:.+`   
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="CodePipeline-UntagResource-request-tagKeys"></a>
The list of keys for the tags to be removed from the resource.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **   
Unable to modify the tag due to a simultaneous update request.  
HTTP Status Code: 400

 ** InvalidArnException **   
The specified resource ARN is invalid.  
HTTP Status Code: 400

 ** InvalidTagsException **   
The specified resource tags are invalid.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The resource was specified in an invalid format.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/UntagResource) 