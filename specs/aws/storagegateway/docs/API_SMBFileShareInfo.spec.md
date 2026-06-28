---
id: "@specs/aws/storagegateway/docs/API_SMBFileShareInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SMBFileShareInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# SMBFileShareInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_SMBFileShareInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SMBFileShareInfo
<a name="API_SMBFileShareInfo"></a>

The Windows file permissions and ownership information assigned, by default, to native S3 objects when S3 File Gateway discovers them in S3 buckets. This operation is only supported for S3 File Gateways.

## Contents
<a name="API_SMBFileShareInfo_Contents"></a>

 ** AccessBasedEnumeration **   <a name="StorageGateway-Type-SMBFileShareInfo-AccessBasedEnumeration"></a>
Indicates whether `AccessBasedEnumeration` is enabled.  
Type: Boolean  
Required: No

 ** AdminUserList **   <a name="StorageGateway-Type-SMBFileShareInfo-AdminUserList"></a>
A list of users or groups in the Active Directory that have administrator rights to the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1`, `user1`, `@group1`, and `@DOMAIN\group1`. Can only be set if Authentication is set to `ActiveDirectory`.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** AuditDestinationARN **   <a name="StorageGateway-Type-SMBFileShareInfo-AuditDestinationARN"></a>
The Amazon Resource Name (ARN) of the storage used for audit logs.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** Authentication **   <a name="StorageGateway-Type-SMBFileShareInfo-Authentication"></a>
The authentication method of the file share. The default is `ActiveDirectory`.  
Valid Values: `ActiveDirectory` \| `GuestAccess`   
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 15.  
Required: No

 ** BucketRegion **   <a name="StorageGateway-Type-SMBFileShareInfo-BucketRegion"></a>
Specifies the Region of the S3 bucket where the SMB file share stores files.  
This parameter is required for SMB file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: No

 ** CacheAttributes **   <a name="StorageGateway-Type-SMBFileShareInfo-CacheAttributes"></a>
Refresh cache information for the file share.  
Type: [CacheAttributes](API_CacheAttributes.md) object  
Required: No

 ** CaseSensitivity **   <a name="StorageGateway-Type-SMBFileShareInfo-CaseSensitivity"></a>
The case of an object name in an Amazon S3 bucket. For `ClientSpecified`, the client determines the case sensitivity. For `CaseSensitive`, the gateway determines the case sensitivity. The default value is `ClientSpecified`.  
Type: String  
Valid Values: `ClientSpecified | CaseSensitive`   
Required: No

 ** DefaultStorageClass **   <a name="StorageGateway-Type-SMBFileShareInfo-DefaultStorageClass"></a>
The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is `S3_STANDARD`. Optional.  
Valid Values: `S3_STANDARD` \| `S3_INTELLIGENT_TIERING` \| `S3_STANDARD_IA` \| `S3_ONEZONE_IA`   
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 50.  
Required: No

 ** EncryptionType **   <a name="StorageGateway-Type-SMBFileShareInfo-EncryptionType"></a>
A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Type: String  
Valid Values: `SseS3 | SseKms | DsseKms`   
Required: No

 ** FileShareARN **   <a name="StorageGateway-Type-SMBFileShareInfo-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** FileShareId **   <a name="StorageGateway-Type-SMBFileShareInfo-FileShareId"></a>
The ID of the file share.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.  
Required: No

 ** FileShareName **   <a name="StorageGateway-Type-SMBFileShareInfo-FileShareName"></a>
The name of the file share. Optional.  
 `FileShareName` must be set if an S3 prefix name is set in `LocationARN`, or if an access point or access point alias is used.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** FileShareStatus **   <a name="StorageGateway-Type-SMBFileShareInfo-FileShareStatus"></a>
The status of the file share.  
Valid Values: `CREATING` \| `UPDATING` \| `AVAILABLE` \| `DELETING`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-SMBFileShareInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** GuessMIMETypeEnabled **   <a name="StorageGateway-Type-SMBFileShareInfo-GuessMIMETypeEnabled"></a>
A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to `true` to enable MIME type guessing, otherwise set to `false`. The default value is `true`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** InvalidUserList **   <a name="StorageGateway-Type-SMBFileShareInfo-InvalidUserList"></a>
A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1`, `user1`, `@group1`, and `@DOMAIN\group1`. Can only be set if Authentication is set to `ActiveDirectory`.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** KMSEncrypted **   <a name="StorageGateway-Type-SMBFileShareInfo-KMSEncrypted"></a>
 *This member has been deprecated.*   
