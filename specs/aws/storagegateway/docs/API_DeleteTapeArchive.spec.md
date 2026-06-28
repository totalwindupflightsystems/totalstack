---
id: "@specs/aws/storagegateway/docs/API_DeleteTapeArchive"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTapeArchive"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DeleteTapeArchive

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DeleteTapeArchive
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTapeArchive
<a name="API_DeleteTapeArchive"></a>

Deletes the specified virtual tape from the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_DeleteTapeArchive_RequestSyntax"></a>

```
{
   "BypassGovernanceRetention": {{boolean}},
   "TapeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTapeArchive_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BypassGovernanceRetention](#API_DeleteTapeArchive_RequestSyntax) **   <a name="StorageGateway-DeleteTapeArchive-request-BypassGovernanceRetention"></a>
Set to `TRUE` to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to `governance` can be deleted. Archived tapes with tape retention lock set to `compliance` can't be deleted.  
Type: Boolean  
Required: No

 ** [TapeARN](#API_DeleteTapeArchive_RequestSyntax) **   <a name="StorageGateway-DeleteTapeArchive-request-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: Yes

## Response Syntax
<a name="API_DeleteTapeArchive_ResponseSyntax"></a>

```
{
   "TapeARN": "string"
}
```

## Response Elements
<a name="API_DeleteTapeArchive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TapeARN](#API_DeleteTapeArchive_ResponseSyntax) **   <a name="StorageGateway-DeleteTapeArchive-response-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape that was deleted from the virtual tape shelf (VTS).  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$` 

## Errors
<a name="API_DeleteTapeArchive_Errors"></a>

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
<a name="API_DeleteTapeArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DeleteTapeArchive) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeleteTapeArchive) 