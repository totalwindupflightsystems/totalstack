---
id: "@specs/aws/cloudtrail/docs/API_GetImport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetImport"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# GetImport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_GetImport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetImport
<a name="API_GetImport"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Returns information about a specific import. 

## Request Syntax
<a name="API_GetImport_RequestSyntax"></a>

```
{
   "ImportId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetImport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImportId](#API_GetImport_RequestSyntax) **   <a name="awscloudtrail-GetImport-request-ImportId"></a>
 The ID for the import.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^[a-f0-9\-]+$`   
Required: Yes

## Response Syntax
<a name="API_GetImport_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "Destinations": [ "string" ],
   "EndEventTime": number,
   "ImportId": "string",
   "ImportSource": { 
      "S3": { 
         "S3BucketAccessRoleArn": "string",
         "S3BucketRegion": "string",
         "S3LocationUri": "string"
      }
   },
   "ImportStatistics": { 
      "EventsCompleted": number,
      "FailedEntries": number,
      "FilesCompleted": number,
      "PrefixesCompleted": number,
      "PrefixesFound": number
   },
   "ImportStatus": "string",
   "StartEventTime": number,
   "UpdatedTimestamp": number
}
```

## Response Elements
<a name="API_GetImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-CreatedTimestamp"></a>
 The timestamp of the import's creation.   
Type: Timestamp

 ** [Destinations](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-Destinations"></a>
 The ARN of the destination event data store.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [EndEventTime](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-EndEventTime"></a>
 Used with `StartEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period.   
Type: Timestamp

 ** [ImportId](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-ImportId"></a>
 The ID of the import.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^[a-f0-9\-]+$` 

 ** [ImportSource](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-ImportSource"></a>
 The source S3 bucket.   
Type: [ImportSource](API_ImportSource.md) object

 ** [ImportStatistics](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-ImportStatistics"></a>
 Provides statistics for the import. CloudTrail does not update import statistics in real-time. Returned values for parameters such as `EventsCompleted` may be lower than the actual value, because CloudTrail updates statistics incrementally over the course of the import.   
Type: [ImportStatistics](API_ImportStatistics.md) object

 ** [ImportStatus](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-ImportStatus"></a>
 The status of the import.   
Type: String  
Valid Values: `INITIALIZING | IN_PROGRESS | FAILED | STOPPED | COMPLETED` 

 ** [StartEventTime](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-StartEventTime"></a>
 Used with `EndEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period.   
Type: Timestamp

 ** [UpdatedTimestamp](#API_GetImport_ResponseSyntax) **   <a name="awscloudtrail-GetImport-response-UpdatedTimestamp"></a>
 The timestamp of when the import was updated.   
Type: Timestamp

## Errors
<a name="API_GetImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ImportNotFoundException **   
 The specified import was not found.   
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_GetImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetImport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetImport) 