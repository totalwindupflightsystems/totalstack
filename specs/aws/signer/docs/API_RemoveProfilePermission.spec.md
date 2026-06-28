---
id: "@specs/aws/signer/docs/API_RemoveProfilePermission"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveProfilePermission"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# RemoveProfilePermission

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_RemoveProfilePermission
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveProfilePermission
<a name="API_RemoveProfilePermission"></a>

Removes cross-account permissions from a signing profile.

## Request Syntax
<a name="API_RemoveProfilePermission_RequestSyntax"></a>

```
DELETE /signing-profiles/{{profileName}}/permissions/{{statementId}}?revisionId={{revisionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemoveProfilePermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileName](#API_RemoveProfilePermission_RequestSyntax) **   <a name="signer-RemoveProfilePermission-request-uri-profileName"></a>
A human-readable name for the signing profile with permissions to be removed.  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

 ** [revisionId](#API_RemoveProfilePermission_RequestSyntax) **   <a name="signer-RemoveProfilePermission-request-uri-revisionId"></a>
An identifier for the current revision of the signing profile permissions.  
Required: Yes

 ** [statementId](#API_RemoveProfilePermission_RequestSyntax) **   <a name="signer-RemoveProfilePermission-request-uri-statementId"></a>
A unique identifier for the cross-account permissions statement.  
Required: Yes

## Request Body
<a name="API_RemoveProfilePermission_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemoveProfilePermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "revisionId": "string"
}
```

## Response Elements
<a name="API_RemoveProfilePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [revisionId](#API_RemoveProfilePermission_ResponseSyntax) **   <a name="signer-RemoveProfilePermission-response-revisionId"></a>
An identifier for the current revision of the profile permissions.  
Type: String

## Errors
<a name="API_RemoveProfilePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ConflictException **   
The resource encountered a conflicting state.  
HTTP Status Code: 409

 ** InternalServiceErrorException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
A specified resource could not be found.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

 ** ValidationException **   
You signing certificate could not be validated.  
HTTP Status Code: 400

## See Also
<a name="API_RemoveProfilePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/RemoveProfilePermission) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/RemoveProfilePermission) 