---
id: "@specs/aws/acm/docs/API_RenewCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RenewCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# RenewCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_RenewCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RenewCertificate
<a name="API_RenewCertificate"></a>

Renews an [eligible ACM certificate](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html). In order to renew your AWS Private CA certificates with ACM, you must first [grant the ACM service principal permission to do so](https://docs.aws.amazon.com/privateca/latest/userguide/assign-permissions.html#PcaPermissions). For more information, see [Testing Managed Renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html) in the ACM User Guide.

## Request Syntax
<a name="API_RenewCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}"
}
```

## Request Parameters
<a name="API_RenewCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_RenewCertificate_RequestSyntax) **   <a name="ACM-RenewCertificate-request-CertificateArn"></a>
String that contains the ARN of the ACM certificate to be renewed. This must be of the form:  
 `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`   
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

## Response Elements
<a name="API_RenewCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RenewCertificate_Errors"></a>

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
<a name="API_RenewCertificate_Examples"></a>

### Renew an ACM Certificate
<a name="API_RenewCertificate_Example_1"></a>

This example illustrates one usage of RenewCertificate.

#### Sample Request
<a name="API_RenewCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
X-Amz-Target: CertificateManager.RenewCertificate
X-Amz-Date: 20190124T171503Z
User-Agent: aws-cli/1.10.20 Python/2.7.3 Linux/3.13.0-83-generic botocore/1.4.11
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160414/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, 
Signature=379429306c5e89b9b4be5b35e29c26cc1da38215d8055a5ed0bdda57bcc881cc

{
  "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012"
}
```

#### Sample Response
<a name="API_RenewCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 3c8d676d-025e-11e6-8823-93164b47113c
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Thu, 24 Jan 2019 17:15:05 GMT
```

## See Also
<a name="API_RenewCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/RenewCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/RenewCertificate) 