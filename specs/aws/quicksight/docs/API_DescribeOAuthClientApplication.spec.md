---
id: "@specs/aws/quicksight/docs/API_DescribeOAuthClientApplication"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeOAuthClientApplication"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeOAuthClientApplication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeOAuthClientApplication
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeOAuthClientApplication
<a name="API_DescribeOAuthClientApplication"></a>

Describes an OAuthClientApplication.

## Request Syntax
<a name="API_DescribeOAuthClientApplication_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/oauth-client-applications/{{OAuthClientApplicationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeOAuthClientApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeOAuthClientApplication_RequestSyntax) **   <a name="QS-DescribeOAuthClientApplication-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [OAuthClientApplicationId](#API_DescribeOAuthClientApplication_RequestSyntax) **   <a name="QS-DescribeOAuthClientApplication-request-uri-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication that you want to describe.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^/][^\p{Cc}]*`   
Required: Yes

## Request Body
<a name="API_DescribeOAuthClientApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeOAuthClientApplication_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "OAuthClientApplication": { 
      "Arn": "string",
      "CreatedTime": number,
      "DataSourceType": "string",
      "IdentityProviderVpcConnectionProperties": { 
         "VpcConnectionArn": "string"
      },
      "LastUpdatedTime": number,
      "Name": "string",
      "OAuthAuthorizationEndpointUrl": "string",
      "OAuthClientApplicationId": "string",
      "OAuthClientAuthenticationType": "string",
      "OAuthScopes": "string",
      "OAuthTokenEndpointUrl": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeOAuthClientApplication_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeOAuthClientApplication_ResponseSyntax) **   <a name="QS-DescribeOAuthClientApplication-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [OAuthClientApplication](#API_DescribeOAuthClientApplication_ResponseSyntax) **   <a name="QS-DescribeOAuthClientApplication-response-OAuthClientApplication"></a>
The information about the OAuthClientApplication.  
Type: [OAuthClientApplication](API_OAuthClientApplication.md) object

 ** [RequestId](#API_DescribeOAuthClientApplication_ResponseSyntax) **   <a name="QS-DescribeOAuthClientApplication-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeOAuthClientApplication_Errors"></a>

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
<a name="API_DescribeOAuthClientApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeOAuthClientApplication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeOAuthClientApplication) 