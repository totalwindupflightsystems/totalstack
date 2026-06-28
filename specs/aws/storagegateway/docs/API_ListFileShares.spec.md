---
id: "@specs/aws/storagegateway/docs/API_ListFileShares"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFileShares"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListFileShares

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListFileShares
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFileShares
<a name="API_ListFileShares"></a>

Gets a list of the file shares for a specific S3 File Gateway, or the list of file shares that belong to the calling AWS account. This operation is only supported for S3 File Gateways.

## Request Syntax
<a name="API_ListFileShares_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFileShares_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_ListFileShares_RequestSyntax) **   <a name="StorageGateway-ListFileShares-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway whose file shares you want to list. If this field is not present, all file shares under your account are listed.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** [Limit](#API_ListFileShares_RequestSyntax) **   <a name="StorageGateway-ListFileShares-request-Limit"></a>
The maximum number of file shares to return in the response. The value must be an integer with a value greater than zero. Optional.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_ListFileShares_RequestSyntax) **   <a name="StorageGateway-ListFileShares-request-Marker"></a>
Opaque pagination token returned from a previous ListFileShares operation. If present, `Marker` specifies where to continue the list from after a previous call to ListFileShares. Optional.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## Response Syntax
<a name="API_ListFileShares_ResponseSyntax"></a>

```
{
   "FileShareInfoList": [ 
      { 
         "FileShareARN": "string",
         "FileShareId": "string",
         "FileShareStatus": "string",
         "FileShareType": "string",
         "GatewayARN": "string"
      }
   ],
   "Marker": "string",
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListFileShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileShareInfoList](#API_ListFileShares_ResponseSyntax) **   <a name="StorageGateway-ListFileShares-response-FileShareInfoList"></a>
An array of information about the S3 File Gateway's file shares.  
Type: Array of [FileShareInfo](API_FileShareInfo.md) objects

 ** [Marker](#API_ListFileShares_ResponseSyntax) **   <a name="StorageGateway-ListFileShares-response-Marker"></a>
If the request includes `Marker`, the response returns that value in this field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [NextMarker](#API_ListFileShares_ResponseSyntax) **   <a name="StorageGateway-ListFileShares-response-NextMarker"></a>
If a value is present, there are more file shares to return. In a subsequent request, use `NextMarker` as the value for `Marker` to retrieve the next set of file shares.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListFileShares_Errors"></a>

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
<a name="API_ListFileShares_Examples"></a>

### Get a list of file shares for a specific S3 File Gateway.
<a name="API_ListFileShares_Example_1"></a>

In the following request, you get information about the first file share exposed by a S3 File Gateway; the `Limit` field restricts the number of file share descriptions returned. To get the remaining file share descriptions, use the `NextMarker` field value in the response JSON as the value for `Marker` in subsequent calls to `ListFileShares`.

#### Sample Request
<a name="API_ListFileShares_Example_1_Request"></a>

```
{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-xxxxxxx",
    "Limit": "1"
}
```

#### Sample Response
<a name="API_ListFileShares_Example_1_Response"></a>

```
{
    "FileShareInfos": [
        {
            "FileShareARN": "arn:aws:storagegateway:us-east-2:111122223333:share/share-XXXXXXXX",
            "FileShareId": "share-XXXXXXXX",
            "FileShareStatus": "AVAILABLE",
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-YYYYYYYY"
        }
    ],
    "NextMarker": "c2hhcmUtMUU0MjIwNzU="
}
```

## See Also
<a name="API_ListFileShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListFileShares) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListFileShares) 