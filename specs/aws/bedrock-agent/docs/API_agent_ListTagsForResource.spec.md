---
id: "@specs/aws/bedrock-agent/docs/API_agent_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_agent_ListTagsForResource"></a>

List all the tags for the resource you specify.

## Request Syntax
<a name="API_agent_ListTagsForResource_RequestSyntax"></a>

```
GET /tags/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_agent_ListTagsForResource_RequestSyntax) **   <a name="bedrock-agent_ListTagsForResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource for which to list tags.  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `.*(^arn:aws:bedrock:[a-zA-Z0-9-]+:/d{12}:(agent|agent-alias|knowledge-base|flow|prompt)/[A-Z0-9]{10}(?:/[A-Z0-9]{10})?$|^arn:aws:bedrock:[a-zA-Z0-9-]+:/d{12}:flow/([A-Z0-9]{10})/alias/([A-Z0-9]{10})$|^arn:aws:bedrock:[a-zA-Z0-9-]+:/d{12}:prompt/([A-Z0-9]{10})?(?::/d+)?$).*`   
Required: Yes

## Request Body
<a name="API_agent_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_ListTagsForResource_ResponseSyntax"></a>

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
<a name="API_agent_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_agent_ListTagsForResource_ResponseSyntax) **   <a name="bedrock-agent_ListTagsForResource-response-tags"></a>
The key-value pairs for the tags associated with the resource.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

## Errors
<a name="API_agent_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## Examples
<a name="API_agent_ListTagsForResource_Examples"></a>

### Example request
<a name="API_agent_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

```
GET /tags/arn:aws:bedrock:us-west-2:123456789012:agent/ABCDEFGHIJ HTTP/1.1
```

## See Also
<a name="API_agent_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ListTagsForResource) 