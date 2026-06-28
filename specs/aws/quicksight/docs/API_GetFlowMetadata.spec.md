---
id: "@specs/aws/quicksight/docs/API_GetFlowMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetFlowMetadata"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# GetFlowMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_GetFlowMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetFlowMetadata
<a name="API_GetFlowMetadata"></a>

Retrieves the metadata of a flow, not including its definition specifying the steps.

## Request Syntax
<a name="API_GetFlowMetadata_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/flows/{{FlowId}}/metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFlowMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_GetFlowMetadata_RequestSyntax) **   <a name="QS-GetFlowMetadata-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the flow that you are getting metadata for.  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: Yes

 ** [FlowId](#API_GetFlowMetadata_RequestSyntax) **   <a name="QS-GetFlowMetadata-request-uri-FlowId"></a>
The unique identifier of the flow.  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: Yes

## Request Body
<a name="API_GetFlowMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFlowMetadata_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreatedTime": number,
   "Description": "string",
   "FlowId": "string",
   "LastUpdatedTime": number,
   "Name": "string",
   "PublishState": "string",
   "RequestId": "string",
   "RunCount": number,
   "UserCount": number
}
```

## Response Elements
<a name="API_GetFlowMetadata_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-Arn"></a>
The Amazon Resource Name (ARN) of the flow.  
Type: String

 ** [CreatedTime](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-CreatedTime"></a>
The time this flow was created.  
Type: Timestamp

 ** [FlowId](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-FlowId"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}` 

 ** [Name](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-Name"></a>
A display name for the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Description](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-Description"></a>
The description for the flow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastUpdatedTime](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-LastUpdatedTime"></a>
The last time this flow was modified.  
Type: Timestamp

 ** [PublishState](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-PublishState"></a>
The publish state for the flow. Valid values are `DRAFT`, `PUBLISHED`, or `PENDING_APPROVAL`.  
Type: String  
Valid Values: `PUBLISHED | DRAFT | PENDING_APPROVAL` 

 ** [RequestId](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [RunCount](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-RunCount"></a>
The number of runs done for the flow.  
Type: Integer

 ** [UserCount](#API_GetFlowMetadata_ResponseSyntax) **   <a name="QS-GetFlowMetadata-response-UserCount"></a>
The number of users who have used the flow.  
Type: Integer

## Errors
<a name="API_GetFlowMetadata_Errors"></a>

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

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_GetFlowMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/GetFlowMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GetFlowMetadata) 