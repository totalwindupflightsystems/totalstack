---
id: "@specs/aws/fsx/docs/API_DescribeS3AccessPointAttachments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeS3AccessPointAttachments"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeS3AccessPointAttachments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeS3AccessPointAttachments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeS3AccessPointAttachments
<a name="API_DescribeS3AccessPointAttachments"></a>

Describes one or more S3 access points attached to Amazon FSx volumes.

The requester requires the following permission to perform this action:
+  `fsx:DescribeS3AccessPointAttachments` 

## Request Syntax
<a name="API_DescribeS3AccessPointAttachments_RequestSyntax"></a>

```
{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "Names": [ "{{string}}" ],
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeS3AccessPointAttachments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeS3AccessPointAttachments_RequestSyntax) **   <a name="FSx-DescribeS3AccessPointAttachments-request-Filters"></a>
Enter a filter Name and Values pair to view a select set of S3 access point attachments.  
Type: Array of [S3AccessPointAttachmentsFilter](API_S3AccessPointAttachmentsFilter.md) objects  
Array Members: Maximum number of 2 items.  
Required: No

 ** [MaxResults](#API_DescribeS3AccessPointAttachments_RequestSyntax) **   <a name="FSx-DescribeS3AccessPointAttachments-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [Names](#API_DescribeS3AccessPointAttachments_RequestSyntax) **   <a name="FSx-DescribeS3AccessPointAttachments-request-Names"></a>
The names of the S3 access point attachments whose descriptions you want to retrieve.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Pattern: `^(?=[a-z0-9])[a-z0-9-]{1,48}[a-z0-9]$`   
Required: No

 ** [NextToken](#API_DescribeS3AccessPointAttachments_RequestSyntax) **   <a name="FSx-DescribeS3AccessPointAttachments-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

## Response Syntax
<a name="API_DescribeS3AccessPointAttachments_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "S3AccessPointAttachments": [ 
      { 
         "CreationTime": number,
         "Lifecycle": "string",
         "LifecycleTransitionReason": { 
            "Message": "string"
         },
         "Name": "string",
         "OntapConfiguration": { 
            "FileSystemIdentity": { 
               "Type": "string",
               "UnixUser": { 
                  "Name": "string"
               },
               "WindowsUser": { 
                  "Name": "string"
               }
            },
            "VolumeId": "string"
         },
         "OpenZFSConfiguration": { 
            "FileSystemIdentity": { 
               "PosixUser": { 
                  "Gid": number,
                  "SecondaryGids": [ number ],
                  "Uid": number
               },
               "Type": "string"
            },
            "VolumeId": "string"
         },
         "S3AccessPoint": { 
            "Alias": "string",
            "ResourceARN": "string",
            "VpcConfiguration": { 
               "VpcId": "string"
            }
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeS3AccessPointAttachments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeS3AccessPointAttachments_ResponseSyntax) **   <a name="FSx-DescribeS3AccessPointAttachments-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

 ** [S3AccessPointAttachments](#API_DescribeS3AccessPointAttachments_ResponseSyntax) **   <a name="FSx-DescribeS3AccessPointAttachments-response-S3AccessPointAttachments"></a>
Array of S3 access point attachments returned after a successful `DescribeS3AccessPointAttachments` operation.  
Type: Array of [S3AccessPointAttachment](API_S3AccessPointAttachment.md) objects  
Array Members: Maximum number of 1000 items.

## Errors
<a name="API_DescribeS3AccessPointAttachments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** S3AccessPointAttachmentNotFound **   
The access point specified was not found.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeS3AccessPointAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeS3AccessPointAttachments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeS3AccessPointAttachments) 