---
id: "@specs/aws/cloudtrail/docs/API_ListDashboards"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDashboards"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# ListDashboards

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_ListDashboards
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDashboards
<a name="API_ListDashboards"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Returns information about all dashboards in the account, in the current Region. 

## Request Syntax
<a name="API_ListDashboards_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDashboards_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDashboards_RequestSyntax) **   <a name="awscloudtrail-ListDashboards-request-MaxResults"></a>
 The maximum number of dashboards to display on a single page.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 1000.  
Required: No

 ** [NamePrefix](#API_ListDashboards_RequestSyntax) **   <a name="awscloudtrail-ListDashboards-request-NamePrefix"></a>
 Specify a name prefix to filter on.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9_\-]+$`   
Required: No

 ** [NextToken](#API_ListDashboards_RequestSyntax) **   <a name="awscloudtrail-ListDashboards-request-NextToken"></a>
 A token you can use to get the next page of dashboard results.   
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** [Type](#API_ListDashboards_RequestSyntax) **   <a name="awscloudtrail-ListDashboards-request-Type"></a>
 Specify a dashboard type to filter on: `CUSTOM` or `MANAGED`.   
Type: String  
Valid Values: `MANAGED | CUSTOM`   
Required: No

## Response Syntax
<a name="API_ListDashboards_ResponseSyntax"></a>

```
{
   "Dashboards": [ 
      { 
         "DashboardArn": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDashboards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Dashboards](#API_ListDashboards_ResponseSyntax) **   <a name="awscloudtrail-ListDashboards-response-Dashboards"></a>
 Contains information about dashboards in the account, in the current Region that match the applied filters.   
Type: Array of [DashboardDetail](API_DashboardDetail.md) objects

 ** [NextToken](#API_ListDashboards_ResponseSyntax) **   <a name="awscloudtrail-ListDashboards-response-NextToken"></a>
 A token you can use to get the next page of dashboard results.   
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

## Errors
<a name="API_ListDashboards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_ListDashboards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/ListDashboards) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListDashboards) 