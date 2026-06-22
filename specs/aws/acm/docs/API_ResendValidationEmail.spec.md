---
id: "@specs/aws/acm/docs/API_ResendValidationEmail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResendValidationEmail"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# ResendValidationEmail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_ResendValidationEmail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResendValidationEmail
<a name="API_ResendValidationEmail"></a>

Resends the email that requests domain ownership validation. The domain owner or an authorized representative must approve the ACM certificate before it can be issued. The certificate can be approved by clicking a link in the mail to navigate to the Amazon certificate approval website and then clicking **I Approve**. However, the validation email can be blocked by spam filters. Therefore, if you do not receive the original mail, you can request that the mail be resent within 72 hours of requesting the ACM certificate. If more than 72 hours have elapsed since your original request or since your last attempt to resend validation mail, you must request a new certificate. For more information about setting up your contact email addresses, see [Configure Email for your Domain](https://docs.aws.amazon.com/acm/latest/userguide/setup-email.html). 

## Request Syntax
<a name="API_ResendValidationEmail_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "Domain": "{{string}}",
   "ValidationDomain": "{{string}}"
}
```

## Request Parameters
<a name="API_ResendValidationEmail_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_ResendValidationEmail_RequestSyntax) **   <a name="ACM-ResendValidationEmail-request-CertificateArn"></a>
String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the [RequestCertificate](API_RequestCertificate.md) action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request. The ARN must be of the form:   
 `arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012`   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

 ** [Domain](#API_ResendValidationEmail_RequestSyntax) **   <a name="ACM-ResendValidationEmail-request-Domain"></a>
The fully qualified domain name (FQDN) of the certificate that needs to be validated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: Yes

 ** [ValidationDomain](#API_ResendValidationEmail_RequestSyntax) **   <a name="ACM-ResendValidationEmail-request-ValidationDomain"></a>
The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the `Domain` value or a superdomain of the `Domain` value. For example, if you requested a certificate for `site.subdomain.example.com` and specify a **ValidationDomain** of `subdomain.example.com`, ACM sends email to the the following five addresses:  
+ admin@subdomain.example.com
+ administrator@subdomain.example.com
+ hostmaster@subdomain.example.com
+ postmaster@subdomain.example.com
+ webmaster@subdomain.example.com
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`   
Required: Yes

## Response Elements
<a name="API_ResendValidationEmail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ResendValidationEmail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **   
The requested Amazon Resource Name (ARN) does not refer to an existing resource.  
HTTP Status Code: 400

 ** InvalidDomainValidationOptionsException **   
One or more values in the [DomainValidationOption](API_DomainValidationOption.md) structure is incorrect.  
HTTP Status Code: 400

 ** InvalidStateException **   
Processing has reached an invalid state.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The supplied input failed to satisfy constraints of an AWS service.  
HTTP Status Code: 400

## Examples
<a name="API_ResendValidationEmail_Examples"></a>

### Resend Validation Email
<a name="API_ResendValidationEmail_Example_1"></a>

This example illustrates one usage of ResendValidationEmail.

#### Sample Request
<a name="API_ResendValidationEmail_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 167
X-Amz-Target: CertificateManager.ResendValidationEmail
X-Amz-Date: 20151222T170722Z
User-Agent: aws-cli/1.9.7 Python/2.7.3 Linux/3.13.0-73-generic botocore/1.3.7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=key_ID/20151222/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, 
Signature=7ec7e70cd614724945545b22bc28296f77803d0c2524573d41c994668f07f435

{
  "CertificateArn": "arn:aws:acm:us-east-1:111122223333 :certificate/12345678-1234-1234-1234-1234567890912",
  "Domain": "www.example.com",
  "ValidationDomain": "example.com"
}
```

#### Sample Response
<a name="API_ResendValidationEmail_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 74bada6d-a8ce-11e5-82ad-d565a2aaa0b3
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 22 Dec 2015 17:07:18 GMT
```

## See Also
<a name="API_ResendValidationEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/ResendValidationEmail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ResendValidationEmail) 