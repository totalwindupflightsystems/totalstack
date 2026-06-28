---
id: "@specs/aws/quicksight/docs/API_DeleteAgent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAgent"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteAgent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteAgent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAgent
<a name="API_DeleteAgent"></a>

Deletes an agent.

## Request Syntax
<a name="API_DeleteAgent_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/agents/{{AgentId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AgentId](#API_DeleteAgent_RequestSyntax) **   <a name="QS-DeleteAgent-request-uri-AgentId"></a>
The unique identifier for the agent to delete.  
Required: Yes

 ** [AwsAccountId](#API_DeleteAgent_RequestSyntax) **   <a name="QS-DeleteAgent-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the agent.  
Required: Yes

## Request Body
<a name="API_DeleteAgent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DeleteAgent_ResponseSyntax) **   <a name="QS-DeleteAgent-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DeleteAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DeleteAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteAgent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteAgent) 