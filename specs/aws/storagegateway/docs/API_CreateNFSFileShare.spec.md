---
id: "@specs/aws/storagegateway/docs/API_CreateNFSFileShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateNFSFileShare"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CreateNFSFileShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CreateNFSFileShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateNFSFileShare
<a name="API_CreateNFSFileShare"></a>

Creates a Network File System (NFS) file share on an existing S3 File Gateway. In Storage Gateway, a file share is a file system mount point backed by Amazon S3 cloud storage. Storage Gateway exposes file shares using an NFS interface. This operation is only supported for S3 File Gateways.

**Important**  
S3 File gateway requires AWS Security Token Service (AWS STS) to be activated to enable you to create a file share. Make sure AWS STS is activated in the AWS Region you are creating your S3 File Gateway in. If AWS STS is not activated in the AWS Region, activate it. For information about how to activate AWS STS, see [Activating and deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the * AWS Identity and Access Management User Guide*.  
S3 File Gateways do not support creating hard or symbolic links on a file share.

## Request Syntax
<a name="API_CreateNFSFileShare_RequestSyntax"></a>

```
{
   "AuditDestinationARN": "{{string}}",
   "BucketRegion": "{{string}}",
   "CacheAttributes": { 
      "CacheStaleTimeoutInSeconds": {{number}}
   },
   "ClientList": [ "{{string}}" ],
   "ClientToken": "{{string}}",
   "DefaultStorageClass": "{{string}}",
   "EncryptionType": "{{string}}",
   "FileShareName": "{{string}}",
   "GatewayARN": "{{string}}",
   "GuessMIMETypeEnabled": {{boolean}},
   "KMSEncrypted": {{boolean}},
   "KMSKey": "{{string}}",
   "LocationARN": "{{string}}",
   "NFSFileShareDefaults": { 
      "DirectoryMode": "{{string}}",
      "FileMode": "{{string}}",
      "GroupId": {{number}},
      "OwnerId": {{number}}
   },
   "NotificationPolicy": "{{string}}",
   "ObjectACL": "{{string}}",
   "ReadOnly": {{boolean}},
   "RequesterPays": {{boolean}},
   "Role": "{{string}}",
   "Squash": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VPCEndpointDNSName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateNFSFileShare_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AuditDestinationARN](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-AuditDestinationARN"></a>
The Amazon Resource Name (ARN) of the storage used for audit logs.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** [BucketRegion](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-BucketRegion"></a>
Specifies the Region of the S3 bucket where the NFS file share stores files.  
This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: No

 ** [CacheAttributes](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-CacheAttributes"></a>
Specifies refresh cache information for the file share.  
Type: [CacheAttributes](API_CacheAttributes.md) object  
Required: No

 ** [ClientList](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-ClientList"></a>
The list of clients that are allowed to access the S3 File Gateway. The list must contain either valid IPv4/IPv6 addresses or valid CIDR blocks.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Pattern: `^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?:\/(?:[0-9]|[1-2][0-9]|3[0-2]))?$|^(?:(?:(?:[A-Fa-f0-9]{1,4}:){6}|(?=(?:[A-Fa-f0-9]{0,4}:){0,6}(?:[0-9]{1,3}\.){3}[0-9]{1,3}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){0,5}|:)(?:(?::[0-9A-Fa-f]{1,4}){1,5}:|:)|::(?:[A-Fa-f0-9]{1,4}:){5})(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}|(?=(?:[A-Fa-f0-9]{0,4}:){0,7}[A-Fa-f0-9]{0,4}(?![:.\w]))(?:(?:[0-9A-Fa-f]{1,4}:){1,7}|:)(?:(:[0-9A-Fa-f]{1,4}){1,7}|:)|(?:[A-Fa-f0-9]{1,4}:){7}:|:(:[A-Fa-f0-9]{1,4}){7})(?:\/(?:12[0-8]|1[01][0-9]|[1-9]?[0-9]))?$`   
Required: No

 ** [ClientToken](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-ClientToken"></a>
A unique string value that you supply that is used by S3 File Gateway to ensure idempotent file share creation.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 100.  
Required: Yes

 ** [DefaultStorageClass](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-DefaultStorageClass"></a>
The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is `S3_STANDARD`. Optional.  
Valid Values: `S3_STANDARD` \| `S3_INTELLIGENT_TIERING` \| `S3_STANDARD_IA` \| `S3_ONEZONE_IA`   
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 50.  
Required: No

 ** [EncryptionType](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-EncryptionType"></a>
A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Type: String  
Valid Values: `SseS3 | SseKms | DsseKms`   
Required: No

 ** [FileShareName](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-FileShareName"></a>
The name of the file share. Optional.  
 `FileShareName` must be set if an S3 prefix name is set in `LocationARN`, or if an access point or access point alias is used.  
A valid NFS file share name can only contain the following characters: `a`-`z`, `A`-`Z`, `0`-`9`, `-`, `.`, and `_`.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** [GatewayARN](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the S3 File Gateway on which you want to create a file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [GuessMIMETypeEnabled](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-GuessMIMETypeEnabled"></a>
A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to `true` to enable MIME type guessing, otherwise set to `false`. The default value is `true`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [KMSEncrypted](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-KMSEncrypted"></a>
 *This parameter has been deprecated.*   
Optional. Set to `true` to use Amazon S3 server-side encryption with your own AWS KMS key (SSE-KMS), or `false` to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the `EncryptionType` parameter instead.  
We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.  
If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3`, then `KMSEncrypted` must be `false`. If `EncryptionType` is `SseKms` or `DsseKms`, then `KMSEncrypted` must be `true`.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [KMSKey](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-KMSKey"></a>
Optional. The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value must be set if `KMSEncrypted` is `true`, or if `EncryptionType` is `SseKms` or `DsseKms`.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** [LocationARN](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-LocationARN"></a>
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
Required: Yes

 ** [NFSFileShareDefaults](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-NFSFileShareDefaults"></a>
File share default values. Optional.  
Type: [NFSFileShareDefaults](API_NFSFileShareDefaults.md) object  
Required: No

 ** [NotificationPolicy](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-NotificationPolicy"></a>
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

 ** [ObjectACL](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-ObjectACL"></a>
A value that sets the access control list (ACL) permission for objects in the S3 bucket that a S3 File Gateway puts objects into. The default value is `private`.  
Type: String  
Valid Values: `private | public-read | public-read-write | authenticated-read | bucket-owner-read | bucket-owner-full-control | aws-exec-read`   
Required: No

 ** [ReadOnly](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-ReadOnly"></a>
A value that sets the write status of a file share. Set this value to `true` to set the write status to read-only, otherwise set to `false`.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [RequesterPays](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-RequesterPays"></a>
A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to `true`, the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.  
 `RequesterPays` is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [Role](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-Role"></a>
The ARN of the AWS Identity and Access Management (IAM) role that an S3 File Gateway assumes when it accesses the underlying storage.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):iam::([0-9]+):role/(\S+)$`   
Required: Yes

 ** [Squash](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-Squash"></a>
A value that maps a user to anonymous user.  
Valid values are the following:  
+  `RootSquash`: Only root is mapped to anonymous user.
+  `NoSquash`: No one is mapped to anonymous user.
+  `AllSquash`: Everyone is mapped to anonymous user.
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 15.  
Required: No

 ** [Tags](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-Tags"></a>
A list of up to 50 tags that can be assigned to the NFS file share. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VPCEndpointDNSName](#API_CreateNFSFileShare_RequestSyntax) **   <a name="StorageGateway-CreateNFSFileShare-request-VPCEndpointDNSName"></a>
Specifies the DNS name for the VPC endpoint that the NFS file share uses to connect to Amazon S3.  
This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`   
Required: No

## Response Syntax
<a name="API_CreateNFSFileShare_ResponseSyntax"></a>

```
{
   "FileShareARN": "string"
}
```

## Response Elements
<a name="API_CreateNFSFileShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileShareARN](#API_CreateNFSFileShare_ResponseSyntax) **   <a name="StorageGateway-CreateNFSFileShare-response-FileShareARN"></a>
The Amazon Resource Name (ARN) of the newly created file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_CreateNFSFileShare_Errors"></a>

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
<a name="API_CreateNFSFileShare_Examples"></a>

### Create an NFS file share
<a name="API_CreateNFSFileShare_Example_1"></a>

In the following request, you create a file share using an existing S3 File Gateway and using your own AWS KMS key to perform server-side encryption of the contents of the file share.

#### Sample Request
<a name="API_CreateNFSFileShare_Example_1_Request"></a>

```
{
    "ClientList": "10.1.1.1",
    "ClientToken": "xy23421",
    "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-XXXXXXX",
    "GuessMIMETypeEnabled": "true",
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "LocationARN": "arn:aws:s3:::amzn-s3-demo-bucket",
    "NFSFileShareDefaults": {
        "FileMode": "0777",
        "DirectoryMode": "0777",
        "GroupId": "500",
        "OwnerId": "500"
    },
    "ObjectACL": "bucket-owner-full-control",
    "ReadOnly": "false",
    "RequesterPays": "false",
    "Role": "arn:aws:iam::111122223333:role/my-role",
    "Squash": "RootSquash"
}
```

#### Sample Response
<a name="API_CreateNFSFileShare_Example_1_Response"></a>

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY"
}
```

### Create an NFS file share with file upload notification on
<a name="API_CreateNFSFileShare_Example_2"></a>

In the following request, you create an NFS file share using an existing file gateway and with file upload notification turned on and settling time set to 60 seconds.

#### Sample Request
<a name="API_CreateNFSFileShare_Example_2_Request"></a>

```
{
    "ClientList": "10.1.1.1",
    "ClientToken": "xy23421",
    "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-XXXXXXX",
    "GuessMIMETypeEnabled": "true",
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "LocationARN": "arn:aws:s3:::amzn-s3-demo-bucket",
    "NFSFileShareDefaults": {
        "FileMode": "0777",
        "DirectoryMode": "0777",
        "GroupId": "500",
        "OwnerId": "500"
    },
    "ObjectACL": "bucket-owner-full-control",
    "ReadOnly": "false",
    "RequesterPays": "false",
    "Role": "arn:aws:iam::111122223333:role/my-role",
    "Squash": "RootSquash",
    "NotificationPolicy": "{\"Upload\": {\"SettlingTimeInSeconds\": 60}}"
}
```

#### Sample Response
<a name="API_CreateNFSFileShare_Example_2_Response"></a>

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY"
}
```

### Create an NFS file share with file upload notification off
<a name="API_CreateNFSFileShare_Example_3"></a>

In the following request, you create an NFS file share using an existing file gateway and with file upload notification turned off.

#### Sample Request
<a name="API_CreateNFSFileShare_Example_3_Request"></a>

```
{
    "ClientList": "10.1.1.1",
    "ClientToken": "xy23421",
    "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-XXXXXXX",
    "GuessMIMETypeEnabled": "true",
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "LocationARN": "arn:aws:s3:::amzn-s3-demo-bucket",
    "NFSFileShareDefaults": {
        "FileMode": "0777",
        "DirectoryMode": "0777",
        "GroupId": "500",
        "OwnerId": "500"
    },
    "ObjectACL": "bucket-owner-full-control",
    "ReadOnly": "false",
    "RequesterPays": "false",
    "Role": "arn:aws:iam::111122223333:role/my-role",
    "Squash": "RootSquash",
    "NotificationPolicy": "{}"
}
```

#### Sample Response
<a name="API_CreateNFSFileShare_Example_3_Response"></a>

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-YYYYYYY"
}
```

## See Also
<a name="API_CreateNFSFileShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CreateNFSFileShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CreateNFSFileShare) 