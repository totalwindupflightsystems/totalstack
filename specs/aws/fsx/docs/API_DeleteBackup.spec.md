---
id: "@specs/aws/fsx/docs/API_DeleteBackup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteBackup"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteBackup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteBackup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteBackup
<a name="API_DeleteBackup"></a>

Deletes an Amazon FSx backup. After deletion, the backup no longer exists, and its data is gone.

The `DeleteBackup` call returns instantly. The backup won't show up in later `DescribeBackups` calls.

**Important**  
The data in a deleted backup is also deleted and can't be recovered by any means.

## Request Syntax
<a name="API_DeleteBackup_RequestSyntax"></a>

```
{
   "BackupId": "{{string}}",
   "ClientRequestToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteBackup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BackupId](#API_DeleteBackup_RequestSyntax) **   <a name="FSx-DeleteBackup-request-BackupId"></a>
The ID of the backup that you want to delete.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$`   
Required: Yes

 ** [ClientRequestToken](#API_DeleteBackup_RequestSyntax) **   <a name="FSx-DeleteBackup-request-ClientRequestToken"></a>
A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This parameter is automatically filled on your behalf when using the AWS CLI or SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

## Response Syntax
<a name="API_DeleteBackup_ResponseSyntax"></a>

```
{
   "BackupId": "string",
   "Lifecycle": "string"
}
```

## Response Elements
<a name="API_DeleteBackup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupId](#API_DeleteBackup_ResponseSyntax) **   <a name="FSx-DeleteBackup-response-BackupId"></a>
The ID of the backup that was deleted.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 128.  
Pattern: `^(backup-[0-9a-f]{8,})$` 

 ** [Lifecycle](#API_DeleteBackup_ResponseSyntax) **   <a name="FSx-DeleteBackup-response-Lifecycle"></a>
The lifecycle status of the backup. If the `DeleteBackup` operation is successful, the status is `DELETED`.  
Type: String  
Valid Values: `AVAILABLE | CREATING | TRANSFERRING | DELETED | FAILED | PENDING | COPYING` 

## Errors
<a name="API_DeleteBackup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BackupBeingCopied **   
You can't delete a backup while it's being copied.    
 ** BackupId **   
The ID of the source backup. Specifies the backup that you are copying.  
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** BackupInProgress **   
Another backup is already under way. Wait for completion before initiating additional backups of this file system.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** BackupNotFound **   
No Amazon FSx backups were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** BackupRestoring **   
You can't delete a backup while it's being used to restore a file system.    
 ** FileSystemId **   
The ID of a file system being restored from the backup.  
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

## See Also
<a name="API_DeleteBackup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteBackup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteBackup) 