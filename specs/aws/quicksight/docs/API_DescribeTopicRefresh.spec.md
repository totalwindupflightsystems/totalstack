---
id: "@specs/aws/quicksight/docs/API_DescribeTopicRefresh"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTopicRefresh"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeTopicRefresh

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeTopicRefresh
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTopicRefresh
<a name="API_DescribeTopicRefresh"></a>

Describes the status of a topic refresh.

## Request Syntax
<a name="API_DescribeTopicRefresh_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/topics/{{TopicId}}/refresh/{{RefreshId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTopicRefresh_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeTopicRefresh_RequestSyntax) **   <a name="QS-DescribeTopicRefresh-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the topic whose refresh you want to describe.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [RefreshId](#API_DescribeTopicRefresh_RequestSyntax) **   <a name="QS-DescribeTopicRefresh-request-uri-RefreshId"></a>
The ID of the refresh, which is performed when the topic is created or updated.  
Required: Yes

 ** [TopicId](#API_DescribeTopicRefresh_RequestSyntax) **   <a name="QS-DescribeTopicRefresh-request-uri-TopicId"></a>
The ID of the topic that you want to describe. This ID is unique per AWS Region for each AWS account.  
Length Constraints: Maximum length of 256.  
Pattern: `^[A-Za-z0-9-_.\\+]*$`   
Required: Yes

## Request Body
<a name="API_DescribeTopicRefresh_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTopicRefresh_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RefreshDetails": { 
      "RefreshArn": "string",
      "RefreshId": "string",
      "RefreshStatus": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeTopicRefresh_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeTopicRefresh_ResponseSyntax) **   <a name="QS-DescribeTopicRefresh-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RefreshDetails](#API_DescribeTopicRefresh_ResponseSyntax) **   <a name="QS-DescribeTopicRefresh-response-RefreshDetails"></a>
Details of the refresh, which is performed when the topic is created or updated.  
Type: [TopicRefreshDetails](API_TopicRefreshDetails.md) object

 ** [RequestId](#API_DescribeTopicRefresh_ResponseSyntax) **   <a name="QS-DescribeTopicRefresh-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeTopicRefresh_Errors"></a>

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

## Examples
<a name="API_DescribeTopicRefresh_Examples"></a>

### Example
<a name="API_DescribeTopicRefresh_Example_1"></a>

This example illustrates one usage of DescribeTopicRefresh.

#### Sample Request
<a name="API_DescribeTopicRefresh_Example_1_Request"></a>

```
GET /accounts/{AwsAccountId}/topics/{TopicId}/refresh/{RefreshId} HTTP/1.1
Content-type: application/json
```

## See Also
<a name="API_DescribeTopicRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeTopicRefresh) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeTopicRefresh) 