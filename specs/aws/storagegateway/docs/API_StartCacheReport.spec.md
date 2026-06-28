---
id: "@specs/aws/storagegateway/docs/API_StartCacheReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartCacheReport"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# StartCacheReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_StartCacheReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartCacheReport
<a name="API_StartCacheReport"></a>

Starts generating a report of the file metadata currently cached by an S3 File Gateway for a specific file share. You can use this report to identify and resolve issues if you have files failing upload from your gateway to Amazon S3. The report is a CSV file containing a list of files which match the set of filter parameters you specify in the request.

**Note**  
The **Files Failing Upload** flag is reset every 24 hours and during gateway reboot. If this report captures the files after the reset, but before they become flagged again, they will not be reported as **Files Failing Upload**.

The following requirements must be met to successfully generate a cache report:
+ You must have `s3:PutObject` and `s3:AbortMultipartUpload` permissions for the Amazon S3 bucket where you want to store the cache report.
+ No other cache reports can currently be in-progress for the specified file share.
+ There must be fewer than 10 existing cache reports for the specified file share.
+ The gateway must be online and connected to AWS.
+ The root disk must have at least 20GB of free space when report generation starts.
+ You must specify at least one value for `InclusionFilters` or `ExclusionFilters` in the request.

## Request Syntax
<a name="API_StartCacheReport_RequestSyntax"></a>

```
{
   "BucketRegion": "{{string}}",
   "ClientToken": "{{string}}",
   "ExclusionFilters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "FileShareARN": "{{string}}",
   "InclusionFilters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "LocationARN": "{{string}}",
   "Role": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VPCEndpointDNSName": "{{string}}"
}
```

## Request Parameters
<a name="API_StartCacheReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BucketRegion](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-BucketRegion"></a>
The AWS Region of the Amazon S3 bucket where you want to save the cache report.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.  
Required: Yes

 ** [ClientToken](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-ClientToken"></a>
A unique identifier that you use to ensure idempotent report generation if you need to retry an unsuccessful `StartCacheReport` request. If you retry a request, use the same `ClientToken` you specified in the initial request.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 100.  
Required: Yes

 ** [ExclusionFilters](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-ExclusionFilters"></a>
The list of filters and parameters that determine which files are excluded from the report. You must specify at least one value for `InclusionFilters` or `ExclusionFilters` in a `StartCacheReport` request.  
Type: Array of [CacheReportFilter](API_CacheReportFilter.md) objects  
Required: No

 ** [FileShareARN](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [InclusionFilters](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-InclusionFilters"></a>
The list of filters and parameters that determine which files are included in the report. You must specify at least one value for `InclusionFilters` or `ExclusionFilters` in a `StartCacheReport` request.  
Type: Array of [CacheReportFilter](API_CacheReportFilter.md) objects  
Required: No

 ** [LocationARN](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-LocationARN"></a>
The ARN of the Amazon S3 bucket where you want to save the cache report.  
We do not recommend saving the cache report to the same Amazon S3 bucket for which you are generating the report.  
This field does not accept access point ARNs.
Type: String  
Length Constraints: Minimum length of 16. Maximum length of 1400.  
Required: Yes

 ** [Role](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-Role"></a>
The ARN of the IAM role used when saving the cache report to Amazon S3.  
The IAM role you specify must have the following permissions to write objects and stop multipart uploads to the report bucket:  
+  `s3:PutObject` 
+  `s3:AbortMultipartUpload` 
The role must also allow the `storagegateway.amazonaws.com` service to assume the role using the `sts:AssumeRole` action.
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):iam::([0-9]+):role/(\S+)$`   
Required: Yes

 ** [Tags](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-Tags"></a>
A list of up to 50 key/value tags that you can assign to the cache report. Using tags can help you categorize your reports and more easily locate them in search results.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VPCEndpointDNSName](#API_StartCacheReport_RequestSyntax) **   <a name="StorageGateway-StartCacheReport-request-VPCEndpointDNSName"></a>
The DNS name of the VPC endpoint associated with the Amazon S3 bucket where you want to save the cache report. Optional.  
If your file share uses a VPC endpoint to connect to Amazon S3 for normal operations, we recommend using the same VPC in your `StartCacheReport` request. Cache report creation will fail if the gateway can't connect to the Amazon S3 bucket for any reason, including invalid VPC configuration.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`   
Required: No

## Response Syntax
<a name="API_StartCacheReport_ResponseSyntax"></a>

```
{
   "CacheReportARN": "string"
}
```

## Response Elements
<a name="API_StartCacheReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CacheReportARN](#API_StartCacheReport_ResponseSyntax) **   <a name="StorageGateway-StartCacheReport-response-CacheReportARN"></a>
The Amazon Resource Name (ARN) of the cache report generated by the `StartCacheReport` request.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_StartCacheReport_Errors"></a>

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
<a name="API_StartCacheReport_Examples"></a>

### Start a cache report
<a name="API_StartCacheReport_Example_1"></a>

The following example starts a cache report that includes information about files that fail to upload, whose error causes are either `InaccessibleStorageClass` or `ObjectMissing`.

#### Sample Request
<a name="API_StartCacheReport_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-1.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.StartCacheReport

{
    "FileShareARN": "arn:aws:storagegateway:us-east-1:123456789012:share/share-ABCD1234",
    "Role": "arn:aws:iam::123456789012:role/bucket-access-role",
    "LocationARN": "arn:aws:s3:::bucket-name",
    "BucketRegion": "us-east-1",
    "ClientToken": "abcdefgh",
    "InclusionFilters": [
        {
            "Name": "UploadFailureReason",
            "Values": [
                "InaccessibleStorageClass",
                "ObjectMissing"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_StartCacheReport_Example_1_Response"></a>

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
<a name="API_StartCacheReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/StartCacheReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/StartCacheReport) 