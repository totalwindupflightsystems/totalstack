---
id: "@specs/aws/storagegateway/docs/API_DescribeSMBFileShares"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSMBFileShares"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeSMBFileShares

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeSMBFileShares
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSMBFileShares
<a name="API_DescribeSMBFileShares"></a>

Gets a description for one or more Server Message Block (SMB) file shares from a S3 File Gateway. This operation is only supported for S3 File Gateways.

## Request Syntax
<a name="API_DescribeSMBFileShares_RequestSyntax"></a>

```
{
   "FileShareARNList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeSMBFileShares_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileShareARNList](#API_DescribeSMBFileShares_RequestSyntax) **   <a name="StorageGateway-DescribeSMBFileShares-request-FileShareARNList"></a>
An array containing the Amazon Resource Name (ARN) of each file share to be described.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeSMBFileShares_ResponseSyntax"></a>

```
{
   "SMBFileShareInfoList": [ 
      { 
         "AccessBasedEnumeration": boolean,
         "AdminUserList": [ "string" ],
         "AuditDestinationARN": "string",
         "Authentication": "string",
         "BucketRegion": "string",
         "CacheAttributes": { 
            "CacheStaleTimeoutInSeconds": number
         },
         "CaseSensitivity": "string",
         "DefaultStorageClass": "string",
         "EncryptionType": "string",
         "FileShareARN": "string",
         "FileShareId": "string",
         "FileShareName": "string",
         "FileShareStatus": "string",
         "GatewayARN": "string",
         "GuessMIMETypeEnabled": boolean,
         "InvalidUserList": [ "string" ],
         "KMSEncrypted": boolean,
         "KMSKey": "string",
         "LocationARN": "string",
         "NotificationPolicy": "string",
         "ObjectACL": "string",
         "OplocksEnabled": boolean,
         "Path": "string",
         "ReadOnly": boolean,
         "RequesterPays": boolean,
         "Role": "string",
         "SMBACLEnabled": boolean,
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ],
         "ValidUserList": [ "string" ],
         "VPCEndpointDNSName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSMBFileShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SMBFileShareInfoList](#API_DescribeSMBFileShares_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBFileShares-response-SMBFileShareInfoList"></a>
An array containing a description for each requested file share.  
Type: Array of [SMBFileShareInfo](API_SMBFileShareInfo.md) objects

## Errors
<a name="API_DescribeSMBFileShares_Errors"></a>

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
<a name="API_DescribeSMBFileShares_Examples"></a>

### Describe an SMB file share
<a name="API_DescribeSMBFileShares_Example_1"></a>

In the following request, you get the description for a single SMB file share identified by its Amazon Resource Name (ARN).

#### Sample Request
<a name="API_DescribeSMBFileShares_Example_1_Request"></a>

```
{
    "FileShareARNList": [
        "arn:aws:storagegateway:us-east-2:204469490176:share/share-XXXXXX"
    ]
}
```

#### Sample Response
<a name="API_DescribeSMBFileShares_Example_1_Response"></a>

```
{
    "SMBFileShareInfoList": [
        {
            "Authentication": "ActiveDirectory",
            "DefaultStorageClass": "S3_INTELLIGENT_TIERING",
            "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-XXXXXXXX",
            "FileShareId": "share-XXXXXXXX",
            "FileShareStatus": "AVAILABLE",
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-YYYYYYYY",
            "GuessMIMETypeEnabled": "true",
            "InvalidUserList": [
                "user1",
                "user2"
            ],
            "KMSEncrypted": "false",
            "LocationARN": "arn:aws:s3:::amzn-s3-demo-bucket",
            "ObjectACL": "bucket-owner-full-control",
            "Path": "/my-path-alpha",
            "ReadOnly": "false",
            "RequesterPays": "false",
            "Role": "arn:aws:iam::111122223333:role/my-role",
            "ValidUserList": [
                "user3",
                "user4"
            ]
        }
    ]
}
```

## See Also
<a name="API_DescribeSMBFileShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeSMBFileShares) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeSMBFileShares) 