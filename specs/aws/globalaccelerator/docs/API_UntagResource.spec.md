---
id: "@specs/aws/globalaccelerator/docs/API_UntagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UntagResource"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# UntagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_UntagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UntagResource
<a name="API_UntagResource"></a>

Remove tags from a Global Accelerator resource. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from an accelerator that was already removed.

For more information, see [Tagging in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="globalaccelerator-UntagResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the Global Accelerator resource to remove tags from. An ARN uniquely identifies a resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="globalaccelerator-UntagResource-request-TagKeys"></a>
The tag key pairs that you want to remove from the specified resources.  
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

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_UntagResource_Examples"></a>

### Remove tags from an accelerator
<a name="API_UntagResource_Example_1"></a>

The following is an example for removing tags from an accelerator. When successful, this command has no output.

```
aws globalaccelerator untag-resource 
       --resource-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh 
       --tag-keys Key="Name" Key="Project"
```

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/UntagResource) 