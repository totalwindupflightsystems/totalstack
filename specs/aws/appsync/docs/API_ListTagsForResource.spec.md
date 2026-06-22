---
id: "@specs/aws/appsync/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists the tags for a resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /v1/tags/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="appsync-ListTagsForResource-request-uri-resourceArn"></a>
The `GraphqlApi` Amazon Resource Name (ARN).  
Length Constraints: Minimum length of 70. Maximum length of 75.  
Pattern: `^arn:aws:appsync:[A-Za-z0-9_/.-]{0,63}:\d{12}:apis/[0-9A-Za-z_-]{26}$`   
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="appsync-ListTagsForResource-response-tags"></a>
A `TagMap` object.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$` 

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to perform this operation on this resource.  
HTTP Status Code: 403

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
The request exceeded a limit. Try your request again.  
HTTP Status Code: 429

 ** NotFoundException **   
The resource specified in the request was not found. Check the resource, and then try again.  
HTTP Status Code: 404

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/ListTagsForResource) 