---
id: "@specs/aws/acm/docs/API_ExportCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExportCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# ExportCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_ExportCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExportCertificate
<a name="API_ExportCertificate"></a>

Exports a private certificate issued by a private certificate authority (CA) or a public certificate for use anywhere. The exported file contains the certificate, the certificate chain, and the encrypted private key associated with the public key that is embedded in the certificate. For security, you must assign a passphrase for the private key when exporting it. 

For information about exporting and formatting a certificate using the ACM console or AWS CLI, see [Export a private certificate](https://docs.aws.amazon.com/acm/latest/userguide/export-private.html) and [Export a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/export-public-certificate).

**Note**  
ACM public certificates created prior to June 17, 2025 cannot be exported.

## Request Syntax
<a name="API_ExportCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "Passphrase": {{blob}}
}
```

## Request Parameters
<a name="API_ExportCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_ExportCertificate_RequestSyntax) **   <a name="ACM-ExportCertificate-request-CertificateArn"></a>
An Amazon Resource Name (ARN) of the issued certificate. This must be of the form:  
 `arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

 ** [Passphrase](#API_ExportCertificate_RequestSyntax) **   <a name="ACM-ExportCertificate-request-Passphrase"></a>
Passphrase to associate with the encrypted exported private key.   
When creating your passphrase, you can use any ASCII character except \#, $, or %.
If you want to later decrypt the private key, you must have the passphrase. You can use the following OpenSSL command to decrypt a private key. After entering the command, you are prompted for the passphrase.  
 `openssl rsa -in encrypted_key.pem -out decrypted_key.pem`   
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 4. Maximum length of 128.  
Required: Yes

## Response Syntax
<a name="API_ExportCertificate_ResponseSyntax"></a>

```
{
   "Certificate": "string",
   "CertificateChain": "string",
   "PrivateKey": "string"
}
```

## Response Elements
<a name="API_ExportCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_ExportCertificate_ResponseSyntax) **   <a name="ACM-ExportCertificate-response-Certificate"></a>
The base64 PEM-encoded certificate.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Pattern: `-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?` 

 ** [CertificateChain](#API_ExportCertificate_ResponseSyntax) **   <a name="ACM-ExportCertificate-response-CertificateChain"></a>
The base64 PEM-encoded certificate chain. This does not include the certificate that you are exporting.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2097152.  
Pattern: `(-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}\u000D?\u000A)*-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?` 

 ** [PrivateKey](#API_ExportCertificate_ResponseSyntax) **   <a name="ACM-ExportCertificate-response-PrivateKey"></a>
The encrypted private key associated with the public key in the certificate. The key is output in PKCS \#8 format and is base64 PEM-encoded.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 524288.  
Pattern: `-{5}BEGIN PRIVATE KEY-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END PRIVATE KEY-{5}(\u000D?\u000A)?` 

## Errors
<a name="API_ExportCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **   
The requested Amazon Resource Name (ARN) does not refer to an existing resource.  
HTTP Status Code: 400

 ** RequestInProgressException **   
The certificate request is in process and the certificate in your account has not yet been issued.  
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

## Examples
<a name="API_ExportCertificate_Examples"></a>

### Example
<a name="API_ExportCertificate_Example_1"></a>

This example illustrates one usage of ExportCertificate.

#### Sample Request
<a name="API_ExportCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 135
X-Amz-Target: CertificateManager.ExportCertificate
X-Amz-Date: 20180331T175638Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=key_ID/20180331/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
Signature=7b3f783da1b701aea1b6b49dea7d5194d7e2b253f152cfb939459ba3b0ba2c1d

{
  "CertificateArn": "arn:aws:acm:us-east-1:account:certificate/12345678-1234-1234-1234-1234556789012",
  "Passphrase": "cGFzc3dvcmQ="
}
```

#### Sample Response
<a name="API_ExportCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: dd520651-350c-11e8-a99a-c76ec78904bf
Content-Type: application/x-amz-json-1.1
Content-Length: 5860
Date: Sat, 31 Mar 2018 17:56:41 GMT
Connection: Keep-alive

{
  "Certificate": 
    "-----BEGIN CERTIFICATE-----Base64-encodedEND CERTIFICATE-----",
  "CertificateChain": 
    "-----BEGIN CERTIFICATE-----Base64-encodedEND CERTIFICATE-----
     -----BEGIN CERTIFICATE-----Base64-encodedEND CERTIFICATE-----",
  "PrivateKey": 
    "-----BEGIN ENCRYPTED PRIVATE KEYBase64-encoded-----END ENCRYPTED PRIVATE KEY-----"
}
```

## See Also
<a name="API_ExportCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/ExportCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ExportCertificate) 