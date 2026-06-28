---
id: "@specs/aws/storagegateway/docs/API_RetrieveTapeArchive"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RetrieveTapeArchive"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# RetrieveTapeArchive

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_RetrieveTapeArchive
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RetrieveTapeArchive
<a name="API_RetrieveTapeArchive"></a>

Retrieves an archived virtual tape from the virtual tape shelf (VTS) to a tape gateway. Virtual tapes archived in the VTS are not associated with any gateway. However after a tape is retrieved, it is associated with a gateway, even though it is also listed in the VTS, that is, archive. This operation is only supported in the tape gateway type.

Once a tape is successfully retrieved to a gateway, it cannot be retrieved again to another gateway. You must archive the tape again before you can retrieve it to another gateway. This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_RetrieveTapeArchive_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "TapeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_RetrieveTapeArchive_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_RetrieveTapeArchive_RequestSyntax) **   <a name="StorageGateway-RetrieveTapeArchive-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway you want to retrieve the virtual tape to. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
You retrieve archived virtual tapes to only one gateway and the gateway must be a tape gateway.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [TapeARN](#API_RetrieveTapeArchive_RequestSyntax) **   <a name="StorageGateway-RetrieveTapeArchive-request-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape you want to retrieve from the virtual tape shelf (VTS).  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: Yes

## Response Syntax
<a name="API_RetrieveTapeArchive_ResponseSyntax"></a>

```
{
   "TapeARN": "string"
}
```

## Response Elements
<a name="API_RetrieveTapeArchive_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TapeARN](#API_RetrieveTapeArchive_ResponseSyntax) **   <a name="StorageGateway-RetrieveTapeArchive-response-TapeARN"></a>
The Amazon Resource Name (ARN) of the retrieved virtual tape.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$` 

## Errors
<a name="API_RetrieveTapeArchive_Errors"></a>

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
<a name="API_RetrieveTapeArchive_Examples"></a>

### Retrieve a tape
<a name="API_RetrieveTapeArchive_Example_1"></a>

The following example request retrieves an archived tape from VTS to a gateway with the ID sgw-12A3456B. In the request, the tape is identified by its ARN. In the ARN the trailing string is the tape barcode. The string 999999999999 is your AWS account number. It takes about 24 hours for retrieval to complete. After the operation is complete, the tape appears in the specified gateway's virtual tape library (VTL).

#### Sample Request
<a name="API_RetrieveTapeArchive_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.RetrieveTapeArchive

{
    "TapeARN": "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST0AA2AF",
    "GatewayARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_RetrieveTapeArchive_Example_1_Response"></a>

```
{
    "TapeARN": "arn:aws:storagegateway:us-east-2:123456789012:tape/TEST0AA2AF"
}
```

## See Also
<a name="API_RetrieveTapeArchive_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/RetrieveTapeArchive) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/RetrieveTapeArchive) 