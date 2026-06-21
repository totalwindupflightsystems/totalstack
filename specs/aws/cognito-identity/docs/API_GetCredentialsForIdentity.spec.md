---
id: "@specs/aws/cognito-identity/docs/API_GetCredentialsForIdentity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCredentialsForIdentity"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# GetCredentialsForIdentity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_GetCredentialsForIdentity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCredentialsForIdentity
<a name="API_GetCredentialsForIdentity"></a>

Returns credentials for the provided identity ID. Any provided logins will be validated against supported login providers. If the token is for `cognito-identity.amazonaws.com`, it will be passed through to AWS Security Token Service with the appropriate role for the token.

This is the final operation in the sequence for developer-authenticated identities and identities from external IdPs in the enhanced authentication flow. This operation issues credentials for the default authenticated role to developer-authenticated identities. For identities from external IdPs, this operation issues credentials for a role chosen from token role claims, the default role, or from claim-matching rules, depending on the configuration of the IdP.

**Note**  
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies.

## Request Syntax
<a name="API_GetCredentialsForIdentity_RequestSyntax"></a>

```
{
   "CustomRoleArn": "{{string}}",
   "IdentityId": "{{string}}",
   "Logins": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## Request Parameters
<a name="API_GetCredentialsForIdentity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CustomRoleArn](#API_GetCredentialsForIdentity_RequestSyntax) **   <a name="CognitoIdentity-GetCredentialsForIdentity-request-CustomRoleArn"></a>
When the token or SAML assertion from your identity provider contains multiple IAM role claims, this optional parameter provides the ARN of the preferred role that you want to request for the current user.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: No

 ** [IdentityId](#API_GetCredentialsForIdentity_RequestSyntax) **   <a name="CognitoIdentity-GetCredentialsForIdentity-request-IdentityId"></a>
A unique identifier in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

 ** [Logins](#API_GetCredentialsForIdentity_RequestSyntax) **   <a name="CognitoIdentity-GetCredentialsForIdentity-request-Logins"></a>
A set of optional name-value pairs that map provider names to provider tokens. The name-value pair will follow the syntax "provider\_name": "provider\_user\_identifier".  
Logins should not be specified when trying to get credentials for an unauthenticated identity.  
The Logins parameter is required when using identities associated with external identity providers such as Facebook. For examples of `Logins` maps, see the code examples in the [External Identity Providers](https://docs.aws.amazon.com/cognito/latest/developerguide/external-identity-providers.html) section of the Amazon Cognito Developer Guide.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 1. Maximum length of 50000.  
Required: No

## Response Syntax
<a name="API_GetCredentialsForIdentity_ResponseSyntax"></a>

```
{
   "Credentials": { 
      "AccessKeyId": "string",
      "Expiration": number,
      "SecretKey": "string",
      "SessionToken": "string"
   },
   "IdentityId": "string"
}
```

## Response Elements
<a name="API_GetCredentialsForIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Credentials](#API_GetCredentialsForIdentity_ResponseSyntax) **   <a name="CognitoIdentity-GetCredentialsForIdentity-response-Credentials"></a>
Credentials for the provided identity ID.  
Type: [Credentials](API_Credentials.md) object

 ** [IdentityId](#API_GetCredentialsForIdentity_ResponseSyntax) **   <a name="CognitoIdentity-GetCredentialsForIdentity-response-IdentityId"></a>
A unique identifier in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+` 

## Errors
<a name="API_GetCredentialsForIdentity_Errors"></a>

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

 ** InvalidIdentityPoolConfigurationException **   
If you provided authentication information in the request, the identity pool has no authenticated role configured, or AWS STS returned an error response to the request to assume the authenticated role from the identity pool. If you provided no authentication information in the request, the identity pool has no unauthenticated role configured, or AWS STS returned an error response to the request to assume the unauthenticated role from the identity pool.  
Your role trust policy must grant `AssumeRoleWithWebIdentity` permissions to `cognito-identity.amazonaws.com`.    
 ** message **   
The message returned for an `InvalidIdentityPoolConfigurationException` 
HTTP Status Code: 400

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
<a name="API_GetCredentialsForIdentity_Examples"></a>

### GetCredentialsForIdentity
<a name="API_GetCredentialsForIdentity_Example_1"></a>

The following example shows a `GetCredentialsForIdentity` request.

#### Sample Request
<a name="API_GetCredentialsForIdentity_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/x-amz-json-1.1
CONTENT-LENGTH: 250
X-AMZ-TARGET: com.amazonaws.cognito.identity.model.AWSCognitoIdentityService.GetCredentialsForIdentity
HOST: <endpoint>
X-AMZ-DATE: 20151020T232759Z

{
  "IdentityId":"us-east-1:88b5cc2c-c8c4-4932-a4e5-fc85EXAMPLE"
}
```

#### Sample Response
<a name="API_GetCredentialsForIdentity_Example_1_Response"></a>

```
1.1 200 OK
content-length: 1168,
content-type: application/x-amz-json-1.1,
date: Mon, 21 Sep 2015 22:38:52 GMT,
x-amzn-requestid: 8906cbc7-60b1-11e5-9f63-1bfexample,

{
  "Credentials":{
     "SecretKey":"2gZ8QJQqkAHBzebQmghavFAfgmYpKWRqexample",
     "SessionToken":"AQoDYXdzEMf//////////wEasAWDYyZbsv2CTPExziDyYEXAMPLE",
     "Expiration":1442877512.0,
     "AccessKeyId":"ASIAJIOA37R6EXAMPLE"
  },
  "IdentityId":"us-east-1:88b5cc2c-c8c4-4932-a4e5-fc85EXAMPLE"
}
```

## See Also
<a name="API_GetCredentialsForIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/GetCredentialsForIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/GetCredentialsForIdentity) 