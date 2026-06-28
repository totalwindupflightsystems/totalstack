---
id: "@specs/aws/storagegateway/docs/API_DescribeFileSystemAssociations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeFileSystemAssociations"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeFileSystemAssociations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeFileSystemAssociations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeFileSystemAssociations
<a name="API_DescribeFileSystemAssociations"></a>

Gets the file system association information. This operation is only supported for FSx File Gateways.

## Request Syntax
<a name="API_DescribeFileSystemAssociations_RequestSyntax"></a>

```
{
   "FileSystemAssociationARNList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeFileSystemAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileSystemAssociationARNList](#API_DescribeFileSystemAssociations_RequestSyntax) **   <a name="StorageGateway-DescribeFileSystemAssociations-request-FileSystemAssociationARNList"></a>
An array containing the Amazon Resource Name (ARN) of each file system association to be described.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeFileSystemAssociations_ResponseSyntax"></a>

```
{
   "FileSystemAssociationInfoList": [ 
      { 
         "AuditDestinationARN": "string",
         "CacheAttributes": { 
            "CacheStaleTimeoutInSeconds": number
         },
         "EndpointNetworkConfiguration": { 
            "IpAddresses": [ "string" ]
         },
         "FileSystemAssociationARN": "string",
         "FileSystemAssociationStatus": "string",
         "FileSystemAssociationStatusDetails": [ 
            { 
               "ErrorCode": "string"
            }
         ],
         "GatewayARN": "string",
         "LocationARN": "string",
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_DescribeFileSystemAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystemAssociationInfoList](#API_DescribeFileSystemAssociations_ResponseSyntax) **   <a name="StorageGateway-DescribeFileSystemAssociations-response-FileSystemAssociationInfoList"></a>
An array containing the `FileSystemAssociationInfo` data type of each file system association to be described.   
Type: Array of [FileSystemAssociationInfo](API_FileSystemAssociationInfo.md) objects

## Errors
<a name="API_DescribeFileSystemAssociations_Errors"></a>

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
<a name="API_DescribeFileSystemAssociations_Examples"></a>

### Example
<a name="API_DescribeFileSystemAssociations_Example_1"></a>

This example illustrates one usage of DescribeFileSystemAssociations.

```
__Sample Request__
{
  "FileSystemAssociationARNList": ["arn:aws:storagegateway:us-east-1:111122223333:fs-association/fsa-1122AABBCCDDEEFFG"]
}
```

### Example
<a name="API_DescribeFileSystemAssociations_Example_2"></a>

This example illustrates one usage of DescribeFileSystemAssociations.

```
__Sample Response__
{
  "FileSystemAssociationInfoList":
  [
    
     "FileSystemAssociationARN": "arn:aws:storagegateway:us-east-1:111122223333:fs-association/fsa-1122AABBCCDDEEFFG",
     "FileSystemAssociationStatus": " AVAILABLE", 
     "GatewayARN": "arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-7A8D6313",
     "LocationARN": "arn:aws:fsx:us-east-1:111122223333:file-system/fs-0bb4bf5cedebd814f",
     "Tags":
      []
    }
  ]
}
```

## See Also
<a name="API_DescribeFileSystemAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeFileSystemAssociations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeFileSystemAssociations) 