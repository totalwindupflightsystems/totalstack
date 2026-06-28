---
id: "@specs/aws/storagegateway/docs/API_RetrieveTapeRecoveryPoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RetrieveTapeRecoveryPoint"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# RetrieveTapeRecoveryPoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_RetrieveTapeRecoveryPoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RetrieveTapeRecoveryPoint
<a name="API_RetrieveTapeRecoveryPoint"></a>

Retrieves the recovery point for the specified virtual tape. This operation is only supported in the tape gateway type.

A recovery point is a point in time view of a virtual tape at which all the data on the tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway.

**Note**  
The virtual tape can be retrieved to only one gateway. The retrieved tape is read-only. The virtual tape can be retrieved to only a tape gateway. There is no charge for retrieving recovery points.

## Request Syntax
<a name="API_RetrieveTapeRecoveryPoint_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "TapeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_RetrieveTapeRecoveryPoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_RetrieveTapeRecoveryPoint_RequestSyntax) **   <a name="StorageGateway-RetrieveTapeRecoveryPoint-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [TapeARN](#API_RetrieveTapeRecoveryPoint_RequestSyntax) **   <a name="StorageGateway-RetrieveTapeRecoveryPoint-request-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: Yes

## Response Syntax
<a name="API_RetrieveTapeRecoveryPoint_ResponseSyntax"></a>

```
{
   "TapeARN": "string"
}
```

## Response Elements
<a name="API_RetrieveTapeRecoveryPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TapeARN](#API_RetrieveTapeRecoveryPoint_ResponseSyntax) **   <a name="StorageGateway-RetrieveTapeRecoveryPoint-response-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape for which the recovery point was retrieved.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$` 

## Errors
<a name="API_RetrieveTapeRecoveryPoint_Errors"></a>

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
<a name="API_RetrieveTapeRecoveryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/RetrieveTapeRecoveryPoint) 