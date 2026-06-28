---
id: "@specs/aws/fsx/docs/API_UpdateDataRepositoryAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDataRepositoryAssociation"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateDataRepositoryAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateDataRepositoryAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDataRepositoryAssociation
<a name="API_UpdateDataRepositoryAssociation"></a>

Updates the configuration of an existing data repository association on an Amazon FSx for Lustre file system. Data repository associations are supported on all FSx for Lustre 2.12 and 2.15 file systems, excluding `scratch_1` deployment type.

## Request Syntax
<a name="API_UpdateDataRepositoryAssociation_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "ImportedFileChunkSize": {{number}},
   "S3": { 
      "AutoExportPolicy": { 
         "Events": [ "{{string}}" ]
      },
      "AutoImportPolicy": { 
         "Events": [ "{{string}}" ]
      }
   }
}
```

## Request Parameters
<a name="API_UpdateDataRepositoryAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_UpdateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-UpdateDataRepositoryAssociation-request-AssociationId"></a>
The ID of the data repository association that you are updating.  
Type: String  
Length Constraints: Minimum length of 13. Maximum length of 23.  
Pattern: `^(dra-[0-9a-f]{8,})$`   
Required: Yes

 ** [ClientRequestToken](#API_UpdateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-UpdateDataRepositoryAssociation-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [ImportedFileChunkSize](#API_UpdateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-UpdateDataRepositoryAssociation-request-ImportedFileChunkSize"></a>
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.  
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 512000.  
Required: No

 ** [S3](#API_UpdateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-UpdateDataRepositoryAssociation-request-S3"></a>
The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.  
Type: [S3DataRepositoryConfiguration](API_S3DataRepositoryConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_UpdateDataRepositoryAssociation_ResponseSyntax"></a>

```
{
   "Association": { 
      "AssociationId": "string",
      "BatchImportMetaDataOnCreate": boolean,
      "CreationTime": number,
      "DataRepositoryPath": "string",
      "DataRepositorySubdirectories": [ "string" ],
      "FailureDetails": { 
         "Message": "string"
      },
      "FileCacheId": "string",
      "FileCachePath": "string",
      "FileSystemId": "string",
      "FileSystemPath": "string",
      "ImportedFileChunkSize": number,
      "Lifecycle": "string",
      "NFS": { 
         "AutoExportPolicy": { 
            "Events": [ "string" ]
         },
         "DnsIps": [ "string" ],
         "Version": "string"
      },
      "ResourceARN": "string",
      "S3": { 
         "AutoExportPolicy": { 
            "Events": [ "string" ]
         },
         "AutoImportPolicy": { 
            "Events": [ "string" ]
         }
      },
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateDataRepositoryAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Association](#API_UpdateDataRepositoryAssociation_ResponseSyntax) **   <a name="FSx-UpdateDataRepositoryAssociation-response-Association"></a>
The response object returned after the data repository association is updated.  
Type: [DataRepositoryAssociation](API_DataRepositoryAssociation.md) object

## Errors
<a name="API_UpdateDataRepositoryAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** DataRepositoryAssociationNotFound **   
No data repository associations were found based upon the supplied parameters.    
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

## See Also
<a name="API_UpdateDataRepositoryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateDataRepositoryAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateDataRepositoryAssociation) 