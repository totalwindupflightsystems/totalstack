---
id: "@specs/aws/rolesanywhere/docs/API_DeleteTrustAnchor"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTrustAnchor"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# DeleteTrustAnchor

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_DeleteTrustAnchor
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTrustAnchor
<a name="API_DeleteTrustAnchor"></a>

Deletes a trust anchor.

 **Required permissions: ** `rolesanywhere:DeleteTrustAnchor`. 

## Request Syntax
<a name="API_DeleteTrustAnchor_RequestSyntax"></a>

```
DELETE /trustanchor/{{trustAnchorId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTrustAnchor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [trustAnchorId](#API_DeleteTrustAnchor_RequestSyntax) **   <a name="rolesanywhere-DeleteTrustAnchor-request-uri-trustAnchorId"></a>
The unique identifier of the trust anchor.  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: Yes

## Request Body
<a name="API_DeleteTrustAnchor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTrustAnchor_ResponseSyntax"></a>

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
<a name="API_DeleteTrustAnchor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [trustAnchor](#API_DeleteTrustAnchor_ResponseSyntax) **   <a name="rolesanywhere-DeleteTrustAnchor-response-trustAnchor"></a>
The state of the trust anchor after a read or write operation.   
Type: [TrustAnchorDetail](API_TrustAnchorDetail.md) object

## Errors
<a name="API_DeleteTrustAnchor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The resource could not be found.  
HTTP Status Code: 404

## See Also
<a name="API_DeleteTrustAnchor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/DeleteTrustAnchor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/DeleteTrustAnchor) 