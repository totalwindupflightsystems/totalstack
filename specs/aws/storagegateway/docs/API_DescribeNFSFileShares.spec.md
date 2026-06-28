---
id: "@specs/aws/storagegateway/docs/API_DescribeNFSFileShares"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeNFSFileShares"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeNFSFileShares

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeNFSFileShares
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeNFSFileShares
<a name="API_DescribeNFSFileShares"></a>

Gets a description for one or more Network File System (NFS) file shares from an S3 File Gateway. This operation is only supported for S3 File Gateways.

## Request Syntax
<a name="API_DescribeNFSFileShares_RequestSyntax"></a>

```
{
   "FileShareARNList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeNFSFileShares_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileShareARNList](#API_DescribeNFSFileShares_RequestSyntax) **   <a name="StorageGateway-DescribeNFSFileShares-request-FileShareARNList"></a>
An array containing the Amazon Resource Name (ARN) of each file share to be described.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeNFSFileShares_ResponseSyntax"></a>

```
{
   "NFSFileShareInfoList": [ 
      { 
         "AuditDestinationARN": "string",
         "BucketRegion": "string",
         "CacheAttributes": { 
            "CacheStaleTimeoutInSeconds": number
         },
         "ClientList": [ "string" ],
         "DefaultStorageClass": "string",
         "EncryptionType": "string",
         "FileShareARN": "string",
         "FileShareId": "string",
         "FileShareName": "string",
         "FileShareStatus": "string",
         "GatewayARN": "string",
         "GuessMIMETypeEnabled": boolean,
         "KMSEncrypted": boolean,
         "KMSKey": "string",
         "LocationARN": "string",
         "NFSFileShareDefaults": { 
            "DirectoryMode": "string",
            "FileMode": "string",
            "GroupId": number,
            "OwnerId": number
         },
         "NotificationPolicy": "string",
         "ObjectACL": "string",
         "Path": "string",
         "ReadOnly": boolean,
         "RequesterPays": boolean,
         "Role": "string",
         "Squash": "string",
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ],
         "VPCEndpointDNSName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeNFSFileShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NFSFileShareInfoList](#API_DescribeNFSFileShares_ResponseSyntax) **   <a name="StorageGateway-DescribeNFSFileShares-response-NFSFileShareInfoList"></a>
An array containing a description for each requested file share.  
Type: Array of [NFSFileShareInfo](API_NFSFileShareInfo.md) objects

## Errors
<a name="API_DescribeNFSFileShares_Errors"></a>

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
<a name="API_DescribeNFSFileShares_Examples"></a>

### Describe an NFS file share
<a name="API_DescribeNFSFileShares_Example_1"></a>

In the following request, you get the description for a single file share identified by its Amazon Resource Name (ARN).

#### Sample Request
<a name="API_DescribeNFSFileShares_Example_1_Request"></a>

```
{
    "FileShareARNList": [
        "arn:aws:storagegateway:us-east-2:204469490176:share/share-XXXXXX"
    ]
}
```

#### Sample Response
<a name="API_DescribeNFSFileShares_Example_1_Response"></a>

```
{
    "NFSFileShareInfoList": [
        {
            "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
            "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-XXXXXXXX",
            "FileShareId": "share-XXXXXXXX",
            "FileShareStatus": "AVAILABLE",
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-YYYYYYYY",
            "GuessMIMETypeEnabled": "true",
            "KMSEncrypted": "true",
            "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
            "LocationARN": "arn:aws:s3:::amzn-s3-demo-bucket",
            "NFSFileShareDefaults": {
                "DirectoryMode": "0777",
                "FileMode": "0777",
                "GroupId": "500",
                "OwnerId": "500"
            },
            "ObjectACL": "bucket-owner-full-control",
            "ReadOnly": "false",
            "Path": "/my-path-alpha",
            "RequesterPays": "false",
            "Role": "arn:aws:iam::111122223333:role/my-role"
        }
    ]
}
```

## See Also
<a name="API_DescribeNFSFileShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeNFSFileShares) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeNFSFileShares) 