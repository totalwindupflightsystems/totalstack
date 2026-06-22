---
id: "@specs/aws/acm/docs/API_ListTagsForCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForCertificate"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# ListTagsForCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_ListTagsForCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForCertificate
<a name="API_ListTagsForCertificate"></a>

Lists the tags that have been applied to the ACM certificate. Use the certificate's Amazon Resource Name (ARN) to specify the certificate. To add a tag to an ACM certificate, use the [AddTagsToCertificate](API_AddTagsToCertificate.md) action. To delete a tag, use the [RemoveTagsFromCertificate](API_RemoveTagsFromCertificate.md) action. 

## Request Syntax
<a name="API_ListTagsForCertificate_RequestSyntax"></a>

```
{
   "CertificateArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**  
In the following list, the required parameters are described first.

 ** [CertificateArn](#API_ListTagsForCertificate_RequestSyntax) **   <a name="ACM-ListTagsForCertificate-request-CertificateArn"></a>
String that contains the ARN of the ACM certificate for which you want to list the tags. This must have the following form:  
 `arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012`   
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`   
Required: Yes

## Response Syntax
<a name="API_ListTagsForCertificate_ResponseSyntax"></a>

```
{
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Tags](#API_ListTagsForCertificate_ResponseSyntax) **   <a name="ACM-ListTagsForCertificate-response-Tags"></a>
The key-value pairs that define the applied tags.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_ListTagsForCertificate_Errors"></a>

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
<a name="API_ListTagsForCertificate_Examples"></a>

### List tags for an ACM Certificate
<a name="API_ListTagsForCertificate_Example_1"></a>

This example illustrates one usage of ListTagsForCertificate.

#### Sample Request
<a name="API_ListTagsForCertificate_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: acm.us-east-1.amazonaws.com
X-Amz-Target: CertificateManager.ListTagsForCertificate
X-Amz-Date: 20160414T162913Z
User-Agent: aws-cli/1.10.20 Python/2.7.3 Linux/3.13.0-83-generic botocore/1.4.11
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=key_ID/20160414/us-east-1/acm/aws4_request, 
SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target,
Signature=c1b80f2b1b6c73c39e1a9594e621648e673b1419101809239b9a5dd8c397953a

{"CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012"}
```

#### Sample Response
<a name="API_ListTagsForCertificate_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 07c10419-025e-11e6-baa2-cd9f4ef8cda6
Content-Type: application/x-amz-json-1.1
Content-Length: 87
Date: Thu, 14 Apr 2016 16:29:16 GMT

{
  "Tags": [{
    "Key": "stack",
    "Value": "production"
  },
  {
    "Key": "website",
    "Value": "example.com"
  }]
}
```

## See Also
<a name="API_ListTagsForCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/ListTagsForCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ListTagsForCertificate) 