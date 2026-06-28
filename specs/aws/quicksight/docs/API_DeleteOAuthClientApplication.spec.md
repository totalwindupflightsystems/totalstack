---
id: "@specs/aws/quicksight/docs/API_DeleteOAuthClientApplication"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteOAuthClientApplication"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteOAuthClientApplication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteOAuthClientApplication
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteOAuthClientApplication
<a name="API_DeleteOAuthClientApplication"></a>

Deletes an OAuthClientApplication.

## Request Syntax
<a name="API_DeleteOAuthClientApplication_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/oauth-client-applications/{{OAuthClientApplicationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteOAuthClientApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteOAuthClientApplication_RequestSyntax) **   <a name="QS-DeleteOAuthClientApplication-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [OAuthClientApplicationId](#API_DeleteOAuthClientApplication_RequestSyntax) **   <a name="QS-DeleteOAuthClientApplication-request-uri-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication that you want to delete.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^/][^\p{Cc}]*`   
Required: Yes

## Request Body
<a name="API_DeleteOAuthClientApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteOAuthClientApplication_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "OAuthClientApplicationId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteOAuthClientApplication_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteOAuthClientApplication_ResponseSyntax) **   <a name="QS-DeleteOAuthClientApplication-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeleteOAuthClientApplication_ResponseSyntax) **   <a name="QS-DeleteOAuthClientApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the OAuthClientApplication that you deleted.  
Type: String

 ** [OAuthClientApplicationId](#API_DeleteOAuthClientApplication_ResponseSyntax) **   <a name="QS-DeleteOAuthClientApplication-response-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^/][^\p{Cc}]*` 

 ** [RequestId](#API_DeleteOAuthClientApplication_ResponseSyntax) **   <a name="QS-DeleteOAuthClientApplication-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DeleteOAuthClientApplication_Errors"></a>

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
<a name="API_DeleteOAuthClientApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteOAuthClientApplication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteOAuthClientApplication) 