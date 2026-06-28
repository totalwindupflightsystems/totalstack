---
id: "@specs/aws/quicksight/docs/API_DescribeKeyRegistration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeKeyRegistration"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeKeyRegistration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeKeyRegistration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeKeyRegistration
<a name="API_DescribeKeyRegistration"></a>

Describes all customer managed key registrations in a Quick Sight account.

## Request Syntax
<a name="API_DescribeKeyRegistration_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/key-registration?default-key-only={{DefaultKeyOnly}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeKeyRegistration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeKeyRegistration_RequestSyntax) **   <a name="QS-DescribeKeyRegistration-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the customer managed key registration that you want to describe.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DefaultKeyOnly](#API_DescribeKeyRegistration_RequestSyntax) **   <a name="QS-DescribeKeyRegistration-request-uri-DefaultKeyOnly"></a>
Determines whether the request returns the default key only.

## Request Body
<a name="API_DescribeKeyRegistration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeKeyRegistration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AwsAccountId": "string",
   "KeyRegistration": [ 
      { 
         "DefaultKey": boolean,
         "KeyArn": "string"
      }
   ],
   "QDataKey": { 
      "QDataKeyArn": "string",
      "QDataKeyType": "string"
   },
   "RequestId": "string",
   "Status": number
}
```

## Response Elements
<a name="API_DescribeKeyRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AwsAccountId](#API_DescribeKeyRegistration_ResponseSyntax) **   <a name="QS-DescribeKeyRegistration-response-AwsAccountId"></a>
The ID of the AWS account that contains the customer managed key registration specified in the request.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [KeyRegistration](#API_DescribeKeyRegistration_ResponseSyntax) **   <a name="QS-DescribeKeyRegistration-response-KeyRegistration"></a>
A list of `RegisteredCustomerManagedKey` objects in a Quick Sight account.  
Type: Array of [RegisteredCustomerManagedKey](API_RegisteredCustomerManagedKey.md) objects

 ** [QDataKey](#API_DescribeKeyRegistration_ResponseSyntax) **   <a name="QS-DescribeKeyRegistration-response-QDataKey"></a>
A list of `QDataKey` objects in a Quick Sight account.  
Type: [QDataKey](API_QDataKey.md) object

 ** [RequestId](#API_DescribeKeyRegistration_ResponseSyntax) **   <a name="QS-DescribeKeyRegistration-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

 ** [Status](#API_DescribeKeyRegistration_ResponseSyntax) **   <a name="QS-DescribeKeyRegistration-response-Status"></a>
The HTTP status of the request.  
Type: Integer

## Errors
<a name="API_DescribeKeyRegistration_Errors"></a>

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
<a name="API_DescribeKeyRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeKeyRegistration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeKeyRegistration) 