---
id: "@specs/aws/cloudtrail/docs/API_StartImport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartImport"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# StartImport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_StartImport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartImport
<a name="API_StartImport"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Starts an import of logged trail events from a source S3 bucket to a destination event data store. By default, CloudTrail only imports events contained in the S3 bucket's `CloudTrail` prefix and the prefixes inside the `CloudTrail` prefix, and does not check prefixes for other AWS services. If you want to import CloudTrail events contained in another prefix, you must include the prefix in the `S3LocationUri`. For more considerations about importing trail events, see [Considerations for copying trail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-to-lake.html#cloudtrail-trail-copy-considerations) in the *CloudTrail User Guide*. 

 When you start a new import, the `Destinations` and `ImportSource` parameters are required. Before starting a new import, disable any access control lists (ACLs) attached to the source S3 bucket. For more information about disabling ACLs, see [Controlling ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html). 

 When you retry an import, the `ImportID` parameter is required. 

**Note**  
 If the destination event data store is for an organization, you must use the management account to import trail events. You cannot use the delegated administrator account for the organization. 

## Request Syntax
<a name="API_StartImport_RequestSyntax"></a>

```
{
   "Destinations": [ "{{string}}" ],
   "EndEventTime": {{number}},
   "ImportId": "{{string}}",
   "ImportSource": { 
      "S3": { 
         "S3BucketAccessRoleArn": "{{string}}",
         "S3BucketRegion": "{{string}}",
         "S3LocationUri": "{{string}}"
      }
   },
   "StartEventTime": {{number}}
}
```

## Request Parameters
<a name="API_StartImport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Destinations](#API_StartImport_RequestSyntax) **   <a name="awscloudtrail-StartImport-request-Destinations"></a>
 The ARN of the destination event data store. Use this parameter for a new import.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: No

 ** [EndEventTime](#API_StartImport_RequestSyntax) **   <a name="awscloudtrail-StartImport-request-EndEventTime"></a>
 Use with `StartEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified `StartEventTime` and `EndEventTime` before attempting to import events.   
Type: Timestamp  
Required: No

 ** [ImportId](#API_StartImport_RequestSyntax) **   <a name="awscloudtrail-StartImport-request-ImportId"></a>
 The ID of the import. Use this parameter when you are retrying an import.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^[a-f0-9\-]+$`   
Required: No

 ** [ImportSource](#API_StartImport_RequestSyntax) **   <a name="awscloudtrail-StartImport-request-ImportSource"></a>
 The source S3 bucket for the import. Use this parameter for a new import.   
Type: [ImportSource](API_ImportSource.md) object  
Required: No

 ** [StartEventTime](#API_StartImport_RequestSyntax) **   <a name="awscloudtrail-StartImport-request-StartEventTime"></a>
 Use with `EndEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified `StartEventTime` and `EndEventTime` before attempting to import events.   
Type: Timestamp  
Required: No

## Response Syntax
<a name="API_StartImport_ResponseSyntax"></a>

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
   "ImportStatus": "string",
   "StartEventTime": number,
   "UpdatedTimestamp": number
}
```

## Response Elements
<a name="API_StartImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-CreatedTimestamp"></a>
 The timestamp for the import's creation.   
Type: Timestamp

 ** [Destinations](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-Destinations"></a>
 The ARN of the destination event data store.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [EndEventTime](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-EndEventTime"></a>
 Used with `StartEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period.   
Type: Timestamp

 ** [ImportId](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-ImportId"></a>
 The ID of the import.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^[a-f0-9\-]+$` 

 ** [ImportSource](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-ImportSource"></a>
 The source S3 bucket for the import.   
Type: [ImportSource](API_ImportSource.md) object

 ** [ImportStatus](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-ImportStatus"></a>
 Shows the status of the import after a `StartImport` request. An import finishes with a status of `COMPLETED` if there were no failures, or `FAILED` if there were failures.   
Type: String  
Valid Values: `INITIALIZING | IN_PROGRESS | FAILED | STOPPED | COMPLETED` 

 ** [StartEventTime](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-StartEventTime"></a>
 Used with `EndEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period.   
Type: Timestamp

 ** [UpdatedTimestamp](#API_StartImport_ResponseSyntax) **   <a name="awscloudtrail-StartImport-response-UpdatedTimestamp"></a>
 The timestamp of the import's last update, if applicable.   
Type: Timestamp

## Errors
<a name="API_StartImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountHasOngoingImportException **   
 This exception is thrown when you start a new import and a previous import is still in progress.   
HTTP Status Code: 400

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** ImportNotFoundException **   
 The specified import was not found.   
HTTP Status Code: 400

 ** InactiveEventDataStoreException **   
The event data store is inactive.  
HTTP Status Code: 400

 ** InsufficientEncryptionPolicyException **   
For the `CreateTrail` `PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and `StartImport` operations, this exception is thrown when the policy on the S3 bucket or AWS KMS key does not have sufficient permissions for the operation.  
For all other operations, this exception is thrown when the policy for the AWS KMS key does not have sufficient permissions for the operation.  
HTTP Status Code: 400

 ** InvalidEventDataStoreCategoryException **   
This exception is thrown when event categories of specified event data stores are not valid.  
HTTP Status Code: 400

 ** InvalidEventDataStoreStatusException **   
The event data store is not in a status that supports the operation.  
HTTP Status Code: 400

 ** InvalidImportSourceException **   
 This exception is thrown when the provided source S3 bucket is not valid for import.   
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_StartImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/StartImport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/StartImport) 