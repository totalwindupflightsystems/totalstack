---
id: "@specs/aws/cognito-identity/docs/API_DescribeIdentity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIdentity"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# DescribeIdentity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_DescribeIdentity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIdentity
<a name="API_DescribeIdentity"></a>

Returns metadata related to the given identity, including when the identity was created and any associated linked logins.

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 

## Request Syntax
<a name="API_DescribeIdentity_RequestSyntax"></a>

```
{
   "IdentityId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeIdentity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityId](#API_DescribeIdentity_RequestSyntax) **   <a name="CognitoIdentity-DescribeIdentity-request-IdentityId"></a>
A unique identifier in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

## Response Syntax
<a name="API_DescribeIdentity_ResponseSyntax"></a>

```
{
   "CreationDate": number,
   "IdentityId": "string",
   "LastModifiedDate": number,
   "Logins": [ "string" ]
}
```

## Response Elements
<a name="API_DescribeIdentity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationDate](#API_DescribeIdentity_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentity-response-CreationDate"></a>
Date on which the identity was created.  
Type: Timestamp

 ** [IdentityId](#API_DescribeIdentity_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentity-response-IdentityId"></a>
A unique identifier in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+` 

 ** [LastModifiedDate](#API_DescribeIdentity_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentity-response-LastModifiedDate"></a>
Date on which the identity was last modified.  
Type: Timestamp

 ** [Logins](#API_DescribeIdentity_ResponseSyntax) **   <a name="CognitoIdentity-DescribeIdentity-response-Logins"></a>
The provider names.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_DescribeIdentity_Errors"></a>

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

## See Also
<a name="API_DescribeIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/DescribeIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/DescribeIdentity) 