---
id: "@specs/aws/cognito-identity/docs/API_UnlinkIdentity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UnlinkIdentity"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# UnlinkIdentity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_UnlinkIdentity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UnlinkIdentity
<a name="API_UnlinkIdentity"></a>

Unlinks a federated identity from an existing account. Unlinked logins will be considered new identities next time they are seen. Removing the last linked login will make this identity inaccessible.

This is a public API. You do not need any credentials to call this API.

## Request Syntax
<a name="API_UnlinkIdentity_RequestSyntax"></a>

```
{
   "IdentityId": "{{string}}",
   "Logins": { 
      "{{string}}" : "{{string}}" 
   },
   "LoginsToRemove": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UnlinkIdentity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityId](#API_UnlinkIdentity_RequestSyntax) **   <a name="CognitoIdentity-UnlinkIdentity-request-IdentityId"></a>
A unique identifier in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

 ** [Logins](#API_UnlinkIdentity_RequestSyntax) **   <a name="CognitoIdentity-UnlinkIdentity-request-Logins"></a>
A set of optional name-value pairs that map provider names to provider tokens.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 1. Maximum length of 50000.  
Required: Yes

 ** [LoginsToRemove](#API_UnlinkIdentity_RequestSyntax) **   <a name="CognitoIdentity-UnlinkIdentity-request-LoginsToRemove"></a>
Provider names to unlink from this identity.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Response Elements
<a name="API_UnlinkIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UnlinkIdentity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExternalServiceException **   
An exception thrown when a dependent service such as Facebook or Twitter is not responding    
 ** message **   
The message returned by an ExternalServiceException
HTTP Status Code: 400

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

 ** NotAuthorizedException **   
Thrown when a user is not authorized to access the requested resource.    
 ** message **   
The message returned by a NotAuthorizedException
HTTP Status Code: 400

 ** ResourceConflictException **   
Thrown when a user tries to use a login which is already linked to another account.    
 ** message **   
The message returned by a ResourceConflictException.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Thrown when the requested resource (for example, a dataset or record) does not exist.    
 ** message **   
The message returned by a ResourceNotFoundException.
HTTP Status Code: 400

 ** TooManyRequestsException **   
Thrown when a request is throttled.    
 ** message **   
Message returned by a TooManyRequestsException
HTTP Status Code: 400

## Examples
<a name="API_UnlinkIdentity_Examples"></a>

### UnlinkIdentity
<a name="API_UnlinkIdentity_Example_1"></a>

The following example shows an `UnlinkIdentity` request. The request body has been formatted for readability and may not match the `content-length` value.

#### Sample Request
<a name="API_UnlinkIdentity_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
CONTENT-LENGTH: 307
X-AMZ-TARGET: com.amazonaws.cognito.identity.model.AWSCognitoIdentityService.UnlinkIdentity
HOST: <endpoint>
X-AMZ-DATE: 20140805T164904Z

{
    "IdentityId": "us-east-1:6820d0d3-3c95-4d9f-8813-c4448fca995f",
    "Logins":
    {
        "accounts.google.com": "<PROVIDER_TOKEN>"
    },
    "LoginsToRemove": ["accounts.google.com"]
}
```

## See Also
<a name="API_UnlinkIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/UnlinkIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/UnlinkIdentity) 