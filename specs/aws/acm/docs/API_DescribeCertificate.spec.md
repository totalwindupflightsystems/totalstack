---
id: "@specs/aws/acm/docs/API_DescribeCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# DescribeCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_DescribeCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCertificate
<a name="API_DescribeCertificate"></a>

Returns detailed metadata about the specified ACM certificate.

If you have just created a certificate using the `RequestCertificate` action, there is a delay of several seconds before you can retrieve information about it.

## Request Syntax
<a name="API_DescribeCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_DescribeCertificate_RequestSyntax) **   <a name="ACM-DescribeCertificate-request-CertificateArn"></a>
The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following form:  
 `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`   
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

## Response Syntax
<a name="API_DescribeCertificate_ResponseSyntax"></a>

```
{
   "Certificate": { 
      "CertificateArn": "string",
      "CertificateAuthorityArn": "string",
      "CreatedAt": number,
      "DomainName": "string",
      "DomainValidationOptions": [ 
         { 
            "DomainName": "string",
            "HttpRedirect": { 
               "RedirectFrom": "string",
               "RedirectTo": "string"
            },
            "ResourceRecord": { 
               "Name": "string",
               "Type": "string",
               "Value": "string"
            },
            "ValidationDomain": "string",
            "ValidationEmails": [ "string" ],
            "ValidationMethod": "string",
            "ValidationStatus": "string"
         }
      ],
      "ExtendedKeyUsages": [ 
         { 
            "Name": "string",
            "OID": "string"
         }
      ],
      "FailureReason": "string",
      "ImportedAt": number,
      "InUseBy": [ "string" ],
      "IssuedAt": number,
      "Issuer": "string",
      "KeyAlgorithm": "string",
      "KeyUsages": [ 
         { 
            "Name": "string"
         }
      ],
      "ManagedBy": "string",
      "NotAfter": number,
      "NotBefore": number,
      "Options": { 
         "CertificateTransparencyLoggingPreference": "string",
         "Export": "string"
      },
      "RenewalEligibility": "string",
      "RenewalSummary": { 
         "DomainValidationOptions": [ 
            { 
               "DomainName": "string",
               "HttpRedirect": { 
                  "RedirectFrom": "string",
                  "RedirectTo": "string"
               },
               "ResourceRecord": { 
                  "Name": "string",
                  "Type": "string",
                  "Value": "string"
               },
               "ValidationDomain": "string",
               "ValidationEmails": [ "string" ],
               "ValidationMethod": "string",
               "ValidationStatus": "string"
            }
         ],
         "RenewalStatus": "string",
         "RenewalStatusReason": "string",
         "UpdatedAt": number
      },
      "RevocationReason": "string",
      "RevokedAt": number,
      "Serial": "string",
      "SignatureAlgorithm": "string",
      "Status": "string",
      "Subject": "string",
      "SubjectAlternativeNames": [ "string" ],
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DescribeCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Certificate](#API_DescribeCertificate_ResponseSyntax) **   <a name="ACM-DescribeCertificate-response-Certificate"></a>
Metadata about an ACM certificate.  
Type: [CertificateDetail](API_CertificateDetail.md) object

## Errors
<a name="API_DescribeCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **   
The requested Amazon Resource Name (ARN) does not refer to an existing resource.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The supplied input failed to satisfy constraints of an AWS service.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeCertificate_Examples"></a>

### Describe an ACM Certificate
<a name="API_DescribeCertificate_Example_1"></a>

This example illustrates one usage of DescribeCertificate.

#### Sample Request
<a name="API_DescribeCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
X-Amz-Target: CertificateManager.DescribeCertificate
X-Amz-Date: 20151221T203246Z
User-Agent: aws-cli/1.9.7 Python/2.7.3 Linux/3.13.0-71-generic botocore/1.3.7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20151221/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, 
Signature=76913a7d6013d34afbdc1bbd6c3e77d5edd3fa2d9883a94d946c6eeea5908d9e

{
  "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012"
}
```

#### Sample Response
<a name="API_DescribeCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: fd1e5a07-a821-11e5-845d-95c070464235
Content-Type: application/x-amz-json-1.1
Content-Length: 1035
Date: Mon, 21 Dec 2015 20:32:43 GMT

{
  "Certificate": {
    "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012",
    "CreatedAt": 1450212224.0,
    "DomainName": "example.com",
    "DomainValidationOptions": [
      {
        "DomainName": "example.com",
        "ValidationDomain": "example.com",
        "ValidationEmails": [
          "hostmaster@example.com",
          "admin@example.com",
          "postmaster@example.com",
          "webmaster@example.com",
          "administrator@example.com"
        ]
      },
      {
        "DomainName": "www.example.com",
        "ValidationDomain": "www.example.com",
        "ValidationEmails": [
          "hostmaster@example.com",
          "admin@example.com",
          "postmaster@example.com",
          "webmaster@example.com",
          "administrator@example.com"
        ]
      }
    ],
    "InUseBy": [
      "arn:aws:cloudfront::111122223333:distribution/E12KXPQHVLSYVC"
    ],
    "IssuedAt": 1450212292.0,
    "Issuer": "Amazon",
    "KeyAlgorithm": "RSA-2048",
    "NotAfter": 1484481600.0,
    "NotBefore": 1450137600.0,
    "Renewal Elegibility": "ELIGIBLE",
    "RenewalSummary": { 
         "DomainValidationOptions": [ 
            { 
               "DomainName": "www.example.com",
               "ResourceRecord": { 
                  "Name": "example",
                  "Type": "CNAME",
                  "Value": "example"
               },
               "ValidationDomain": "www.amazon.com",
               "ValidationEmails": [ "example@amazon.com" ],
               "ValidationMethod": "DNS",
               "ValidationStatus": "SUCCESS"
            }
         ],
         "RenewalStatus": "SUCCESS",
         "UpdatedAt": 1450212224.0
      },
    "Serial": "07:71:71:f4:6b:e7:bf:63:87:e6:ad:3c:b2:0f:d0:5b",
    "SignatureAlgorithm": "SHA256WITHRSA",
    "Status": "ISSUED",
    "Subject": "CN=example.com",
    "SubjectAlternativeNames": [
      "example.com",
      "www.example.com"
    ]
  }
}
```

## See Also
<a name="API_DescribeCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/DescribeCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DescribeCertificate) 