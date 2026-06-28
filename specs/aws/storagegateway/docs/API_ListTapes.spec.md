---
id: "@specs/aws/storagegateway/docs/API_ListTapes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTapes"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListTapes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListTapes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTapes
<a name="API_ListTapes"></a>

Lists virtual tapes in your virtual tape library (VTL) and your virtual tape shelf (VTS). You specify the tapes to list by specifying one or more tape Amazon Resource Names (ARNs). If you don't specify a tape ARN, the operation lists all virtual tapes in both your VTL and VTS.

This operation supports pagination. By default, the operation returns a maximum of up to 100 tapes. You can optionally specify the `Limit` parameter in the body to limit the number of tapes in the response. If the number of tapes returned in the response is truncated, the response includes a `Marker` element that you can use in your subsequent request to retrieve the next set of tapes. This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_ListTapes_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Marker": "{{string}}",
   "TapeARNs": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListTapes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListTapes_RequestSyntax) **   <a name="StorageGateway-ListTapes-request-Limit"></a>
An optional number limit for the tapes in the list returned by this call.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_ListTapes_RequestSyntax) **   <a name="StorageGateway-ListTapes-request-Marker"></a>
A string that indicates the position at which to begin the returned list of tapes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** [TapeARNs](#API_ListTapes_RequestSyntax) **   <a name="StorageGateway-ListTapes-request-TapeARNs"></a>
The Amazon Resource Name (ARN) of each of the tapes you want to list. If you don't specify a tape ARN, the response lists all tapes in both your VTL and VTS.  
Type: Array of strings  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: No

## Response Syntax
<a name="API_ListTapes_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "TapeInfos": [ 
      { 
         "GatewayARN": "string",
         "PoolEntryDate": number,
         "PoolId": "string",
         "RetentionStartDate": number,
         "TapeARN": "string",
         "TapeBarcode": "string",
         "TapeSizeInBytes": number,
         "TapeStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTapes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListTapes_ResponseSyntax) **   <a name="StorageGateway-ListTapes-response-Marker"></a>
A string that indicates the position at which to begin returning the next list of tapes. Use the marker in your next request to continue pagination of tapes. If there are no more tapes to list, this element does not appear in the response body.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [TapeInfos](#API_ListTapes_ResponseSyntax) **   <a name="StorageGateway-ListTapes-response-TapeInfos"></a>
An array of [TapeInfo](API_TapeInfo.md) objects, where each object describes a single tape. If there are no tapes in the tape library or VTS, then the `TapeInfos` is an empty array.  
Type: Array of [TapeInfo](API_TapeInfo.md) objects

## Errors
<a name="API_ListTapes_Errors"></a>

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
<a name="API_ListTapes_Examples"></a>

### Example request
<a name="API_ListTapes_Example_1"></a>

The ListTapes request in the following example does not specify a `limit`, `marker`, or `TapeARN` field in the response body. This example lists the only two tapes in the VTL and VTS. The response returns up to the first 100 tapes.

#### Sample Request
<a name="API_ListTapes_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20160425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.ListTapes

{
    "TapeARN": "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST38A29D"
}
```

#### Sample Response
<a name="API_ListTapes_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Mon, 29 Apr 2016 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 346

{
    "Marker": "string",
    "TapeInfos": [
        {
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
            "TapeARN": "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST38A29D",
            "TapeBarcode": "TEST38A29D",
            "TapeSizeInBytes": "107374182400",
            "TapeStatus": "AVAILABLE"
        },
        {
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-23A4567C",
            "TapeARN": "arn:aws:storagegateway:us-east-2:999999999999:tape/TEST49B39F",
            "TapeBarcode": "TEST49B39F",
            "TapeSizeInBytes": "107374182400",
            "TapeStatus": "ARCHIVED"
        }
    ]
}
```

## See Also
<a name="API_ListTapes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListTapes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListTapes) 