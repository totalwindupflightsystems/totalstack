---
id: "@specs/aws/cognito-identity/docs/API_DescribeIdentityPool"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIdentityPool"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# DescribeIdentityPool

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_DescribeIdentityPool
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIdentityPool
<a name="API_DescribeIdentityPool"></a>

Gets details about the requested identity pool, including pool name and ID, description, tags, and identity provviders.

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 

## Request Syntax
<a name="API_DescribeIdentityPool_RequestSyntax"></a>

```
{
   "IdentityPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeIdentityPool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityPoolId](#API_DescribeIdentityPool_RequestSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-request-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

## Response Syntax
<a name="API_DescribeIdentityPool_ResponseSyntax"></a>

```
{
   "AllowClassicFlow": boolean,
   "AllowUnauthenticatedIdentities": boolean,
   "CognitoIdentityProviders": [ 
      { 
         "ClientId": "string",
         "ProviderName": "string",
         "ServerSideTokenCheck": boolean
      }
   ],
   "DeveloperProviderName": "string",
   "IdentityPoolId": "string",
   "IdentityPoolName": "string",
   "IdentityPoolTags": { 
      "string" : "string" 
   },
   "OpenIdConnectProviderARNs": [ "string" ],
   "SamlProviderARNs": [ "string" ],
   "SupportedLoginProviders": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_DescribeIdentityPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AllowClassicFlow](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-AllowClassicFlow"></a>
Enables or disables the Basic (Classic) authentication flow. For more information, see [Identity Pools (Federated Identities) Authentication Flow](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html) in the *Amazon Cognito Developer Guide*.  
Type: Boolean

 ** [AllowUnauthenticatedIdentities](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-AllowUnauthenticatedIdentities"></a>
TRUE if the identity pool supports unauthenticated logins.  
Type: Boolean

 ** [CognitoIdentityProviders](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-CognitoIdentityProviders"></a>
A list representing an Amazon Cognito user pool and its client ID.  
Type: Array of [CognitoIdentityProvider](API_CognitoIdentityProvider.md) objects

 ** [DeveloperProviderName](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-DeveloperProviderName"></a>
The "domain" by which Cognito will refer to your users.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w._-]+` 

 ** [IdentityPoolId](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+` 

 ** [IdentityPoolName](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-IdentityPoolName"></a>
A string that you provide.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w\s+=,.@-]+` 

 ** [IdentityPoolTags](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-IdentityPoolTags"></a>
The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [OpenIdConnectProviderARNs](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-OpenIdConnectProviderARNs"></a>
The ARNs of the OpenID Connect providers.  
Type: Array of strings  
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [SamlProviderARNs](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-SamlProviderARNs"></a>
An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.  
Type: Array of strings  
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [SupportedLoginProviders](#API_DescribeIdentityPool_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentityPool-response-SupportedLoginProviders"></a>
Optional key:value pairs mapping provider names to provider app IDs.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Pattern: `[\w.;_/-]+` 

## Errors
<a name="API_DescribeIdentityPool_Errors"></a>

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

 ** NotAuthorizedException **   
Thrown when a user is not authorized to access the requested resource.    
 ** message **   
The message returned by a NotAuthorizedException
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
<a name="API_DescribeIdentityPool_Examples"></a>

### DescribeIdentityPool
<a name="API_DescribeIdentityPool_Example_1"></a>

The following examples show a request and response for the `DescribeIdentityPool` operation. The request and response bodies have been edited for readability and may not match the stated `content-length` values.

#### Sample Request
<a name="API_DescribeIdentityPool_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
CONTENT-LENGTH: 224
X-AMZ-TARGET: com.amazonaws.cognito.identity.model.AWSCognitoIdentityService.DescribeIdentityPool
HOST: <endpoint>
X-AMZ-DATE: 20140804T203833Z
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature>

{
    "IdentityPoolId": "us-east-1:177a950c-2c08-43f0-9983-28727EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeIdentityPool_Example_1_Response"></a>

```
1.1 200 OK
x-amzn-requestid: c5cc0ad5-c604-455a-87ee-cb830b22341a
date: Mon, 04 Aug 2014 20:38:33 GMT
content-type: application/json
content-length: 367

{
    "AllowUnauthenticatedIdentities": true,
    "IdentityPoolId": "us-east-1:177a950c-2c08-43f0-9983-28727EXAMPLE",
    "IdentityPoolName": "MyIdentityPool",
    "SupportedLoginProviders":
    {
        "accounts.google.com": "123456789012.apps.googleusercontent.com",
        "graph.facebook.com": "7346241598935555",
        "www.amazon.com": "amzn1.application-oa2-client.188a56d827a7d6555a8b67a5d"
    }
}
```

## See Also
<a name="API_DescribeIdentityPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/DescribeIdentityPool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/DescribeIdentityPool) 