---
id: "@specs/aws/globalaccelerator/docs/API_UpdateCrossAccountAttachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCrossAccountAttachment"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# UpdateCrossAccountAttachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_UpdateCrossAccountAttachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCrossAccountAttachment
<a name="API_UpdateCrossAccountAttachment"></a>

Update a cross-account attachment to add or remove principals or resources. When you update an attachment to remove a principal (account ID or accelerator) or a resource, AWS Global Accelerator revokes the permission for specific resources. 

For more information, see [ Working with cross-account attachments and resources in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_UpdateCrossAccountAttachment_RequestSyntax"></a>

```
{
   "AddPrincipals": [ "{{string}}" ],
   "AddResources": [ 
      { 
         "Cidr": "{{string}}",
         "EndpointId": "{{string}}",
         "Region": "{{string}}"
      }
   ],
   "AttachmentArn": "{{string}}",
   "Name": "{{string}}",
   "RemovePrincipals": [ "{{string}}" ],
   "RemoveResources": [ 
      { 
         "Cidr": "{{string}}",
         "EndpointId": "{{string}}",
         "Region": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateCrossAccountAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AddPrincipals](#API_UpdateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-UpdateCrossAccountAttachment-request-AddPrincipals"></a>
The principals to add to the cross-account attachment. A principal is an account or the Amazon Resource Name (ARN) of an accelerator that the attachment gives permission to work with resources from another account. The resources are also listed in the attachment.  
To add more than one principal, separate the account numbers or accelerator ARNs, or both, with commas.  
Type: Array of strings  
Length Constraints: Maximum length of 256.  
Pattern: `(^\d{12}$|arn:.*)`   
Required: No

 ** [AddResources](#API_UpdateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-UpdateCrossAccountAttachment-request-AddResources"></a>
The resources to add to the cross-account attachment. A resource listed in a cross-account attachment can be used with an accelerator by the principals that are listed in the attachment.  
To add more than one resource, separate the resource ARNs with commas.  
Type: Array of [Resource](API_Resource.md) objects  
Required: No

 ** [AttachmentArn](#API_UpdateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-UpdateCrossAccountAttachment-request-AttachmentArn"></a>
The Amazon Resource Name (ARN) of the cross-account attachment to update.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [Name](#API_UpdateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-UpdateCrossAccountAttachment-request-Name"></a>
The name of the cross-account attachment.   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `[\S\s]+`   
Required: No

 ** [RemovePrincipals](#API_UpdateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-UpdateCrossAccountAttachment-request-RemovePrincipals"></a>
The principals to remove from the cross-account attachment. A principal is an account or the Amazon Resource Name (ARN) of an accelerator that the attachment gives permission to work with resources from another account. The resources are also listed in the attachment.  
To remove more than one principal, separate the account numbers or accelerator ARNs, or both, with commas.  
Type: Array of strings  
Length Constraints: Maximum length of 256.  
Pattern: `(^\d{12}$|arn:.*)`   
Required: No

 ** [RemoveResources](#API_UpdateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-UpdateCrossAccountAttachment-request-RemoveResources"></a>
The resources to remove from the cross-account attachment. A resource listed in a cross-account attachment can be used with an accelerator by the principals that are listed in the attachment.  
To remove more than one resource, separate the resource ARNs with commas.  
Type: Array of [Resource](API_Resource.md) objects  
Required: No

## Response Syntax
<a name="API_UpdateCrossAccountAttachment_ResponseSyntax"></a>

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
<a name="API_UpdateCrossAccountAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CrossAccountAttachment](#API_UpdateCrossAccountAttachment_ResponseSyntax) **   <a name="globalaccelerator-UpdateCrossAccountAttachment-response-CrossAccountAttachment"></a>
Information about the updated cross-account attachment.  
Type: [Attachment](API_Attachment.md) object

## Errors
<a name="API_UpdateCrossAccountAttachment_Errors"></a>

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

 ** LimitExceededException **   
Processing your request would cause you to exceed an AWS Global Accelerator limit.  
HTTP Status Code: 400

 ** TransactionInProgressException **   
There's already a transaction in progress. Another transaction can't be processed.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateCrossAccountAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/UpdateCrossAccountAttachment) 