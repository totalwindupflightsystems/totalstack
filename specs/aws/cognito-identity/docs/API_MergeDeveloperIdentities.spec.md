---
id: "@specs/aws/cognito-identity/docs/API_MergeDeveloperIdentities"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MergeDeveloperIdentities"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# MergeDeveloperIdentities

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_MergeDeveloperIdentities
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MergeDeveloperIdentities
<a name="API_MergeDeveloperIdentities"></a>

Merges two users having different `IdentityId`s, existing in the same identity pool, and identified by the same developer provider. You can use this action to request that discrete users be merged and identified as a single user in the Cognito environment. Cognito associates the given source user (`SourceUserIdentifier`) with the `IdentityId` of the `DestinationUserIdentifier`. Only developer-authenticated users can be merged. If the users to be merged are associated with the same public provider, but as two different users, an exception will be thrown.

The number of linked logins is limited to 20. So, the number of linked logins for the source user, `SourceUserIdentifier`, and the destination user, `DestinationUserIdentifier`, together should not be larger than 20. Otherwise, an exception will be thrown.

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 

## Request Syntax
<a name="API_MergeDeveloperIdentities_RequestSyntax"></a>

```
{
   "DestinationUserIdentifier": "{{string}}",
   "DeveloperProviderName": "{{string}}",
   "IdentityPoolId": "{{string}}",
   "SourceUserIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_MergeDeveloperIdentities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationUserIdentifier](#API_MergeDeveloperIdentities_RequestSyntax) **   <a name="CognitoIdentity-MergeDeveloperIdentities-request-DestinationUserIdentifier"></a>
User identifier for the destination user. The value should be a `DeveloperUserIdentifier`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** [DeveloperProviderName](#API_MergeDeveloperIdentities_RequestSyntax) **   <a name="CognitoIdentity-MergeDeveloperIdentities-request-DeveloperProviderName"></a>
The "domain" by which Cognito will refer to your users. This is a (pseudo) domain name that you provide while creating an identity pool. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the `DeveloperProviderName`, you can use letters as well as period (.), underscore (\_), and dash (-).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w._-]+`   
Required: Yes

 ** [IdentityPoolId](#API_MergeDeveloperIdentities_RequestSyntax) **   <a name="CognitoIdentity-MergeDeveloperIdentities-request-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

 ** [SourceUserIdentifier](#API_MergeDeveloperIdentities_RequestSyntax) **   <a name="CognitoIdentity-MergeDeveloperIdentities-request-SourceUserIdentifier"></a>
User identifier for the source user. The value should be a `DeveloperUserIdentifier`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

## Response Syntax
<a name="API_MergeDeveloperIdentities_ResponseSyntax"></a>

```
{
   "IdentityId": "string"
}
```

## Response Elements
<a name="API_MergeDeveloperIdentities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityId](#API_MergeDeveloperIdentities_ResponseSyntax) **   <a name="CognitoIdentity-MergeDeveloperIdentities-response-IdentityId"></a>
A unique identifier in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+` 

## Errors
<a name="API_MergeDeveloperIdentities_Errors"></a>

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

## See Also
<a name="API_MergeDeveloperIdentities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/MergeDeveloperIdentities) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/MergeDeveloperIdentities) 