---
id: "@specs/aws/quicksight/docs/API_DescribeAgentPermissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAgentPermissions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAgentPermissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAgentPermissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAgentPermissions
<a name="API_DescribeAgentPermissions"></a>

Describes the resource permissions for an agent.

## Request Syntax
<a name="API_DescribeAgentPermissions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/agents/{{AgentId}}/permissions HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAgentPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AgentId](#API_DescribeAgentPermissions_RequestSyntax) **   <a name="QS-DescribeAgentPermissions-request-uri-AgentId"></a>
The unique identifier for the agent.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_.+]+`   
Required: Yes

 ** [AwsAccountId](#API_DescribeAgentPermissions_RequestSyntax) **   <a name="QS-DescribeAgentPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the agent.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeAgentPermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAgentPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AgentId": "string",
   "Arn": "string",
   "Permissions": [ 
      { 
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeAgentPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentId](#API_DescribeAgentPermissions_ResponseSyntax) **   <a name="QS-DescribeAgentPermissions-response-AgentId"></a>
The unique identifier for the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[0-9a-zA-Z-_.+]+` 

 ** [Arn](#API_DescribeAgentPermissions_ResponseSyntax) **   <a name="QS-DescribeAgentPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1284.  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}` 

 ** [Permissions](#API_DescribeAgentPermissions_ResponseSyntax) **   <a name="QS-DescribeAgentPermissions-response-Permissions"></a>
The resource permissions for the agent.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.

 ** [RequestId](#API_DescribeAgentPermissions_ResponseSyntax) **   <a name="QS-DescribeAgentPermissions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeAgentPermissions_Errors"></a>

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

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
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
<a name="API_DescribeAgentPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAgentPermissions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAgentPermissions) 