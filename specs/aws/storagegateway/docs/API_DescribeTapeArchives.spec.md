---
id: "@specs/aws/storagegateway/docs/API_DescribeTapeArchives"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTapeArchives"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeTapeArchives

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeTapeArchives
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTapeArchives
<a name="API_DescribeTapeArchives"></a>

Returns a description of specified virtual tapes in the virtual tape shelf (VTS). This operation is only supported in the tape gateway type.

If a specific `TapeARN` is not specified, Storage Gateway returns a description of all virtual tapes found in the VTS associated with your account.

## Request Syntax
<a name="API_DescribeTapeArchives_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Marker": "{{string}}",
   "TapeARNs": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeTapeArchives_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_DescribeTapeArchives_RequestSyntax) **   <a name="StorageGateway-DescribeTapeArchives-request-Limit"></a>
Specifies that the number of virtual tapes described be limited to the specified number.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_DescribeTapeArchives_RequestSyntax) **   <a name="StorageGateway-DescribeTapeArchives-request-Marker"></a>
An opaque string that indicates the position at which to begin describing virtual tapes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** [TapeARNs](#API_DescribeTapeArchives_RequestSyntax) **   <a name="StorageGateway-DescribeTapeArchives-request-TapeARNs"></a>
Specifies one or more unique Amazon Resource Names (ARNs) that represent the virtual tapes you want to describe.  
Type: Array of strings  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: No

## Response Syntax
<a name="API_DescribeTapeArchives_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "TapeArchives": [ 
      { 
         "CompletionTime": number,
         "KMSKey": "string",
         "PoolEntryDate": number,
         "PoolId": "string",
         "RetentionStartDate": number,
         "RetrievedTo": "string",
         "TapeARN": "string",
         "TapeBarcode": "string",
         "TapeCreatedDate": number,
         "TapeSizeInBytes": number,
         "TapeStatus": "string",
         "TapeUsedInBytes": number,
         "Worm": boolean
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTapeArchives_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeTapeArchives_ResponseSyntax) **   <a name="StorageGateway-DescribeTapeArchives-response-Marker"></a>
An opaque string that indicates the position at which the virtual tapes that were fetched for description ended. Use this marker in your next request to fetch the next set of virtual tapes in the virtual tape shelf (VTS). If there are no more virtual tapes to describe, this field does not appear in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [TapeArchives](#API_DescribeTapeArchives_ResponseSyntax) **   <a name="StorageGateway-DescribeTapeArchives-response-TapeArchives"></a>
An array of virtual tape objects in the virtual tape shelf (VTS). The description includes of the Amazon Resource Name (ARN) of the virtual tapes. The information returned includes the Amazon Resource Names (ARNs) of the tapes, size of the tapes, status of the tapes, progress of the description, and tape barcode.  
Type: Array of [TapeArchive](API_TapeArchive.md) objects

## Errors
<a name="API_DescribeTapeArchives_Errors"></a>

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
<a name="API_DescribeTapeArchives_Examples"></a>

### Retrieve description tapes in VTS
<a name="API_DescribeTapeArchives_Example_1"></a>

The following example shows a request that retrieves description of two tapes archived to VTS in the AWS Region specified in the request. The request identifies the tapes by their ARN value. The trailing string in the ARN is the tape barcode. If you don't provide the tape ARN, the tape gateway returns information about all tapes archived to VTS.

#### Sample Request
<a name="API_DescribeTapeArchives_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120425/us-east-2/storagegateway/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=9cd5a3584d1d67d57e61f120f35102d6b3649066abdd4bf4bbcf05bd9f2f8fe2
x-amz-date: 20131028T120000Z
x-amz-target: StorageGateway_20130630.DescribeTapeArchives

{
    "TapeARNs": [
        "arn:aws:storagegateway:us-east-2:999999999999:tape/AM08A1AD",
        "arn:aws:storagegateway:us-east-2:999999999999:tape/AMZN01A2A4"
    ]
}
```

#### Sample Response
<a name="API_DescribeTapeArchives_Example_1_Response"></a>

```
{
    "TapeArchives": [
        {
            "CompletionTime": "1380308527.236",
            "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
            "TapeARN": "arn:aws:storagegateway:us-east-2:999999999:tape/AM08A1AD",
            "TapeBarcode": "AM08A1AD",
            "TapeSizeInBytes": "107374182400",
            "TapeStatus": "ARCHIVED"
        },
        {
            "CompletionTime": "1382918022.647",
            "TapeARN": "arn:aws:storagegateway:us-east-2:999999999:tape/AMZN01A2A4",
            "TapeBarcode": "AMZN01A2A4",
            "TapeSizeInBytes": "429496729600",
            "TapeStatus": "ARCHIVED"
        }
    ]
}
```

## See Also
<a name="API_DescribeTapeArchives_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeTapeArchives) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeTapeArchives) 