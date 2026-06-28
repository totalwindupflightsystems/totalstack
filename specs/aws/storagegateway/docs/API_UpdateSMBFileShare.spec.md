---
id: "@specs/aws/storagegateway/docs/API_UpdateSMBFileShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSMBFileShare"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateSMBFileShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateSMBFileShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSMBFileShare
<a name="API_UpdateSMBFileShare"></a>

Updates a Server Message Block (SMB) file share. This operation is only supported for S3 File Gateways.

**Note**  
To leave a file share field unchanged, set the corresponding input field to null.

**Important**  
File gateways require AWS Security Token Service (AWS STS) to be activated to enable you to create a file share. Make sure that AWS STS is activated in the AWS Region you are creating your file gateway in. If AWS STS is not activated in this AWS Region, activate it. For information about how to activate AWS STS, see [Activating and deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the * AWS Identity and Access Management User Guide*.  
File gateways don't support creating hard or symbolic links on a file share.

## Request Syntax
<a name="API_UpdateSMBFileShare_RequestSyntax"></a>

```
{
   "AccessBasedEnumeration": {{boolean}},
   "AdminUserList": [ "{{string}}" ],
   "AuditDestinationARN": "{{string}}",
   "CacheAttributes": { 
      "CacheStaleTimeoutInSeconds": {{number}}
   },
   "CaseSensitivity": "{{string}}",
   "DefaultStorageClass": "{{string}}",
   "EncryptionType": "{{string}}",
   "FileShareARN": "{{string}}",
   "FileShareName": "{{string}}",
   "GuessMIMETypeEnabled": {{boolean}},
   "InvalidUserList": [ "{{string}}" ],
   "KMSEncrypted": {{boolean}},
   "KMSKey": "{{string}}",
   "NotificationPolicy": "{{string}}",
   "ObjectACL": "{{string}}",
   "OplocksEnabled": {{boolean}},
   "ReadOnly": {{boolean}},
   "RequesterPays": {{boolean}},
   "SMBACLEnabled": {{boolean}},
   "ValidUserList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateSMBFileShare_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessBasedEnumeration](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-AccessBasedEnumeration"></a>
The files and folders on this share will only be visible to users with read access.  
Type: Boolean  
Required: No

 ** [AdminUserList](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-AdminUserList"></a>
A list of users or groups in the Active Directory that have administrator rights to the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1`, `user1`, `@group1`, and `@DOMAIN\group1`. Can only be set if Authentication is set to `ActiveDirectory`.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** [AuditDestinationARN](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-AuditDestinationARN"></a>
The Amazon Resource Name (ARN) of the storage used for audit logs.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** [CacheAttributes](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-CacheAttributes"></a>
Specifies refresh cache information for the file share.  
Type: [CacheAttributes](API_CacheAttributes.md) object  
Required: No

 ** [CaseSensitivity](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-CaseSensitivity"></a>
The case of an object name in an Amazon S3 bucket. For `ClientSpecified`, the client determines the case sensitivity. For `CaseSensitive`, the gateway determines the case sensitivity. The default value is `ClientSpecified`.  
Type: String  
Valid Values: `ClientSpecified | CaseSensitive`   
Required: No

 ** [DefaultStorageClass](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-DefaultStorageClass"></a>
The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is `S3_STANDARD`. Optional.  
Valid Values: `S3_STANDARD` \| `S3_INTELLIGENT_TIERING` \| `S3_STANDARD_IA` \| `S3_ONEZONE_IA`   
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 50.  
Required: No

 ** [EncryptionType](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-EncryptionType"></a>
A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Type: String  
Valid Values: `SseS3 | SseKms | DsseKms`   
Required: No

 ** [FileShareARN](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-FileShareARN"></a>
The Amazon Resource Name (ARN) of the SMB file share that you want to update.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [FileShareName](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-FileShareName"></a>
The name of the file share. Optional.  
 `FileShareName` must be set if an S3 prefix name is set in `LocationARN`, or if an access point or access point alias is used.  
A valid SMB file share name cannot contain the following characters: `[`,`]`,`#`,`;`,`<`,`>`,`:`,`"`,`\`,`/`,`|`,`?`,`*`,`+`, or ASCII control characters `1-31`.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** [GuessMIMETypeEnabled](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-GuessMIMETypeEnabled"></a>
A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to `true` to enable MIME type guessing, otherwise set to `false`. The default value is `true`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [InvalidUserList](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-InvalidUserList"></a>
A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1`, `user1`, `@group1`, and `@DOMAIN\group1`. Can only be set if Authentication is set to `ActiveDirectory`.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** [KMSEncrypted](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-KMSEncrypted"></a>
 *This parameter has been deprecated.*   
Optional. Set to `true` to use Amazon S3 server-side encryption with your own AWS KMS key (SSE-KMS), or `false` to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the `EncryptionType` parameter instead.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [KMSKey](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-KMSKey"></a>
Optional. The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value must be set if `KMSEncrypted` is `true`, or if `EncryptionType` is `SseKms` or `DsseKms`.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** [NotificationPolicy](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-NotificationPolicy"></a>
The notification policy of the file share. `SettlingTimeInSeconds` controls the number of seconds to wait after the last point in time a client wrote to a file before generating an `ObjectUploaded` notification. Because clients can make many small writes to files, it's best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.  
 `SettlingTimeInSeconds` has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.  
This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.
The following example sets `NotificationPolicy` on with `SettlingTimeInSeconds` set to 60.  
 `{\"Upload\": {\"SettlingTimeInSeconds\": 60}}`   
The following example sets `NotificationPolicy` off.  
 `{}`   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `^\{[\w\s:\{\}\[\]"]*}$`   
Required: No

 ** [ObjectACL](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-ObjectACL"></a>
A value that sets the access control list (ACL) permission for objects in the S3 bucket that a S3 File Gateway puts objects into. The default value is `private`.  
Type: String  
Valid Values: `private | public-read | public-read-write | authenticated-read | bucket-owner-read | bucket-owner-full-control | aws-exec-read`   
Required: No

 ** [OplocksEnabled](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-OplocksEnabled"></a>
Specifies whether opportunistic locking is enabled for the SMB file share.  
Enabling opportunistic locking on case-sensitive shares is not recommended for workloads that involve access to files with the same name in different case.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [ReadOnly](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-ReadOnly"></a>
A value that sets the write status of a file share. Set this value to `true` to set write status to read-only, otherwise set to `false`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [RequesterPays](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-RequesterPays"></a>
A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to `true`, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.  
 `RequesterPays` is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [SMBACLEnabled](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-SMBACLEnabled"></a>
Set this value to `true` to enable access control list (ACL) on the SMB file share. Set it to `false` to map file and directory permissions to the POSIX permissions.  
For more information, see [Using Windows ACLs to limit SMB file share access](https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html) in the *Amazon S3 File Gateway User Guide*.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [ValidUserList](#API_UpdateSMBFileShare_RequestSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-request-ValidUserList"></a>
A list of users or groups in the Active Directory that are allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1`, `user1`, `@group1`, and `@DOMAIN\group1`. Can only be set if Authentication is set to `ActiveDirectory`.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

## Response Syntax
<a name="API_UpdateSMBFileShare_ResponseSyntax"></a>

```
{
   "FileShareARN": "string"
}
```

## Response Elements
<a name="API_UpdateSMBFileShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileShareARN](#API_UpdateSMBFileShare_ResponseSyntax) **   <a name="StorageGateway-UpdateSMBFileShare-response-FileShareARN"></a>
The Amazon Resource Name (ARN) of the updated SMB file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateSMBFileShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
An internal server error has occurred during the request. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more information about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

 ** InvalidGatewayRequestException **   
An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more detail about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

## Examples
<a name="API_UpdateSMBFileShare_Examples"></a>

### Update an SMB file share
<a name="API_UpdateSMBFileShare_Example_1"></a>

In the following request, you update an SMB file share using an existing file gateway and using your own AWS KMS key to perform server-side encryption of the contents of the file share.

#### Sample Request
<a name="API_UpdateSMBFileShare_Example_1_Request"></a>

```
{
    "CacheAttributes": { 
      "CacheStaleTimeoutInSeconds": 600
    },
    "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY",
    "FileShareName": "my-file-share",
    "GuessMIMETypeEnabled": "true",
    "InvalidList": [
        "user2",
        "user3",
        "@group1"
    ],
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "ObjectACL": "bucket-owner-full-control",
    "ReadOnly": "false",
    "RequesterPays": "false",
    "ValidList": [
        "user1",
        "user4",
        "@group2"
    ]
}
```

#### Sample Response
<a name="API_UpdateSMBFileShare_Example_1_Response"></a>

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY"
}
```

### Update an SMB file share with file upload notification turned on
<a name="API_UpdateSMBFileShare_Example_2"></a>

In the following request, you update an SMB file share with file upload notification turned on and settling time set to 60 seconds.

#### Sample Request
<a name="API_UpdateSMBFileShare_Example_2_Request"></a>

```
{
    "CacheAttributes": { 
      "CacheStaleTimeoutInSeconds": 600
    },
    "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY",
    "FileShareName": "my-file-share",
    "GuessMIMETypeEnabled": "true",
    "InvalidList": [
        "user2",
        "user3",
        "@group1"
    ],
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "NotificationPolicy": "{\"Upload\": {\"SettlingTimeInSeconds\": 60}}",
    "ObjectACL": "bucket-owner-full-control",
    "ReadOnly": "false",
    "RequesterPays": "false",
    "ValidList": [
        "user1",
        "user4",
        "@group2"
    ]
}
```

#### Sample Response
<a name="API_UpdateSMBFileShare_Example_2_Response"></a>

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY"
}
```

### Update an SMB file share with file upload notification turned off
<a name="API_UpdateSMBFileShare_Example_3"></a>

In the following request, you update an SMB file share with file upload notification turned off.

#### Sample Request
<a name="API_UpdateSMBFileShare_Example_3_Request"></a>

```
{
    "CacheAttributes": { 
      "CacheStaleTimeoutInSeconds": 600
    },
    "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY",
    "FileShareName": "my-file-share",
    "GuessMIMETypeEnabled": "true",
    "InvalidList": [
        "user2",
        "user3",
        "@group1"
    ],
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "NotificationPolicy": "{}",
    "ObjectACL": "bucket-owner-full-control",
    "ReadOnly": "false",
    "RequesterPays": "false",
    "ValidList": [
        "user1",
        "user4",
        "@group2"
    ]
}
```

## See Also
<a name="API_UpdateSMBFileShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateSMBFileShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateSMBFileShare) 