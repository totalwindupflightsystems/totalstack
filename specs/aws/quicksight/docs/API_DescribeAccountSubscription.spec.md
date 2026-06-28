---
id: "@specs/aws/quicksight/docs/API_DescribeAccountSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAccountSubscription"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAccountSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAccountSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAccountSubscription
<a name="API_DescribeAccountSubscription"></a>

Use the DescribeAccountSubscription operation to receive a description of an Quick Sight account's subscription. A successful API call returns an `AccountInfo` object that includes an account's name, subscription status, authentication type, edition, and notification email address.

## Request Syntax
<a name="API_DescribeAccountSubscription_RequestSyntax"></a>

```
GET /account/{{AwsAccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAccountSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeAccountSubscription_RequestSyntax) **   <a name="QS-DescribeAccountSubscription-request-uri-AwsAccountId"></a>
The AWS account ID associated with your Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeAccountSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAccountSubscription_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccountInfo": { 
      "AccountName": "string",
      "AccountSubscriptionStatus": "string",
      "AuthenticationType": "string",
      "Edition": "string",
      "IAMIdentityCenterInstanceArn": "string",
      "NotificationEmail": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeAccountSubscription_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeAccountSubscription_ResponseSyntax) **   <a name="QS-DescribeAccountSubscription-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccountInfo](#API_DescribeAccountSubscription_ResponseSyntax) **   <a name="QS-DescribeAccountSubscription-response-AccountInfo"></a>
A structure that contains the following elements:  
+ Your Quick Sight account name.
+ The edition of Quick Sight that your account is using.
+ The notification email address that is associated with the Amazon Quick Sight account. 
+ The authentication type of the Quick Sight account.
+ The status of the Quick Sight account's subscription.
Type: [AccountInfo](API_AccountInfo.md) object

 ** [RequestId](#API_DescribeAccountSubscription_ResponseSyntax) **   <a name="QS-DescribeAccountSubscription-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeAccountSubscription_Errors"></a>

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
<a name="API_DescribeAccountSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAccountSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAccountSubscription) 