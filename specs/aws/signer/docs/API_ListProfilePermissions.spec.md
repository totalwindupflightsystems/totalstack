---
id: "@specs/aws/signer/docs/API_ListProfilePermissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListProfilePermissions"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# ListProfilePermissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_ListProfilePermissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListProfilePermissions
<a name="API_ListProfilePermissions"></a>

Lists the cross-account permissions associated with a signing profile.

## Request Syntax
<a name="API_ListProfilePermissions_RequestSyntax"></a>

```
GET /signing-profiles/{{profileName}}/permissions?nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProfilePermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nextToken](#API_ListProfilePermissions_RequestSyntax) **   <a name="signer-ListProfilePermissions-request-uri-nextToken"></a>
String for specifying the next set of paginated results.

 ** [profileName](#API_ListProfilePermissions_RequestSyntax) **   <a name="signer-ListProfilePermissions-request-uri-profileName"></a>
Name of the signing profile containing the cross-account permissions.  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

## Request Body
<a name="API_ListProfilePermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProfilePermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "permissions": [ 
      { 
         "action": "string",
         "principal": "string",
         "profileVersion": "string",
         "statementId": "string"
      }
   ],
   "policySizeBytes": number,
   "revisionId": "string"
}
```

## Response Elements
<a name="API_ListProfilePermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListProfilePermissions_ResponseSyntax) **   <a name="signer-ListProfilePermissions-response-nextToken"></a>
String for specifying the next set of paginated results.  
Type: String

 ** [permissions](#API_ListProfilePermissions_ResponseSyntax) **   <a name="signer-ListProfilePermissions-response-permissions"></a>
List of permissions associated with the Signing Profile.  
Type: Array of [Permission](API_Permission.md) objects

 ** [policySizeBytes](#API_ListProfilePermissions_ResponseSyntax) **   <a name="signer-ListProfilePermissions-response-policySizeBytes"></a>
Total size of the policy associated with the Signing Profile in bytes.  
Type: Integer

 ** [revisionId](#API_ListProfilePermissions_ResponseSyntax) **   <a name="signer-ListProfilePermissions-response-revisionId"></a>
The identifier for the current revision of profile permissions.  
Type: String

## Errors
<a name="API_ListProfilePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

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
<a name="API_ListProfilePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/ListProfilePermissions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/ListProfilePermissions) 