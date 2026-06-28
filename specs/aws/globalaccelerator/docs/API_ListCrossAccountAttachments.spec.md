---
id: "@specs/aws/globalaccelerator/docs/API_ListCrossAccountAttachments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCrossAccountAttachments"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListCrossAccountAttachments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListCrossAccountAttachments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCrossAccountAttachments
<a name="API_ListCrossAccountAttachments"></a>

List the cross-account attachments that have been created in AWS Global Accelerator.

## Request Syntax
<a name="API_ListCrossAccountAttachments_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCrossAccountAttachments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListCrossAccountAttachments_RequestSyntax) **   <a name="globalaccelerator-ListCrossAccountAttachments-request-MaxResults"></a>
The number of cross-account attachment objects that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListCrossAccountAttachments_RequestSyntax) **   <a name="globalaccelerator-ListCrossAccountAttachments-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListCrossAccountAttachments_ResponseSyntax"></a>

```
{
   "CrossAccountAttachments": [ 
      { 
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCrossAccountAttachments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CrossAccountAttachments](#API_ListCrossAccountAttachments_ResponseSyntax) **   <a name="globalaccelerator-ListCrossAccountAttachments-response-CrossAccountAttachments"></a>
Information about the cross-account attachments.  
Type: Array of [Attachment](API_Attachment.md) objects

 ** [NextToken](#API_ListCrossAccountAttachments_ResponseSyntax) **   <a name="globalaccelerator-ListCrossAccountAttachments-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListCrossAccountAttachments_Errors"></a>

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

 ** InvalidNextTokenException **   
There isn't another item to return.  
HTTP Status Code: 400

## See Also
<a name="API_ListCrossAccountAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListCrossAccountAttachments) 