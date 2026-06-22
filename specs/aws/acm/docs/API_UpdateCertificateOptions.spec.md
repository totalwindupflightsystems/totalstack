---
id: "@specs/aws/acm/docs/API_UpdateCertificateOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCertificateOptions"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# UpdateCertificateOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_UpdateCertificateOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCertificateOptions
<a name="API_UpdateCertificateOptions"></a>

Updates a certificate. You can use this function to specify whether to export your certificate. Certificate transparency logging opt-out is no longer available. For more information, see [Certificate Transparency Logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency) and [AWS Certificate Manager Exportable Managed Certificates](https://docs.aws.amazon.com/acm/latest/userguide/acm-exportable-certificates.html).

## Request Syntax
<a name="API_UpdateCertificateOptions_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}",
   "Options": { 
      "CertificateTransparencyLoggingPreference": "{{string}}",
      "Export": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateCertificateOptions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_UpdateCertificateOptions_RequestSyntax) **   <a name="ACM-UpdateCertificateOptions-request-CertificateArn"></a>
ARN of the requested certificate to update. This must be of the form:  
 `arn:aws:acm:us-east-1:account:certificate/12345678-1234-1234-1234-123456789012 `   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

 ** [Options](#API_UpdateCertificateOptions_RequestSyntax) **   <a name="ACM-UpdateCertificateOptions-request-Options"></a>
Use to update the options for your certificate. Currently, you can specify whether to export your certificate. Certificate transparency logging opt-out is no longer available. All public certificates are recorded in a certificate transparency log. For more information, see [Certificate Transparency Logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency).  
Type: [CertificateOptions](API_CertificateOptions.md) object  
Required: Yes

## Response Elements
<a name="API_UpdateCertificateOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCertificateOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **   
The requested Amazon Resource Name (ARN) does not refer to an existing resource.  
HTTP Status Code: 400

 ** InvalidStateException **   
Processing has reached an invalid state.  
HTTP Status Code: 400

 ** LimitExceededException **   
An ACM quota has been exceeded.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The supplied input failed to satisfy constraints of an AWS service.  
HTTP Status Code: 400

## Examples
<a name="API_UpdateCertificateOptions_Examples"></a>

### UpdateCertificateOptions
<a name="API_UpdateCertificateOptions_Example_1"></a>

This example illustrates one usage of UpdateCertificateOptions.

#### Sample Request
<a name="API_UpdateCertificateOptions_Example_1_Request"></a>

```
POST / HTTP/1.1
acm.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 185
X-Amz-Target: CertificateManager.UpdateCertificateOptions
X-Amz-Date: 20180326T222032Z
User-Agent: aws-cli/1.14.28 Python/2.7.9 Windows/8 botocore/1.8.32
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=key_ID/20151222/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, 
Signature=7ec7e70cd614724945545b22bc28296f77803d0c2524573d41c994668f07f435

{
  "CertificateArn": "arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012",
  "CertificateOptions": {
    "CertificateTransparencyLoggingPreference": "DISABLED"
  }
}
```

### Example
<a name="API_UpdateCertificateOptions_Example_2"></a>

This example illustrates one usage of UpdateCertificateOptions.

#### Sample Response
<a name="API_UpdateCertificateOptions_Example_2_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: e6f55ecb-3143-11e8-af72-0bd5049841d5
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Tue, 22 Dec 2015 17:07:18 GMT
```

## See Also
<a name="API_UpdateCertificateOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/UpdateCertificateOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/UpdateCertificateOptions) 