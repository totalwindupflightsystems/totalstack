---
id: "@specs/aws/rolesanywhere/docs/API_GetSubject"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetSubject"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# GetSubject

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_GetSubject
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetSubject
<a name="API_GetSubject"></a>

Gets a *subject*, which associates a certificate identity with authentication attempts. The subject stores auditing information such as the status of the last authentication attempt, the certificate data used in the attempt, and the last time the associated identity attempted authentication. 

 **Required permissions: ** `rolesanywhere:GetSubject`. 

## Request Syntax
<a name="API_GetSubject_RequestSyntax"></a>

```
GET /subject/{{subjectId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSubject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [subjectId](#API_GetSubject_RequestSyntax) **   <a name="rolesanywhere-GetSubject-request-uri-subjectId"></a>
The unique identifier of the subject.   
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: Yes

## Request Body
<a name="API_GetSubject_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSubject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "subject": { 
      "createdAt": "string",
      "credentials": [ 
         { 
            "enabled": boolean,
            "failed": boolean,
            "issuer": "string",
            "seenAt": "string",
            "serialNumber": "string",
            "x509CertificateData": "string"
         }
      ],
      "enabled": boolean,
      "instanceProperties": [ 
         { 
            "failed": boolean,
            "properties": { 
               "string" : "string" 
            },
            "seenAt": "string"
         }
      ],
      "lastSeenAt": "string",
      "subjectArn": "string",
      "subjectId": "string",
      "updatedAt": "string",
      "x509Subject": "string"
   }
}
```

## Response Elements
<a name="API_GetSubject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [subject](#API_GetSubject_ResponseSyntax) **   <a name="rolesanywhere-GetSubject-response-subject"></a>
The state of the subject after a read or write operation.  
Type: [SubjectDetail](API_SubjectDetail.md) object

## Errors
<a name="API_GetSubject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The resource could not be found.  
HTTP Status Code: 404

## See Also
<a name="API_GetSubject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/GetSubject) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/GetSubject) 