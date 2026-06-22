---
id: "@specs/aws/bedrock/docs/API_agent_PrepareFlow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PrepareFlow"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# PrepareFlow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_PrepareFlow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PrepareFlow
<a name="API_agent_PrepareFlow"></a>

Prepares the `DRAFT` version of a flow so that it can be invoked. For more information, see [Test a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_PrepareFlow_RequestSyntax"></a>

```
POST /flows/{{flowIdentifier}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_PrepareFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowIdentifier](#API_agent_PrepareFlow_RequestSyntax) **   <a name="bedrock-agent_PrepareFlow-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent_PrepareFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_PrepareFlow_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "id": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_agent_PrepareFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [id](#API_agent_PrepareFlow_ResponseSyntax) **   <a name="bedrock-agent_PrepareFlow-response-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [status](#API_agent_PrepareFlow_ResponseSyntax) **   <a name="bedrock-agent_PrepareFlow-response-status"></a>
The status of the flow. When you submit this request, the status will be `NotPrepared`. If preparation succeeds, the status becomes `Prepared`. If it fails, the status becomes `FAILED`.  
Type: String  
Valid Values: `Failed | Prepared | Preparing | NotPrepared` 

## Errors
<a name="API_agent_PrepareFlow_Errors"></a>

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

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 402

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_PrepareFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/PrepareFlow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PrepareFlow) 