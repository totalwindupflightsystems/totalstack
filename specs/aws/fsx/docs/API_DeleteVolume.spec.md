---
id: "@specs/aws/fsx/docs/API_DeleteVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteVolume"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteVolume
<a name="API_DeleteVolume"></a>

Deletes an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.

## Request Syntax
<a name="API_DeleteVolume_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "OntapConfiguration": { 
      "BypassSnaplockEnterpriseRetention": {{boolean}},
      "FinalBackupTags": [ 
         { 
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "SkipFinalBackup": {{boolean}}
   },
   "OpenZFSConfiguration": { 
      "Options": [ "{{string}}" ]
   },
   "VolumeId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DeleteVolume_RequestSyntax) **   <a name="FSx-DeleteVolume-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [OntapConfiguration](#API_DeleteVolume_RequestSyntax) **   <a name="FSx-DeleteVolume-request-OntapConfiguration"></a>
For Amazon FSx for ONTAP volumes, specify whether to take a final backup of the volume and apply tags to the backup. To apply tags to the backup, you must have the `fsx:TagResource` permission.  
Type: [DeleteVolumeOntapConfiguration](API_DeleteVolumeOntapConfiguration.md) object  
Required: No

 ** [OpenZFSConfiguration](#API_DeleteVolume_RequestSyntax) **   <a name="FSx-DeleteVolume-request-OpenZFSConfiguration"></a>
For Amazon FSx for OpenZFS volumes, specify whether to delete all child volumes and snapshots.  
Type: [DeleteVolumeOpenZFSConfiguration](API_DeleteVolumeOpenZFSConfiguration.md) object  
Required: No

 ** [VolumeId](#API_DeleteVolume_RequestSyntax) **   <a name="FSx-DeleteVolume-request-VolumeId"></a>
The ID of the volume that you are deleting.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: Yes

## Response Syntax
<a name="API_DeleteVolume_ResponseSyntax"></a>

```
{
   "Lifecycle": "string",
   "OntapResponse": { 
      "FinalBackupId": "string",
      "FinalBackupTags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   },
   "VolumeId": "string"
}
```

## Response Elements
<a name="API_DeleteVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Lifecycle](#API_DeleteVolume_ResponseSyntax) **   <a name="FSx-DeleteVolume-response-Lifecycle"></a>
The lifecycle state of the volume being deleted. If the `DeleteVolume` operation is successful, this value is `DELETING`.  
Type: String  
Valid Values: `CREATING | CREATED | DELETING | FAILED | MISCONFIGURED | PENDING | AVAILABLE` 

 ** [OntapResponse](#API_DeleteVolume_ResponseSyntax) **   <a name="FSx-DeleteVolume-response-OntapResponse"></a>
Returned after a `DeleteVolume` request, showing the status of the delete request.  
Type: [DeleteVolumeOntapResponse](API_DeleteVolumeOntapResponse.md) object

 ** [VolumeId](#API_DeleteVolume_ResponseSyntax) **   <a name="FSx-DeleteVolume-response-VolumeId"></a>
The ID of the volume that's being deleted.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$` 

## Errors
<a name="API_DeleteVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** VolumeNotFound **   
No Amazon FSx volumes were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DeleteVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteVolume) 