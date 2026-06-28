---
id: "@specs/aws/storagegateway/docs/API_DescribeTapes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTapes"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeTapes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeTapes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTapes
<a name="API_DescribeTapes"></a>

Returns a description of virtual tapes that correspond to the specified Amazon Resource Names (ARNs). If `TapeARN` is not specified, returns a description of the virtual tapes associated with the specified gateway. This operation is only supported for the tape gateway type.

The operation supports pagination. By default, the operation returns a maximum of up to 100 tapes. You can optionally specify the `Limit` field in the body to limit the number of tapes in the response. If the number of tapes returned in the response is truncated, the response includes a `Marker` field. You can use this `Marker` value in your subsequent request to retrieve the next set of tapes.

## Request Syntax
<a name="API_DescribeTapes_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}",
   "TapeARNs": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeTapes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeTapes_RequestSyntax) **   <a name="StorageGateway-DescribeTapes-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [Limit](#API_DescribeTapes_RequestSyntax) **   <a name="StorageGateway-DescribeTapes-request-Limit"></a>
Specifies that the number of virtual tapes described be limited to the specified number.  
Amazon Web Services may impose its own limit, if this field is not set.
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_DescribeTapes_RequestSyntax) **   <a name="StorageGateway-DescribeTapes-request-Marker"></a>
A marker value, obtained in a previous call to `DescribeTapes`. This marker indicates which page of results to retrieve.  
If not specified, the first page of results is retrieved.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** [TapeARNs](#API_DescribeTapes_RequestSyntax) **   <a name="StorageGateway-DescribeTapes-request-TapeARNs"></a>
Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe. If this parameter is not specified, Tape gateway returns a description of all virtual tapes associated with the specified gateway.  
Type: Array of strings  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: No

## Response Syntax
<a name="API_DescribeTapes_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "Tapes": [ 
      { 
         "KMSKey": "string",
         "PoolEntryDate": number,
         "PoolId": "string",
         "Progress": number,
         "RetentionStartDate": number,
         "TapeARN": "string",
         "TapeBarcode": "string",
         "TapeCreatedDate": number,
         "TapeSizeInBytes": number,
         "TapeStatus": "string",
         "TapeUsedInBytes": number,
         "VTLDevice": "string",
         "Worm": boolean
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTapes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeTapes_ResponseSyntax) **   <a name="StorageGateway-DescribeTapes-response-Marker"></a>
An opaque string that can be used as part of a subsequent `DescribeTapes` call to retrieve the next page of results.  
If a response does not contain a marker, then there are no more results to be retrieved.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [Tapes](#API_DescribeTapes_ResponseSyntax) **   <a name="StorageGateway-DescribeTapes-response-Tapes"></a>
An array of virtual tape descriptions.  
Type: Array of [Tape](API_Tape.md) objects

## Errors
<a name="API_DescribeTapes_Errors"></a>

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
<a name="API_DescribeTapes_Examples"></a>

### Get descriptions of specific tapes
<a name="API_DescribeTapes_Example_1"></a>

In the following request you obtain descriptions of tapes in the tape gateway with ID sgw-12A3456B. The request identifies specific tapes by specifying ARNs for the tapes. In the ARN, the trailing string, for example "TEST04A2A1"- is the tape barcode value. The string 999999999999 is your account number.

#### Sample Request
<a name="API_DescribeTapes_Example_1_Request"></a>

```
{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B",
    "TapeARNs": [
        "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST04A2A1",
        "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST05A2A0"
    ]
}
```

#### Sample Response
<a name="API_DescribeTapes_Example_1_Response"></a>

```
{
    "Tapes": [
        {
            "TapeARN": "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST04A2A1",
            "TapeBarcode": "TEST04A2A1",
            "TapeSizeInBytes": "107374182400",
            "TapeStatus": "AVAILABLE"
        },
        {
            "TapeARN": "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST05A2A0",
            "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
            "TapeBarcode": "TEST05A2A0",
            "TapeSizeInBytes": "107374182400",
            "TapeStatus": "AVAILABLE"
        }
    ]
}
```

## See Also
<a name="API_DescribeTapes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeTapes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeTapes) 