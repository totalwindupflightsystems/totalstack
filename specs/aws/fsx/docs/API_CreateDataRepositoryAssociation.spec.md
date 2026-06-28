---
id: "@specs/aws/fsx/docs/API_CreateDataRepositoryAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDataRepositoryAssociation"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateDataRepositoryAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateDataRepositoryAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDataRepositoryAssociation
<a name="API_CreateDataRepositoryAssociation"></a>

Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and 2.15 file systems, excluding `scratch_1` deployment type.

Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see [Linking your file system to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html).

**Note**  
 `CreateDataRepositoryAssociation` isn't supported on Amazon File Cache resources. To create a DRA on Amazon File Cache, use the `CreateFileCache` operation.

## Request Syntax
<a name="API_CreateDataRepositoryAssociation_RequestSyntax"></a>

```
{
   "BatchImportMetaDataOnCreate": {{boolean}},
   "ClientRequestToken": "{{string}}",
   "DataRepositoryPath": "{{string}}",
   "FileSystemId": "{{string}}",
   "FileSystemPath": "{{string}}",
   "ImportedFileChunkSize": {{number}},
   "S3": { 
      "AutoExportPolicy": { 
         "Events": [ "{{string}}" ]
      },
      "AutoImportPolicy": { 
         "Events": [ "{{string}}" ]
      }
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDataRepositoryAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BatchImportMetaDataOnCreate](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-BatchImportMetaDataOnCreate"></a>
Set to `true` to run an import data repository task to import metadata from the data repository to the file system after the data repository association is created. Default is `false`.  
Type: Boolean  
Required: No

 ** [ClientRequestToken](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [DataRepositoryPath](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-DataRepositoryPath"></a>
The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional). This path specifies where in the S3 data repository files will be imported from or exported to.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: Yes

 ** [FileSystemId](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

 ** [FileSystemPath](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-FileSystemPath"></a>
A path on the file system that points to a high-level directory (such as `/ns1/`) or subdirectory (such as `/ns1/subdir/`) that will be mapped 1-1 with `DataRepositoryPath`. The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path `/ns1/`, then you cannot link another data repository with file system path `/ns1/ns2`.  
This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.  
If you specify only a forward slash (`/`) as the file system path, you can link only one data repository to the file system. You can only specify "/" as the file system path for the first data repository associated with a file system.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`   
Required: No

 ** [ImportedFileChunkSize](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-ImportedFileChunkSize"></a>
For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.  
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 512000.  
Required: No

 ** [S3](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-S3"></a>
The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.  
Type: [S3DataRepositoryConfiguration](API_S3DataRepositoryConfiguration.md) object  
Required: No

 ** [Tags](#API_CreateDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_CreateDataRepositoryAssociation_ResponseSyntax"></a>

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
<a name="API_CreateDataRepositoryAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Association](#API_CreateDataRepositoryAssociation_ResponseSyntax) **   <a name="FSx-CreateDataRepositoryAssociation-response-Association"></a>
The response object returned after the data repository association is created.  
Type: [DataRepositoryAssociation](API_DataRepositoryAssociation.md) object

## Errors
<a name="API_CreateDataRepositoryAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **   
No Amazon FSx file systems were found based upon supplied parameters.    
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

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataRepositoryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateDataRepositoryAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateDataRepositoryAssociation) 