---
id: "@specs/aws/sesv2/docs/API_TagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TagResource"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# TagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_TagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TagResource
<a name="API_TagResource"></a>

Add one or more tags (keys and values) to a specified resource. A *tag* is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value*, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /v2/email/tags HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_TagResource_RequestSyntax) **   <a name="SES-TagResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that you want to add one or more tags to.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="SES-TagResource-request-Tags"></a>
A list of the tags that you want to add to the resource. A tag consists of a required tag key (`Key`) and an associated tag value (`Value`). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.  
Type: Array of [Tag](API_Tag.md) objects  
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

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
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/TagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/TagResource) 