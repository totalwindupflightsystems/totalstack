---
id: "@specs/aws/storagegateway/docs/API_AssignTapePool"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssignTapePool"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AssignTapePool

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AssignTapePool
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssignTapePool
<a name="API_AssignTapePool"></a>

Assigns a tape to a tape pool for archiving. The tape assigned to a pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the S3 storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.

## Request Syntax
<a name="API_AssignTapePool_RequestSyntax"></a>

```
{
   "BypassGovernanceRetention": {{boolean}},
   "PoolId": "{{string}}",
   "TapeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_AssignTapePool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BypassGovernanceRetention](#API_AssignTapePool_RequestSyntax) **   <a name="StorageGateway-AssignTapePool-request-BypassGovernanceRetention"></a>
Set permissions to bypass governance retention. If the lock type of the archived tape is `Governance`, the tape's archived age is not older than `RetentionLockInDays`, and the user does not already have `BypassGovernanceRetention`, setting this to TRUE enables the user to bypass the retention lock. This parameter is set to true by default for calls from the console.  
Valid values: `TRUE` \| `FALSE`   
Type: Boolean  
Required: No

 ** [PoolId](#API_AssignTapePool_RequestSyntax) **   <a name="StorageGateway-AssignTapePool-request-PoolId"></a>
The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** [TapeARN](#API_AssignTapePool_RequestSyntax) **   <a name="StorageGateway-AssignTapePool-request-TapeARN"></a>
The unique Amazon Resource Name (ARN) of the virtual tape that you want to add to the tape pool.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: Yes

## Response Syntax
<a name="API_AssignTapePool_ResponseSyntax"></a>

```
{
   "TapeARN": "string"
}
```

## Response Elements
<a name="API_AssignTapePool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TapeARN](#API_AssignTapePool_ResponseSyntax) **   <a name="StorageGateway-AssignTapePool-response-TapeARN"></a>
The unique Amazon Resource Names (ARN) of the virtual tape that was added to the tape pool.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$` 

## Errors
<a name="API_AssignTapePool_Errors"></a>

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
<a name="API_AssignTapePool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/AssignTapePool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AssignTapePool) 