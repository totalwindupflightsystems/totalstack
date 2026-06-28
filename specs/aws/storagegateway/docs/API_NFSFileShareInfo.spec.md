---
id: "@specs/aws/storagegateway/docs/API_NFSFileShareInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NFSFileShareInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# NFSFileShareInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_NFSFileShareInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NFSFileShareInfo
<a name="API_NFSFileShareInfo"></a>

The Unix file permissions and ownership information assigned, by default, to native S3 objects when an S3 File Gateway discovers them in S3 buckets. This operation is only supported in S3 File Gateways.

## Contents
<a name="API_NFSFileShareInfo_Contents"></a>

 ** AuditDestinationARN **   <a name="StorageGateway-Type-NFSFileShareInfo-AuditDestinationARN"></a>
The Amazon Resource Name (ARN) of the storage used for audit logs.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** BucketRegion **   <a name="StorageGateway-Type-NFSFileShareInfo-BucketRegion"></a>
Specifies the Region of the S3 bucket where the NFS file share stores files.  
This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: No

 ** CacheAttributes **   <a name="StorageGateway-Type-NFSFileShareInfo-CacheAttributes"></a>
Refresh cache information for the file share.  
Type: [CacheAttributes](API_CacheAttributes.md) object  
Required: No

 ** ClientList **   <a name="StorageGateway-Type-NFSFileShareInfo-ClientList"></a>
The list of clients that are allowed to access the S3 File Gateway. The list must contain either valid IPv4/IPv6 addresses or valid CIDR blocks.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Pattern: `^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\/(?:[0-9]|[1-2][0-9]|3[0-2]))?$|^(?:(?:(?:[A-Fa-f0-9]{1,4}:){6}|(?=(?:[A-Fa-f0-9]{0,4}:){0,6}(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){0,5}|:)(?:(?::[0-9A-Fa-f]{1,4}){1,5}:|:)|::(?:[A-Fa-f0-9]{1,4}:){5})(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|(?=(?:[A-Fa-f0-9]{0,4}:){0,7}[A-Fa-f0-9]{0,4}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){1,7}|:)(?:(:[0-9A-Fa-f]{1,4}){1,7}|:)|(?:[A-Fa-f0-9]{1,4}:){7}:|:(:[A-Fa-f0-9]{1,4}){7})(?:\/(?:12[0-8]|1[01][0-9]|[1-9]?[0-9]))?$`   
Required: No

 ** DefaultStorageClass **   <a name="StorageGateway-Type-NFSFileShareInfo-DefaultStorageClass"></a>
The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is `S3_STANDARD`. Optional.  
Valid Values: `S3_STANDARD` \| `S3_INTELLIGENT_TIERING` \| `S3_STANDARD_IA` \| `S3_ONEZONE_IA`   
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 50.  
Required: No

 ** EncryptionType **   <a name="StorageGateway-Type-NFSFileShareInfo-EncryptionType"></a>
A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Type: String  
Valid Values: `SseS3 | SseKms | DsseKms`   
Required: No

 ** FileShareARN **   <a name="StorageGateway-Type-NFSFileShareInfo-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** FileShareId **   <a name="StorageGateway-Type-NFSFileShareInfo-FileShareId"></a>
The ID of the file share.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.  
Required: No

 ** FileShareName **   <a name="StorageGateway-Type-NFSFileShareInfo-FileShareName"></a>
The name of the file share. Optional.  
 `FileShareName` must be set if an S3 prefix name is set in `LocationARN`, or if an access point or access point alias is used.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** FileShareStatus **   <a name="StorageGateway-Type-NFSFileShareInfo-FileShareStatus"></a>
The status of the file share.  
Valid Values: `CREATING` \| `UPDATING` \| `AVAILABLE` \| `DELETING`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-NFSFileShareInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** GuessMIMETypeEnabled **   <a name="StorageGateway-Type-NFSFileShareInfo-GuessMIMETypeEnabled"></a>
A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to `true` to enable MIME type guessing, otherwise set to `false`. The default value is `true`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** KMSEncrypted **   <a name="StorageGateway-Type-NFSFileShareInfo-KMSEncrypted"></a>
 *This member has been deprecated.*   
Optional. Set to `true` to use Amazon S3 server-side encryption with your own AWS KMS key (SSE-KMS), or `false` to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the `EncryptionType` parameter instead.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** KMSKey **   <a name="StorageGateway-Type-NFSFileShareInfo-KMSKey"></a>
Optional. The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value must be set if `KMSEncrypted` is `true`, or if `EncryptionType` is `SseKms` or `DsseKms`.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** LocationARN **   <a name="StorageGateway-Type-NFSFileShareInfo-LocationARN"></a>
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

 ** NFSFileShareDefaults **   <a name="StorageGateway-Type-NFSFileShareInfo-NFSFileShareDefaults"></a>
Describes Network File System (NFS) file share default values. Files and folders stored as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files and folders are assigned these default Unix permissions. This operation is only supported for S3 File Gateways.  
Type: [NFSFileShareDefaults](API_NFSFileShareDefaults.md) object  
Required: No

 ** NotificationPolicy **   <a name="StorageGateway-Type-NFSFileShareInfo-NotificationPolicy"></a>
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

 ** ObjectACL **   <a name="StorageGateway-Type-NFSFileShareInfo-ObjectACL"></a>
A value that sets the access control list (ACL) permission for objects in the S3 bucket that an S3 File Gateway puts objects into. The default value is `private`.  
Type: String  
Valid Values: `private | public-read | public-read-write | authenticated-read | bucket-owner-read | bucket-owner-full-control | aws-exec-read`   
Required: No

 ** Path **   <a name="StorageGateway-Type-NFSFileShareInfo-Path"></a>
The file share path used by the NFS client to identify the mount point.  
Type: String  
Required: No

 ** ReadOnly **   <a name="StorageGateway-Type-NFSFileShareInfo-ReadOnly"></a>
A value that sets the write status of a file share. Set this value to `true` to set the write status to read-only, otherwise set to `false`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** RequesterPays **   <a name="StorageGateway-Type-NFSFileShareInfo-RequesterPays"></a>
A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to `true`, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.  
 `RequesterPays` is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** Role **   <a name="StorageGateway-Type-NFSFileShareInfo-Role"></a>
The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):iam::([0-9]+):role/(\S+)$`   
Required: No

 ** Squash **   <a name="StorageGateway-Type-NFSFileShareInfo-Squash"></a>
The user mapped to anonymous user. Valid options are the following:  
+  `RootSquash`: Only root is mapped to anonymous user.
+  `NoSquash`: No one is mapped to anonymous user.
+  `AllSquash`: Everyone is mapped to anonymous user.
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 15.  
Required: No

 ** Tags **   <a name="StorageGateway-Type-NFSFileShareInfo-Tags"></a>
A list of up to 50 tags assigned to the NFS file share, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the `ListTagsForResource` API operation.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** VPCEndpointDNSName **   <a name="StorageGateway-Type-NFSFileShareInfo-VPCEndpointDNSName"></a>
Specifies the DNS name for the VPC endpoint that the NFS file share uses to connect to Amazon S3.  
This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`   
Required: No

## See Also
<a name="API_NFSFileShareInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/NFSFileShareInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/NFSFileShareInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/NFSFileShareInfo) 