---
id: "@specs/aws/globalaccelerator/docs/API_CreateCrossAccountAttachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCrossAccountAttachment"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CreateCrossAccountAttachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CreateCrossAccountAttachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCrossAccountAttachment
<a name="API_CreateCrossAccountAttachment"></a>

Create a cross-account attachment in AWS Global Accelerator. You create a cross-account attachment to specify the *principals* who have permission to work with *resources* in accelerators in their own account. You specify, in the same attachment, the resources that are shared.

A principal can be an AWS account number or the Amazon Resource Name (ARN) for an accelerator. For account numbers that are listed as principals, to work with a resource listed in the attachment, you must sign in to an account specified as a principal. Then, you can work with resources that are listed, with any of your accelerators. If an accelerator ARN is listed in the cross-account attachment as a principal, anyone with permission to make updates to the accelerator can work with resources that are listed in the attachment. 

Specify each principal and resource separately. To specify two CIDR address pools, list them individually under `Resources`, and so on. For a command line operation, for example, you might use a statement like the following:

 ` "Resources": [{"Cidr": "169.254.60.0/24"},{"Cidr": "169.254.59.0/24"}]` 

For more information, see [ Working with cross-account attachments and resources in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_CreateCrossAccountAttachment_RequestSyntax"></a>

```
{
   "IdempotencyToken": "{{string}}",
   "Name": "{{string}}",
   "Principals": [ "{{string}}" ],
   "Resources": [ 
      { 
         "Cidr": "{{string}}",
         "EndpointId": "{{string}}",
         "Region": "{{string}}"
      }
   ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCrossAccountAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdempotencyToken](#API_CreateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-CreateCrossAccountAttachment-request-IdempotencyToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [Name](#API_CreateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-CreateCrossAccountAttachment-request-Name"></a>
The name of the cross-account attachment.   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `[\S\s]+`   
Required: Yes

 ** [Principals](#API_CreateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-CreateCrossAccountAttachment-request-Principals"></a>
The principals to include in the cross-account attachment. A principal can be an AWS account number or the Amazon Resource Name (ARN) for an accelerator.   
Type: Array of strings  
Length Constraints: Maximum length of 256.  
Pattern: `(^\d{12}$|arn:.*)`   
Required: No

 ** [Resources](#API_CreateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-CreateCrossAccountAttachment-request-Resources"></a>
The Amazon Resource Names (ARNs) for the resources to include in the cross-account attachment. A resource can be any supported AWS resource type for Global Accelerator or a CIDR range for a bring your own IP address (BYOIP) address pool.   
Type: Array of [Resource](API_Resource.md) objects  
Required: No

 ** [Tags](#API_CreateCrossAccountAttachment_RequestSyntax) **   <a name="globalaccelerator-CreateCrossAccountAttachment-request-Tags"></a>
Add tags for a cross-account attachment.  
For more information, see [Tagging in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreateCrossAccountAttachment_ResponseSyntax"></a>

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
<a name="API_CreateCrossAccountAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CrossAccountAttachment](#API_CreateCrossAccountAttachment_ResponseSyntax) **   <a name="globalaccelerator-CreateCrossAccountAttachment-response-CrossAccountAttachment"></a>
Information about the cross-account attachment.  
Type: [Attachment](API_Attachment.md) object

## Errors
<a name="API_CreateCrossAccountAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
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
<a name="API_CreateCrossAccountAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CreateCrossAccountAttachment) 