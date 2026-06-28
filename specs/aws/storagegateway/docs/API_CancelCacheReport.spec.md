---
id: "@specs/aws/storagegateway/docs/API_CancelCacheReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelCacheReport"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CancelCacheReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CancelCacheReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelCacheReport
<a name="API_CancelCacheReport"></a>

Cancels generation of a specified cache report. You can use this operation to manually cancel an IN-PROGRESS report for any reason. This action changes the report status from IN-PROGRESS to CANCELLED. You can only cancel in-progress reports. If the the report you attempt to cancel is in FAILED, ERROR, or COMPLETED state, the cancel operation returns an error.

## Request Syntax
<a name="API_CancelCacheReport_RequestSyntax"></a>

```
{
   "CacheReportARN": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelCacheReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CacheReportARN](#API_CancelCacheReport_RequestSyntax) **   <a name="StorageGateway-CancelCacheReport-request-CacheReportARN"></a>
The Amazon Resource Name (ARN) of the cache report you want to cancel.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_CancelCacheReport_ResponseSyntax"></a>

```
{
   "CacheReportARN": "string"
}
```

## Response Elements
<a name="API_CancelCacheReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CacheReportARN](#API_CancelCacheReport_ResponseSyntax) **   <a name="StorageGateway-CancelCacheReport-response-CacheReportARN"></a>
The Amazon Resource Name (ARN) of the cache report you want to cancel.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_CancelCacheReport_Errors"></a>

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
<a name="API_CancelCacheReport_Examples"></a>

### Cancel a cache report
<a name="API_CancelCacheReport_Example_1"></a>

The following example cancels the cache report with the specified ARN.

#### Sample Request
<a name="API_CancelCacheReport_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-1.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.CancelCacheReport

{
    "CacheReportARN": "arn:aws:storagegateway:us-east-1:123456789012:share/share-ABCD1234/cache-report/report-ABCD1234"
}
```

#### Sample Response
<a name="API_CancelCacheReport_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 80

{
    "CacheReportARN": "arn:aws:storagegateway:us-east-1:123456789012:share/share-ABCD1234/cache-report/report-ABCD1234"
}
```

## See Also
<a name="API_CancelCacheReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CancelCacheReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CancelCacheReport) 