---
id: "@specs/aws/rolesanywhere/docs/API_CreateProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateProfile"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# CreateProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_CreateProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateProfile
<a name="API_CreateProfile"></a>

Creates a *profile*, a list of the roles that Roles Anywhere service is trusted to assume. You use profiles to intersect permissions with IAM managed policies.

 **Required permissions: ** `rolesanywhere:CreateProfile`. 

## Request Syntax
<a name="API_CreateProfile_RequestSyntax"></a>

```
POST /profiles HTTP/1.1
Content-type: application/json

{
   "acceptRoleSessionName": {{boolean}},
   "durationSeconds": {{number}},
   "enabled": {{boolean}},
   "managedPolicyArns": [ "{{string}}" ],
   "name": "{{string}}",
   "requireInstanceProperties": {{boolean}},
   "roleArns": [ "{{string}}" ],
   "sessionPolicy": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [acceptRoleSessionName](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-acceptRoleSessionName"></a>
Used to determine if a custom role session name will be accepted in a temporary credential request.  
Type: Boolean  
Required: No

 ** [durationSeconds](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-durationSeconds"></a>
 Used to determine how long sessions vended using this profile are valid for. See the `Expiration` section of the [CreateSession API documentation](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object) page for more details. In requests, if this value is not provided, the default value will be 3600.   
Type: Integer  
Valid Range: Minimum value of 900. Maximum value of 43200.  
Required: No

 ** [enabled](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-enabled"></a>
Specifies whether the profile is enabled.  
Type: Boolean  
Required: No

 ** [managedPolicyArns](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-managedPolicyArns"></a>
A list of managed policy ARNs that apply to the vended session credentials.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [name](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-name"></a>
The name of the profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[ a-zA-Z0-9-_]*`   
Required: Yes

 ** [requireInstanceProperties](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-requireInstanceProperties"></a>
Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile.   
Type: Boolean  
Required: No

 ** [roleArns](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-roleArns"></a>
A list of IAM roles that this profile can assume in a temporary credential request.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 250 items.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:iam(:.*){2}(:role.*)`   
Required: Yes

 ** [sessionPolicy](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-sessionPolicy"></a>
A session policy that applies to the trust boundary of the vended session credentials.   
Type: String  
Required: No

 ** [tags](#API_CreateProfile_RequestSyntax) **   <a name="rolesanywhere-CreateProfile-request-tags"></a>
The tags to attach to the profile.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "profile": { 
      "acceptRoleSessionName": boolean,
      "attributeMappings": [ 
         { 
            "certificateField": "string",
            "mappingRules": [ 
               { 
                  "specifier": "string"
               }
            ]
         }
      ],
      "createdAt": "string",
      "createdBy": "string",
      "durationSeconds": number,
      "enabled": boolean,
      "managedPolicyArns": [ "string" ],
      "name": "string",
      "profileArn": "string",
      "profileId": "string",
      "requireInstanceProperties": boolean,
      "roleArns": [ "string" ],
      "sessionPolicy": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_CreateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [profile](#API_CreateProfile_ResponseSyntax) **   <a name="rolesanywhere-CreateProfile-response-profile"></a>
The state of the profile after a read or write operation.  
Type: [ProfileDetail](API_ProfileDetail.md) object

## Errors
<a name="API_CreateProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_CreateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/CreateProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/CreateProfile) 