---
id: "@specs/aws/signer/docs/API_CancelSigningProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelSigningProfile"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# CancelSigningProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_CancelSigningProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelSigningProfile
<a name="API_CancelSigningProfile"></a>

Changes the state of an `ACTIVE` signing profile to `CANCELED`. A canceled profile is still viewable with the `ListSigningProfiles` operation, but it cannot perform new signing jobs, and is deleted two years after cancelation.

## Request Syntax
<a name="API_CancelSigningProfile_RequestSyntax"></a>

```
DELETE /signing-profiles/{{profileName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelSigningProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileName](#API_CancelSigningProfile_RequestSyntax) **   <a name="signer-CancelSigningProfile-request-uri-profileName"></a>
The name of the signing profile to be canceled.  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

## Request Body
<a name="API_CancelSigningProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelSigningProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelSigningProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelSigningProfile_Errors"></a>

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

## See Also
<a name="API_CancelSigningProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/CancelSigningProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/CancelSigningProfile) 