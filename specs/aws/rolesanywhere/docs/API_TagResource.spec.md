---
id: "@specs/aws/rolesanywhere/docs/API_TagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TagResource"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# TagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_TagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TagResource
<a name="API_TagResource"></a>

Attaches tags to a resource.

 **Required permissions: ** `rolesanywhere:TagResource`. 

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /TagResource HTTP/1.1
Content-type: application/json

{
   "resourceArn": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
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

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="rolesanywhere-TagResource-request-resourceArn"></a>
The ARN of the resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="rolesanywhere-TagResource-request-tags"></a>
The tags to attach to the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The resource could not be found.  
HTTP Status Code: 404

 ** TooManyTagsException **   
Too many tags.  
HTTP Status Code: 400

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/TagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/TagResource) 