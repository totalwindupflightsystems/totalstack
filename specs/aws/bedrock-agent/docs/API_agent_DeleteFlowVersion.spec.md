---
id: "@specs/aws/bedrock-agent/docs/API_agent_DeleteFlowVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFlowVersion"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# DeleteFlowVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_DeleteFlowVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFlowVersion
<a name="API_agent_DeleteFlowVersion"></a>

Deletes a version of a flow.

## Request Syntax
<a name="API_agent_DeleteFlowVersion_RequestSyntax"></a>

```
DELETE /flows/{{flowIdentifier}}/versions/{{flowVersion}}/?skipResourceInUseCheck={{skipResourceInUseCheck}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_DeleteFlowVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowIdentifier](#API_agent_DeleteFlowVersion_RequestSyntax) **   <a name="bedrock-agent_DeleteFlowVersion-request-uri-flowIdentifier"></a>
The unique identifier of the flow whose version that you want to delete  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

 ** [flowVersion](#API_agent_DeleteFlowVersion_RequestSyntax) **   <a name="bedrock-agent_DeleteFlowVersion-request-uri-flowVersion"></a>
The version of the flow that you want to delete.  
Pattern: `[0-9]{1,5}`   
Required: Yes

 ** [skipResourceInUseCheck](#API_agent_DeleteFlowVersion_RequestSyntax) **   <a name="bedrock-agent_DeleteFlowVersion-request-uri-skipResourceInUseCheck"></a>
By default, this value is `false` and deletion is stopped if the resource is in use. If you set it to `true`, the resource will be deleted even if the resource is in use.

## Request Body
<a name="API_agent_DeleteFlowVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_DeleteFlowVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_DeleteFlowVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_agent_DeleteFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_DeleteFlowVersion-response-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [version](#API_agent_DeleteFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_DeleteFlowVersion-response-version"></a>
The version of the flow being deleted.  
Type: String  
Pattern: `[0-9]{1,5}` 

## Errors
<a name="API_agent_DeleteFlowVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
There was a conflict performing an operation.  
HTTP Status Code: 409

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

## See Also
<a name="API_agent_DeleteFlowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/DeleteFlowVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeleteFlowVersion) 