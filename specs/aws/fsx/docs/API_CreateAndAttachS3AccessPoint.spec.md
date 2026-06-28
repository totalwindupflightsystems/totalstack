---
id: "@specs/aws/fsx/docs/API_CreateAndAttachS3AccessPoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAndAttachS3AccessPoint"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateAndAttachS3AccessPoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateAndAttachS3AccessPoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAndAttachS3AccessPoint
<a name="API_CreateAndAttachS3AccessPoint"></a>

Creates an S3 access point and attaches it to an Amazon FSx volume. For FSx for OpenZFS file systems, the volume must be hosted on a high-availability file system, either Single-AZ or Multi-AZ. For more information, see [Accessing your data using Amazon S3 access points](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/s3accesspoints-for-FSx.html) in the Amazon FSx for OpenZFS User Guide. For FSx for ONTAP file systems, see [Accessing data using Amazon S3 access points](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/s3-access-points.html) in the Amazon FSx for NetApp ONTAP User Guide. 

The requester requires the following permissions to perform these actions:
+  `fsx:CreateAndAttachS3AccessPoint` 
+  `s3:CreateAccessPoint` 
+  `s3:GetAccessPoint` 
+  `s3:PutAccessPointPolicy` 
+  `s3:DeleteAccessPoint` 

The following actions are related to `CreateAndAttachS3AccessPoint`:
+  [DescribeS3AccessPointAttachments](API_DescribeS3AccessPointAttachments.md) 
+  [DetachAndDeleteS3AccessPoint](API_DetachAndDeleteS3AccessPoint.md) 

## Request Syntax
<a name="API_CreateAndAttachS3AccessPoint_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Name": "{{string}}",
   "OntapConfiguration": { 
      "FileSystemIdentity": { 
         "Type": "{{string}}",
         "UnixUser": { 
            "Name": "{{string}}"
         },
         "WindowsUser": { 
            "Name": "{{string}}"
         }
      },
      "VolumeId": "{{string}}"
   },
   "OpenZFSConfiguration": { 
      "FileSystemIdentity": { 
         "PosixUser": { 
            "Gid": {{number}},
            "SecondaryGids": [ {{number}} ],
            "Uid": {{number}}
         },
         "Type": "{{string}}"
      },
      "VolumeId": "{{string}}"
   },
   "S3AccessPoint": { 
      "Policy": "{{string}}",
      "VpcConfiguration": { 
         "VpcId": "{{string}}"
      }
   },
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateAndAttachS3AccessPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateAndAttachS3AccessPoint_RequestSyntax) **   <a name="FSx-CreateAndAttachS3AccessPoint-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [Name](#API_CreateAndAttachS3AccessPoint_RequestSyntax) **   <a name="FSx-CreateAndAttachS3AccessPoint-request-Name"></a>
The name you want to assign to this S3 access point.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Pattern: `^(?=[a-z0-9])[a-z0-9-]{1,48}[a-z0-9]$`   
Required: Yes

 ** [OntapConfiguration](#API_CreateAndAttachS3AccessPoint_RequestSyntax) **   <a name="FSx-CreateAndAttachS3AccessPoint-request-OntapConfiguration"></a>
Specifies the FSx for ONTAP volume that the S3 access point will be attached to, and the file system user identity.  
Type: [CreateAndAttachS3AccessPointOntapConfiguration](API_CreateAndAttachS3AccessPointOntapConfiguration.md) object  
Required: No

 ** [OpenZFSConfiguration](#API_CreateAndAttachS3AccessPoint_RequestSyntax) **   <a name="FSx-CreateAndAttachS3AccessPoint-request-OpenZFSConfiguration"></a>
Specifies the configuration to use when creating and attaching an S3 access point to an FSx for OpenZFS volume.  
Type: [CreateAndAttachS3AccessPointOpenZFSConfiguration](API_CreateAndAttachS3AccessPointOpenZFSConfiguration.md) object  
Required: No

 ** [S3AccessPoint](#API_CreateAndAttachS3AccessPoint_RequestSyntax) **   <a name="FSx-CreateAndAttachS3AccessPoint-request-S3AccessPoint"></a>
Specifies the virtual private cloud (VPC) configuration if you're creating an access point that is restricted to a VPC. For more information, see [Creating access points restricted to a virtual private cloud](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/access-points-vpc.html).  
Type: [CreateAndAttachS3AccessPointS3Configuration](API_CreateAndAttachS3AccessPointS3Configuration.md) object  
Required: No

 ** [Type](#API_CreateAndAttachS3AccessPoint_RequestSyntax) **   <a name="FSx-CreateAndAttachS3AccessPoint-request-Type"></a>
The type of S3 access point you want to create. Valid values are `OPENZFS` and `ONTAP`.  
Type: String  
Valid Values: `OPENZFS | ONTAP`   
Required: Yes

## Response Syntax
<a name="API_CreateAndAttachS3AccessPoint_ResponseSyntax"></a>

```
{
   "S3AccessPointAttachment": { 
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
}
```

## Response Elements
<a name="API_CreateAndAttachS3AccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [S3AccessPointAttachment](#API_CreateAndAttachS3AccessPoint_ResponseSyntax) **   <a name="FSx-CreateAndAttachS3AccessPoint-response-S3AccessPointAttachment"></a>
Describes the configuration of the S3 access point created.  
Type: [S3AccessPointAttachment](API_S3AccessPointAttachment.md) object

## Errors
<a name="API_CreateAndAttachS3AccessPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessPointAlreadyOwnedByYou **   
An access point with that name already exists in the AWS Region in your AWS account.    
 ** ErrorCode **   
An error code indicating that an access point with that name already exists in the AWS Region in your AWS account.  
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** InvalidAccessPoint **   
The access point specified doesn't exist.    
 ** ErrorCode **   
An error code indicating that the access point specified doesn't exist.  
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InvalidRequest **   
The action or operation requested is invalid. Verify that the action is typed correctly.    
 ** ErrorCode **   
An error code indicating that the action or operation requested is invalid.  
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** TooManyAccessPoints **   
You have reached the maximum number of S3 access points attachments allowed for your account in this AWS Region, or for the file system. For more information, or to request an increase, see [Service quotas on FSx resources](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/limits.html) in the FSx for OpenZFS User Guide.    
 ** ErrorCode **   
An error code indicating that you have reached the maximum number of S3 access points attachments allowed for your account in this AWS Region, or for the file system.  
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** VolumeNotFound **   
No Amazon FSx volumes were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateAndAttachS3AccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateAndAttachS3AccessPoint) 