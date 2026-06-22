---
id: "@specs/aws/acm/docs/API_ImportCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ImportCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# ImportCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_ImportCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ImportCertificate
<a name="API_ImportCertificate"></a>

Imports a certificate into AWS Certificate Manager (ACM) to use with services that are integrated with ACM. Note that [integrated services](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html) allow only certificate types and keys they support to be associated with their resources. Further, their support differs depending on whether the certificate is imported into IAM or into ACM. For more information, see the documentation for each service. For more information about importing certificates into ACM, see [Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the * AWS Certificate Manager User Guide*. 

**Note**  
ACM does not provide [managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html) for certificates that you import.

Note the following guidelines when importing third party certificates:
+ You must enter the private key that matches the certificate you are importing.
+ The private key must be unencrypted. You cannot import a private key that is protected by a password or a passphrase.
+ The private key must be no larger than 5 KB (5,120 bytes).
+ The certificate, private key, and certificate chain must be PEM-encoded.
+ The current time must be between the `Not Before` and `Not After` certificate fields.
+ The `Issuer` field must not be empty.
+ The OCSP authority URL, if present, must not exceed 1000 characters.
+ To import a new certificate, omit the `CertificateArn` argument. Include this argument only when you want to replace a previously imported certificate.
+ When you import a certificate by using the CLI, you must specify the certificate, the certificate chain, and the private key by their file names preceded by `fileb://`. For example, you can specify a certificate saved in the `C:\temp` folder as `fileb://C:\temp\certificate_to_import.pem`. If you are making an HTTP or HTTPS Query request, include these arguments as BLOBs. 
+ When you import a certificate by using an SDK, you must specify the certificate, the certificate chain, and the private key files in the manner required by the programming language you're using. 
+ The cryptographic algorithm of an imported certificate must match the algorithm of the signing CA. For example, if the signing CA key type is RSA, then the certificate key type must also be RSA.

This operation returns the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the imported certificate.

## Request Syntax
<a name="API_ImportCertificate_RequestSyntax"></a>

```
{
   "Certificate": {{blob}},
   "CertificateArn": "{{string}}",
   "CertificateChain": {{blob}},
   "PrivateKey": {{blob}},
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ImportCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [Certificate](#API_ImportCertificate_RequestSyntax) **   <a name="ACM-ImportCertificate-request-Certificate"></a>
The certificate to import.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Required: Yes

 ** [PrivateKey](#API_ImportCertificate_RequestSyntax) **   <a name="ACM-ImportCertificate-request-PrivateKey"></a>
The private key that matches the public key in the certificate.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 5120.  
Required: Yes

 ** [CertificateArn](#API_ImportCertificate_RequestSyntax) **   <a name="ACM-ImportCertificate-request-CertificateArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an imported certificate to replace. To import a new certificate, omit this field.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: No

 ** [CertificateChain](#API_ImportCertificate_RequestSyntax) **   <a name="ACM-ImportCertificate-request-CertificateChain"></a>
The PEM encoded certificate chain.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 1. Maximum length of 2097152.  
Required: No

 ** [Tags](#API_ImportCertificate_RequestSyntax) **   <a name="ACM-ImportCertificate-request-Tags"></a>
One or more resource tags to associate with the imported certificate.   
Note: You cannot apply tags when reimporting a certificate.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_ImportCertificate_ResponseSyntax"></a>

```
{
   "CertificateArn": "string"
}
```

## Response Elements
<a name="API_ImportCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CertificateArn](#API_ImportCertificate_ResponseSyntax) **   <a name="ACM-ImportCertificate-response-CertificateArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the imported certificate.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*` 

## Errors
<a name="API_ImportCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.  
HTTP Status Code: 400

 ** InvalidArnException **   
The requested Amazon Resource Name (ARN) does not refer to an existing resource.  
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

 ** ResourceNotFoundException **   
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.  
HTTP Status Code: 400

 ** TagPolicyException **   
A specified tag did not comply with an existing tag policy and was rejected.  
HTTP Status Code: 400

 ** TooManyTagsException **   
The request contains too many tags. Try the request again with fewer tags.  
HTTP Status Code: 400

 ** ValidationException **   
The supplied input failed to satisfy constraints of an AWS service.  
HTTP Status Code: 400

## Examples
<a name="API_ImportCertificate_Examples"></a>

### Import a certificate
<a name="API_ImportCertificate_Example_1"></a>

This example illustrates one usage of ImportCertificate.

#### Sample Request
<a name="API_ImportCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
X-Amz-Target: CertificateManager.ImportCertificate
X-Amz-Date: 20161011T184744Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=key_ID/20161011/us-east-1/acm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,
Signature=60f965247476c4672c498c24ba255e52a62a7e4bd8678d8ee788af5ffe42f377

{
    "CertificateChain": "Base64-encoded blob",
    "PrivateKey": "Base64-encoded blob",
    "Certificate": "Base64-encoded blob"	
}
```

#### Sample Response
<a name="API_ImportCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 32f9ab0a-8fe3-11e6-8d69-c91606b24a3f
Content-Type: application/x-amz-json-1.1
Content-Length: 104
Date: Tue, 11 Oct 2016 18:47:46 GMT

{"CertificateArn":"arn:aws:acm:us-east-1:111122223333:certificate/91228a40-ad89-4ce0-9f6c-07009fc8fdfb"}
```

## See Also
<a name="API_ImportCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/ImportCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ImportCertificate) 