---
id: "@specs/aws/quicksight/docs/API_DeleteActionConnector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteActionConnector"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteActionConnector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteActionConnector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteActionConnector
<a name="API_DeleteActionConnector"></a>

Hard deletes an action connector, making it unrecoverable. This operation removes the connector and all its associated configurations. Any resources currently using this action connector will no longer be able to perform actions through it.

## Request Syntax
<a name="API_DeleteActionConnector_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/action-connectors/{{ActionConnectorId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteActionConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ActionConnectorId](#API_DeleteActionConnector_RequestSyntax) **   <a name="QS-DeleteActionConnector-request-uri-ActionConnectorId"></a>
The unique identifier of the action connector to delete.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AwsAccountId](#API_DeleteActionConnector_RequestSyntax) **   <a name="QS-DeleteActionConnector-request-uri-AwsAccountId"></a>
The AWS account ID that contains the action connector to delete.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DeleteActionConnector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteActionConnector_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "ActionConnectorId": "string",
   "Arn": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteActionConnector_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteActionConnector_ResponseSyntax) **   <a name="QS-DeleteActionConnector-response-Status"></a>
The HTTP status code of the request.

The following data is returned in JSON format by the service.

 ** [ActionConnectorId](#API_DeleteActionConnector_ResponseSyntax) **   <a name="QS-DeleteActionConnector-response-ActionConnectorId"></a>
The unique identifier of the deleted action connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [Arn](#API_DeleteActionConnector_ResponseSyntax) **   <a name="QS-DeleteActionConnector-response-Arn"></a>
The Amazon Resource Name (ARN) of the deleted action connector.  
Type: String

 ** [RequestId](#API_DeleteActionConnector_ResponseSyntax) **   <a name="QS-DeleteActionConnector-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DeleteActionConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_DeleteActionConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteActionConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteActionConnector) 