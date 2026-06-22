---
id: "@specs/aws/acm/docs/API_GetCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# GetCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_GetCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetCertificate
<a name="API_GetCertificate"></a>

Retrieves a certificate and its certificate chain. The certificate may be either a public or private certificate issued using the ACM `RequestCertificate` action, or a certificate imported into ACM using the `ImportCertificate` action. The chain consists of the certificate of the issuing CA and the intermediate certificates of any other subordinate CAs. All of the certificates are base64 encoded. You can use [OpenSSL](https://wiki.openssl.org/index.php/Command_Line_Utilities) to decode the certificates and inspect individual fields.

## Request Syntax
<a name="API_GetCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_GetCertificate_RequestSyntax) **   <a name="ACM-GetCertificate-request-CertificateArn"></a>
String that contains a certificate ARN in the following format:  
 `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`   
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

## Response Syntax
<a name="API_GetCertificate_ResponseSyntax"></a>

```
{
   "Certificate": "string",
   "CertificateChain": "string"
}
```

## Response Elements
<a name="API_GetCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_GetCertificate_ResponseSyntax) **   <a name="ACM-GetCertificate-response-Certificate"></a>
The ACM-issued certificate corresponding to the ARN specified as input.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Pattern: `-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?` 

 ** [CertificateChain](#API_GetCertificate_ResponseSyntax) **   <a name="ACM-GetCertificate-response-CertificateChain"></a>
Certificates forming the requested certificate's chain of trust. The chain consists of the certificate of the issuing CA and the intermediate certificates of any other subordinate CAs.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2097152.  
Pattern: `(-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}\u000D?\u000A)*-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?` 

## Errors
<a name="API_GetCertificate_Errors"></a>

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

 ** ValidationException **   
The supplied input failed to satisfy constraints of an AWS service.  
HTTP Status Code: 400

## Examples
<a name="API_GetCertificate_Examples"></a>

### Get an ACM Certificate
<a name="API_GetCertificate_Example_1"></a>

This example illustrates one usage of GetCertificate.

#### Sample Request
<a name="API_GetCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
X-Amz-Target: CertificateManager.GetCertificate
X-Amz-Date: 20151221T210018Z
User-Agent: aws-cli/1.9.7 Python/2.7.3 Linux/3.13.0-71-generic botocore/1.3.7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151221/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, 
Signature=b51b4c2d5518473a8552fdab8e313c76254e9ca64e4d8ab69c2ebef83dbd459b

{
  "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012"
}
```

#### Sample Response
<a name="API_GetCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: d5300b5a-a825-11e5-9141-fbb8a078e3eb
Content-Type: application/x-amz-json-1.1
Content-Length: 6506
Date: Mon, 21 Dec 2015 21:00:15 GMT

{
  "Certificate":
    "-----BEGIN CERTIFICATE-----Base64-encoded-----END CERTIFICATE-----",
  "CertificateChain":
    "-----BEGIN CERTIFICATE-----Base64-encoded-----END CERTIFICATE-----"
    "-----BEGIN CERTIFICATE-----Base64-encoded-----END CERTIFICATE-----"
    "-----BEGIN CERTIFICATE-----Base64-encoded-----END CERTIFICATE-----"
}
```

## See Also
<a name="API_GetCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/GetCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/GetCertificate) 