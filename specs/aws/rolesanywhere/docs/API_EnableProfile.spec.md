---
id: "@specs/aws/rolesanywhere/docs/API_EnableProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnableProfile"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# EnableProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_EnableProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnableProfile
<a name="API_EnableProfile"></a>

Enables temporary credential requests for a profile. 

 **Required permissions: ** `rolesanywhere:EnableProfile`. 

## Request Syntax
<a name="API_EnableProfile_RequestSyntax"></a>

```
POST /profile/{{profileId}}/enable HTTP/1.1
```

## URI Request Parameters
<a name="API_EnableProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileId](#API_EnableProfile_RequestSyntax) **   <a name="rolesanywhere-EnableProfile-request-uri-profileId"></a>
The unique identifier of the profile.  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: Yes

## Request Body
<a name="API_EnableProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_EnableProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_EnableProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [profile](#API_EnableProfile_ResponseSyntax) **   <a name="rolesanywhere-EnableProfile-response-profile"></a>
The state of the profile after a read or write operation.  
Type: [ProfileDetail](API_ProfileDetail.md) object

## Errors
<a name="API_EnableProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The resource could not be found.  
HTTP Status Code: 404

## See Also
<a name="API_EnableProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/EnableProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/EnableProfile) 