Optional. Set to `true` to use Amazon S3 server-side encryption with your own AWS KMS key (SSE-KMS), or `false` to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the `EncryptionType` parameter instead.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** KMSKey **   <a name="StorageGateway-Type-SMBFileShareInfo-KMSKey"></a>
Optional. The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value must be set if `KMSEncrypted` is `true`, or if `EncryptionType` is `SseKms` or `DsseKms`.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** LocationARN **   <a name="StorageGateway-Type-SMBFileShareInfo-LocationARN"></a>
A custom ARN for the backend storage used for storing data for file shares. It includes a resource ARN with an optional prefix concatenation. The prefix must end with a forward slash (/).  
You can specify LocationARN as a bucket ARN, access point ARN or access point alias, as shown in the following examples.  
Bucket ARN:  
 `arn:aws:s3:::amzn-s3-demo-bucket/prefix/`   
Access point ARN:  
 `arn:aws:s3:region:account-id:accesspoint/access-point-name/prefix/`   
If you specify an access point, the bucket policy must be configured to delegate access control to the access point. For information, see [Delegating access control to access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html#access-points-delegating-control) in the *Amazon S3 User Guide*.  
Access point alias:  
 `test-ap-ab123cdef4gehijklmn5opqrstuvuse1a-s3alias` 
Type: String  
Length Constraints: Minimum length of 16. Maximum length of 1400.  
Required: No

 ** NotificationPolicy **   <a name="StorageGateway-Type-SMBFileShareInfo-NotificationPolicy"></a>
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

 ** ObjectACL **   <a name="StorageGateway-Type-SMBFileShareInfo-ObjectACL"></a>
A value that sets the access control list (ACL) permission for objects in the S3 bucket that an S3 File Gateway puts objects into. The default value is `private`.  
Type: String  
Valid Values: `private | public-read | public-read-write | authenticated-read | bucket-owner-read | bucket-owner-full-control | aws-exec-read`   
Required: No

 ** OplocksEnabled **   <a name="StorageGateway-Type-SMBFileShareInfo-OplocksEnabled"></a>
Specifies whether opportunistic locking is enabled for the SMB file share.  
Enabling opportunistic locking on case-sensitive shares is not recommended for workloads that involve access to files with the same name in different case.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** Path **   <a name="StorageGateway-Type-SMBFileShareInfo-Path"></a>
The file share path used by the SMB client to identify the mount point.  
Type: String  
Required: No

 ** ReadOnly **   <a name="StorageGateway-Type-SMBFileShareInfo-ReadOnly"></a>
A value that sets the write status of a file share. Set this value to `true` to set the write status to read-only, otherwise set to `false`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** RequesterPays **   <a name="StorageGateway-Type-SMBFileShareInfo-RequesterPays"></a>
A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to `true`, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.  
 `RequesterPays` is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** Role **   <a name="StorageGateway-Type-SMBFileShareInfo-Role"></a>
The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):iam::([0-9]+):role/(\S+)$`   
Required: No

 ** SMBACLEnabled **   <a name="StorageGateway-Type-SMBFileShareInfo-SMBACLEnabled"></a>
If this value is set to `true`, it indicates that access control list (ACL) is enabled on the SMB file share. If it is set to `false`, it indicates that file and directory permissions are mapped to the POSIX permission.  
For more information, see [Using Windows ACLs to limit SMB file share access](https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html) in the *Amazon S3 File Gateway User Guide*.  
Type: Boolean  
Required: No

 ** Tags **   <a name="StorageGateway-Type-SMBFileShareInfo-Tags"></a>
A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the `ListTagsForResource` API operation.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** ValidUserList **   <a name="StorageGateway-Type-SMBFileShareInfo-ValidUserList"></a>
A list of users or groups in the Active Directory that are allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1`, `user1`, `@group1`, and `@DOMAIN\group1`. Can only be set if Authentication is set to `ActiveDirectory`.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** VPCEndpointDNSName **   <a name="StorageGateway-Type-SMBFileShareInfo-VPCEndpointDNSName"></a>
Specifies the DNS name for the VPC endpoint that the SMB file share uses to connect to Amazon S3.  
This parameter is required for SMB file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`   
Required: No

## See Also
<a name="API_SMBFileShareInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/SMBFileShareInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/SMBFileShareInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/SMBFileShareInfo) 