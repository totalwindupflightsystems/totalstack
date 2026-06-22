---
id: "@specs/aws/codepipeline/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Gets the set of key-value pairs (metadata) that are used to manage the resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTagsForResource_RequestSyntax) **   <a name="CodePipeline-ListTagsForResource-request-maxResults"></a>
The maximum number of results to return in a single call.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="CodePipeline-ListTagsForResource-request-nextToken"></a>
The token that was returned from the previous API call, which would be used to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use pagination.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="CodePipeline-ListTagsForResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to get tags for.  
Type: String  
Pattern: `arn:aws(-[\w]+)*:codepipeline:.+:[0-9]{12}:.+`   
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tags": [ 
      { 
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="CodePipeline-ListTagsForResource-response-nextToken"></a>
If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent API call to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use pagination.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="CodePipeline-ListTagsForResource-response-tags"></a>
The tags for the resource.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **   
The specified resource ARN is invalid.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The resource was specified in an invalid format.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ListTagsForResource) 