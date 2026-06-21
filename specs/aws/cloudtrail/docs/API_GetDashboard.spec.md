---
id: "@specs/aws/cloudtrail/docs/API_GetDashboard"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetDashboard"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# GetDashboard

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_GetDashboard
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetDashboard
<a name="API_GetDashboard"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Returns the specified dashboard. 

## Request Syntax
<a name="API_GetDashboard_RequestSyntax"></a>

```
{
   "DashboardId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DashboardId](#API_GetDashboard_RequestSyntax) **   <a name="awscloudtrail-GetDashboard-request-DashboardId"></a>
 The name or ARN for the dashboard.   
Type: String  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

## Response Syntax
<a name="API_GetDashboard_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DashboardArn": "string",
   "LastRefreshFailureReason": "string",
   "LastRefreshId": "string",
   "RefreshSchedule": { 
      "Frequency": { 
         "Unit": "string",
         "Value": number
      },
      "Status": "string",
      "TimeOfDay": "string"
   },
   "Status": "string",
   "TerminationProtectionEnabled": boolean,
   "Type": "string",
   "UpdatedTimestamp": number,
   "Widgets": [ 
      { 
         "QueryAlias": "string",
         "QueryParameters": [ "string" ],
         "QueryStatement": "string",
         "ViewProperties": { 
            "string" : "string" 
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-CreatedTimestamp"></a>
 The timestamp that shows when the dashboard was created.   
Type: Timestamp

 ** [DashboardArn](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-DashboardArn"></a>
 The ARN for the dashboard.   
Type: String  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [LastRefreshFailureReason](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-LastRefreshFailureReason"></a>
 Provides information about failures for the last scheduled refresh.   
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 1000.  
Pattern: `.*` 

 ** [LastRefreshId](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-LastRefreshId"></a>
 The ID of the last dashboard refresh.   
Type: String  
Length Constraints: Minimum length of 10. Maximum length of 20.  
Pattern: `\d+` 

 ** [RefreshSchedule](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-RefreshSchedule"></a>
 The refresh schedule for the dashboard, if configured.   
Type: [RefreshSchedule](API_RefreshSchedule.md) object

 ** [Status](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-Status"></a>
 The status of the dashboard.   
Type: String  
Valid Values: `CREATING | CREATED | UPDATING | UPDATED | DELETING` 

 ** [TerminationProtectionEnabled](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-TerminationProtectionEnabled"></a>
 Indicates whether termination protection is enabled for the dashboard.   
Type: Boolean

 ** [Type](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-Type"></a>
 The type of dashboard.   
Type: String  
Valid Values: `MANAGED | CUSTOM` 

 ** [UpdatedTimestamp](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-UpdatedTimestamp"></a>
 The timestamp that shows when the dashboard was last updated.   
Type: Timestamp

 ** [Widgets](#API_GetDashboard_ResponseSyntax) **   <a name="awscloudtrail-GetDashboard-response-Widgets"></a>
 An array of widgets for the dashboard.   
Type: Array of [Widget](API_Widget.md) objects

## Errors
<a name="API_GetDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **   
This exception is thrown when the specified resource is not found.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_GetDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/GetDashboard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/GetDashboard) 