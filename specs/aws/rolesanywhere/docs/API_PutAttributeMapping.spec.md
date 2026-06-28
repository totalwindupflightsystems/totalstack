---
id: "@specs/aws/rolesanywhere/docs/API_PutAttributeMapping"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAttributeMapping"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# PutAttributeMapping

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_PutAttributeMapping
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAttributeMapping
<a name="API_PutAttributeMapping"></a>

Put an entry in the attribute mapping rules that will be enforced by a given profile. A mapping specifies a certificate field and one or more specifiers that have contextual meanings.

## Request Syntax
<a name="API_PutAttributeMapping_RequestSyntax"></a>

```
PUT /profiles/{{profileId}}/mappings HTTP/1.1
Content-type: application/json

{
   "certificateField": "{{string}}",
   "mappingRules": [ 
      { 
         "specifier": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_PutAttributeMapping_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileId](#API_PutAttributeMapping_RequestSyntax) **   <a name="rolesanywhere-PutAttributeMapping-request-uri-profileId"></a>
The unique identifier of the profile.  
Length Constraints: Fixed length of 36.  
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`   
Required: Yes

## Request Body
<a name="API_PutAttributeMapping_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificateField](#API_PutAttributeMapping_RequestSyntax) **   <a name="rolesanywhere-PutAttributeMapping-request-certificateField"></a>
Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.  
Type: String  
Valid Values: `x509Subject | x509Issuer | x509SAN`   
Required: Yes

 ** [mappingRules](#API_PutAttributeMapping_RequestSyntax) **   <a name="rolesanywhere-PutAttributeMapping-request-mappingRules"></a>
A list of mapping entries for every supported specifier or sub-field.  
Type: Array of [MappingRule](API_MappingRule.md) objects  
Required: Yes

## Response Syntax
<a name="API_PutAttributeMapping_ResponseSyntax"></a>

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
<a name="API_PutAttributeMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [profile](#API_PutAttributeMapping_ResponseSyntax) **   <a name="rolesanywhere-PutAttributeMapping-response-profile"></a>
The state of the profile after a read or write operation.  
Type: [ProfileDetail](API_ProfileDetail.md) object

## Errors
<a name="API_PutAttributeMapping_Errors"></a>

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
<a name="API_PutAttributeMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/PutAttributeMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/PutAttributeMapping) 