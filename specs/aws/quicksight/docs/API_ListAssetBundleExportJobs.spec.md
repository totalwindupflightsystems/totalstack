---
id: "@specs/aws/quicksight/docs/API_ListAssetBundleExportJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAssetBundleExportJobs"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListAssetBundleExportJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListAssetBundleExportJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAssetBundleExportJobs
<a name="API_ListAssetBundleExportJobs"></a>

Lists all asset bundle export jobs that have been taken place in the last 14 days. Jobs created more than 14 days ago are deleted forever and are not returned. If you are using the same job ID for multiple jobs, `ListAssetBundleExportJobs` only returns the most recent job that uses the repeated job ID.

## Request Syntax
<a name="API_ListAssetBundleExportJobs_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/asset-bundle-export-jobs?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssetBundleExportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListAssetBundleExportJobs_RequestSyntax) **   <a name="QS-ListAssetBundleExportJobs-request-uri-AwsAccountId"></a>
The ID of the AWS account that the export jobs were executed in.   
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListAssetBundleExportJobs_RequestSyntax) **   <a name="QS-ListAssetBundleExportJobs-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAssetBundleExportJobs_RequestSyntax) **   <a name="QS-ListAssetBundleExportJobs-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListAssetBundleExportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssetBundleExportJobs_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AssetBundleExportJobSummaryList": [ 
      { 
         "Arn": "string",
         "AssetBundleExportJobId": "string",
         "CreatedTime": number,
         "ExportFormat": "string",
         "IncludeAllDependencies": boolean,
         "IncludePermissions": boolean,
         "IncludeTags": boolean,
         "JobStatus": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListAssetBundleExportJobs_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListAssetBundleExportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleExportJobs-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AssetBundleExportJobSummaryList](#API_ListAssetBundleExportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleExportJobs-response-AssetBundleExportJobSummaryList"></a>
A list of export job summaries.  
Type: Array of [AssetBundleExportJobSummary](API_AssetBundleExportJobSummary.md) objects

 ** [NextToken](#API_ListAssetBundleExportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleExportJobs-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListAssetBundleExportJobs_ResponseSyntax) **   <a name="QS-ListAssetBundleExportJobs-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String  
Pattern: `.*\S.*` 

## Errors
<a name="API_ListAssetBundleExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_ListAssetBundleExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListAssetBundleExportJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListAssetBundleExportJobs) 