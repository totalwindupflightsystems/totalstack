---
id: "@specs/aws/cognito-identity/docs/API_GetPrincipalTagAttributeMap"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetPrincipalTagAttributeMap"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# GetPrincipalTagAttributeMap

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_GetPrincipalTagAttributeMap
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetPrincipalTagAttributeMap
<a name="API_GetPrincipalTagAttributeMap"></a>

Use `GetPrincipalTagAttributeMap` to list all mappings between `PrincipalTags` and user attributes.

## Request Syntax
<a name="API_GetPrincipalTagAttributeMap_RequestSyntax"></a>

```
{
   "IdentityPoolId": "{{string}}",
   "IdentityProviderName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPrincipalTagAttributeMap_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityPoolId](#API_GetPrincipalTagAttributeMap_RequestSyntax) **   <a name="CognitoIdentity-GetPrincipalTagAttributeMap-request-IdentityPoolId"></a>
You can use this operation to get the ID of the Identity Pool you setup attribute mappings for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

 ** [IdentityProviderName](#API_GetPrincipalTagAttributeMap_RequestSyntax) **   <a name="CognitoIdentity-GetPrincipalTagAttributeMap-request-IdentityProviderName"></a>
You can use this operation to get the provider name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Response Syntax
<a name="API_GetPrincipalTagAttributeMap_ResponseSyntax"></a>

```
{
   "IdentityPoolId": "string",
   "IdentityProviderName": "string",
   "PrincipalTags": { 
      "string" : "string" 
   },
   "UseDefaults": boolean
}
```

## Response Elements
<a name="API_GetPrincipalTagAttributeMap_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityPoolId](#API_GetPrincipalTagAttributeMap_ResponseSyntax) **   <a name="CognitoIdentity-GetPrincipalTagAttributeMap-response-IdentityPoolId"></a>
You can use this operation to get the ID of the Identity Pool you setup attribute mappings for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+` 

 ** [IdentityProviderName](#API_GetPrincipalTagAttributeMap_ResponseSyntax) **   <a name="CognitoIdentity-GetPrincipalTagAttributeMap-response-IdentityProviderName"></a>
You can use this operation to get the provider name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [PrincipalTags](#API_GetPrincipalTagAttributeMap_ResponseSyntax) **   <a name="CognitoIdentity-GetPrincipalTagAttributeMap-response-PrincipalTags"></a>
You can use this operation to add principal tags. The `PrincipalTags`operation enables you to reference user attributes in your IAM permissions policy.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [UseDefaults](#API_GetPrincipalTagAttributeMap_ResponseSyntax) **   <a name="CognitoIdentity-GetPrincipalTagAttributeMap-response-UseDefaults"></a>
You can use this operation to list   
Type: Boolean

## Errors
<a name="API_GetPrincipalTagAttributeMap_Errors"></a>

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
<a name="API_GetPrincipalTagAttributeMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/GetPrincipalTagAttributeMap) 