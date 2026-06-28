---
id: "@specs/aws/storagegateway/docs/API_CreateTapePool"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTapePool"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CreateTapePool

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CreateTapePool
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTapePool
<a name="API_CreateTapePool"></a>

Creates a new custom tape pool. You can use custom tape pool to enable tape retention lock on tapes that are archived in the custom pool.

## Request Syntax
<a name="API_CreateTapePool_RequestSyntax"></a>

```
{
   "PoolName": "{{string}}",
   "RetentionLockTimeInDays": {{number}},
   "RetentionLockType": "{{string}}",
   "StorageClass": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateTapePool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PoolName](#API_CreateTapePool_RequestSyntax) **   <a name="StorageGateway-CreateTapePool-request-PoolName"></a>
The name of the new custom tape pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*$`   
Required: Yes

 ** [RetentionLockTimeInDays](#API_CreateTapePool_RequestSyntax) **   <a name="StorageGateway-CreateTapePool-request-RetentionLockTimeInDays"></a>
Tape retention lock time is set in days. Tape retention lock can be enabled for up to 100 years (36,500 days).  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 36500.  
Required: No

 ** [RetentionLockType](#API_CreateTapePool_RequestSyntax) **   <a name="StorageGateway-CreateTapePool-request-RetentionLockType"></a>
Tape retention lock can be configured in two modes. When configured in governance mode, AWS accounts with specific IAM permissions are authorized to remove the tape retention lock from archived virtual tapes. When configured in compliance mode, the tape retention lock cannot be removed by any user, including the root AWS account.  
Type: String  
Valid Values: `COMPLIANCE | GOVERNANCE | NONE`   
Required: No

 ** [StorageClass](#API_CreateTapePool_RequestSyntax) **   <a name="StorageGateway-CreateTapePool-request-StorageClass"></a>
The storage class that is associated with the new custom pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.  
Type: String  
Valid Values: `DEEP_ARCHIVE | GLACIER`   
Required: Yes

 ** [Tags](#API_CreateTapePool_RequestSyntax) **   <a name="StorageGateway-CreateTapePool-request-Tags"></a>
A list of up to 50 tags that can be assigned to tape pool. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreateTapePool_ResponseSyntax"></a>

```
{
   "PoolARN": "string"
}
```

## Response Elements
<a name="API_CreateTapePool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PoolARN](#API_CreateTapePool_ResponseSyntax) **   <a name="StorageGateway-CreateTapePool-response-PoolARN"></a>
The unique Amazon Resource Name (ARN) that represents the custom tape pool. Use the [ListTapePools](API_ListTapePools.md) operation to return a list of tape pools for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_CreateTapePool_Errors"></a>

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

## See Also
<a name="API_CreateTapePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CreateTapePool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CreateTapePool) 