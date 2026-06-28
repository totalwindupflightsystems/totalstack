---
id: "@specs/aws/rolesanywhere/docs/API_CreateTrustAnchor"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTrustAnchor"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# CreateTrustAnchor

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_CreateTrustAnchor
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTrustAnchor
<a name="API_CreateTrustAnchor"></a>

Creates a trust anchor to establish trust between IAM Roles Anywhere and your certificate authority (CA). You can define a trust anchor as a reference to an AWS Private Certificate Authority (AWS Private CA) or by uploading a CA certificate. Your AWS workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary AWS credentials.

 **Required permissions: ** `rolesanywhere:CreateTrustAnchor`. 

## Request Syntax
<a name="API_CreateTrustAnchor_RequestSyntax"></a>

```
POST /trustanchors HTTP/1.1
Content-type: application/json

{
   "enabled": {{boolean}},
   "name": "{{string}}",
   "notificationSettings": [ 
      { 
         "channel": "{{string}}",
         "enabled": {{boolean}},
         "event": "{{string}}",
         "threshold": {{number}}
      }
   ],
   "source": { 
      "sourceData": { ... },
      "sourceType": "{{string}}"
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateTrustAnchor_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTrustAnchor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [enabled](#API_CreateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-CreateTrustAnchor-request-enabled"></a>
Specifies whether the trust anchor is enabled.  
Type: Boolean  
Required: No

 ** [name](#API_CreateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-CreateTrustAnchor-request-name"></a>
The name of the trust anchor.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[ a-zA-Z0-9-_]*`   
Required: Yes

 ** [notificationSettings](#API_CreateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-CreateTrustAnchor-request-notificationSettings"></a>
A list of notification settings to be associated to the trust anchor.  
Type: Array of [NotificationSetting](API_NotificationSetting.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 50 items.  
Required: No

 ** [source](#API_CreateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-CreateTrustAnchor-request-source"></a>
The trust anchor type and its related certificate data.  
Type: [Source](API_Source.md) object  
Required: Yes

 ** [tags](#API_CreateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-CreateTrustAnchor-request-tags"></a>
The tags to attach to the trust anchor.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateTrustAnchor_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "trustAnchor": { 
      "createdAt": "string",
      "enabled": boolean,
      "name": "string",
      "notificationSettings": [ 
         { 
            "channel": "string",
            "configuredBy": "string",
            "enabled": boolean,
            "event": "string",
            "threshold": number
         }
      ],
      "source": { 
         "sourceData": { ... },
         "sourceType": "string"
      },
      "trustAnchorArn": "string",
      "trustAnchorId": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_CreateTrustAnchor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [trustAnchor](#API_CreateTrustAnchor_ResponseSyntax) **   <a name="rolesanywhere-CreateTrustAnchor-response-trustAnchor"></a>
The state of the trust anchor after a read or write operation.   
Type: [TrustAnchorDetail](API_TrustAnchorDetail.md) object

## Errors
<a name="API_CreateTrustAnchor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_CreateTrustAnchor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/CreateTrustAnchor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/CreateTrustAnchor) 