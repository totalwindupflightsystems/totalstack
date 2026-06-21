---
id: "@specs/aws/cognito-identity/docs/API_SetIdentityPoolRoles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SetIdentityPoolRoles"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# SetIdentityPoolRoles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_SetIdentityPoolRoles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SetIdentityPoolRoles
<a name="API_SetIdentityPoolRoles"></a>

Sets the roles for an identity pool. These roles are used when making calls to [GetCredentialsForIdentity](API_GetCredentialsForIdentity.md) action.

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 

## Request Syntax
<a name="API_SetIdentityPoolRoles_RequestSyntax"></a>

```
{
   "IdentityPoolId": "{{string}}",
   "RoleMappings": { 
      "{{string}}" : { 
         "AmbiguousRoleResolution": "{{string}}",
         "RulesConfiguration": { 
            "Rules": [ 
               { 
                  "Claim": "{{string}}",
                  "MatchType": "{{string}}",
                  "RoleARN": "{{string}}",
                  "Value": "{{string}}"
               }
            ]
         },
         "Type": "{{string}}"
      }
   },
   "Roles": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## Request Parameters
<a name="API_SetIdentityPoolRoles_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityPoolId](#API_SetIdentityPoolRoles_RequestSyntax) **   <a name="CognitoIdentity-SetIdentityPoolRoles-request-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

 ** [RoleMappings](#API_SetIdentityPoolRoles_RequestSyntax) **   <a name="CognitoIdentity-SetIdentityPoolRoles-request-RoleMappings"></a>
How users for a specific identity provider are to mapped to roles. This is a string to [RoleMapping](API_RoleMapping.md) object map. The string identifies the identity provider, for example, `graph.facebook.com` or `cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id`.  
Up to 25 rules can be specified per identity provider.  
Type: String to [RoleMapping](API_RoleMapping.md) object map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** [Roles](#API_SetIdentityPoolRoles_RequestSyntax) **   <a name="CognitoIdentity-SetIdentityPoolRoles-request-Roles"></a>
The map of roles associated with this pool. For a given role, the key will be either "authenticated" or "unauthenticated" and the value will be the Role ARN.  
Type: String to string map  
Map Entries: Maximum number of 2 items.  
Key Pattern: `(un)?authenticated`   
Value Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

## Response Elements
<a name="API_SetIdentityPoolRoles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetIdentityPoolRoles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **   
Thrown if there are parallel requests to modify a resource.    
 ** message **   
The message returned by a ConcurrentModificationException.
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

## See Also
<a name="API_SetIdentityPoolRoles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/SetIdentityPoolRoles) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/SetIdentityPoolRoles) 