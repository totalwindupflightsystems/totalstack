---
id: "@specs/aws/quicksight/docs/API_DeleteFlow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFlow"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteFlow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteFlow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFlow
<a name="API_DeleteFlow"></a>

Permanently deletes a flow from the specified AWS account. This operation cannot be undone.

## Request Syntax
<a name="API_DeleteFlow_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/flows/{{FlowId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteFlow_RequestSyntax) **   <a name="QS-DeleteFlow-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the flow that you are deleting.  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: Yes

 ** [FlowId](#API_DeleteFlow_RequestSyntax) **   <a name="QS-DeleteFlow-request-uri-FlowId"></a>
The unique identifier of the flow to delete.  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

## Request Body
<a name="API_DeleteFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteFlow_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteFlow_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteFlow_ResponseSyntax) **   <a name="QS-DeleteFlow-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DeleteFlow_ResponseSyntax) **   <a name="QS-DeleteFlow-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DeleteFlow_Errors"></a>

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
<a name="API_DeleteFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteFlow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteFlow) 