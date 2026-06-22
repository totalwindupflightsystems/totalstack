---
id: "@specs/aws/acm/docs/API_RevokeCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RevokeCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# RevokeCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_RevokeCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RevokeCertificate
<a name="API_RevokeCertificate"></a>

Revokes a public ACM certificate. You can only revoke certificates that have been previously exported.

**Important**  
Once a certificate is revoked, you cannot reuse the certificate. Revoking a certificate is permanent.

## Request Syntax
<a name="API_RevokeCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "RevocationReason": "{{string}}"
}
```

## Request Parameters
<a name="API_RevokeCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_RevokeCertificate_RequestSyntax) **   <a name="ACM-RevokeCertificate-request-CertificateArn"></a>
The Amazon Resource Name (ARN) of the public or private certificate that will be revoked. The ARN must have the following form:   
 `arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

 ** [RevocationReason](#API_RevokeCertificate_RequestSyntax) **   <a name="ACM-RevokeCertificate-request-RevocationReason"></a>
Specifies why you revoked the certificate.  
Type: String  
Valid Values: `UNSPECIFIED | KEY_COMPROMISE | CA_COMPROMISE | AFFILIATION_CHANGED | SUPERCEDED | SUPERSEDED | CESSATION_OF_OPERATION | CERTIFICATE_HOLD | REMOVE_FROM_CRL | PRIVILEGE_WITHDRAWN | A_A_COMPROMISE`   
Required: Yes

## Response Syntax
<a name="API_RevokeCertificate_ResponseSyntax"></a>

```
{
   "CertificateArn": "string"
}
```

## Response Elements
<a name="API_RevokeCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateArn](#API_RevokeCertificate_ResponseSyntax) **   <a name="ACM-RevokeCertificate-response-CertificateArn"></a>
The Amazon Resource Name (ARN) of the public or private certificate that was revoked.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*` 

## Errors
<a name="API_RevokeCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have access required to perform this action.  
HTTP Status Code: 400

 ** ConflictException **   
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.  
HTTP Status Code: 400

 ** InvalidArnException **   
The requested Amazon Resource Name (ARN) does not refer to an existing resource.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The certificate is in use by another AWS service in the caller's account. Remove the association and try again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied because it exceeded a quota.    
 ** throttlingReasons **   
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **   
The supplied input failed to satisfy constraints of an AWS service.  
HTTP Status Code: 400

## See Also
<a name="API_RevokeCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/RevokeCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/RevokeCertificate) 