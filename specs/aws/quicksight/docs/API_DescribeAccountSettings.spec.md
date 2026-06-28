---
id: "@specs/aws/quicksight/docs/API_DescribeAccountSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAccountSettings"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAccountSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAccountSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAccountSettings
<a name="API_DescribeAccountSettings"></a>

Describes the settings that were used when your Quick Sight subscription was first created in this AWS account.

## Request Syntax
<a name="API_DescribeAccountSettings_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/settings HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAccountSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeAccountSettings_RequestSyntax) **   <a name="QS-DescribeAccountSettings-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the settings that you want to list.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeAccountSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAccountSettings_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccountSettings": { 
      "AccountName": "string",
      "DefaultNamespace": "string",
      "Edition": "string",
      "NotificationEmail": "string",
      "PublicSharingEnabled": boolean,
      "TerminationProtectionEnabled": boolean
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeAccountSettings_ResponseSyntax) **   <a name="QS-DescribeAccountSettings-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccountSettings](#API_DescribeAccountSettings_ResponseSyntax) **   <a name="QS-DescribeAccountSettings-response-AccountSettings"></a>
The Amazon Quick Sight settings for this AWS account. This information includes the edition of Amazon Quick Sight that you subscribed to (Standard or Enterprise) and the notification email for the Amazon Quick Sight subscription.   
In the Quick Sight console, the Amazon Quick Sight subscription is sometimes referred to as a Quick Sight "account" even though it's technically not an account by itself. Instead, it's a subscription to the Amazon Quick Sight service for your AWS account. The edition that you subscribe to applies to Quick in every AWS Region where you use it.  
Type: [AccountSettings](API_AccountSettings.md) object

 ** [RequestId](#API_DescribeAccountSettings_ResponseSyntax) **   <a name="QS-DescribeAccountSettings-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeAccountSettings_Errors"></a>

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

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DescribeAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAccountSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAccountSettings) 