---
id: "@specs/aws/storagegateway/docs/API_ListCacheReports"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCacheReports"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListCacheReports

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListCacheReports
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCacheReports
<a name="API_ListCacheReports"></a>

Returns a list of existing cache reports for all file shares associated with your AWS account. This list includes all information provided by the `DescribeCacheReport` action, such as report name, status, completion progress, start time, end time, filters, and tags.

## Request Syntax
<a name="API_ListCacheReports_RequestSyntax"></a>

```
{
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCacheReports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_ListCacheReports_RequestSyntax) **   <a name="StorageGateway-ListCacheReports-request-Marker"></a>
Opaque pagination token returned from a previous `ListCacheReports` operation. If present, `Marker` specifies where to continue the list from after a previous call to `ListCacheReports`. Optional.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## Response Syntax
<a name="API_ListCacheReports_ResponseSyntax"></a>

```
{
   "CacheReportList": [ 
      { 
         "CacheReportARN": "string",
         "CacheReportStatus": "string",
         "EndTime": number,
         "ExclusionFilters": [ 
            { 
               "Name": "string",
               "Values": [ "string" ]
            }
         ],
         "FileShareARN": "string",
         "InclusionFilters": [ 
            { 
               "Name": "string",
               "Values": [ "string" ]
            }
         ],
         "LocationARN": "string",
         "ReportCompletionPercent": number,
         "ReportName": "string",
         "Role": "string",
         "StartTime": number,
         "Tags": [ 
            { 
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListCacheReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CacheReportList](#API_ListCacheReports_ResponseSyntax) **   <a name="StorageGateway-ListCacheReports-response-CacheReportList"></a>
A list of existing cache reports for all file shares associated with your AWS account. This list includes all information provided by the `DescribeCacheReport` action, such as report status, completion progress, start time, end time, filters, and tags.  
Type: Array of [CacheReportInfo](API_CacheReportInfo.md) objects

 ** [Marker](#API_ListCacheReports_ResponseSyntax) **   <a name="StorageGateway-ListCacheReports-response-Marker"></a>
If the request includes `Marker`, the response returns that value in this field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListCacheReports_Errors"></a>

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
<a name="API_ListCacheReports_Examples"></a>

### Get information about all cache reports
<a name="API_ListCacheReports_Example_1"></a>

The following example gets information about all existing cache reports.

#### Sample Request
<a name="API_ListCacheReports_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-1.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.ListCacheReports

{}
```

#### Sample Response
<a name="API_ListCacheReports_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 80

{
    "CacheReportList": [
        {
            "CacheReportARN": "arn:aws:storagegateway:us-east-1:0123456789012:share/share-ABCD1234/cache-report/report-ABCD1234",
            "CacheReportStatus": "COMPLETED",
            "ReportCompletionPercent": 100,
            "EndTime": "2025-02-11T21:32:09.535000+00:00",
            "Role": "arn:aws:iam::123456789012:role/bucket-access-role",
            "FileShareARN": "arn:aws:storagegateway:us-east-1:123456789012:share/share-ABCD1234",
            "LocationARN": "arn:aws:s3:::bucket-name",
            "StartTime": "2025-02-11T21:31:42.081000+00:00",
            "InclusionFilters": [
                {
                    "Name": "UploadFailureReason",
                    "Values": [
                        "InaccessibleStorageClass",
                        "ObjectMissing"
                    ]
                }
            ],
            "ReportName": "cache_report-ABCD1234_1739309502081.csv",
            "Tags": []
        }
    ]
}
```

## See Also
<a name="API_ListCacheReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListCacheReports) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListCacheReports) 