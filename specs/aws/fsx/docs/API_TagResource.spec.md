---
id: "@specs/aws/fsx/docs/API_TagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TagResource"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# TagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_TagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TagResource
<a name="API_TagResource"></a>

Tags an Amazon FSx resource.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_TagResource_RequestSyntax) **   <a name="FSx-TagResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the Amazon FSx resource that you want to tag.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="FSx-TagResource-request-Tags"></a>
A list of tags for the resource. If a tag with a given key already exists, the value is replaced by the one specified in this parameter.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** NotServiceResourceError **   
The resource specified for the tagging operation is not a resource type owned by Amazon FSx. Use the API of the relevant service to perform the operation.     
 ** Message **   
A detailed error message.  
 ** ResourceARN **   
The Amazon Resource Name (ARN) of the non-Amazon FSx resource.
HTTP Status Code: 400

 ** ResourceDoesNotSupportTagging **   
The resource specified does not support tagging.     
 ** Message **   
A detailed error message.  
 ** ResourceARN **   
The Amazon Resource Name (ARN) of the resource that doesn't support tagging.
HTTP Status Code: 400

 ** ResourceNotFound **   
The resource specified by the Amazon Resource Name (ARN) can't be found.    
 ** Message **   
A detailed error message.  
 ** ResourceARN **   
The resource ARN of the resource that can't be found.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/TagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/TagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/TagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/TagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/TagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/TagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/TagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/TagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/TagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/TagResource) 