---
id: "@specs/aws/storagegateway/docs/API_DeleteTape"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTape"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DeleteTape

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DeleteTape
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTape
<a name="API_DeleteTape"></a>

Deletes the specified virtual tape. This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_DeleteTape_RequestSyntax"></a>

```
{
   "BypassGovernanceRetention": {{boolean}},
   "GatewayARN": "{{string}}",
   "TapeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTape_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BypassGovernanceRetention](#API_DeleteTape_RequestSyntax) **   <a name="StorageGateway-DeleteTape-request-BypassGovernanceRetention"></a>
Set to `TRUE` to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to `governance` can be deleted. Archived tapes with tape retention lock set to `compliance` can't be deleted.  
Type: Boolean  
Required: No

 ** [GatewayARN](#API_DeleteTape_RequestSyntax) **   <a name="StorageGateway-DeleteTape-request-GatewayARN"></a>
The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [TapeARN](#API_DeleteTape_RequestSyntax) **   <a name="StorageGateway-DeleteTape-request-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape to delete.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: Yes

## Response Syntax
<a name="API_DeleteTape_ResponseSyntax"></a>

```
{
   "TapeARN": "string"
}
```

## Response Elements
<a name="API_DeleteTape_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TapeARN](#API_DeleteTape_ResponseSyntax) **   <a name="StorageGateway-DeleteTape-response-TapeARN"></a>
The Amazon Resource Name (ARN) of the deleted virtual tape.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$` 

## Errors
<a name="API_DeleteTape_Errors"></a>

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
<a name="API_DeleteTape_Examples"></a>

### Delete a tape from a gateway
<a name="API_DeleteTape_Example_1"></a>

The following example deletes a tape from a tape gateway with ID sgw-12A3456B. The request identifies the tape by its ARN. The operation deletes the tapes from the specified gateway's virtual tape library (VTL). In the response, tape gateway returns the ARN of deleted tape.

#### Sample Request
<a name="API_DeleteTape_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20131025T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9EXAMPLE
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DeleteTape

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:123456789012:gateway/sgw-12A3456B",
    "TapeARN": "arn:aws:storagegateway:us-east-2:123456789012:tape/TEST05A2A0"
}
```

#### Sample Response
<a name="API_DeleteTape_Example_1_Response"></a>

```
{
    "TapeARN": "arn:aws:storagegateway:us-east-2:123456789012:tape/TEST05A2A0"
}
```

## See Also
<a name="API_DeleteTape_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DeleteTape) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeleteTape) 