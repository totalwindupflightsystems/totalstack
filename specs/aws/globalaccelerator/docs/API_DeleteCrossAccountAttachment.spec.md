---
id: "@specs/aws/globalaccelerator/docs/API_DeleteCrossAccountAttachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCrossAccountAttachment"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DeleteCrossAccountAttachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DeleteCrossAccountAttachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCrossAccountAttachment
<a name="API_DeleteCrossAccountAttachment"></a>

Delete a cross-account attachment. When you delete an attachment, AWS Global Accelerator revokes the permission to use the resources in the attachment from all principals in the list of principals. AWS Global Accelerator revokes the permission for specific resources.

For more information, see [ Working with cross-account attachments and resources in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_DeleteCrossAccountAttachment_RequestSyntax"></a>

```
{
   "AttachmentArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCrossAccountAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttachmentArn](#API_DeleteCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-DeleteCrossAccountAttachment-request-AttachmentArn"></a>
The Amazon Resource Name (ARN) for the cross-account attachment to delete.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Elements
<a name="API_DeleteCrossAccountAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCrossAccountAttachment_Errors"></a>

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

 ** TransactionInProgressException **   
There's already a transaction in progress. Another transaction can't be processed.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteCrossAccountAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DeleteCrossAccountAttachment) 