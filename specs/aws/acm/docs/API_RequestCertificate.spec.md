---
id: "@specs/aws/acm/docs/API_RequestCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RequestCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# RequestCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_RequestCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RequestCertificate
<a name="API_RequestCertificate"></a>

Requests an ACM certificate for use with other AWS services. To request an ACM certificate, you must specify a fully qualified domain name (FQDN) in the `DomainName` parameter. You can also specify additional FQDNs in the `SubjectAlternativeNames` parameter. 

If you are requesting a private certificate, domain validation is not required. If you are requesting a public certificate, each domain name that you specify must be validated to verify that you own or control the domain. You can use [DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html) or [email validation](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html). We recommend that you use DNS validation.

**Note**  
ACM behavior differs from the [RFC 6125](https://datatracker.ietf.org/doc/html/rfc6125#appendix-B.2) specification of the certificate validation process. ACM first checks for a Subject Alternative Name, and, if it finds one, ignores the common name (CN).

After successful completion of the `RequestCertificate` action, there is a delay of several seconds before you can retrieve information about the new certificate.

## Request Syntax
<a name="API_RequestCertificate_RequestSyntax"></a>

```
{
   "CertificateAuthorityArn": "{{string}}",
   "DomainName": "{{string}}",
   "DomainValidationOptions": [ 
      { 
         "DomainName": "{{string}}",
         "ValidationDomain": "{{string}}"
      }
   ],
   "IdempotencyToken": "{{string}}",
   "KeyAlgorithm": "{{string}}",
   "ManagedBy": "{{string}}",
   "Options": { 
      "CertificateTransparencyLoggingPreference": "{{string}}",
      "Export": "{{string}}"
   },
   "SubjectAlternativeNames": [ "{{string}}" ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ValidationMethod": "{{string}}"
}
```

## Request Parameters
<a name="API_RequestCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [DomainName](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-DomainName"></a>
Fully qualified domain name (FQDN), such as www.example.com, that you want to secure with an ACM certificate. Use an asterisk (\*) to create a wildcard certificate that protects several sites in the same domain. For example, \*.example.com protects www.example.com, site.example.com, and images.example.com.   
In compliance with [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280), the length of the domain name (technically, the Common Name) that you provide cannot exceed 64 octets (characters), including periods. To add a longer domain name, specify it in the Subject Alternative Name field, which supports names up to 253 octets in length.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: Yes

 ** [CertificateAuthorityArn](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate. If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the [AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) user guide. The ARN must have the following form:   
 `arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** [DomainValidationOptions](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-DomainValidationOptions"></a>
The domain name that you want ACM to use to send you emails so that you can validate domain ownership.  
Type: Array of [DomainValidationOption](API_DomainValidationOption.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Required: No

 ** [IdempotencyToken](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-IdempotencyToken"></a>
Customer chosen string that can be used to distinguish between calls to `RequestCertificate`. Idempotency tokens time out after one hour. Therefore, if you call `RequestCertificate` multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `\w+`   
Required: No

 ** [KeyAlgorithm](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-KeyAlgorithm"></a>
Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. RSA is the default key algorithm for ACM certificates. Elliptic Curve Digital Signature Algorithm (ECDSA) keys are smaller, offering security comparable to RSA keys but with greater computing efficiency. However, ECDSA is not supported by all network clients. Some AWS services may require RSA keys, or only support ECDSA keys of a particular size, while others allow the use of either RSA and ECDSA keys to ensure that compatibility is not broken. Check the requirements for the AWS service where you plan to deploy your certificate. For more information about selecting an algorithm, see [Key algorithms](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-characteristics.html#algorithms-term).  
Algorithms supported for an ACM certificate request include:   
+  `RSA_2048` 
+  `EC_prime256v1` 
+  `EC_secp384r1` 
Other listed algorithms are for imported certificates only. 
When you request a private PKI certificate signed by a CA from AWS Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.
Default: RSA\_2048  
Type: String  
Valid Values: `RSA_1024 | RSA_2048 | RSA_3072 | RSA_4096 | EC_prime256v1 | EC_secp384r1 | EC_secp521r1`   
Required: No

 ** [ManagedBy](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-ManagedBy"></a>
Identifies the AWS service that manages the certificate issued by ACM.  
Type: String  
Valid Values: `CLOUDFRONT`   
Required: No

 ** [Options](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-Options"></a>
You can use this parameter to specify whether to export your certificate.  
Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log. For more information, see [Certificate Transparency Logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency).  
You can export public ACM certificates to use with AWS services as well as outside the AWS Cloud. For more information, see [AWS Certificate Manager exportable public certificate](https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html).  
Type: [CertificateOptions](API_CertificateOptions.md) object  
Required: No

 ** [SubjectAlternativeNames](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-SubjectAlternativeNames"></a>
Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. For example, add the name www.example.net to a certificate for which the `DomainName` field is www.example.com if users can reach your site by using either name. The maximum number of domain names that you can add to an ACM certificate is 100. However, the initial quota is 10 domain names. If you need more than 10 names, you must request a quota increase. For more information, see [Quotas](https://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html).  
 The maximum length of a SAN DNS name is 253 octets. The name is made up of multiple labels separated by periods. No label can be longer than 63 octets. Consider the following examples:   
+  `(63 octets).(63 octets).(63 octets).(61 octets)` is legal because the total length is 253 octets (63\+1\+63\+1\+63\+1\+61) and no label exceeds 63 octets.
+  `(64 octets).(63 octets).(63 octets).(61 octets)` is not legal because the total length exceeds 253 octets (64\+1\+63\+1\+63\+1\+61) and the first label exceeds 63 octets.
+  `(63 octets).(63 octets).(63 octets).(62 octets)` is not legal because the total length of the DNS name (63\+1\+63\+1\+63\+1\+62) exceeds 253 octets.
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: No

 ** [Tags](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-Tags"></a>
One or more resource tags to associate with the certificate.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** [ValidationMethod](#API_RequestCertificate_RequestSyntax) **   <a name="ACM-RequestCertificate-request-ValidationMethod"></a>
The method you want to use if you are requesting a public certificate to validate that you own or control domain. You can [validate with DNS](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html) or [validate with email](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html). We recommend that you use DNS validation.   
Type: String  
Valid Values: `EMAIL | DNS | HTTP`   
Required: No

## Response Syntax
<a name="API_RequestCertificate_ResponseSyntax"></a>

```
{
   "CertificateArn": "string"
}
```

## Response Elements
<a name="API_RequestCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateArn](#API_RequestCertificate_ResponseSyntax) **   <a name="ACM-RequestCertificate-response-CertificateArn"></a>
String that contains the ARN of the issued certificate. This must be of the form:  
 `arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*` 

## Errors
<a name="API_RequestCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **   
The requested Amazon Resource Name (ARN) does not refer to an existing resource.  
HTTP Status Code: 400

 ** InvalidDomainValidationOptionsException **   
One or more values in the [DomainValidationOption](API_DomainValidationOption.md) structure is incorrect.  
HTTP Status Code: 400

 ** InvalidParameterException **   
An input parameter was invalid.  
HTTP Status Code: 400

 ** InvalidTagException **   
One or both of the values that make up the key-value pair is not valid. For example, you cannot specify a tag value that begins with `aws:`.  
HTTP Status Code: 400

 ** LimitExceededException **   
An ACM quota has been exceeded.  
HTTP Status Code: 400

 ** TagPolicyException **   
A specified tag did not comply with an existing tag policy and was rejected.  
HTTP Status Code: 400

 ** TooManyTagsException **   
The request contains too many tags. Try the request again with fewer tags.  
HTTP Status Code: 400

## Examples
<a name="API_RequestCertificate_Examples"></a>

### Request a public ACM certificate
<a name="API_RequestCertificate_Example_1"></a>

This example illustrates one usage of RequestCertificate.

#### Sample Request
<a name="API_RequestCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 171
X-Amz-Target: CertificateManager.RequestCertificate
X-Amz-Date: 20180326T215401Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20151222/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, 
Signature=dbba4b1fa1199c011c0b781b94c97b14cbe75fa64dc6424232c903798d2a83b5

{
  "IdempotencyToken": "184627",
  "CertificateOptions": {
    "CertificateTransparencyLoggingPreference": "DISABLED"
  },
  "ValidationMethod": "DNS",
  "DomainName": "www.example.com"
}
```

#### Sample Response
<a name="API_RequestCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 32c3ca21-3140-11e8-8ba0-f79627c5200e
Content-Type: application/x-amz-json-1.1
Content-Length: 104
Date: Mon, 26 Mar 2018 21:54:03 GMT

{
  "CertificateArn":"arn:aws:acm:us-east-1:123456789012:certificate/1ad574bd-eeb0-466e-b961-74ec8b405093"
}
```

### Request a private certificate
<a name="API_RequestCertificate_Example_2"></a>

This example illustrates one usage of RequestCertificate.

#### Sample Request
<a name="API_RequestCertificate_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 305
X-Amz-Target: CertificateManager.RequestCertificate
X-Amz-Date: 20180331T173532Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=key_ID/20180331/us-east-1/acm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
Signature=11be86a0995ac158327fe8ccf6f44c19af7e6768fbafe0ec10e74436770272fa

{
  "IdempotencyToken": "12563",
  "CertificateAuthorityArn": "arn:aws:acm-pca:us-east-1:account:certificate-authority/12345678-1234-1234-1234-123456789012",
  "DomainName": "www.example.com"
}
```

#### Sample Response
<a name="API_RequestCertificate_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: eaedc93a-3509-11e8-a99a-c76ec78904bf
Content-Type: application/x-amz-json-1.1
Content-Length: 104
Date: Sat, 31 Mar 2018 17:35:34 GMT
Connection: Keep-alive

{
  "CertificateArn": "arn:aws:acm:us-east-1:account:certificate/88888888-4444-4444-4444-111111111111"
}
```

## See Also
<a name="API_RequestCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/RequestCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/RequestCertificate) 