---
id: "@specs/aws/globalaccelerator/docs/API_DescribeCrossAccountAttachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCrossAccountAttachment"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DescribeCrossAccountAttachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DescribeCrossAccountAttachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCrossAccountAttachment
<a name="API_DescribeCrossAccountAttachment"></a>

Gets configuration information about a cross-account attachment.

## Request Syntax
<a name="API_DescribeCrossAccountAttachment_RequestSyntax"></a>

```
{
   "AttachmentArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCrossAccountAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttachmentArn](#API_DescribeCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-DescribeCrossAccountAttachment-request-AttachmentArn"></a>
The Amazon Resource Name (ARN) for the cross-account attachment to describe.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DescribeCrossAccountAttachment_ResponseSyntax"></a>

```
{
   "CrossAccountAttachment": { 
      "AttachmentArn": "string",
      "CreatedTime": number,
      "LastModifiedTime": number,
      "Name": "string",
      "Principals": [ "string" ],
      "Resources": [ 
         { 
            "Cidr": "string",
            "EndpointId": "string",
            "Region": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeCrossAccountAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CrossAccountAttachment](#API_DescribeCrossAccountAttachment_ResponseSyntax) **   <a name="globalaccelerator-DescribeCrossAccountAttachment-response-CrossAccountAttachment"></a>
Information about the cross-account attachment.  
Type: [Attachment](API_Attachment.md) object

## Errors
<a name="API_DescribeCrossAccountAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** AttachmentNotFoundException **   
No cross-account attachment was found.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeCrossAccountAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DescribeCrossAccountAttachment) 