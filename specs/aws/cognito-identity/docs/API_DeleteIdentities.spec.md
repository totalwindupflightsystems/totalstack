---
id: "@specs/aws/cognito-identity/docs/API_DeleteIdentities"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteIdentities"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# DeleteIdentities

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_DeleteIdentities
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteIdentities
<a name="API_DeleteIdentities"></a>

Deletes identities from an identity pool. You can specify a list of 1-60 identities that you want to delete.

You must use AWS developer credentials to call this operation.

## Request Syntax
<a name="API_DeleteIdentities_RequestSyntax"></a>

```
{
   "IdentityIdsToDelete": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DeleteIdentities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityIdsToDelete](#API_DeleteIdentities_RequestSyntax) **   <a name="CognitoIdentity-DeleteIdentities-request-IdentityIdsToDelete"></a>
A list of 1-60 identities that you want to delete.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 60 items.  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

## Response Syntax
<a name="API_DeleteIdentities_ResponseSyntax"></a>

```
{
   "UnprocessedIdentityIds": [ 
      { 
         "ErrorCode": "string",
         "IdentityId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DeleteIdentities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UnprocessedIdentityIds](#API_DeleteIdentities_ResponseSyntax) **   <a name="CognitoIdentity-DeleteIdentities-response-UnprocessedIdentityIds"></a>
An array of UnprocessedIdentityId objects, each of which contains an ErrorCode and IdentityId.  
Type: Array of [UnprocessedIdentityId](API_UnprocessedIdentityId.md) objects  
Array Members: Maximum number of 60 items.

## Errors
<a name="API_DeleteIdentities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Thrown when the service encounters an error during processing the request.    
 ** message **   
The message returned by an InternalErrorException.
HTTP Status Code: 500

 ** InvalidParameterException **   
Thrown for missing or bad input parameter(s).    
 ** message **   
The message returned by an InvalidParameterException.
HTTP Status Code: 400

 ** TooManyRequestsException **   
Thrown when a request is throttled.    
 ** message **   
Message returned by a TooManyRequestsException
HTTP Status Code: 400

## See Also
<a name="API_DeleteIdentities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/DeleteIdentities) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/DeleteIdentities) 