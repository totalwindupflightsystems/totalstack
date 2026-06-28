---
id: "@specs/aws/rolesanywhere/docs/API_UpdateTrustAnchor"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateTrustAnchor"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# UpdateTrustAnchor

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_UpdateTrustAnchor
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateTrustAnchor
<a name="API_UpdateTrustAnchor"></a>

Updates a trust anchor. You establish trust between IAM Roles Anywhere and your certificate authority (CA) by configuring a trust anchor. You can define a trust anchor as a reference to an AWS Private Certificate Authority (AWS Private CA) or by uploading a CA certificate. Your AWS workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary AWS credentials.

 **Required permissions: ** `rolesanywhere:UpdateTrustAnchor`. 

## Request Syntax
<a name="API_UpdateTrustAnchor_RequestSyntax"></a>

```
PATCH /trustanchor/{{trustAnchorId}} HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "source": { 
      "sourceData": { ... },
      "sourceType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateTrustAnchor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [trustAnchorId](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-uri-trustAnchorId"></a>
The unique identifier of the trust anchor.  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: Yes

## Request Body
<a name="API_UpdateTrustAnchor_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-name"></a>
The name of the trust anchor.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[ a-zA-Z0-9-_]*`   
Required: No

 ** [source](#API_UpdateTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-request-source"></a>
The trust anchor type and its related certificate data.  
Type: [Source](API_Source.md) object  
Required: No

## Response Syntax
<a name="API_UpdateTrustAnchor_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateTrustAnchor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [trustAnchor](#API_UpdateTrustAnchor_ResponseSyntax) **   <a name="rolesanywhere-UpdateTrustAnchor-response-trustAnchor"></a>
The state of the trust anchor after a read or write operation.   
Type: [TrustAnchorDetail](API_TrustAnchorDetail.md) object

## Errors
<a name="API_UpdateTrustAnchor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The resource could not be found.  
HTTP Status Code: 404

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateTrustAnchor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/UpdateTrustAnchor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/UpdateTrustAnchor) 