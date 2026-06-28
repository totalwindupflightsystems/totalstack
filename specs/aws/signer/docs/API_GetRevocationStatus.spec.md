---
id: "@specs/aws/signer/docs/API_GetRevocationStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRevocationStatus"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# GetRevocationStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_GetRevocationStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRevocationStatus
<a name="API_GetRevocationStatus"></a>

Retrieves the revocation status of one or more of the signing profile, signing job, and signing certificate.

## Request Syntax
<a name="API_GetRevocationStatus_RequestSyntax"></a>

```
GET /revocations?certificateHashes={{certificateHashes}}&jobArn={{jobArn}}&platformId={{platformId}}&profileVersionArn={{profileVersionArn}}&signatureTimestamp={{signatureTimestamp}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRevocationStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [certificateHashes](#API_GetRevocationStatus_RequestSyntax) **   <a name="signer-GetRevocationStatus-request-uri-certificateHashes"></a>
A list of composite signed hashes that identify certificates.  
A certificate identifier consists of a subject certificate TBS hash (signed by the parent CA) combined with a parent CA TBS hash (signed by the parent CA’s CA). Root certificates are defined as their own CA.  
The following example shows how to calculate a hash for this parameter using OpenSSL commands:   
 `openssl asn1parse -in childCert.pem -strparse 4 -out childCert.tbs`   
 `openssl sha384 < childCert.tbs -binary > childCertTbsHash`   
 `openssl asn1parse -in parentCert.pem -strparse 4 -out parentCert.tbs`   
 `openssl sha384 < parentCert.tbs -binary > parentCertTbsHash xxd -p childCertTbsHash > certificateHash.hex xxd -p parentCertTbsHash >> certificateHash.hex`   
 `cat certificateHash.hex | tr -d '\n'`   
Required: Yes

 ** [jobArn](#API_GetRevocationStatus_RequestSyntax) **   <a name="signer-GetRevocationStatus-request-uri-jobArn"></a>
The ARN of a signing job.  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

 ** [platformId](#API_GetRevocationStatus_RequestSyntax) **   <a name="signer-GetRevocationStatus-request-uri-platformId"></a>
The ID of a signing platform.   
Required: Yes

 ** [profileVersionArn](#API_GetRevocationStatus_RequestSyntax) **   <a name="signer-GetRevocationStatus-request-uri-profileVersionArn"></a>
The version of a signing profile.  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

 ** [signatureTimestamp](#API_GetRevocationStatus_RequestSyntax) **   <a name="signer-GetRevocationStatus-request-uri-signatureTimestamp"></a>
The timestamp of the signature that validates the profile or job.  
Required: Yes

## Request Body
<a name="API_GetRevocationStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRevocationStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "revokedEntities": [ "string" ]
}
```

## Response Elements
<a name="API_GetRevocationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [revokedEntities](#API_GetRevocationStatus_ResponseSyntax) **   <a name="signer-GetRevocationStatus-response-revokedEntities"></a>
A list of revoked entities (including zero or more of the signing profile ARN, signing job ARN, and certificate hashes) supplied as input to the API.  
Type: Array of strings

## Errors
<a name="API_GetRevocationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** InternalServiceErrorException **   
An internal error occurred.  
HTTP Status Code: 500

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

 ** ValidationException **   
You signing certificate could not be validated.  
HTTP Status Code: 400

## See Also
<a name="API_GetRevocationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/GetRevocationStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/GetRevocationStatus) 